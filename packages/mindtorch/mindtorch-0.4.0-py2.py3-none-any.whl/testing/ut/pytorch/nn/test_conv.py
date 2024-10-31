#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import torch

from mindspore import context
import mindspore as ms
import mindspore.nn as nn

import mindtorch.torch as ms_pytorch
from mindtorch.torch.nn import Module, Parameter
from mindtorch.torch.nn import Conv1d, Conv2d, Conv3d
from mindtorch.torch.nn import ConvTranspose1d, ConvTranspose2d, ConvTranspose3d
from mindtorch.torch import tensor

from ...utils import SKIP_ENV_ASCEND, SKIP_ENV_GRAPH_MODE, SKIP_ENV_PYNATIVE_MODE, set_mode_by_env_config,\
                    param_compare, is_test_under_ascend_context
set_mode_by_env_config()

np.random.seed(0)

def test_torch_ms_conv1d_padding():
    input_init = np.random.randn(1, 3, 16).astype(float)
    weight_init = np.random.randn(64, 3, 3).astype(float)
    weight_init_t = weight_init
    bias_init = np.random.randn(64).astype(float)

    class Conv1dPadModel(torch.nn.Module):
        def __init__(self, stride=1, padding=0, dilation=1, padding_mode='zeros'):
            super(Conv1dPadModel, self).__init__()
            self.conv = torch.nn.Conv1d(in_channels=3, out_channels=64, kernel_size=3, stride=stride,
                                        padding=padding, dilation=dilation, padding_mode=padding_mode)
            self.conv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
            self.conv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

        def forward(self, inputs):
            x = self.conv(inputs)
            return x

    class Conv1dPadModelMs(Module):
        def __init__(self, stride=1, padding=0, dilation=1, padding_mode='zeros'):
            super(Conv1dPadModelMs, self).__init__()
            self.conv = Conv1d(in_channels=3, out_channels=64, kernel_size=3, stride=stride,
                               padding=padding, dilation=dilation, padding_mode=padding_mode)
            self.conv.weight = Parameter(tensor(weight_init_t, ms_pytorch.float32))
            self.conv.bias = Parameter(tensor(bias_init, ms_pytorch.float32))


        def forward(self, inputs):
            x = self.conv(inputs)
            return x

    py_input = torch.tensor(input_init, dtype=torch.float32)
    ms_input = tensor(input_init, ms_pytorch.float32)

    _atol = 1e-5
    if is_test_under_ascend_context():
        _atol = 1e-2

    # padding = 'same'
    py_net1 = Conv1dPadModel(padding='same')
    ms_net1 = Conv1dPadModelMs(padding='same')
    py_output1 = py_net1(py_input)
    ms_output1 = ms_net1(ms_input)
    assert(py_output1.shape == ms_output1.shape)
    assert np.allclose(py_output1.detach().numpy(), ms_output1.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 'same', dilation = (1, 2)
    py_net2 = Conv1dPadModel(padding='same', dilation=1)
    ms_net2 = Conv1dPadModelMs(padding='same', dilation=1)
    py_output2 = py_net2(py_input)
    ms_output2 = ms_net2(ms_input)
    assert(py_output2.shape == ms_output2.shape)
    assert np.allclose(py_output2.detach().numpy(), ms_output2.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 'valid'
    py_net3 = Conv1dPadModel(padding='valid')
    ms_net3 = Conv1dPadModelMs(padding='valid')
    py_output3 = py_net3(py_input)
    ms_output3 = ms_net3(ms_input)
    assert(py_output3.shape == ms_output3.shape)
    assert np.allclose(py_output3.detach().numpy(), ms_output3.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 'valid', dilation = (1, 2)
    py_net4 = Conv1dPadModel(padding='valid', dilation=1)
    ms_net4 = Conv1dPadModelMs(padding='valid', dilation=1)
    py_output4 = py_net4(py_input)
    ms_output4 = ms_net4(ms_input)
    assert(py_output4.shape == ms_output4.shape)
    assert np.allclose(py_output4.detach().numpy(), ms_output4.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 1, padding_mode='zeros'
    py_net5 = Conv1dPadModel(padding = 1, padding_mode='zeros')
    ms_net5 = Conv1dPadModelMs(padding = 1, padding_mode='zeros')
    py_output5 = py_net5(py_input)
    ms_output5 = ms_net5(ms_input)
    assert(py_output5.shape == ms_output5.shape)
    assert np.allclose(py_output5.detach().numpy(), ms_output5.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = (2,2), padding_mode='zeros'
    py_net6 = Conv1dPadModel(padding = 2, padding_mode='zeros')
    ms_net6 = Conv1dPadModelMs(padding = 2, padding_mode='zeros')
    py_output6 = py_net6(py_input)
    ms_output6 = ms_net6(ms_input)
    assert(py_output6.shape == ms_output6.shape)
    assert np.allclose(py_output6.detach().numpy(), ms_output6.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # 2d-input testcase
    input_init = np.random.randn(3, 16).astype(float)
    py_input = torch.tensor(input_init, dtype=torch.float32)
    ms_input = tensor(input_init, ms_pytorch.float32)
    py_net1 = Conv1dPadModel(padding='same')
    ms_net1 = Conv1dPadModelMs(padding='same')
    py_output1 = py_net1(py_input)
    ms_output1 = ms_net1(ms_input)
    assert(py_output1.shape == ms_output1.shape)
    assert np.allclose(py_output1.detach().numpy(), ms_output1.numpy(), atol=_atol) #cpu上 atol>=1e-05

def test_torch_ms_conv2d_network():
    """Test torch and ms conv cell output."""
    weight1_init = np.random.randn(16, 3, 3, 3).astype(float)
    weight2_init = np.random.randn(32, 16, 1, 1).astype(float)
    weight3_init = np.random.randn(16, 32, 1, 1).astype(float)
    weight4_init = np.random.randn(1, 16, 3, 3).astype(float)

    bias1_init = np.random.randn(16).astype(float)
    bias3_init = np.random.randn(16).astype(float)
    bias4_init = np.random.randn(1).astype(float)

    class ConvModel(torch.nn.Module):
        def __init__(self):
            super(ConvModel, self).__init__()
            self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3)
            self.conv2 = torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=1, padding=2, bias=False)
            self.conv3 = torch.nn.Conv2d(in_channels=32, out_channels=16, kernel_size=1, padding=6)
            self.conv4 = torch.nn.Conv2d(in_channels=16, out_channels=1, kernel_size=3, padding='same')
            self.init_param()

        def init_param(self):
            self.conv1.weight = torch.nn.Parameter(torch.tensor(weight1_init, dtype=torch.float32))
            self.conv1.bias = torch.nn.Parameter(torch.tensor(bias1_init, dtype=torch.float32))
            self.conv2.weight = torch.nn.Parameter(torch.tensor(weight2_init, dtype=torch.float32))
            self.conv3.weight = torch.nn.Parameter(torch.tensor(weight3_init, dtype=torch.float32))
            self.conv3.bias = torch.nn.Parameter(torch.tensor(bias3_init, dtype=torch.float32))
            self.conv4.weight = torch.nn.Parameter(torch.tensor(weight4_init, dtype=torch.float32))
            self.conv4.bias = torch.nn.Parameter(torch.tensor(bias4_init, dtype=torch.float32)) 

        def forward(self, inputs):
            x = self.conv1(inputs)
            x = self.conv2(x)
            x = self.conv3(x)
            x = self.conv4(x)
            return x

    class ConvModelms(Module):
        def __init__(self):
            super(ConvModelms, self).__init__()
            self.conv1 = Conv2d(in_channels=3, out_channels=16, kernel_size=3)
            self.conv2 = Conv2d(in_channels=16, out_channels=32, kernel_size=1, padding=2, bias=False)
            self.conv3 = Conv2d(in_channels=32, out_channels=16, kernel_size=1, padding=6)
            self.conv4 = Conv2d(in_channels=16, out_channels=1, kernel_size=3, padding='same')
            self.init_param()

        def init_param(self):
            self.conv1.weight = Parameter(tensor(weight1_init, ms_pytorch.float32))
            self.conv1.bias = Parameter(tensor(bias1_init, ms_pytorch.float32))
            self.conv2.weight = Parameter(tensor(weight2_init, ms_pytorch.float32))
            self.conv3.weight = Parameter(tensor(weight3_init, ms_pytorch.float32))
            self.conv3.bias = Parameter(tensor(bias3_init, ms_pytorch.float32))
            self.conv4.weight = Parameter(tensor(weight4_init, ms_pytorch.float32))
            self.conv4.bias = Parameter(tensor(bias4_init, ms_pytorch.float32))

        def forward(self, inputs):
            x = self.conv1(inputs)
            x = self.conv2(x)
            x = self.conv3(x)
            x = self.conv4(x)
            return x

    py_net = ConvModel()
    py_input = torch.tensor(np.ones(shape=(1, 3, 32, 32)), dtype=torch.float32)
    py_output = py_net(py_input)

    ms_net = ConvModelms()
    ms_net.train()
    ms_input = tensor(np.ones(shape=(1, 3, 32, 32)), ms_pytorch.float32)
    ms_output = ms_net(ms_input)
    assert (py_output.shape == ms_output.shape)
    if is_test_under_ascend_context():
        assert np.allclose(py_output.detach().numpy(), ms_output.asnumpy(), atol=3e-2, rtol=3e-2)
    else:
        assert np.allclose(py_output.detach().numpy(), ms_output.asnumpy(), atol=1e-3)


def test_torch_ms_conv2d_padding():
    input_init = np.random.randn(1, 3, 16, 50).astype(float)
    weight_init = np.random.randn(64, 3, 3, 5).astype(float)
    bias_init = np.random.randn(64).astype(float)

    class Conv2dPadModel(torch.nn.Module):
        def __init__(self, stride=1, padding=0, dilation=1, padding_mode='zeros'):
            super(Conv2dPadModel, self).__init__()
            self.conv = torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(3, 5), stride=stride,
                                        padding=padding, dilation=dilation, padding_mode=padding_mode)
            self.conv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
            self.conv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

        def forward(self, inputs):
            x = self.conv(inputs)
            return x

    class Conv2dPadModelMs(Module):
        def __init__(self, stride=1, padding=0, dilation=1, padding_mode='zeros'):
            super(Conv2dPadModelMs, self).__init__()
            self.conv = Conv2d(in_channels=3, out_channels=64, kernel_size=(3, 5), stride=stride,
                               padding=padding, dilation=dilation, padding_mode=padding_mode)
            self.conv.weight = Parameter(tensor(weight_init, ms_pytorch.float32))
            self.conv.bias = Parameter(tensor(bias_init, ms_pytorch.float32))

        def forward(self, inputs):
            x = self.conv(inputs)
            return x

    _atol = 1e-5
    if is_test_under_ascend_context():
        _atol = 2e-2

    py_input = torch.tensor(input_init, dtype=torch.float32)
    ms_input = tensor(input_init, ms_pytorch.float32) 

    # padding = 'same'
    py_net1 = Conv2dPadModel(padding='same')
    ms_net1 = Conv2dPadModelMs(padding='same')
    py_output1 = py_net1(py_input)
    ms_output1 = ms_net1(ms_input)
    assert(py_output1.shape == ms_output1.shape)
    assert np.allclose(py_output1.detach().numpy(), ms_output1.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 'same', dilation = (1, 2)
    py_net2 = Conv2dPadModel(padding='same', dilation=(1, 2))
    ms_net2 = Conv2dPadModelMs(padding='same', dilation=(1, 2))
    py_output2 = py_net2(py_input)
    ms_output2 = ms_net2(ms_input)
    assert(py_output2.shape == ms_output2.shape)
    assert np.allclose(py_output2.detach().numpy(), ms_output2.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 'valid'
    py_net3 = Conv2dPadModel(padding='valid')
    ms_net3 = Conv2dPadModelMs(padding='valid')
    py_output3 = py_net3(py_input)
    ms_output3 = ms_net3(ms_input)
    assert(py_output3.shape == ms_output3.shape)
    assert np.allclose(py_output3.detach().numpy(), ms_output3.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 'valid', dilation = (1, 2)
    py_net4 = Conv2dPadModel(padding='valid', dilation=(1, 2))
    ms_net4 = Conv2dPadModelMs(padding='valid', dilation=(1, 2))
    py_output4 = py_net4(py_input)
    ms_output4 = ms_net4(ms_input)
    assert(py_output4.shape == ms_output4.shape)
    assert np.allclose(py_output4.detach().numpy(), ms_output4.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 1, padding_mode='zeros'
    py_net5 = Conv2dPadModel(padding = 1, padding_mode='zeros')
    ms_net5 = Conv2dPadModelMs(padding = 1, padding_mode='zeros')
    py_output5 = py_net5(py_input)
    ms_output5 = ms_net5(ms_input)
    assert(py_output5.shape == ms_output5.shape)
    assert np.allclose(py_output5.detach().numpy(), ms_output5.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = (2,2), padding_mode='zeros'
    py_net6 = Conv2dPadModel(padding = (2, 2), padding_mode='zeros')
    ms_net6 = Conv2dPadModelMs(padding = (2, 2), padding_mode='zeros')
    py_output6 = py_net6(py_input)
    ms_output6 = ms_net6(ms_input)
    assert(py_output6.shape == ms_output6.shape)
    assert np.allclose(py_output6.detach().numpy(), ms_output6.asnumpy(), atol=_atol) #cpu上 atol>=1e-05


def test_torch_ms_conv2d_grad():
    data = np.random.randn(1, 2, 5, 5).astype(np.float32)
    net = ms_pytorch.nn.Conv2d(2, 3, 3)
    input = ms_pytorch.tensor(data)
    grad_func = ms.grad(net, grad_position=None, weights=net.trainable_params())
    weight_grad, bias_grad = grad_func(input)
    assert np.count_nonzero(weight_grad.asnumpy()) != 0
    assert np.count_nonzero(bias_grad.asnumpy()) != 0


def test_torch_ms_conv3d_padding():
    input_init = np.random.randn(1, 3, 50, 50, 50).astype(float)
    weight_init = np.random.randn(64, 3, 3, 3, 3).astype(float)
    bias_init = np.random.randn(64).astype(float)

    class Conv3dPadModel(torch.nn.Module):
        def __init__(self, stride=1, padding=0, dilation=1, padding_mode='zeros'):
            super(Conv3dPadModel, self).__init__()
            self.conv = torch.nn.Conv3d(in_channels=3, out_channels=64, kernel_size=(3, 3, 3), stride=stride,
                                        padding=padding, dilation=dilation, padding_mode=padding_mode)
            self.conv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
            self.conv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

        def forward(self, inputs):
            x = self.conv(inputs)
            return x

    class Conv3dPadModelMs(Module):
        def __init__(self, stride=1, padding=0, dilation=1, padding_mode='zeros'):
            super(Conv3dPadModelMs, self).__init__()
            self.conv = Conv3d(in_channels=3, out_channels=64, kernel_size=(3, 3, 3), stride=stride,
                               padding=padding, dilation=dilation, padding_mode=padding_mode)
            self.conv.weight = Parameter(tensor(weight_init, ms_pytorch.float32))
            self.conv.bias = Parameter(tensor(bias_init, ms_pytorch.float32))

        def forward(self, inputs):
            x = self.conv(inputs)
            return x

    py_input = torch.tensor(input_init, dtype=torch.float32)
    ms_input = tensor(input_init, ms_pytorch.float32)

    _atol = 1e-5
    if is_test_under_ascend_context():
        _atol = 2e-2

    # padding = 'same'
    py_net1 = Conv3dPadModel(padding='same')
    ms_net1 = Conv3dPadModelMs(padding='same')
    py_output1 = py_net1(py_input)
    ms_output1 = ms_net1(ms_input)
    assert(py_output1.shape == ms_output1.shape)
    assert np.allclose(py_output1.detach().numpy(), ms_output1.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 'same', dilation = (1, 2)
    py_net2 = Conv3dPadModel(padding='same', dilation=(1, 2, 2))
    ms_net2 = Conv3dPadModelMs(padding='same', dilation=(1, 2, 2))
    py_output2 = py_net2(py_input)
    ms_output2 = ms_net2(ms_input)
    assert(py_output2.shape == ms_output2.shape)
    assert np.allclose(py_output2.detach().numpy(), ms_output2.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 'valid'
    py_net3 = Conv3dPadModel(padding='valid')
    ms_net3 = Conv3dPadModelMs(padding='valid')
    py_output3 = py_net3(py_input)
    ms_output3 = ms_net3(ms_input)
    assert(py_output3.shape == ms_output3.shape)
    assert np.allclose(py_output3.detach().numpy(), ms_output3.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 'valid', dilation = (1, 2)
    py_net4 = Conv3dPadModel(padding='valid', dilation=(1, 2, 2))
    ms_net4 = Conv3dPadModelMs(padding='valid', dilation=(1, 2, 2))
    py_output4 = py_net4(py_input)
    ms_output4 = ms_net4(ms_input)
    assert(py_output4.shape == ms_output4.shape)
    assert np.allclose(py_output4.detach().numpy(), ms_output4.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = 1, padding_mode='zeros'
    py_net5 = Conv3dPadModel(padding = 1, padding_mode='zeros')
    ms_net5 = Conv3dPadModelMs(padding = 1, padding_mode='zeros')
    py_output5 = py_net5(py_input)
    ms_output5 = ms_net5(ms_input)
    assert(py_output5.shape == ms_output5.shape)
    assert np.allclose(py_output5.detach().numpy(), ms_output5.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

    # padding = (2,2), padding_mode='zeros'
    py_net6 = Conv3dPadModel(padding = (2, 2, 2), padding_mode='zeros')
    ms_net6 = Conv3dPadModelMs(padding = (2, 2, 2), padding_mode='zeros')
    py_output6 = py_net6(py_input)
    ms_output6 = ms_net6(ms_input)
    assert(py_output6.shape == ms_output6.shape)
    assert np.allclose(py_output6.detach().numpy(), ms_output6.asnumpy(), atol=_atol) #cpu上 atol>=1e-05

@SKIP_ENV_ASCEND(reason='padding too large tbe ops can not process on Ascend')
def test_torch_ms_conv_transposed3d_output_size1():
    batch_size = 2
    in_channal = 4
    out_channal = 2
    groups = 1
    kernel_size = (3, 5, 2)
    data = np.random.randn(batch_size, in_channal, 10, 12, 14).astype(np.float32)
    weight_ = np.random.randn(in_channal, out_channal // groups, *kernel_size).astype(np.float32)
    bias_ = np.random.randn(out_channal).astype(np.float32)

    m = torch.nn.ConvTranspose3d(in_channal, out_channal, kernel_size, stride=(2, 1, 1), padding=(0, 4, 2))
    m.weight = torch.nn.Parameter(torch.tensor(weight_), requires_grad=True)
    m.bias = torch.nn.Parameter(torch.tensor(bias_), requires_grad=True)
    input = torch.tensor(data)
    torch_output1 = m(input, (21, 8, 11))
    torch_output2 = m(input, (22, 8, 11))

    m = ms_pytorch.nn.ConvTranspose3d(in_channal, out_channal, kernel_size, stride=(2, 1, 1), padding=(0, 4, 2))
    m.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight_), requires_grad=True)
    m.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias_), requires_grad=True)
    input = ms_pytorch.tensor(data)
    ms_output1 = m(input, (21, 8, 11))
    ms_output2 = m(input, (22, 8, 11))

    assert torch_output1.shape == ms_output1.shape
    assert np.allclose(torch_output1.detach().numpy(), ms_output1.numpy(), atol=1e-5)
    assert torch_output1.detach().numpy().dtype == ms_output1.numpy().dtype
    assert torch_output2.shape == ms_output2.shape
    assert np.allclose(torch_output2.detach().numpy(), ms_output2.numpy(), atol=1e-5)
    assert torch_output2.detach().numpy().dtype == ms_output2.numpy().dtype

def test_torch_ms_conv_transposed3d_output_size1_small_padding():
    batch_size = 2
    in_channal = 4
    out_channal = 2
    groups = 1
    kernel_size = (3, 5, 2)
    data = np.random.randn(batch_size, in_channal, 10, 12, 14).astype(np.float32)
    weight_ = np.random.randn(in_channal, out_channal // groups, *kernel_size).astype(np.float32)
    bias_ = np.random.randn(out_channal).astype(np.float32)

    m = torch.nn.ConvTranspose3d(in_channal, out_channal, kernel_size, stride=(2, 1, 1), padding=(0, 1, 1))
    m.weight = torch.nn.Parameter(torch.tensor(weight_), requires_grad=True)
    m.bias = torch.nn.Parameter(torch.tensor(bias_), requires_grad=True)
    input = torch.tensor(data)
    torch_output1 = m(input, (21, 14, 13))
    torch_output2 = m(input, (22, 14, 13))

    m = ms_pytorch.nn.ConvTranspose3d(in_channal, out_channal, kernel_size, stride=(2, 1, 1), padding=(0, 1, 1))
    m.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight_), requires_grad=True)
    m.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias_), requires_grad=True)
    input = ms_pytorch.tensor(data)
    ms_output1 = m(input, (21, 14, 13))
    ms_output2 = m(input, (22, 14, 13))

    _atol = 1e-5
    if is_test_under_ascend_context():
        _atol = 2e-2

    assert torch_output1.shape == ms_output1.shape
    assert np.allclose(torch_output1.detach().numpy(), ms_output1.numpy(), atol=_atol)
    assert torch_output1.detach().numpy().dtype == ms_output1.numpy().dtype
    assert torch_output2.shape == ms_output2.shape
    assert np.allclose(torch_output2.detach().numpy(), ms_output2.numpy(), atol=_atol)
    assert torch_output2.detach().numpy().dtype == ms_output2.numpy().dtype


def test_torch_ms_conv_transposed3d_output_size2():
    batch_size = 2
    in_channal = 4
    out_channal = 2
    kernel_size = 3
    data = np.random.randn(batch_size, in_channal, 10, 12, 15).astype(np.float32)
    weight_ = np.random.randn(in_channal, out_channal, *((kernel_size,) * 3)).astype(np.float32)
    bias_ = np.random.randn(out_channal).astype(np.float32)

    m = torch.nn.ConvTranspose3d(in_channal, out_channal, kernel_size, stride=2)
    input = torch.tensor(data)
    m.weight = torch.nn.Parameter(torch.tensor(weight_), requires_grad=True)
    m.bias = torch.nn.Parameter(torch.tensor(bias_), requires_grad=True)
    torch_output1 = m(input, (21, 25, 31))
    torch_output2 = m(input, (22, 26, 32))

    m = ms_pytorch.nn.ConvTranspose3d(in_channal, out_channal, kernel_size, stride=2)
    input = ms_pytorch.tensor(data)
    m.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight_), requires_grad=True)
    m.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias_), requires_grad=True)
    ms_output1 = m(input, (21, 25, 31))
    ms_output2 = m(input, (22, 26, 32))

    _atol = 1e-5
    if is_test_under_ascend_context():
        _atol = 2e-2

    assert torch_output1.shape == ms_output1.shape
    # print(np.max(np.abs(torch_output1.detach().numpy() - ms_output1.numpy())))
    assert np.allclose(torch_output1.detach().numpy(), ms_output1.numpy(), atol=_atol)
    assert torch_output1.detach().numpy().dtype == ms_output1.numpy().dtype
    assert torch_output2.shape == ms_output2.shape
    assert np.allclose(torch_output2.detach().numpy(), ms_output2.numpy(), atol=_atol)
    assert torch_output2.detach().numpy().dtype == ms_output2.numpy().dtype

def test_torch_ms_conv_transposed3d_grad():
    batch_size = 2
    in_channal = 4
    out_channal = 2
    kernel_size = 3
    data = np.random.randn(batch_size, in_channal, 10, 12, 15).astype(np.float32)
    net = ms_pytorch.nn.ConvTranspose3d(in_channal, out_channal, kernel_size, stride=2)
    input = ms_pytorch.tensor(data)
    grad_func = ms.grad(net, grad_position=None, weights=net.trainable_params())
    weight_grad, bias_grad = grad_func(input)
    assert np.count_nonzero(weight_grad.asnumpy()) != 0
    assert np.count_nonzero(bias_grad.asnumpy()) != 0

    input = ms_pytorch.tensor(data)
    grad_func = ms.grad(net, grad_position=None, weights=net.trainable_params())
    weight_grad, bias_grad = grad_func(input, (21, 25, 31))
    assert np.count_nonzero(weight_grad.asnumpy()) != 0
    assert np.count_nonzero(bias_grad.asnumpy()) != 0


def test_torch_ms_deconv1d_padding():

    weight_init = weight_init_t = np.random.randn(3, 10, 3).astype(float)
    bias_init = np.random.randn(10).astype(float)


    class DConv1dPadModel(torch.nn.Module):
        def __init__(self, stride=1, padding=0, output_padding=1):
            super(DConv1dPadModel, self).__init__()
            self.dconv = torch.nn.ConvTranspose1d(in_channels=3, out_channels=10, kernel_size=3, stride=stride,
                                                  padding=padding, output_padding=output_padding)
            self.dconv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
            self.dconv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

        def forward(self, inputs):
            x = self.dconv(inputs)
            return x

    class DConv1dPadModelMs(Module):
        def __init__(self, stride=1, padding=0, output_padding=1):
            super(DConv1dPadModelMs, self).__init__()
            self.dconv = ConvTranspose1d(in_channels=3, out_channels=10, kernel_size=3, stride=stride,
                                        padding=padding, output_padding=output_padding)
            self.dconv.weight = Parameter(tensor(weight_init_t, ms_pytorch.float32))
            self.dconv.bias = Parameter(tensor(bias_init, ms_pytorch.float32))

        def forward(self, inputs):
            x = self.dconv(inputs)
            return x

    _atol = 1e-5
    if is_test_under_ascend_context():
        _atol = 1e-2

    py_in = torch.ones(size=(10, 3, 10), dtype=torch.float32)
    py_net1 = DConv1dPadModel(stride=2, padding=0, output_padding=0)
    py_out1 = py_net1(py_in)

    ms_in = tensor(data=np.ones(shape=(10, 3, 10), dtype=np.float32))
    ms_net1 = DConv1dPadModelMs(stride=2, padding=0, output_padding=0)
    ms_out1 = ms_net1(ms_in)
    assert (ms_out1.shape == py_out1.shape)
    assert np.allclose(py_out1.detach().numpy(), ms_out1.asnumpy(), atol=_atol)

    py_net2 = DConv1dPadModel(stride=2, padding=2, output_padding=0)
    py_out2 = py_net2(py_in)

    ms_net2 = DConv1dPadModelMs(stride=2, padding=2, output_padding=0)
    ms_out2 = ms_net2(ms_in)
    assert (ms_out2.shape == py_out2.shape)
    assert np.allclose(py_out2.detach().numpy(), ms_out2.asnumpy(), atol=_atol)

    py_net3 = DConv1dPadModel(stride=3, padding=2, output_padding=0)
    py_out3 = py_net3(py_in)

    ms_net3 = DConv1dPadModelMs(stride=3, padding=2, output_padding=0)
    ms_out3 = ms_net3(ms_in)
    assert (ms_out3.shape == py_out3.shape)
    assert np.allclose(py_out3.detach().numpy(), ms_out3.asnumpy(), atol=_atol)

    # add 2D test case
    py_in = torch.ones(size=(3, 10), dtype=torch.float32)
    py_net1 = DConv1dPadModel(stride=2, padding=0, output_padding=0)
    py_out1 = py_net1(py_in)

    ms_in = tensor(data=np.ones(shape=(3, 10), dtype=np.float32))
    ms_net1 = DConv1dPadModelMs(stride=2, padding=0, output_padding=0)
    ms_out1 = ms_net1(ms_in)
    assert (ms_out1.shape == py_out1.shape)
    assert np.allclose(py_out1.detach().numpy(), ms_out1.numpy(), atol=_atol)


def test_torch_ms_deconv2d_padding():
    weight_init = np.random.randn(3, 10, 3, 3).astype(float)
    bias_init = np.random.randn(10).astype(float)

    class DConv2dPadModel(torch.nn.Module):
        def __init__(self, stride=(1, 1), padding=(0, 0), output_padding=(1, 1)):
            super(DConv2dPadModel, self).__init__()
            self.dconv = torch.nn.ConvTranspose2d(in_channels=3, out_channels=10, kernel_size=(3, 3), stride=stride,
                                                  padding=padding, output_padding=output_padding)
            self.dconv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
            self.dconv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

        def forward(self, inputs):
            x = self.dconv(inputs)
            return x

    class DConv2dPadModelMs(Module):
        def __init__(self, stride=(1, 1), padding=(0, 0), output_padding=(1, 1)):
            super(DConv2dPadModelMs, self).__init__()
            self.dconv = ConvTranspose2d(in_channels=3, out_channels=10, kernel_size=(3, 3), stride=stride,
                                        padding=padding, output_padding=output_padding)
            self.dconv.weight = Parameter(tensor(weight_init, ms_pytorch.float32))
            self.dconv.bias = Parameter(tensor(bias_init, ms_pytorch.float32))

        def forward(self, inputs):
            x = self.dconv(inputs)
            return x

    _atol = 1e-5
    if is_test_under_ascend_context():
        _atol = 1e-2

    py_in = torch.ones(size=(10, 3, 10, 10), dtype=torch.float32)
    py_net1 = DConv2dPadModel(stride=2, padding=0, output_padding=0)
    py_out1 = py_net1(py_in)

    ms_in = tensor(data=np.ones(shape=(10, 3, 10, 10), dtype=np.float32))
    ms_net1 = DConv2dPadModelMs(stride=2, padding=0, output_padding=0)
    ms_out1 = ms_net1(ms_in)
    assert (ms_out1.shape == py_out1.shape)
    assert np.allclose(py_out1.detach().numpy(), ms_out1.asnumpy(), atol=_atol)

    py_net2 = DConv2dPadModel(stride=2, padding=2, output_padding=0)
    py_out2 = py_net2(py_in)

    ms_net2 = DConv2dPadModelMs(stride=2, padding=2, output_padding=0)
    ms_out2 = ms_net2(ms_in)
    assert (ms_out2.shape == py_out2.shape)
    assert np.allclose(py_out2.detach().numpy(), ms_out2.asnumpy(), atol=_atol)

    py_net3 = DConv2dPadModel(stride=3, padding=2, output_padding=0)
    py_out3 = py_net3(py_in)

    ms_net3 = DConv2dPadModelMs(stride=3, padding=2, output_padding=0)
    ms_out3 = ms_net3(ms_in)
    assert (ms_out3.shape == py_out3.shape)
    assert np.allclose(py_out3.detach().numpy(), ms_out3.asnumpy(), atol=_atol)

    # 3D testcase
    py_in = torch.ones(size=(3, 10, 10), dtype=torch.float32)
    py_net1 = DConv2dPadModel(stride=2, padding=0, output_padding=0)
    py_out1 = py_net1(py_in)

    ms_in = tensor(data=np.ones(shape=(3, 10, 10), dtype=np.float32))
    ms_net1 = DConv2dPadModelMs(stride=2, padding=0, output_padding=0)
    ms_out1 = ms_net1(ms_in)
    assert (ms_out1.shape == py_out1.shape)
    assert np.allclose(py_out1.detach().numpy(), ms_out1.numpy(), atol=_atol)


def test_torch_ms_deconv3d_padding():
    weight_init = np.random.randn(3, 10, 3, 3, 3).astype(float)
    bias_init = np.random.randn(10).astype(float)

    class DConv3dPadModel(torch.nn.Module):
        def __init__(self, stride=(1, 1, 1), padding=(0, 0, 0), output_padding=(1, 1, 1)):
            super(DConv3dPadModel, self).__init__()
            self.dconv = torch.nn.ConvTranspose3d(in_channels=3, out_channels=10, kernel_size=(3, 3, 3), stride=stride,
                                                  padding=padding, output_padding=output_padding)
            self.dconv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
            self.dconv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

        def forward(self, inputs, output_size = None):
            x = self.dconv(inputs, output_size)
            return x

    class DConv3dPadModelMs(Module):
        def __init__(self, stride=(1, 1, 1), padding=(0, 0, 0), output_padding=(1, 1, 1)):
            super(DConv3dPadModelMs, self).__init__()
            self.dconv = ConvTranspose3d(in_channels=3, out_channels=10, kernel_size=(3, 3, 3), stride=stride,
                                        padding=padding, output_padding=output_padding)
            self.dconv.weight = Parameter(tensor(weight_init, ms_pytorch.float32))
            self.dconv.bias = Parameter(tensor(bias_init, ms_pytorch.float32))

        def forward(self, inputs, output_size = None):
            x = self.dconv(inputs, output_size)
            return x

    _atol = 1e-5
    if is_test_under_ascend_context():
        _atol = 1e-2

    py_in = torch.ones(size=(10, 3, 10, 10, 10), dtype=torch.float32)
    py_net1 = DConv3dPadModel(stride=2, padding=0, output_padding=0)
    py_out1 = py_net1(py_in)

    ms_in = tensor(data=np.ones(shape=(10, 3, 10, 10, 10), dtype=np.float32))
    ms_net1 = DConv3dPadModelMs(stride=2, padding=0, output_padding=0)
    ms_out1 = ms_net1(ms_in)
    assert (ms_out1.shape == py_out1.shape)
    assert np.allclose(py_out1.detach().numpy(), ms_out1.asnumpy(), atol=_atol)

    py_net2 = DConv3dPadModel(stride=2, padding=2, output_padding=0)
    py_out2 = py_net2(py_in)

    ms_net2 = DConv3dPadModelMs(stride=2, padding=2, output_padding=0)
    ms_out2 = ms_net2(ms_in)
    assert (ms_out2.shape == py_out2.shape)
    assert np.allclose(py_out2.detach().numpy(), ms_out2.asnumpy(), atol=_atol)

    py_net3 = DConv3dPadModel(stride=3, padding=2, output_padding=0)
    py_out3 = py_net3(py_in)

    ms_net3 = DConv3dPadModelMs(stride=3, padding=2, output_padding=0)
    ms_out3 = ms_net3(ms_in)
    assert (ms_out3.shape == py_out3.shape)
    assert np.allclose(py_out3.detach().numpy(), ms_out3.asnumpy(), atol=_atol)


    py_net4 = DConv3dPadModel(stride=3, padding=2)
    py_out4 = py_net4(py_in)

    ms_net4 = DConv3dPadModelMs(stride=3, padding=2)
    ms_out4 = ms_net4(ms_in)
    assert (ms_out4.shape == py_out4.shape)
    assert np.allclose(py_out4.detach().numpy(), ms_out4.asnumpy(), atol=_atol)

    py_net4 = DConv3dPadModel(stride=3, padding=2)
    py_out4 = py_net4(py_in, output_size=(27, 27, 27))

    ms_net4 = DConv3dPadModelMs(stride=3, padding=2)
    ms_out4 = ms_net4(ms_in, output_size=(27, 27, 27))
    assert (ms_out4.shape == py_out4.shape)
    assert np.allclose(py_out4.detach().numpy(), ms_out4.asnumpy(), atol=_atol)

    # 4D testcase
    py_in = torch.ones(size=(3, 10, 10, 10), dtype=torch.float32)
    py_net1 = DConv3dPadModel(stride=2, padding=0, output_padding=0)
    py_out1 = py_net1(py_in)

    ms_in = tensor(data=np.ones(shape=(3, 10, 10, 10), dtype=np.float32))
    ms_net1 = DConv3dPadModelMs(stride=2, padding=0, output_padding=0)
    ms_out1 = ms_net1(ms_in)
    assert (ms_out1.shape == py_out1.shape)
    assert np.allclose(py_out1.detach().numpy(), ms_out1.asnumpy(), atol=_atol)


@SKIP_ENV_GRAPH_MODE(reason="conv2d attr under pynative-mode support to be dynamically changed at any time.")
def test_conv2d_setattr():
    conv2d = Conv2d(8, 8, 3)
    x = ms_pytorch.Tensor(1, 8, 11, 11)
    assert conv2d(x).shape == (1, 8, 9, 9)
    conv2d.stride = (2, 2)
    conv2d.dilation = (2, 2)
    conv2d.padding = (4, 4)
    assert conv2d(x).shape == (1, 8, 8, 8)


@SKIP_ENV_PYNATIVE_MODE(reason="conv2d attr under graph-mode only support to be dynamically changed before first running")
def test_conv2d_setattr_graph_before_running():
    conv2d = Conv2d(8, 8, 3)
    conv2d.stride = (2, 2)
    conv2d.dilation = (2, 2)
    conv2d.padding = (4, 4)
    x = ms_pytorch.Tensor(1, 8, 11, 11)
    # if not work, result shape is (1, 8, 9, 9)
    assert conv2d(x).shape == (1, 8, 8, 8)

def test_torch_ms_conv1d_grad():
    data = np.random.randn(1, 2, 5).astype(np.float32)
    net = ms_pytorch.nn.Conv1d(2, 3, 3)
    input = ms_pytorch.tensor(data)
    grad_func = ms.grad(net, grad_position=None, weights=net.trainable_params())
    weight_grad, bias_grad = grad_func(input)
    assert np.count_nonzero(weight_grad.asnumpy()) != 0
    assert np.count_nonzero(bias_grad.asnumpy()) != 0

def test_torch_ms_conv2d_padding_mode_reflect():
    weight1_init = np.random.randn(16, 3, 3, 3).astype(float)
    bias1_init = np.random.randn(16).astype(float)

    torch_conv = torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=2, padding_mode='reflect')
    torch_conv.weight = torch.nn.Parameter(torch.tensor(weight1_init, dtype=torch.float32))
    torch_conv.bias = torch.nn.Parameter(torch.tensor(bias1_init, dtype=torch.float32))

    ms_conv = ms_pytorch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=2, padding_mode='reflect')
    ms_conv.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight1_init, dtype=ms_pytorch.float32))
    ms_conv.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias1_init, dtype=ms_pytorch.float32))

    torch_input = torch.tensor(np.ones(shape=(1, 3, 32, 32)), dtype=torch.float32)
    torch_result = torch_conv(torch_input)

    ms_input = ms_pytorch.tensor(np.ones(shape=(1, 3, 32, 32)), dtype=ms_pytorch.float32)
    ms_result = ms_conv(ms_input)

    if is_test_under_ascend_context():
        param_compare(torch_result.detach(), ms_result, atol=6e-3, equal_nan=True)
    else:
        param_compare(torch_result.detach(), ms_result, atol=1e-6, equal_nan=True)

def test_torch_ms_conv2d_padding_mode_replicate():
    weight1_init = np.random.randn(16, 3, 3, 3).astype(float)
    bias1_init = np.random.randn(16).astype(float)

    torch_conv = torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=2, padding_mode='replicate')
    torch_conv.weight = torch.nn.Parameter(torch.tensor(weight1_init, dtype=torch.float32))
    torch_conv.bias = torch.nn.Parameter(torch.tensor(bias1_init, dtype=torch.float32))

    ms_conv = ms_pytorch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=2, padding_mode='replicate')
    ms_conv.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight1_init, dtype=ms_pytorch.float32))
    ms_conv.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias1_init, dtype=ms_pytorch.float32))

    torch_input = torch.tensor(np.ones(shape=(1, 3, 32, 32)), dtype=torch.float32)
    torch_result = torch_conv(torch_input)

    ms_input = ms_pytorch.tensor(np.ones(shape=(1, 3, 32, 32)), dtype=ms_pytorch.float32)
    ms_result = ms_conv(ms_input)

    if is_test_under_ascend_context():
        param_compare(torch_result.detach(), ms_result, rtol=1e-3, atol=3e-3, equal_nan=True)
    else:
        param_compare(torch_result.detach(), ms_result, atol=1e-5, equal_nan=True)

def test_torch_ms_conv2d_padding_mode_circular():
    weight1_init = np.random.randn(16, 3, 3, 3).astype(float)
    bias1_init = np.random.randn(16).astype(float)

    torch_conv = torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=2, padding_mode='circular')
    torch_conv.weight = torch.nn.Parameter(torch.tensor(weight1_init, dtype=torch.float32))
    torch_conv.bias = torch.nn.Parameter(torch.tensor(bias1_init, dtype=torch.float32))

    ms_conv = ms_pytorch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=2, padding_mode='circular')
    ms_conv.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight1_init, dtype=ms_pytorch.float32))
    ms_conv.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias1_init, dtype=ms_pytorch.float32))

    torch_input = torch.tensor(np.ones(shape=(1, 3, 32, 32)), dtype=torch.float32)
    torch_result = torch_conv(torch_input)

    ms_input = ms_pytorch.tensor(np.ones(shape=(1, 3, 32, 32)), dtype=ms_pytorch.float32)
    ms_result = ms_conv(ms_input)

    if is_test_under_ascend_context():
        param_compare(torch_result.detach(), ms_result, rtol=1e-3, atol=3e-3, equal_nan=True)
    else:
        param_compare(torch_result.detach(), ms_result, atol=1e-6, equal_nan=True)


def test_torch_ms_conv1d_padding_mode_reflect():
    data = np.random.randn(1, 3, 16).astype(float)
    weight_init = np.random.randn(64, 3, 3).astype(float)
    bias_init = np.random.randn(64).astype(float)

    torch_conv = torch.nn.Conv1d(in_channels=3, out_channels=16, kernel_size=3, padding=2, padding_mode='reflect')
    torch_conv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
    torch_conv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

    ms_conv = ms_pytorch.nn.Conv1d(in_channels=3, out_channels=16, kernel_size=3, padding=2, padding_mode='reflect')
    ms_conv.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight_init, dtype=ms_pytorch.float32))
    ms_conv.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias_init, dtype=ms_pytorch.float32))

    torch_input = torch.tensor(data, dtype=torch.float32)
    torch_result = torch_conv(torch_input)

    ms_input = ms_pytorch.tensor(data, dtype=ms_pytorch.float32)
    ms_result = ms_conv(ms_input)

    if is_test_under_ascend_context():
        param_compare(torch_result.detach(), ms_result, atol=6e-3, equal_nan=True)
    else:
        param_compare(torch_result.detach(), ms_result, atol=1e-6, equal_nan=True)

def test_torch_ms_conv1d_padding_mode_replicate():
    data = np.random.randn(1, 3, 16).astype(float)
    weight_init = np.random.randn(64, 3, 3).astype(float)
    bias_init = np.random.randn(64).astype(float)

    torch_conv = torch.nn.Conv1d(in_channels=3, out_channels=64, kernel_size=3, padding=2, padding_mode='replicate')
    torch_conv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
    torch_conv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

    ms_conv = ms_pytorch.nn.Conv1d(in_channels=3, out_channels=64, kernel_size=3, padding=2, padding_mode='replicate')
    ms_conv.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight_init, dtype=ms_pytorch.float32))
    ms_conv.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias_init, dtype=ms_pytorch.float32))

    torch_input = torch.tensor(data, dtype=torch.float32)
    torch_result = torch_conv(torch_input)

    ms_input = ms_pytorch.tensor(data, dtype=ms_pytorch.float32)
    ms_result = ms_conv(ms_input)

    if is_test_under_ascend_context():
        param_compare(torch_result.detach(), ms_result, atol=6e-3, equal_nan=True)
    else:
        param_compare(torch_result.detach(), ms_result, atol=1e-6, equal_nan=True)

def test_torch_ms_conv1d_padding_mode_circular():
    data = np.random.randn(1, 3, 16).astype(float)
    weight_init = np.random.randn(64, 3, 3).astype(float)
    bias_init = np.random.randn(64).astype(float)

    torch_conv = torch.nn.Conv1d(in_channels=3, out_channels=64, kernel_size=3, padding=2, padding_mode='circular')
    torch_conv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
    torch_conv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

    ms_conv = ms_pytorch.nn.Conv1d(in_channels=3, out_channels=64, kernel_size=3, padding=2, padding_mode='circular')
    ms_conv.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight_init, dtype=ms_pytorch.float32))
    ms_conv.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias_init, dtype=ms_pytorch.float32))

    torch_input = torch.tensor(data, dtype=torch.float32)
    torch_result = torch_conv(torch_input)

    ms_input = ms_pytorch.tensor(data, dtype=ms_pytorch.float32)
    ms_result = ms_conv(ms_input)

    if is_test_under_ascend_context():
        param_compare(torch_result.detach(), ms_result, atol=6e-3, equal_nan=True)
    else:
        param_compare(torch_result.detach(), ms_result, atol=1e-6, equal_nan=True)

# TODO: ms.ops.pad(mode='reflect') not support 5D input, so conv3d not support padding_mode='reflect'
'''
def test_torch_ms_conv3d_padding_mode_reflect():
    weight_init = np.random.randn(64, 3, 3, 3, 3).astype(float)
    bias_init = np.random.randn(64).astype(float)
    data = np.random.randn(1, 3, 50, 50, 50).astype(float)

    torch_conv = torch.nn.Conv3d(in_channels=3, out_channels=64, kernel_size=(3, 3, 3), padding=2, padding_mode='reflect')
    torch_conv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
    torch_conv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

    ms_conv = ms_pytorch.nn.Conv3d(in_channels=3, out_channels=64, kernel_size=(3, 3, 3), padding=2, padding_mode='reflect')
    ms_conv.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight_init, dtype=ms_pytorch.float32))
    ms_conv.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias_init, dtype=ms_pytorch.float32))

    torch_input = torch.tensor(data, dtype=torch.float32)
    torch_result = torch_conv(torch_input)

    ms_input = ms_pytorch.tensor(data, dtype=ms_pytorch.float32)
    ms_result = ms_conv(ms_input)

    assert np.allclose(torch_result.detach().numpy(), ms_result.numpy())
'''

def test_torch_ms_conv3d_padding_mode_replicate():
    weight_init = np.random.randn(64, 3, 3, 3, 3).astype(float)
    bias_init = np.random.randn(64).astype(float)
    data = np.random.randn(1, 3, 50, 50, 50).astype(float)

    torch_conv = torch.nn.Conv3d(in_channels=3, out_channels=64, kernel_size=(3, 3, 3), padding=2, padding_mode='replicate')
    torch_conv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
    torch_conv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

    ms_conv = ms_pytorch.nn.Conv3d(in_channels=3, out_channels=64, kernel_size=(3, 3, 3), padding=2, padding_mode='replicate')
    ms_conv.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight_init, dtype=ms_pytorch.float32))
    ms_conv.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias_init, dtype=ms_pytorch.float32))

    torch_input = torch.tensor(data, dtype=torch.float32)
    torch_result = torch_conv(torch_input)

    ms_input = ms_pytorch.tensor(data, dtype=ms_pytorch.float32)
    ms_result = ms_conv(ms_input)

    if is_test_under_ascend_context():
        param_compare(torch_result.detach(), ms_result, atol=3e-2, rtol=3e-2, equal_nan=True)
    else:
        param_compare(torch_result.detach(), ms_result, atol=1e-5, equal_nan=True)


def test_torch_ms_conv3d_padding_mode_circular():
    weight_init = np.random.randn(64, 3, 3, 3, 3).astype(float)
    bias_init = np.random.randn(64).astype(float)
    data = np.random.randn(1, 3, 50, 50, 50).astype(float)

    torch_conv = torch.nn.Conv3d(in_channels=3, out_channels=64, kernel_size=(3, 3, 3), padding=2, padding_mode='circular')
    torch_conv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
    torch_conv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))

    ms_conv = ms_pytorch.nn.Conv3d(in_channels=3, out_channels=64, kernel_size=(3, 3, 3), padding=2, padding_mode='circular')
    ms_conv.weight = ms_pytorch.nn.Parameter(ms_pytorch.tensor(weight_init, dtype=ms_pytorch.float32))
    ms_conv.bias = ms_pytorch.nn.Parameter(ms_pytorch.tensor(bias_init, dtype=ms_pytorch.float32))

    torch_input = torch.tensor(data, dtype=torch.float32)
    torch_result = torch_conv(torch_input)

    ms_input = ms_pytorch.tensor(data, dtype=ms_pytorch.float32)
    ms_result = ms_conv(ms_input)

    if is_test_under_ascend_context():
        param_compare(torch_result.detach(), ms_result, atol=2e-2, equal_nan=True)
    else:
        param_compare(torch_result.detach(), ms_result, atol=1e-5, equal_nan=True)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_torch_ms_conv1d_padding()

    test_torch_ms_conv2d_network()
    test_torch_ms_conv2d_padding()

    test_torch_ms_conv3d_padding()

    test_torch_ms_deconv1d_padding()
    test_torch_ms_deconv2d_padding()
    # test_torch_ms_deconv3d_padding()  # TODO Unsupport CPU
    test_torch_ms_conv2d_grad()
    test_torch_ms_conv1d_grad()

    test_torch_ms_conv2d_padding_mode_reflect()
    test_torch_ms_conv2d_padding_mode_replicate()
    test_torch_ms_conv2d_padding_mode_circular()

    test_torch_ms_conv1d_padding_mode_reflect()
    test_torch_ms_conv1d_padding_mode_replicate()
    test_torch_ms_conv1d_padding_mode_circular()

    # test_torch_ms_conv3d_padding_mode_reflect()
    test_torch_ms_conv3d_padding_mode_replicate()
    test_torch_ms_conv3d_padding_mode_circular()