from abc import ABC, abstractmethod
from collections.abc import Mapping
from functools import cached_property
from typing import Any

from torch import Tensor

from cirkit.backend.torch.graph.modules import AbstractTorchModule
from cirkit.backend.torch.parameters.parameter import TorchParameter
from cirkit.backend.torch.semiring import Semiring, SumProductSemiring


class TorchLayer(AbstractTorchModule, ABC):
    """The abstract base class for all layers."""

    def __init__(
        self,
        num_input_units: int,
        num_output_units: int,
        arity: int = 1,
        *,
        semiring: Semiring | None = None,
        num_folds: int = 1,
    ) -> None:
        """Init class.

        Args:
            num_input_units (int): The number of input units.
            num_output_units (int): The number of output units.
            arity (int, optional): The arity of the layer. Defaults to 1.
            num_folds (int): The number of channels. Defaults to 1.
        """
        if num_input_units < 0:
            raise ValueError("The number of input units must be non-negative")
        if num_output_units <= 0:
            raise ValueError("The number of output units must be positive")
        if arity <= 0:
            raise ValueError("The arity must be positive")
        super().__init__(num_folds=num_folds)
        self.num_input_units = num_input_units
        self.num_output_units = num_output_units
        self.arity = arity
        self.semiring = semiring if semiring is not None else SumProductSemiring

    @property
    @abstractmethod
    def config(self) -> Mapping[str, Any]:
        ...

    @property
    def params(self) -> Mapping[str, TorchParameter]:
        return {}

    @property
    def sub_modules(self) -> Mapping[str, "TorchLayer"]:
        """Retrieve a dictionary mapping string identifiers to torch sub-module layers.,
        that must be passed to the ```__init__``` method of the top-level layer

        Returns:
            A dictionary of torch modules.
        """
        return {}

    # Expected to be fixed, so use cached property to avoid recalculation.
    @cached_property
    def num_parameters(self) -> int:
        """The number of parameters."""
        return sum(p.numel() for p in self.parameters())

    # Expected to be fixed, so use cached property to avoid recalculation.
    @cached_property
    def num_buffers(self) -> int:
        """The number of buffers."""
        return sum(buffer.numel() for buffer in self.buffers())

    # We should run forward with layer(x) instead of layer.forward(x). However, in nn.Module, the
    # typing and docstring for forward is not auto-copied to __call__. Therefore, we override
    # __call__ here to provide a complete interface and documentation for layer(x).
    # NOTE: Should we want to change the interface or docstring of forward in subclasses, __call__
    #       also needs to be overriden to sync the change.
    # TODO: if pytorch finds a way to sync forward and __call__, we can remove this __call__
    def __call__(self, x: Tensor) -> Tensor:
        """Invoke the forward function.

        Args:
            x (Tensor): The input to this layer, shape (F, H, B, Ki).

        Returns:
            Tensor: The output of this layer, shape (F, B, Ko).
        """
        # IGNORE: Idiom for nn.Module.__call__.
        return super().__call__(x)  # type: ignore[no-any-return,misc]

    @abstractmethod
    def forward(self, x: Tensor) -> Tensor:
        """Run forward pass.

        Args:
            x (Tensor): The input to this layer, shape (F, H, B, Ki).

        Returns:
            Tensor: The output of this layer, shape (F, B, Ko).
        """

    def extra_repr(self) -> str:
        return (
            "  ".join(
                [
                    f"folds: {self.num_folds}",
                    f"arity: {self.arity}",
                    f"input-units: {self.num_input_units}",
                    f"output-units: {self.num_output_units}",
                ]
            )
            + "\n"
            + f"input-shape: {(self.num_folds, self.arity, -1, self.num_input_units)}"
            + "\n"
            + f"output-shape: {(self.num_folds, -1, self.num_output_units)}"
        )
