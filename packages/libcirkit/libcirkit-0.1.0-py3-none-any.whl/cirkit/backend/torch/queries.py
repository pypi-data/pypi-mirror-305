import functools
from abc import ABC

import torch
from torch import Tensor

from cirkit.backend.torch.circuits import TorchCircuit
from cirkit.backend.torch.layers import TorchInnerLayer, TorchInputLayer, TorchLayer
from cirkit.utils.scope import Scope


class Query(ABC):
    """An object used to run queries of circuits compiled using the torch backend."""

    def __init__(self) -> None:
        ...


class IntegrateQuery(Query):
    """The integration query object."""

    def __init__(self, circuit: TorchCircuit) -> None:
        """Initialize an integration query object.

        Args:
            circuit: The circuit to integrate over.

        Raises:
            ValueError: If the circuit to integrate is not smooth or not decomposable.
        """
        if not circuit.properties.smooth or not circuit.properties.decomposable:
            raise ValueError(
                f"The circuit to integrate must be smooth and decomposable, "
                f"but found {circuit.properties}"
            )
        super().__init__()
        self._circuit = circuit

    def __call__(self, x: Tensor, *, integrate_vars: Scope) -> Tensor:
        """Solve an integration query, given an input batch and the variables to integrate.

        Args:
            x: An input batch of shape (B, C, D), where B is the batch size, C is the number of
                channels per variable, and D is the number of variables.
            integrate_vars: The variables to integrate. It must be a subset of the variables on
                which the circuit given in the constructor is defined on.

        Returns:
            The result of the integration query, given as a tensor of shape (B, O, K),
                where B is the batch size, O is the number of output vectors of the circuit, and
                K is the number of units in each output vector.
        """
        if not integrate_vars <= self._circuit.scope:
            raise ValueError("The variables to marginalize must be a subset of the circuit scope")
        integrate_vars_idx = torch.tensor(tuple(integrate_vars), device=self._circuit.device)
        output = self._circuit.evaluate(
            x,
            module_fn=functools.partial(
                IntegrateQuery._layer_fn, integrate_vars_idx=integrate_vars_idx
            ),
        )  # (O, B, K)
        return output.transpose(0, 1)  # (B, O, K)

    @staticmethod
    def _layer_fn(layer: TorchLayer, x: Tensor, *, integrate_vars_idx: Tensor) -> Tensor:
        # Evaluate a layer: if it is not an input layer, then evaluate it in the usual
        # feed-forward way. Otherwise, use the variables to integrate to solve the marginal
        # queries on the input layers.
        output = layer(x)  # (F, B, Ko)
        if not isinstance(layer, TorchInputLayer):
            return output
        if layer.num_variables > 1:
            raise NotImplementedError("Integration of multivariate input layers is not supported")
        # integration_mask: Boolean mask of shape (F, 1)
        integration_mask = torch.isin(layer.scope_idx, integrate_vars_idx)
        if not torch.any(integration_mask).item():
            return output
        # output: output of the layer of shape (F, B, Ko)
        # integration_mask: Boolean mask of shape (F, 1, 1)
        # integration_output: result of the integration of the layer of shape (F, 1, Ko)
        integration_mask = integration_mask.unsqueeze(dim=2)
        integration_output = layer.integrate()
        # Use the integration mask to select which output should be the result of
        # an integration operation, and which should not be
        # This is done in parallel for all folds, and regardless of whether the
        # circuit is folded or unfolded
        return torch.where(integration_mask, integration_output, output)


class SamplingQuery(Query):
    """The sampling query object."""

    def __init__(self, circuit: TorchCircuit) -> None:
        """Initialize a sampling query object. Currently, only sampling from the joint distribution
            is supported, i.e., sampling won't work in the case of circuits obtained by
            marginalization, or by observing evidence. Conditional sampling is currently not
            implemented.

        Args:
            circuit: The circuit to sample from.

        Raises:
            ValueError: If the circuit to sample from is not normalised.
        """
        if not circuit.properties.smooth or not circuit.properties.decomposable:
            raise ValueError(
                f"The circuit to sample from must be smooth and decomposable, "
                f"but found {circuit.properties}"
            )
        # TODO: add a check to verify the circuit is monotonic and normalized?
        super().__init__()
        self._circuit = circuit

    def __call__(self, num_samples: int = 1) -> tuple[Tensor, list[Tensor]]:
        """Sample a number of data points.

        Args:
            num_samples: The number of samples to return.

        Return:
            A pair (samples, mixture_samples), consisting of (i) an assignment to the observed
            variables the circuit is defined on, and (ii) the samples of the finitely-discrete
            latent variables associated to the sum units. The samples (i) are returned as a
            tensor of shape (num_samples, num_channels, num_variables).

        Raises:
            ValueError: if the number of samples is not a positive number.
        """
        if num_samples <= 0:
            raise ValueError("The number of samples must be a positive number")

        mixture_samples: list[Tensor] = []
        # samples: (O, C, K, num_samples, D)
        samples = self._circuit.evaluate(
            module_fn=functools.partial(
                self._layer_fn,
                num_samples=num_samples,
                mixture_samples=mixture_samples,
            ),
        )
        # samples: (num_samples, O, K, C, D)
        samples = samples.permute(3, 0, 2, 1, 4)
        # TODO: fix for the case of multi-output circuits, i.e., O != 1 or K != 1
        samples = samples[:, 0, 0]  # (num_samples, C, D)
        return samples, mixture_samples

    def _layer_fn(
        self, layer: TorchLayer, *inputs: Tensor, num_samples: int, mixture_samples: list[Tensor]
    ) -> Tensor:
        # Sample from an input layer
        if not inputs:
            assert isinstance(layer, TorchInputLayer)
            samples = layer.sample(num_samples)
            samples = self._pad_samples(samples, layer.scope_idx)
            mixture_samples.append(samples)
            return samples

        # Sample through an inner layer
        assert isinstance(layer, TorchInnerLayer)
        samples, mix_samples = layer.sample(*inputs)
        if mix_samples is not None:
            mixture_samples.append(mix_samples)
        return samples

    def _pad_samples(self, samples: Tensor, scope_idx: Tensor) -> Tensor:
        """Pads univariate samples to the size of the scope of the circuit (output dimension)
        according to scope for compatibility in downstream inner nodes.
        """
        if scope_idx.shape[1] != 1:
            raise NotImplementedError("Padding is only implemented for univariate samples")

        # padded_samples: (F, C, K, num_samples, D)
        padded_samples = torch.zeros(
            (*samples.shape, len(self._circuit.scope)), device=samples.device, dtype=samples.dtype
        )
        fold_idx = torch.arange(samples.shape[0], device=samples.device)
        padded_samples[fold_idx, :, :, :, scope_idx.squeeze(dim=1)] = samples
        return padded_samples
