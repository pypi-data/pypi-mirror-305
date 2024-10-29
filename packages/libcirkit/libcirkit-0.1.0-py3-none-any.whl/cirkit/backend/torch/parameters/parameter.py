from collections.abc import Iterator

import torch
from torch import Tensor

from cirkit.backend.torch.graph.folding import (
    build_address_book_entry,
    build_address_book_stacked_entry,
    build_unfold_index_info,
)
from cirkit.backend.torch.graph.modules import (
    AddressBook,
    AddressBookEntry,
    FoldIndexInfo,
    TorchDiAcyclicGraph,
)
from cirkit.backend.torch.parameters.nodes import TorchParameterNode
from cirkit.utils.algorithms import subgraph


class ParameterAddressBook(AddressBook):
    def lookup(
        self, module_outputs: list[Tensor], *, in_graph: Tensor | None = None
    ) -> Iterator[tuple[TorchParameterNode | None, tuple[Tensor, ...]]]:
        # A useful function combining the modules outputs, and then possibly applying an index
        def select_index(mids: list[int], idx: Tensor | None) -> Tensor:
            if len(mids) == 1:
                t = module_outputs[mids[0]]
            else:
                t = torch.cat([module_outputs[mid] for mid in mids], dim=0)
            return t if idx is None else t[idx]

        # Loop through the entries and yield inputs
        for entry in self._entries:
            in_module_ids = entry.in_module_ids

            # Catch the case there are some inputs coming from other modules
            if in_module_ids:
                x = tuple(
                    select_index(mids, in_idx)
                    for mids, in_idx in zip(in_module_ids, entry.in_fold_idx)
                )
                yield entry.module, x
                continue

            # Catch the case there are no inputs coming from other modules
            yield entry.module, ()

    @classmethod
    def from_index_info(cls, fold_idx_info: FoldIndexInfo) -> "ParameterAddressBook":
        # The address book entries being built
        entries: list[AddressBookEntry] = []

        # A useful dictionary mapping module ids to their number of folds
        num_folds: dict[int, int] = {}

        # Build the bookkeeping data structure by following the topological ordering
        for mid, m in enumerate(fold_idx_info.ordering):
            # Retrieve the index information of the input modules
            in_modules_fold_idx = fold_idx_info.in_fold_idx[mid]

            # Catch the case of a folded module having the input of the network as input
            if in_modules_fold_idx:
                entry = build_address_book_entry(m, in_modules_fold_idx, num_folds=num_folds)
            # Catch the case of a folded module without inputs
            else:
                entry = AddressBookEntry(m, [], [])

            num_folds[mid] = m.num_folds
            entries.append(entry)

        # Append the last bookkeeping entry with the information to compute the output tensor
        entry = build_address_book_stacked_entry(
            None, [fold_idx_info.out_fold_idx], num_folds=num_folds, output=True
        )
        entries.append(entry)

        return ParameterAddressBook(entries)


class TorchParameter(TorchDiAcyclicGraph[TorchParameterNode]):
    @property
    def num_folds(self) -> int:
        return self._address_book.num_outputs

    @property
    def shape(self) -> tuple[int, ...]:
        return self.outputs[0].shape

    def subgraph(self, *roots: TorchParameterNode) -> "TorchParameter":
        if self.is_folded:
            raise ValueError("Cannot extract a sub-computational graph from a folded one")
        nodes, in_nodes = subgraph(roots, self.node_inputs)
        return TorchParameter(nodes, in_nodes, outputs=roots)

    def reset_parameters(self) -> None:
        """Reset the input parameters."""
        for p in self.nodes:
            p.reset_parameters()

    def __call__(self) -> Tensor:
        # IGNORE: Idiom for nn.Module.__call__.
        return super().__call__()  # type: ignore[no-any-return,misc]

    def forward(self) -> Tensor:
        return self.evaluate()  # (F, d1, d2, ..., dk)

    def _build_unfold_index_info(self) -> FoldIndexInfo:
        return build_unfold_index_info(
            self.topological_ordering(), outputs=self.outputs, incomings_fn=self.node_inputs
        )

    def _build_address_book(self, fold_idx_info: FoldIndexInfo) -> AddressBook:
        return ParameterAddressBook.from_index_info(fold_idx_info)

    def extra_repr(self) -> str:
        return f"shape: {(self.num_folds, *self.shape)}"
