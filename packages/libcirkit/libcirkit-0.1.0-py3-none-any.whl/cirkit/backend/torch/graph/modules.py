from abc import ABC, abstractmethod
from collections.abc import Iterator, Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Protocol, TypeVar, cast

import torch
from torch import Tensor, nn

from cirkit.utils.algorithms import DiAcyclicGraph, subgraph


class AbstractTorchModule(nn.Module, ABC):
    """An abstract class representing a torch.nn.Module that can be folded."""

    def __init__(self, *, num_folds: int = 1):
        """Initialize the abstract torch module object.

        Args:
            num_folds: The number of folds computed by the module.
        """
        super().__init__()
        self._num_folds = num_folds

    @property
    def num_folds(self) -> int:
        return self._num_folds

    @property
    @abstractmethod
    def fold_settings(self) -> tuple[Any, ...]:
        """Retrieve a tuple of attributes on which modules must agree on in order to be folded.

        Returns:
            A tuple of attributes.
        """

    @property
    def sub_modules(self) -> Mapping[str, "AbstractTorchModule"]:
        """Retrieve a dictionary mapping string identifiers to torch sub-modules,
        that must be passed to the ```__init__``` method of the top-level torch module.

        Returns:
            A dictionary of torch modules.
        """
        return {}


TorchModule = TypeVar("TorchModule", bound=AbstractTorchModule)
"""TypeVar: A torch module type that subclasses
    [AbstractTorchModule][cirkit.backend.torch.graph.modules.AbstractTorchModule]."""


@dataclass(frozen=True)
class FoldIndexInfo:
    ordering: list[TorchModule]
    in_fold_idx: dict[int, list[list[tuple[int, int]]]]
    out_fold_idx: list[tuple[int, int]]


@dataclass(frozen=True)
class AddressBookEntry:
    module: TorchModule | None
    in_module_ids: list[list[int]]
    in_fold_idx: list[Tensor | None]


class AddressBook(ABC):
    def __init__(self, entries: list[AddressBookEntry]) -> None:
        last_entry = entries[-1]
        if last_entry.module is not None:
            raise ValueError(
                "The last entry of the address book must not have a module associated to it"
            )
        if len(last_entry.in_fold_idx) != 1:
            raise ValueError(
                "The last entry of the address book must have only one fold index tensor"
            )
        (out_fold_idx,) = last_entry.in_fold_idx
        if len(out_fold_idx.shape) != 1:
            raise ValueError("The output fold index tensor should be a 1-dimensional tensor")
        super().__init__()
        self._entries = entries
        self._num_outputs = out_fold_idx.shape[0]

    def __len__(self) -> int:
        return len(self._entries)

    def __iter__(self) -> Iterator[AddressBookEntry]:
        return iter(self._entries)

    @property
    def num_outputs(self) -> int:
        return self._num_outputs

    def set_device(self, device: str | torch.device | int) -> "AddressBook":
        def set_book_entry_device(entry: AddressBookEntry) -> AddressBookEntry:
            return AddressBookEntry(
                entry.module,
                entry.in_module_ids,
                [idx if idx is None else idx.to(device) for idx in entry.in_fold_idx],
            )

        self._entries = [set_book_entry_device(entry) for entry in self._entries]
        return self

    @abstractmethod
    def lookup(
        self, module_outputs: list[Tensor], *, in_graph: Tensor | None = None
    ) -> Iterator[tuple[TorchModule | None, tuple[Tensor, ...]]]:
        ...


class ModuleEvalFunctional(Protocol):  # pylint: disable=too-few-public-methods
    """The protocol of a function that evaluates a module on some inputs."""

    def __call__(self, module: TorchModule, *inputs: Tensor) -> Tensor:
        """Evaluate a module on some inputs.

        Args:
            module: The module to evaluate.
            inputs: The tensor inputs to the module

        Returns:
            Tensor: The output of the module as specified by this functional.
        """


class TorchDiAcyclicGraph(nn.Module, DiAcyclicGraph[TorchModule], ABC):
    """A torch directed acyclic graph module, i.e., a computational graph made of torch modules."""

    def __init__(
        self,
        modules: Sequence[TorchModule],
        in_modules: dict[TorchModule, Sequence[TorchModule]],
        outputs: Sequence[TorchModule],
        *,
        fold_idx_info: FoldIndexInfo | None = None,
    ):
        """Initialize a Torch computational graph.

        Args:
            modules: The module nodes.
            in_modules: A dictionary mapping modules to their input modules, if any.
            outputs: A list of modules that are the output modules in the computational graph.
            fold_idx_info: The folding index information. It can be None if the Torch graph is
                not folded. This will be consumed (i.e., set to None) when the address book data
                structure is built.
        """
        modules: list[TorchModule] = nn.ModuleList(modules)  # type: ignore
        super().__init__()
        super(nn.Module, self).__init__(modules, in_modules, outputs)
        self._device = None
        self._is_folded = fold_idx_info is not None
        if fold_idx_info is None:
            fold_idx_info = self._build_unfold_index_info()
        self._address_book = self._build_address_book(fold_idx_info)

    @property
    def device(self) -> str | torch.device | int | None:
        """Retrieve the device the module is allocated to.

        Returns:
            A device, which can be a string, and integer or a torch.device object.
        """
        return self._device

    @property
    def is_folded(self) -> bool:
        """Retrieves whether the computational graph is folded or not.

        Returns:
            True if it is folded, False otherwise.
        """
        return self._is_folded

    @property
    def address_book(self) -> AddressBook:
        """Retrieve the address book object of the computational graph.

        Returns:
            The address book.
        """
        return self._address_book

    def subgraph(self, *roots: TorchModule) -> "TorchDiAcyclicGraph[TorchModule]":
        if self.is_folded:
            raise ValueError("Cannot extract a sub-computational graph from a folded one")
        nodes, in_nodes = subgraph(roots, self.node_inputs)
        return TorchDiAcyclicGraph[TorchModule](nodes, in_nodes, outputs=roots)

    def to(
        self,
        device: str | torch.device | int | None = None,
        dtype: torch.dtype | None = None,
        non_blocking: bool = False,
    ) -> "TorchDiAcyclicGraph":
        """Specialization of the torch module's to() method. This is used to set the device
            attribute.

        Args:
            device: The device.
            dtype: The dtype.
            non_blocking: Whether the method should be non-blocking.

        Returns:
            Itself.
        """
        if device is not None:
            self._set_device(device)
        return cast(TorchDiAcyclicGraph, super().to(device, dtype, non_blocking))

    def evaluate(
        self, x: Tensor | None = None, module_fn: ModuleEvalFunctional | None = None
    ) -> Tensor:
        """Evaluate the Torch graph by following the topological ordering,
            and by using the address book information to retrieve the inputs to each module.

        Args:
            x: The input of the Torch computational graph. It can be None.
            module_fn: A functional over modules that overrides the forward method defined by a
                module. It can be None. If it is None, then the ```__call__``` method defined by
                the module itself is used.

        Returns:
            The output tensor of the Torch graph.
            If the Torch graph has multiple outputs, then they will be stacked.

        Raises:
            RuntimeError: If the address book is somehow not well-formed.
        """
        # Evaluate the computational graph by following the topological ordering,
        # and by using the book address information to retrieve the inputs to each
        # (possibly folded) torch module.
        module_outputs: list[Tensor] = []
        for module, inputs in self._address_book.lookup(module_outputs, in_graph=x):
            if module is None:
                (output,) = inputs
                return output
            if module_fn is None:
                y = module(*inputs)
            else:
                y = module_fn(module, *inputs)
            module_outputs.append(y)
        raise RuntimeError("The address book is malformed")

    def _set_device(self, device: str | torch.device | int) -> None:
        self._address_book.set_device(device)
        self._device = device

    @abstractmethod
    def _build_unfold_index_info(self) -> FoldIndexInfo:
        ...

    @abstractmethod
    def _build_address_book(self, fold_idx_info: FoldIndexInfo) -> AddressBook:
        ...

    def __repr__(self) -> str:
        def indent(s: str) -> str:
            s = s.split("\n")
            r = s[0]
            if len(s) == 1:
                return r
            return r + "\n" + "\n".join(f"  {t}" for t in s[1:])

        lines = [self.__class__.__name__ + "("]
        extra_lines = self.extra_repr()
        if extra_lines:
            lines.append(f"  {indent(extra_lines)}")
        for i, entry in enumerate(self._address_book):
            if entry.module is None:
                continue
            repr_module = indent(repr(entry.module))
            lines.append(f"  ({i}): {repr_module}")
        lines.append(")")
        return "\n".join(lines)
