#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import mindspore.ops as P
from mindspore.ops._primitive_cache import _get_cache_prim
from mindspore import _no_grad as torch_no_grad
from mindtorch.torch.nn import init
from mindtorch.torch.nn.functional import linear
from mindtorch.torch.functional import empty
from mindtorch.torch.nn.parameter import Parameter, UninitializedParameter
from mindtorch.utils import unsupported_attr
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor
from .module import Module
from .lazy import LazyModuleMixin

__all__ = ['Linear', 'Identity', 'Bilinear', 'LazyLinear']


class Linear(Module):
    r"""Applies a linear transformation to the incoming data: :math:`y = xA^T + b`

    Args:
        in_features: size of each input sample
        out_features: size of each output sample
        bias: If set to ``False``, the layer will not learn an additive bias.
            Default: ``True``

    Shape:
        - Input: :math:`(*, H_{in})` where :math:`*` means any number of
          dimensions including none and :math:`H_{in} = \text{in\_features}`.
        - Output: :math:`(*, H_{out})` where all but the last dimension
          are the same shape as the input and :math:`H_{out} = \text{out\_features}`.

    Attributes:
        weight: the learnable weights of the module of shape
            :math:`(\text{out\_features}, \text{in\_features})`. The values are
            initialized from :math:`\mathcal{U}(-\sqrt{k}, \sqrt{k})`, where
            :math:`k = \frac{1}{\text{in\_features}}`
        bias:   the learnable bias of the module of shape :math:`(\text{out\_features})`.
                If :attr:`bias` is ``True``, the values are initialized from
                :math:`\mathcal{U}(-\sqrt{k}, \sqrt{k})` where
                :math:`k = \frac{1}{\text{in\_features}}`

    Examples::

        >>> import mindtorch.torch as torch
        >>> import mindtorch.torch.nn as nn
        >>> m = nn.Linear(20, 30)
        >>> input = torch.randn(128, 20)
        >>> output = m(input)
        >>> print(output.size())
        torch.Size([128, 30])
    """
    def __init__(self, in_features, out_features, bias=True, device=None, dtype=None):
        super(Linear, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.has_bias = False
        self.bias = None
        self.weight = Parameter(empty((self.out_features, self.in_features), dtype=dtype, device=device),
                                requires_grad=True)
        if bias:
            self.bias = Parameter(empty(self.out_features, dtype=dtype, device=device), requires_grad=True)
            self.has_bias = True
        self.reset_parameters()

    def reset_parameters(self):
        init.kaiming_uniform_(self.weight, a=math.sqrt(5))
        if self.has_bias:
            fan_in, _ = init._calculate_fan_in_and_fan_out(self.weight)
            bound = 1 / math.sqrt(fan_in) if fan_in > 0 else 0
            init.uniform_(self.bias, -bound, bound)

    def forward(self, input):
        return linear(input, self.weight, self.bias)

    def extra_repr(self) -> str:
        return f'in_features={self.in_features}, out_features={self.out_features}, bias={self.bias is not None}'


class Identity(Module):
    def __init__(self, *args, **kwargs):
        super(Identity, self).__init__()
        unsupported_attr(args)
        unsupported_attr(kwargs)

    def forward(self, input):
        return input


class Bilinear(Module):
    def __init__(self, in1_features, in2_features, out_features, bias=True, device=None, dtype=None):
        super(Bilinear, self).__init__()
        self.in1_features = in1_features
        self.in2_features = in2_features
        self.out_features = out_features

        self.has_bias = False
        self.weight = Parameter(empty((self.out_features, self.in1_features, self.in2_features),
                                      dtype=dtype, device=device), requires_grad=True)
        if bias:
            self.bias = Parameter(empty(self.out_features, dtype=dtype, device=device), requires_grad=True)
            self.has_bias = True
        self.reset_parameters()

    def reset_parameters(self):
        bound = 1 / math.sqrt(self.weight.shape[1])
        init.uniform_(self.weight, -bound, bound)
        if self.has_bias:
            init.uniform_(self.bias, -bound, bound)

    def forward(self, input1, input2):
        input1 = cast_to_ms_tensor(input1)
        input2 = cast_to_ms_tensor(input2)
        input1_shape = input1.shape
        input2_shape = input2.shape
        if len(input1_shape) != 2:
            input1 = input1.reshape((-1, input1_shape[-1]))
        x = P.matmul(input1, self.weight.permute(1, 0, 2).reshape(self.weight.shape[1], -1))
        if len(input2_shape) != 2:
            input2 = input2.reshape((-1, input2_shape[-1]))
        x = P.mul(x, P.tile(input2, (1, self.out_features)))
        x = x.reshape(x.shape[0], self.out_features, -1)
        reducesum = _get_cache_prim(P. P.ReduceSum)()
        x = reducesum(x, -1)
        if self.has_bias:
            bias_add = _get_cache_prim(P.BiasAdd)()
            x = bias_add(x, self.bias)
        x = x.reshape(*input1_shape[:-1], -1)
        return cast_to_adapter_tensor(x)

    def extra_repr(self):
        return 'in1_features={}, in2_features={}, out_features={}, bias={}'.format(
            self.in1_features, self.in2_features, self.out_features, self.has_bias is not None
        )

class LazyLinear(LazyModuleMixin, Linear):

    cls_to_become = Linear
    weight: UninitializedParameter
    bias: UninitializedParameter

    def __init__(self, out_features: int, bias: bool = True,
                 device=None, dtype=None) -> None:
        factory_kwargs = {'device': device, 'dtype': dtype}
        super().__init__(1, 1, False) # Currently, Parameter does not support contain zero dimension.
        self.weight = UninitializedParameter(**factory_kwargs)
        self.out_features = out_features
        if bias:
            self.bias = UninitializedParameter(**factory_kwargs)

    def reset_parameters(self):
        if not self.has_uninitialized_params() and self.in_features != 0:
            super().reset_parameters()

    def initialize_parameters(self, input):
        if self.has_uninitialized_params():
            with torch_no_grad():
                self.in_features = input.shape[-1]
                self.weight.materialize((self.out_features, self.in_features))
                if self.bias is not None:
                    self.bias.materialize((self.out_features,))
                self.reset_parameters()
