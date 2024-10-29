from collections.abc import Callable, Iterator, Sequence

import torch
from torch import Tensor

from cirkit.backend.torch.graph.folding import (
    build_address_book_stacked_entry,
    build_unfold_index_info,
)
from cirkit.backend.torch.graph.modules import (
    AddressBook,
    AddressBookEntry,
    FoldIndexInfo,
    TorchDiAcyclicGraph,
)
from cirkit.backend.torch.layers import TorchInputLayer, TorchLayer
from cirkit.symbolic.circuit import StructuralProperties
from cirkit.utils.scope import Scope


class LayerAddressBook(AddressBook):
    def __init__(self, entries: list[AddressBookEntry]):
        super().__init__(entries)

    def lookup(
        self, module_outputs: list[Tensor], *, in_graph: Tensor | None = None
    ) -> Iterator[tuple[TorchLayer | None, tuple[Tensor, ...]]]:
        # Loop through the entries and yield inputs
        for entry in self._entries:
            # Catch the case there are some inputs coming from other modules
            if entry.in_module_ids:
                (in_fold_idx,) = entry.in_fold_idx
                (in_module_ids,) = entry.in_module_ids
                if len(in_module_ids) == 1:
                    x = module_outputs[in_module_ids[0]]
                else:
                    x = torch.cat([module_outputs[mid] for mid in in_module_ids], dim=0)
                x = x[in_fold_idx]
                yield entry.module, (x,)
                continue

            # Catch the case there are no inputs coming from other modules
            # That is, we are gathering the inputs of input layers
            assert isinstance(entry.module, TorchInputLayer)
            if in_graph is None:
                yield entry.module, ()
            else:
                # in_graph: An input batch (assignments to variables) of shape (B, C, D)
                # scope_idx: The scope of the layers in each fold, a tensor of shape (F, D'), D' < D
                # x: (B, C, D) -> (B, C, F, D') -> (F, C, B, D')
                x = in_graph[..., entry.module.scope_idx].permute(2, 1, 0, 3)
                yield entry.module, (x,)

    @classmethod
    def from_index_info(
        cls,
        fold_idx_info: FoldIndexInfo,
        *,
        incomings_fn: Callable[[TorchLayer], Sequence[TorchLayer]],
    ) -> "LayerAddressBook":
        # The address book entries being built
        entries: list[AddressBookEntry] = []

        # A useful dictionary mapping module ids to their number of folds
        num_folds: dict[int, int] = {}

        # Build the bookkeeping data structure by following the topological ordering
        for mid, m in enumerate(fold_idx_info.ordering):
            # Retrieve the index information of the input modules
            in_modules_fold_idx = fold_idx_info.in_fold_idx[mid]

            # Catch the case of a folded module having the output of another module as input
            if incomings_fn(m):
                entry = build_address_book_stacked_entry(
                    m, in_modules_fold_idx, num_folds=num_folds
                )
            else:
                # Catch the case of a folded module having the input of the network as input
                # That is, this is the case of an input layer
                entry = AddressBookEntry(m, [], [])

            num_folds[mid] = m.num_folds
            entries.append(entry)

        # Append the last bookkeeping entry with the information to compute the output tensor
        entry = build_address_book_stacked_entry(
            None, [fold_idx_info.out_fold_idx], num_folds=num_folds, output=True
        )
        entries.append(entry)

        return LayerAddressBook(entries)


class AbstractTorchCircuit(TorchDiAcyclicGraph[TorchLayer]):
    def __init__(
        self,
        scope: Scope,
        num_channels: int,
        layers: Sequence[TorchLayer],
        in_layers: dict[TorchLayer, Sequence[TorchLayer]],
        outputs: Sequence[TorchLayer],
        *,
        properties: StructuralProperties,
        fold_idx_info: FoldIndexInfo | None = None,
    ) -> None:
        super().__init__(
            layers,
            in_layers,
            outputs,
            fold_idx_info=fold_idx_info,
        )
        self._scope = scope
        self._num_channels = num_channels
        self._properties = properties

    @property
    def scope(self) -> Scope:
        return self._scope

    @property
    def num_variables(self) -> int:
        return len(self.scope)

    @property
    def num_channels(self) -> int:
        return self._num_channels

    @property
    def properties(self) -> StructuralProperties:
        return self._properties

    @property
    def layers(self) -> Sequence[TorchLayer]:
        return self.nodes

    def layer_inputs(self, l: TorchLayer) -> Sequence[TorchLayer]:
        return self.node_inputs(l)

    def layer_outputs(self, l: TorchLayer) -> Sequence[TorchLayer]:
        return self.node_outputs(l)

    @property
    def layers_inputs(self) -> dict[TorchLayer, Sequence[TorchLayer]]:
        return self.nodes_inputs

    @property
    def layers_outputs(self) -> dict[TorchLayer, Sequence[TorchLayer]]:
        return self.nodes_outputs

    def reset_parameters(self) -> None:
        # For each layer, initialize its parameters, if any
        for l in self.layers:
            for p in l.params.values():
                p.reset_parameters()

    def _set_device(self, device: str | torch.device | int) -> None:
        for l in self.layers:
            for p in l.params.values():
                p._set_device(device)
        super()._set_device(device)

    def _build_unfold_index_info(self) -> FoldIndexInfo:
        return build_unfold_index_info(
            self.topological_ordering(), outputs=self.outputs, incomings_fn=self.node_inputs
        )

    def _build_address_book(self, fold_idx_info: FoldIndexInfo) -> LayerAddressBook:
        return LayerAddressBook.from_index_info(fold_idx_info, incomings_fn=self.layer_inputs)

    def _evaluate_layers(self, x: Tensor) -> Tensor:
        # Evaluate layers on the given input
        y = self.evaluate(x)  # (O, B, K)
        return y.transpose(0, 1)  # (B, O, K)


class TorchCircuit(AbstractTorchCircuit):
    """The tensorized circuit with concrete computational graph in PyTorch.

    This class is aimed for computation, and therefore does not include structural properties.
    """

    def __call__(self, x: Tensor) -> Tensor:
        """Invoke the forward function.

        Args:
            x (Tensor): The input of the circuit, shape (B, C, D).

        Returns:
            Tensor: The output of the circuit, shape (B, num_out, num_cls).
        """  # TODO: single letter name?
        # IGNORE: Idiom for nn.Module.__call__.
        return super().__call__(x)  # type: ignore[no-any-return,misc]

    def forward(self, x: Tensor) -> Tensor:
        return self._evaluate_layers(x)


class TorchConstantCircuit(AbstractTorchCircuit):
    """The tensorized circuit with concrete computational graph in PyTorch.

    This class is aimed for computation, and therefore does not include strutural properties.
    """

    def __call__(self) -> Tensor:
        """Invoke the forward function.

        Returns:
            Tensor: The output of the circuit, shape (B, num_out, num_cls).
        """  # TODO: single letter name?
        # IGNORE: Idiom for nn.Module.__call__.
        return super().__call__()  # type: ignore[no-any-return,misc]

    def forward(self) -> Tensor:
        # Evaluate the layers using some dummy input
        x = torch.empty(size=(1, self.num_channels, self.num_variables), device=self.device)
        x = self._evaluate_layers(x)  # (B, O, K)
        return x.squeeze(dim=0)  # (O, K)
