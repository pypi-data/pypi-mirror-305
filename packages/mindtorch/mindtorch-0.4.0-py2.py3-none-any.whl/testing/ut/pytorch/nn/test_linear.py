#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.torch.nn import Module, Linear, Identity, Bilinear
from mindtorch.torch import tensor
import mindtorch.torch as ms_torch
import numpy as np
import torch

from ...utils import set_mode_by_env_config, is_test_under_graph_context
set_mode_by_env_config()


def test_linear_model():
    class LinearModel(Module):
        def __init__(self):
            super(LinearModel, self).__init__()
            self.line1 = Linear(in_features=32, out_features=64)
            self.line2 = Linear(in_features=64, out_features=128, bias=False)
            self.line3 = Linear(in_features=128, out_features=10)

        def forward(self, inputs):
            x = self.line1(inputs)
            x = self.line2(x)
            x = self.line3(x)
            return x

    model = LinearModel()
    model.train()

    def weight_init(m):
        if isinstance(m, Linear):
            m.weight.data = m.weight.data.normal_adapter(0, 0.01)
            if m.has_bias:
                m.bias.data = m.bias.data.zero_adapter()

    model.apply(weight_init)

    inputs = tensor(np.ones(shape=(5, 32)), torch.float32)
    output = model(inputs)
    assert output.shape == (5, 10)


class IdentityModel(Module):
    def __init__(self):
        super(IdentityModel, self).__init__()
        self.identity = Identity()

    def forward(self, inputs):
        return self.identity(inputs)

class TorchIdentityModel(torch.nn.Module):
    def __init__(self):
        super(TorchIdentityModel, self).__init__()
        self.identity = torch.nn.Identity()

    def forward(self, inputs):
        return self.identity(inputs)


def test_identity():
    net = IdentityModel()
    input_tensor = tensor(np.ones(shape=(5, 32)).astype(np.float32))
    input_param = ms_torch.nn.Parameter(input_tensor)

    output_tensor = net(input_tensor)
    output_param = net(input_param)
    np.testing.assert_almost_equal(output_tensor.numpy(), input_tensor.numpy())
    if not is_test_under_graph_context():
        assert id(input_tensor) == id(output_tensor)
        assert type(output_tensor) == ms_torch.Tensor
        assert isinstance(output_param, ms_torch.nn.Parameter)

    net = TorchIdentityModel()
    input_tensor = torch.tensor(np.ones(shape=(5, 32)).astype(np.float32))
    input_param = torch.nn.Parameter(input_tensor)
    output_tensor = net(input_tensor)
    output_param = net(input_param)
    np.testing.assert_almost_equal(output_tensor.numpy(), input_tensor.numpy())
    assert id(input_tensor) == id(output_tensor)
    assert type(output_tensor) == torch.Tensor
    assert isinstance(output_param, torch.nn.Parameter)


def test_bilinear_model():
    class BilinearModel(Module):
        def __init__(self):
            super(BilinearModel, self).__init__()
            self.line1 = Bilinear(in1_features=4, in2_features=3, out_features=5)
            self.line2 = Bilinear(in1_features=5, in2_features=5, out_features=7, bias=False)

        def forward(self, inputs1, inputs2):
            x = self.line1(inputs1, inputs2)
            x = self.line2(x, x)
            return x

    model = BilinearModel()
    model.train()

    def weight_init(m):
        if isinstance(m, Bilinear):
            m.weight.data = m.weight.data.normal_adapter(0, 0.01)
            if m.has_bias:
                m.bias.data = m.bias.data.zero_adapter()

    model.apply(weight_init)

    inputs1 = tensor(np.ones(shape=(10, 4)), torch.float32)
    inputs2 = tensor(np.ones(shape=(10, 3)), torch.float32)

    output = model(inputs1, inputs2)
    assert output.shape == (10, 7)


def test_linear_model2():
    linear = Linear(64, 3)
    x = tensor(np.ones((1, 2, 64))).to(ms_torch.float32)
    assert linear(x).shape == (1, 2, 3)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_linear_model()
    test_identity()
    test_bilinear_model()
    test_linear_model2()
