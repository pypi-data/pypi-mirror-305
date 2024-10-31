#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

import torch
from torch.nn import functional as F
import mindspore as ms
from mindspore import context

import mindtorch.torch as ms_torch
from mindtorch.torch.nn.functional import pad

from ....utils import set_mode_by_env_config, param_compare, SKIP_ENV_CPU, SKIP_ENV_GPU, SKIP_ENV_ASCEND,\
                      SKIP_ENV_GRAPH_MODE, enable_backward
set_mode_by_env_config()


def test_pad_shape():
    p1d = (1, 1)
    py_t4d = torch.ones(3, 3, 4, 2)
    py_out_1 = F.pad(py_t4d, p1d, "constant", 0)

    ms_t4d = ms_torch.ones(3, 3, 4, 2)
    ms_out_1 = pad(ms_t4d, p1d, "constant", 0)
    assert np.allclose(py_out_1.numpy(), ms_out_1.asnumpy())

    p3d = (1, 1, 0, 2, 1, 1)
    py_out_2 = F.pad(py_t4d, p3d, "constant", 2)
    ms_out_2 = pad(ms_t4d, p3d, "constant", 2)
    assert np.allclose(py_out_2.numpy(), ms_out_2.asnumpy())


def test_pad_mode():
    p1d = (1, 1)
    py_t4d = torch.ones(4, 3, 2)
    py_out_1 = F.pad(py_t4d, p1d, "reflect")

    ms_t4d = ms_torch.ones(4, 3, 2)
    ms_out_1 = pad(ms_t4d, p1d, "reflect")
    assert np.allclose(py_out_1.numpy(), ms_out_1.asnumpy())

def test_pad_constant_value_2d_padding_4d_input():
    padding = (2, 2, 3, 3)
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', None)
    torch_result= F.pad(torch.tensor(data), padding, 'constant', None)
    param_compare(ms_result, torch_result)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', -float('inf'))
    torch_result= F.pad(torch.tensor(data), padding, 'constant', -float('inf'))
    param_compare(ms_result, torch_result)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', 3)
    torch_result= F.pad(torch.tensor(data), padding, 'constant', 3)
    param_compare(ms_result, torch_result)

def test_pad_constant_value_2d_padding_5d_input():
    padding = (2, 2, 3, 3)
    data = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', None)
    torch_result= F.pad(torch.tensor(data), padding, 'constant', None)
    param_compare(ms_result, torch_result)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', -float('inf'))
    torch_result= F.pad(torch.tensor(data), padding, 'constant', -float('inf'))
    param_compare(ms_result, torch_result)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', 3)
    torch_result= F.pad(torch.tensor(data), padding, 'constant', 3)
    param_compare(ms_result, torch_result)


def test_pad_constant_value_3d_padding_4d_input():
    padding = (2, 2, 3, 3, 4, 4)
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', None)
    torch_result= F.pad(torch.tensor(data), padding, 'constant', None)
    param_compare(ms_result, torch_result)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', -float('inf'))
    torch_result= F.pad(torch.tensor(data), padding, 'constant', -float('inf'))
    param_compare(ms_result, torch_result)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', 3)
    torch_result= F.pad(torch.tensor(data), padding, 'constant', 3)
    param_compare(ms_result, torch_result)

def test_pad_constant_value_3d_padding_5d_input():
    padding = (2, 2, 3, 3, 4, 4)
    data = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', None)
    torch_result= F.pad(torch.tensor(data), padding, 'constant', None)
    param_compare(ms_result, torch_result)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', -float('inf'))
    torch_result= F.pad(torch.tensor(data), padding, 'constant', -float('inf'))
    param_compare(ms_result, torch_result)

    ms_result = pad(ms_torch.tensor(data), padding, 'constant', 3)
    torch_result= F.pad(torch.tensor(data), padding, 'constant', 3)
    param_compare(ms_result, torch_result)

def test_pad_reflect_1d_padding_2d_3d_input():
    padding = (2, 2)
    data = np.random.randn(2, 3, 4).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'reflect')
    torch_result= F.pad(torch.tensor(data), padding, 'reflect')
    param_compare(ms_result, torch_result)

    data = np.random.randn(3, 4).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'reflect')
    torch_result= F.pad(torch.tensor(data), padding, 'reflect')
    param_compare(ms_result, torch_result)

def test_pad_reflect_2d_padding_3d_4d_input():
    padding = (2, 2, 3, 3)
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'reflect')
    torch_result= F.pad(torch.tensor(data), padding, 'reflect')
    param_compare(ms_result, torch_result)

    data = np.random.randn(3, 4, 5).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'reflect')
    torch_result= F.pad(torch.tensor(data), padding, 'reflect')
    param_compare(ms_result, torch_result)


@SKIP_ENV_CPU(reason='reflect mode not support 3d padding')
@SKIP_ENV_GPU(reason='reflect mode not support 3d padding')
@SKIP_ENV_ASCEND(reason='reflect mode not support 3d padding')
def test_pad_reflect_3d_padding_4d_5d_input():
    padding = (3, 3, 2, 2, 1, 1)
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'reflect')
    torch_result= F.pad(torch.tensor(data), padding, 'reflect')
    param_compare(ms_result, torch_result)

    data = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'reflect')
    torch_result= F.pad(torch.tensor(data), padding, 'reflect')
    param_compare(ms_result, torch_result)

def test_pad_replicate_1d_padding_2d_3d_input():
    padding = (2, 2)
    data = np.random.randn(2, 3, 4).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'replicate')
    torch_result= F.pad(torch.tensor(data), padding, 'replicate')
    param_compare(ms_result, torch_result)

    data = np.random.randn(3, 4).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'replicate')
    torch_result= F.pad(torch.tensor(data), padding, 'replicate')
    param_compare(ms_result, torch_result)

def test_pad_replicate_2d_padding_3d_4d_input():
    padding = (2, 2, 3, 3)
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'replicate')
    torch_result= F.pad(torch.tensor(data), padding, 'replicate')
    param_compare(ms_result, torch_result)

    data = np.random.randn(3, 4, 5).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'replicate')
    torch_result= F.pad(torch.tensor(data), padding, 'replicate')
    param_compare(ms_result, torch_result)


def test_pad_replicate_3d_padding_4d_5d_input():
    padding = (3, 3, 2, 2, 1, 1)
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'replicate')
    torch_result= F.pad(torch.tensor(data), padding, 'replicate')
    param_compare(ms_result, torch_result)

    data = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'replicate')
    torch_result= F.pad(torch.tensor(data), padding, 'replicate')
    param_compare(ms_result, torch_result)

def test_pad_circular_1d_padding_3d_input():
    padding = (2, 2)
    data = np.random.randn(2, 3, 4).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'circular')
    torch_result= F.pad(torch.tensor(data), padding, 'circular')
    param_compare(ms_result, torch_result)

def test_pad_circular_2d_padding_4d_input():
    padding = (2, 2, 3, 3)
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'circular')
    torch_result= F.pad(torch.tensor(data), padding, 'circular')
    param_compare(ms_result, torch_result)


def test_pad_circular_3d_padding_5d_input():
    padding = (3, 3, 2, 2, 1, 1)
    data = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)

    ms_result = pad(ms_torch.tensor(data), padding, 'circular')
    torch_result= F.pad(torch.tensor(data), padding, 'circular')
    param_compare(ms_result, torch_result)

@SKIP_ENV_GRAPH_MODE(reason='def pad(input, pad,...): `pad` name is the same as function name, not support GraphMode')
def test_pad_graph():
    class PadNet(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
        def forward(self, x, padding):
            output = pad(x, padding, 'circular')
            return output

    data = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)

    net = PadNet()
    padding = (3, 3, 2, 2, 1, 1)
    x = ms_torch.tensor(data)
    ms_result = net(x, padding)

    torch_result= F.pad(torch.tensor(data), padding, 'circular')
    param_compare(ms_result, torch_result)

@SKIP_ENV_GRAPH_MODE(reason='def pad(input, pad,...): `pad` name is the same as function name, not support GraphMode')
def test_pad_grad():
    class PadNet(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
        def forward(self, x, padding):
            output = pad(x, padding, 'circular')
            output = ms_torch.sum(output)
            return output

    data = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)

    net = PadNet()
    padding = (3, 3, 2, 2, 1, 1)

    torch_x = torch.tensor(data).requires_grad_(True)
    torch_out = torch.sum(torch.nn.functional.pad(torch_x, padding, 'circular'))
    torch_out.backward()
    torch_gradient = torch_x.grad

    x = ms_torch.tensor(data).requires_grad_(True)
    # Automatic differentiation method 1
    ms_out, ms_gradient = ms.ops.value_and_grad(net)(x, padding)
    param_compare(ms_out, torch_out.detach())
    param_compare(ms_gradient, torch_gradient)


def test_pad_pad():
    py_p1d = [1, torch.tensor(1)]
    py_t4d = torch.ones(3, 3, 4, 2)
    py_out_1 = F.pad(py_t4d, py_p1d, "constant", 0)

    ms_p1d = [1, ms_torch.tensor(1)]
    ms_t4d = ms_torch.ones(3, 3, 4, 2)
    ms_out_1 = pad(ms_t4d, ms_p1d, "constant", 0)
    param_compare(py_out_1, ms_out_1)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_pad_shape()
    test_pad_mode()
    test_pad_constant_value_2d_padding_4d_input()
    test_pad_constant_value_2d_padding_5d_input()
    test_pad_constant_value_3d_padding_4d_input()
    test_pad_constant_value_3d_padding_5d_input()
    test_pad_reflect_1d_padding_2d_3d_input()
    test_pad_reflect_2d_padding_3d_4d_input()
    test_pad_reflect_3d_padding_4d_5d_input()
    test_pad_replicate_1d_padding_2d_3d_input()
    test_pad_replicate_2d_padding_3d_4d_input()
    test_pad_replicate_3d_padding_4d_5d_input()
    test_pad_circular_1d_padding_3d_input()
    test_pad_circular_2d_padding_4d_input()
    test_pad_circular_3d_padding_5d_input()
    test_pad_graph()
    test_pad_grad()
    test_pad_pad()