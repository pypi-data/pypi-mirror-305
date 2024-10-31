#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindtorch.torch as ms_torch
from mindtorch.torch.nn import Module, ReLU, ReLU6
import mindtorch.torch.nn as nn
import numpy as np
from mindspore import context
import mindspore as ms
import torch
import pytest

from ...utils import set_mode_by_env_config, SKIP_ENV_PYNATIVE_MODE, SKIP_ENV_GRAPH_MODE, SKIP_ENV_ASCEND, \
    param_compare, type_shape_compare, SKIP_ENV_CPU
set_mode_by_env_config()


def test_relu1():
    ms_net = ReLU()
    torch_net = torch.nn.ReLU()
    data = np.array([-1, 0, 1, -2, 4, 5, 6, 7])

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data.astype(np.float32))
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_relu2():
    ms_net = ReLU(inplace=True)
    torch_net = torch.nn.ReLU(inplace=True)
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]])

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data.astype(np.float32))
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_input.asnumpy(), torch_input.numpy())
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())


def test_hardtanh1():
    ms_net = nn.Hardtanh()
    torch_net = torch.nn.Hardtanh()
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_hardtanh2():
    ms_net = nn.Hardtanh(inplace=True)
    torch_net = torch.nn.Hardtanh(inplace=True)
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_input.asnumpy(), torch_input.numpy())
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())


@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_relu6():
    ms_net = ReLU6(inplace=True)
    torch_net = torch.nn.ReLU6(inplace=True)

    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]])

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data.astype(np.float32))
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_input.asnumpy(), torch_input.numpy())
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

def test_silu1():
    ms_net = nn.SiLU()
    torch_net = torch.nn.SiLU()

    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)
    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_silu2():
    ms_net = nn.SiLU(inplace=True)
    torch_net = torch.nn.SiLU(inplace=True)

    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)
    torch_input = torch.tensor(data)
    ms_input = ms_torch.tensor(data)

    torch_output = torch_net(torch_input)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_input.asnumpy(), torch_input.numpy())
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())


def test_hardswish1():
    ms_net = nn.Hardswish()
    torch_net = torch.nn.Hardswish()
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())


@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_hardswish2():
    ms_net = nn.Hardswish(inplace=True)
    torch_net = torch.nn.Hardswish(inplace=True)
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    ms_input = ms_torch.tensor(data)

    torch_output = torch_net(torch_input)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_input.asnumpy(), torch_input.numpy())
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())


def test_leakyReLU1():
    ms_net = nn.LeakyReLU(negative_slope=1.2)
    torch_net = torch.nn.LeakyReLU(negative_slope=1.2)
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())


@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_leakyReLU2():
    ms_net = nn.LeakyReLU(negative_slope=0.1, inplace=True)
    torch_net = torch.nn.LeakyReLU(negative_slope=0.1, inplace=True)

    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)
    torch_input = torch.tensor(data)
    ms_input = ms_torch.tensor(data)

    torch_output = torch_net(torch_input)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_input.asnumpy(), torch_input.numpy())
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())


def test_sigmoid():
    ms_net = nn.Sigmoid()
    torch_net = torch.nn.Sigmoid()
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())


def test_logsigmoid():
    ms_net = nn.LogSigmoid()
    torch_net = torch.nn.LogSigmoid()
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-5)


def test_elu():
    ms_net = nn.ELU()
    torch_net = torch.nn.ELU()
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-5)

def test_elu_alpha_2():
    ms_net = nn.ELU(alpha=2)
    torch_net = torch.nn.ELU(alpha=2)
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-5)

@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_elu_alpha_inplace():
    ms_net = nn.ELU(inplace=True)
    torch_net = torch.nn.ELU(inplace=True)
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-5)
    assert np.allclose(ms_input.asnumpy(), torch_input.numpy(), atol=1e-5)

def test_rrelu():
    ms_net = nn.RReLU()
    torch_net = torch.nn.RReLU()
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-5)

def test_selu():
    data = np.random.rand(2, 3).astype(np.float32)

    ms_net = nn.SELU(inplace=False)
    torch_net = torch.nn.SELU(inplace=False)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-5)

def test_celu():
    data = np.random.rand(2, 3).astype(np.float32)

    ms_net = nn.CELU(inplace=False)
    torch_net = torch.nn.CELU(inplace=False)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-5)


def test_gelu1():
    data = np.random.rand(2, 3).astype(np.float32)

    ms_net = nn.GELU()
    torch_net = torch.nn.GELU()

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)
    param_compare(ms_output, torch_output, atol=1e-5)


def test_gelu2():
    data = np.random.rand(2, 3).astype(np.float32)

    ms_net = nn.GELU('tanh')
    torch_net = torch.nn.GELU('tanh')

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)
    param_compare(ms_output, torch_output)


def test_mish():
    data = np.random.rand(2, 3).astype(np.float32)

    ms_net = nn.Mish(inplace=False)
    torch_net = torch.nn.Mish(inplace=False)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    if context.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-3)
    else:
        assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-5)


def test_softshrink():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_net = torch.nn.Softshrink(lambd=1)
    ms_net = nn.Softshrink(lambd=1)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    param_compare(ms_output, torch_output, atol=1e-5)

def test_tanh():
    ms_net = nn.Tanh()
    torch_net = torch.nn.Tanh()
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)
    torch_output1 = torch_net(torch_input.double())
    torch_output2 = torch_net(torch_input.long())

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)
    ms_output1 = ms_net(ms_input.double())
    ms_output2 = ms_net(ms_input.long())

    param_compare(ms_output, torch_output, atol=1e-3)
    param_compare(ms_output1, torch_output1)
    param_compare(ms_output2, torch_output2, atol=1e-3)

def test_tanh_complex():
    np_1 = np.random.randn(3, 4).astype(np.complex64)
    np_2 = (np.random.randn(3, 4) * 1j).astype(np.complex64)
    ms_input = ms_torch.tensor(np_1 + np_2)
    ms_net = nn.Tanh()
    ms_output = ms_net(ms_input)

    torch_input = torch.tensor(np_1 + np_2)
    torch_net = torch.nn.Tanh()
    torch_output = torch_net(torch_input)

    param_compare(ms_output, torch_output)

def test_tanhshrink1():
    ms_net = nn.Tanhshrink()
    torch_net = torch.nn.Tanhshrink()
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    param_compare(ms_output, torch_output, atol=1e-3)

def test_tanhshrink2():
    ms_net = nn.Tanhshrink()
    torch_net = torch.nn.Tanhshrink()
    data1 = np.random.randn(5) * 5

    torch_input1 = torch.tensor(data1)
    torch_output1 = torch_net(torch_input1)
    torch_output2 = torch_net(torch_input1.long())

    ms_input1 = ms_torch.tensor(data1)
    ms_output1 = ms_net(ms_input1)
    ms_output2 = ms_net(ms_input1.long())

    param_compare(ms_output1, torch_output1, atol=1e-3)
    param_compare(ms_output2, torch_output2, atol=1e-3)

def test_tanhshrink_complex():
    np_1 = np.random.randn(3, 4).astype(np.complex64)
    np_2 = (np.random.randn(3, 4) * 1j).astype(np.complex64)

    torch_input1 = torch.tensor(np_1 + np_2)
    torch_net = torch.nn.Tanhshrink()
    torch_output1 = torch_net(torch_input1)

    ms_input1 = ms_torch.tensor(np_1 + np_2)
    ms_net = nn.Tanhshrink()
    ms_output1 = ms_net(ms_input1)

    param_compare(ms_output1, torch_output1, atol=1e-5)

def test_threshold1():
    ms_net = nn.Threshold(threshold=3.5, value=20)
    torch_net = torch.nn.Threshold(threshold=3.5, value=20)
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_threshold2():
    #ms_net = nn.Threshold(threshold=3.5, value=3, inplace=True)
    #torch_net = torch.nn.Threshold(threshold=3.5, value=3, inplace=True)
    #data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)
    ms_net = nn.Threshold(threshold=1, value=9, inplace=True)
    torch_net = torch.nn.Threshold(threshold=1, value=9, inplace=True)
    data = np.ones((5, 6, 8)).astype(np.uint8)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype


def test_softmax1():
    ms_net = nn.Softmax(dim=-1)
    torch_net = torch.nn.Softmax(dim=-1)
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    param_compare(ms_output, torch_output)


def test_softmax2():
    ms_net = nn.Softmax(dim=1)
    torch_net = torch.nn.Softmax(dim=1)
    data = np.array([[[-1, 0, 1, -2, 4, 5, 6, 7]],
                     [[-1, 0, 1, -2, 4, 5, 6, 7]],
                     [[5, 4, 1, 2, 3, 4, -5, -6]]
                     ]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    param_compare(ms_output, torch_output)

@SKIP_ENV_ASCEND(reason='Softmax not support float64 input on Ascend')
def test_softmax3():
    ms_net = nn.Softmax(dim=2)
    torch_net = torch.nn.Softmax(dim=2)
    data = np.random.randn(2, 3, 3)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    param_compare(ms_output, torch_output)

def test_softmax4():
    ms_net = nn.Softmax()
    torch_net = torch.nn.Softmax()
    data = np.random.randn(2, 3, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    param_compare(ms_output, torch_output)

def test_logsoftmax1():
    ms_net = nn.LogSoftmax(dim=-1)
    torch_net = torch.nn.LogSoftmax(dim=-1)
    data = np.array([[-1, 0, 1, -2, 4, 5, 6, 7]]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    param_compare(ms_output, torch_output)


def test_logsoftmax2():
    ms_net = nn.LogSoftmax(dim=0)
    torch_net = torch.nn.LogSoftmax(dim=0)
    data = np.array([[[-1, 0, 1, -2, 4, 5, 6, 7]],
                     [[-1, 0, 1, -2, 4, 5, 6, 7]],
                     [[5, 4, 1, 2, 3, 4, -5, -6]]
                     ]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    param_compare(ms_output, torch_output)

def test_logsoftmax3():
    ms_net = nn.LogSoftmax()
    torch_net = torch.nn.LogSoftmax()
    data = np.random.randn(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    param_compare(ms_output, torch_output, atol=1e-5)

def test_softmin1():
    ms_net = nn.Softmin(dim=1)
    torch_net = torch.nn.Softmin(dim=1)
    data = np.array([[[-1, 0, 1, -2, 4, 5, 6, 7]],
                     [[-1, 0, 1, -2, 4, 5, 6, 7]],
                     [[5, 4, 1, 2, 3, 4, -5, -6]]
                     ]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    param_compare(ms_output, torch_output)

def test_softmin2():
    ms_net1 = nn.Softmin()
    torch_net1 = torch.nn.Softmin()
    data1 = np.random.randn(2, 3, 3).astype(np.float32)

    torch_input1 = torch.tensor(data1)
    torch_output1 = torch_net1(torch_input1)

    ms_input1 = ms_torch.tensor(data1)
    ms_output1 = ms_net1(ms_input1)

    param_compare(ms_output1, torch_output1)

def test_softsign_fp32():
    ms_net = nn.Softsign()
    torch_net = torch.nn.Softsign()
    data = np.array([[-1, 0, 1, -2, 4, -5, 6, -7]],).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output1 = torch_net(torch_input)
    torch_output2 = torch_net(torch_input.long())

    ms_input = ms_torch.tensor(data)
    ms_output1 = ms_net(ms_input)
    ms_output2 = ms_net(ms_input.long())

    param_compare(ms_output1, torch_output1)
    param_compare(ms_output2, torch_output2)

@SKIP_ENV_ASCEND(reason='Softsign not support float64 input on Ascend')
def test_softsign_fp64():
    ms_net = nn.Softsign()
    torch_net = torch.nn.Softsign()
    data = np.random.randn(5).astype(np.float64) * 5

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    param_compare(ms_output, torch_output)

@SKIP_ENV_GRAPH_MODE(reason="ms.ops.narrow has some error now.")
def test_glu():
    ms_net = nn.GLU(dim=0)
    torch_net = torch.nn.GLU(dim=0)
    data = np.array([[[-1, 0, 1, -2]],
                     [[2, 2, 3, 4]]
                     ]).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())


def test_hardshrink():
    ms_net = nn.Hardshrink(lambd=0.8)
    torch_net = torch.nn.Hardshrink(lambd=0.8)
    data = np.random.randn(3, 4, 5).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    assert np.allclose(ms_output.numpy(), torch_output.numpy())
    assert ms_output.numpy().dtype == torch_output.numpy().dtype


def test_hardsigmoid():
    ms_net = nn.Hardsigmoid()
    torch_net = torch.nn.Hardsigmoid()

    data = np.array([[-4, -3, 1, 0, -1.5, 2.8, 3.7, 100]]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_net(ms_input)

    torch_input = torch.tensor(data)
    torch_out = torch_net(torch_input)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_multi_head_attention1():
    _embed_dim = 8
    _target_seq_length = 3
    _batch_size = 2
    _source_seq_length = 6
    _num_heads = 1

    ms_net = nn.MultiheadAttention(embed_dim=_embed_dim, num_heads=_num_heads, dropout=0.5)
    torch_net = torch.nn.MultiheadAttention(embed_dim=_embed_dim, num_heads=_num_heads, dropout=0.5)

    query = np.random.randn(_target_seq_length, _batch_size, _embed_dim).astype(np.float32)
    key = np.random.randn(_source_seq_length, _batch_size, _embed_dim).astype(np.float32)
    value = np.random.randn(_source_seq_length, _batch_size, _embed_dim).astype(np.float32)

    torch_query = torch.tensor(query)
    torch_key = torch.tensor(key)
    torch_value = torch.tensor(value)
    torch_output = torch_net(torch_query, torch_key, torch_value, need_weights=False)

    ms_query = ms_torch.tensor(query)
    ms_key = ms_torch.tensor(key)
    ms_val = ms_torch.tensor(value)
    ms_output = ms_net(ms_query, ms_key, ms_val, need_weights=False)

    assert ms_output[0].shape == torch_output[0].shape

def test_multi_head_attention2():
    _embed_dim = 10
    _target_seq_length = 6
    _batch_size = 5
    _source_seq_length = 8
    _num_heads = 2

    ms_net = nn.MultiheadAttention(embed_dim=_embed_dim, num_heads=_num_heads, dropout=0.5, batch_first=True)
    torch_net = torch.nn.MultiheadAttention(embed_dim=_embed_dim, num_heads=_num_heads, dropout=0.5, batch_first=True)

    query = np.random.randn(_batch_size, _target_seq_length, _embed_dim).astype(np.float32)
    key = np.random.randn(_batch_size, _source_seq_length, _embed_dim).astype(np.float32)
    value = np.random.randn(_batch_size, _source_seq_length, _embed_dim).astype(np.float32)

    torch_query = torch.tensor(query)
    torch_key = torch.tensor(key)
    torch_value = torch.tensor(value)
    torch_output = torch_net(torch_query, torch_key, torch_value, need_weights=False)

    ms_query = ms_torch.tensor(query)
    ms_key = ms_torch.tensor(key)
    ms_val = ms_torch.tensor(value)
    ms_output = ms_net(ms_query, ms_key, ms_val, need_weights=False)

    assert ms_output[0].shape == torch_output[0].shape

def test_prelu():
    input = np.array([[[[0.1, 0.6], [0.9, 0.9]]]]).astype(np.float32)
    weight_init = 0.25
    torch_input = torch.tensor(input)
    torch_out = torch.nn.PReLU(num_parameters=1, init=weight_init)(torch_input)
    ms_torch_input = ms_torch.tensor(input)
    ms_torch_out = ms_torch.nn.PReLU(num_parameters=1, init=weight_init)(ms_torch_input)
    assert np.allclose(torch_out.detach().numpy(), ms_torch_out.detach().numpy())

    input1 = np.array([0.1, 0.6, 0.9]).astype(np.float32)
    weight_init = 0.25
    torch_input1 = torch.tensor(input1)
    torch_out1 = torch.nn.PReLU(num_parameters=1, init=weight_init)(torch_input1)
    ms_torch_input1 = ms_torch.tensor(input1)
    ms_torch_out1 = ms_torch.nn.PReLU(num_parameters=1, init=weight_init)(ms_torch_input1)
    assert np.allclose(torch_out1.detach().numpy(), ms_torch_out1.detach().numpy())
    assert torch_out1.detach().numpy().shape == ms_torch_out1.detach().numpy().shape
    assert torch_out1.detach().numpy().dtype == ms_torch_out1.detach().numpy().dtype

    input2 = np.array([0.1]).astype(np.float32)
    weight_init = 0.25
    torch_input2 = torch.tensor(input2)
    torch_out2 = torch.nn.PReLU(num_parameters=1, init=weight_init)(torch_input2)
    ms_torch_input2 = ms_torch.tensor(input2)
    ms_torch_out2 = ms_torch.nn.PReLU(num_parameters=1, init=weight_init)(ms_torch_input2)
    assert np.allclose(torch_out2.detach().numpy(), ms_torch_out2.detach().numpy())
    assert torch_out2.detach().numpy().shape == ms_torch_out2.detach().numpy().shape
    assert torch_out2.detach().numpy().dtype == ms_torch_out2.detach().numpy().dtype

    input3 = 100.0
    weight_init = 0.25
    torch_input3 = torch.tensor(input3)
    ms_torch_input3 = ms_torch.tensor(input3)
    torch_out3 = torch.nn.PReLU(num_parameters=1, init=weight_init)(torch_input3)
    ms_torch_out3 = ms_torch.nn.PReLU(num_parameters=1, init=weight_init)(ms_torch_input3)
    assert np.allclose(torch_out3.detach().numpy(), ms_torch_out3.detach().numpy())
    assert torch_out3.detach().numpy().shape == ms_torch_out3.detach().numpy().shape
    assert torch_out3.detach().numpy().dtype == ms_torch_out3.detach().numpy().dtype


def test_prelu_grad():
    net = ms_torch.nn.PReLU()
    x = ms_torch.Tensor([1, 2, -3])
    grad_fn = ms.grad(net, grad_position=None, weights=net.trainable_params())
    grad = grad_fn(x)[0]
    assert np.count_nonzero(grad.asnumpy()) != 0

@SKIP_ENV_ASCEND(reason='Softplus not support float64 input on Ascend')
def test_softplus():
    ms_net = nn.Softplus(beta=2, threshold=15)
    torch_net = torch.nn.Softplus(beta=2, threshold=15)
    data = np.random.randn(2, 3, 4, 5).astype(np.float64)*50

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    ms_net1 = nn.Softplus(threshold=15.)
    torch_net1 = torch.nn.Softplus(threshold=15.)
    torch_output1 = torch_net1(torch_input.double())
    ms_output1 = ms_net1(ms_input.double())

    param_compare(ms_output, torch_output, atol=1e-5)
    param_compare(ms_output1, torch_output1, atol=1e-5)

def test_softplus_no_param():
    ms_net = nn.Softplus()
    torch_net = torch.nn.Softplus()
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)*50

    torch_input = torch.tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_net(ms_input)

    ms_net1 = nn.Softplus(threshold=15.)
    torch_net1 = torch.nn.Softplus(threshold=15.)
    torch_output1 = torch_net1(torch_input)
    ms_output1 = ms_net1(ms_input)

    param_compare(ms_output, torch_output, atol=1e-5)
    param_compare(ms_output1, torch_output1, atol=1e-5)

@SKIP_ENV_ASCEND(reason='Softmax2d not support float64 input on Ascend')
def test_softmax2d_fp64():
    ms_net = nn.Softmax2d()
    torch_net = torch.nn.Softmax2d()

    data2 = np.random.randn(3, 4, 5)*50
    torch_input2 = torch.tensor(data2)
    torch_output2 = torch_net(torch_input2)
    ms_input2 = ms_torch.tensor(data2)
    ms_output2 = ms_net(ms_input2)

    param_compare(ms_output2, torch_output2)

def test_softmax2d_fp32():
    ms_net = nn.Softmax2d()
    torch_net = torch.nn.Softmax2d()
    data1 = np.random.randn(2, 3, 4, 5).astype(np.float32)*50

    torch_input1 = torch.tensor(data1)
    torch_output1 = torch_net(torch_input1)

    ms_input1 = ms_torch.tensor(data1)
    ms_output1 = ms_net(ms_input1)

    param_compare(ms_output1, torch_output1)

def _scaled_dot_attn_ref(Q, K, V, dims, unseen_mask=None, key_padding_mask=None,
                            average_attn_weights=False):
    """ Numpy-based reference implementation of scaled dot attention
    for testing"""

    QKT = _batchmatmul(
        Q,
        np.transpose(K, axes=[0, 1, 3, 2])
        / np.sqrt(dims[3], dtype=np.float32),  # divide by sqrt(d_head)
    )
    b1, b2, s1, s2 = QKT.shape
    if unseen_mask is not None or key_padding_mask is not None:
        # assert s1 == s2
        for i in range(b1):
            for j in range(b2):
                for m in range(s1):
                    for n in range(s2):
                        if unseen_mask is not None and unseen_mask[m][n] == 0:
                            QKT[i, j, m, n] = -np.inf
                        if key_padding_mask is not None and key_padding_mask[i][n]:
                            QKT[i, j, m, n] = -np.inf

    reference = _softmax(QKT)
    ref_attn_weight = reference
    if average_attn_weights:
        ref_attn_weight = np.sum(ref_attn_weight, axis=1) / b2
    reference = _batchmatmul(reference, V)
    return reference, ref_attn_weight

def _batchmatmul(a, b):  # batchmatmul over 4 dim matrix
    """ Numpy-based batch matrix multiply over 4 dim matrix"""
    assert a.shape[0] == b.shape[0]
    assert a.shape[1] == b.shape[1]
    retval = np.zeros(
        (a.shape[0], a.shape[1], a.shape[2], b.shape[3]), dtype=np.float32
    )
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            retval[i, j, :, :] = np.matmul(a[i, j, :, :], b[i, j, :, :])
    return retval

def _softmax(x):  # softmax over 4 dim matrix
    """ Numpy-based reference softmax over 4 dim matrix"""
    np.seterr(invalid='ignore')
    output = np.zeros(x.shape, dtype=np.float64)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            for k in range(x.shape[2]):
                x_curr = x[i, j, k, :]
                e_x = np.exp(x_curr - np.amax(x_curr))
                output[i, j, k, :] = e_x / np.sum(e_x)
    return output

def _split_heads_ref(X, dims, nheads, d_head):
    X_split = np.reshape(X, dims[:2] + [nheads, d_head])
    X_split_transposed = np.transpose(X_split, [0, 2, 1, 3])
    reference = np.reshape(X_split_transposed, [dims[0], nheads, dims[1], d_head])
    return reference

def _combine_heads_ref(X, dims, nheads, d_head):
    X_transposed = np.transpose(X, [0, 2, 1, 3])
    reference = np.reshape(X_transposed, dims[:2] + [nheads * d_head])
    return reference

def _fc(X, X_weight, X_bias):
    X_fc_b = X_bias.detach().numpy()
    X_fc_w = X_weight.detach().numpy()
    return np.matmul(X, np.transpose(X_fc_w)) + X_fc_b

def _multihead_attn_test_helper(add_key_padding_mask=False, add_bias_kv=False, add_zero_attn=False,
                                saved_kv=False, same_embed_dim=False,
                                average_attn_weights=False):
    batch_sz = 2
    seq_len = 2
    d_head = 3
    nheads = 3
    d_model = d_head * nheads
    if same_embed_dim:
        kv_dim = d_model
    else:
        kv_dim = 5
    dims = [batch_sz, seq_len, kv_dim]

    np.random.seed(1)  # output=nan is not equal

    saved_k = None
    saved_k_tensor = None
    saved_v = None
    saved_v_tensor = None
    if saved_kv:
        saved_k = np.random.rand(batch_sz * nheads, seq_len, d_head)
        saved_k_tensor = ms_torch.from_numpy(saved_k).to(ms_torch.float32)
        saved_v = np.random.rand(batch_sz * nheads, seq_len, d_head)
        saved_v_tensor = ms_torch.from_numpy(saved_v).to(ms_torch.float32)

    key_padding_mask = None
    key_padding_mask_tensor = None
    if add_key_padding_mask:
        seq_mask = np.random.randint(0, 2, (1, seq_len))
        key_padding_mask = (np.repeat(seq_mask, batch_sz, axis=0) == 1)
        key_padding_mask_tensor = ms_torch.from_numpy(key_padding_mask)
    decoder_state = np.random.rand(batch_sz, d_model)
    K = np.random.rand(*dims)
    V = K
    Q = np.expand_dims(decoder_state, 1)
    attn_mask = np.random.randint(0, 2, size=(1, seq_len))
    attn_mask_tensor = ms_torch.from_numpy(attn_mask).float()
    attn_mask_tensor = attn_mask_tensor.masked_fill(attn_mask_tensor == 0, float('-inf'))
    attn_mask_tensor = attn_mask_tensor.masked_fill(attn_mask_tensor > 0, float('0.0'))
    attn_mask_tensor = attn_mask_tensor.double()

    decoder_state_tensor = ms_torch.from_numpy(decoder_state).to(ms_torch.float32)
    source_hid_tensor = ms_torch.from_numpy(K).to(ms_torch.float32).transpose(0, 1)

    multihead_attn_module = nn.MultiheadAttention(d_model, nheads,
                                                add_bias_kv=add_bias_kv,
                                                add_zero_attn=add_zero_attn,
                                                kdim=kv_dim, vdim=kv_dim)
    if add_bias_kv:
        bias_k = multihead_attn_module.bias_k.detach().numpy()
        bias_v = multihead_attn_module.bias_v.detach().numpy()
    else:
        bias_k = None
        bias_v = None

    _Q = decoder_state_tensor.unsqueeze(1).transpose(0, 1)
    _V = source_hid_tensor
    _K = source_hid_tensor

    if multihead_attn_module._qkv_same_embed_dim:
        result, result_weight = nn.functional.multi_head_attention_forward(
            _Q, _K, _V,
            d_model, nheads,
            multihead_attn_module.in_proj_weight, multihead_attn_module.in_proj_bias,
            multihead_attn_module.bias_k, multihead_attn_module.bias_v,
            multihead_attn_module.add_zero_attn, multihead_attn_module.dropout,
            multihead_attn_module.out_proj.weight, multihead_attn_module.out_proj.bias,
            multihead_attn_module.training, key_padding_mask_tensor, True, attn_mask_tensor,
            static_k=saved_k_tensor, static_v=saved_v_tensor,
            average_attn_weights=average_attn_weights,
        )
    else:
        result, result_weight = nn.functional.multi_head_attention_forward(
            _Q, _K, _V,
            d_model, nheads,
            None, multihead_attn_module.in_proj_bias,
            multihead_attn_module.bias_k, multihead_attn_module.bias_v,
            multihead_attn_module.add_zero_attn, multihead_attn_module.dropout,
            multihead_attn_module.out_proj.weight, multihead_attn_module.out_proj.bias,
            multihead_attn_module.training, key_padding_mask_tensor, True, attn_mask_tensor,
            True, multihead_attn_module.q_proj_weight,
            multihead_attn_module.k_proj_weight, multihead_attn_module.v_proj_weight,
            static_k=saved_k_tensor, static_v=saved_v_tensor,
            average_attn_weights=average_attn_weights,
        )

    result = result.squeeze(0).detach().numpy()

    if multihead_attn_module._qkv_same_embed_dim:
        q_proj_weight = multihead_attn_module.in_proj_weight[:d_model]
        k_proj_weight = multihead_attn_module.in_proj_weight[d_model:(d_model * 2)]
        v_proj_weight = multihead_attn_module.in_proj_weight[(d_model * 2):]
    else:
        q_proj_weight = multihead_attn_module.q_proj_weight
        k_proj_weight = multihead_attn_module.k_proj_weight
        v_proj_weight = multihead_attn_module.v_proj_weight

    Q_fc = _fc(Q, q_proj_weight, multihead_attn_module.in_proj_bias[:d_model])
    K_fc = _fc(K, k_proj_weight, multihead_attn_module.in_proj_bias[d_model:(d_model * 2)])
    V_fc = _fc(V, v_proj_weight, multihead_attn_module.in_proj_bias[(d_model * 2):])

    if add_bias_kv:
        K_fc = np.concatenate((K_fc, np.repeat(bias_k, K_fc.shape[0], axis=0)), axis=1)
        V_fc = np.concatenate((V_fc, np.repeat(bias_v, V_fc.shape[0], axis=0)), axis=1)
        if attn_mask is not None:
            attn_mask = np.concatenate((attn_mask, np.ones([1, 1])), axis=1)
        if key_padding_mask is not None:
            key_padding_mask = np.concatenate(
                (key_padding_mask, np.full((batch_sz, 1), False, dtype=bool)), axis=1)
        dims[1] += 1
    Q_split = _split_heads_ref(
        Q_fc, [batch_sz, 1, d_model], nheads, d_head
    )

    if saved_k is not None:
        K_split = np.reshape(saved_k, [dims[0], nheads, dims[1], d_head])
    else:
        K_split = _split_heads_ref(K_fc, dims, nheads, d_head)

    if saved_v is not None:
        V_split = np.reshape(saved_v, [dims[0], nheads, dims[1], d_head])
    else:
        V_split = _split_heads_ref(V_fc, dims, nheads, d_head)

    if add_zero_attn:
        dims[1] += 1
        K_split = np.concatenate(
            (K_split, np.zeros([K_split.shape[0], K_split.shape[1], 1, K_split.shape[3]])), axis=2)
        V_split = np.concatenate(
            (V_split, np.zeros([V_split.shape[0], V_split.shape[1], 1, V_split.shape[3]])), axis=2)

        if attn_mask is not None:
            attn_mask = np.concatenate((attn_mask, np.ones([1, 1])), axis=1)

        if key_padding_mask is not None:
            key_padding_mask = np.concatenate(
                (key_padding_mask, np.full((batch_sz, 1), False, dtype=bool)), axis=1)
    attn_heads, ref_attn_weight = _scaled_dot_attn_ref(
        Q=Q_split,
        K=K_split,
        V=V_split,
        dims=Q_split.shape,
        unseen_mask=attn_mask,
        key_padding_mask=key_padding_mask,
        average_attn_weights=average_attn_weights
    )
    combined_attn_heads = _combine_heads_ref(
        X=attn_heads, dims=[batch_sz, 1], nheads=nheads, d_head=d_head
    )

    reference = _fc(combined_attn_heads, multihead_attn_module.out_proj.weight,
                    multihead_attn_module.out_proj.bias)
    reference = np.squeeze(reference, axis=1)

    # result = reference
    assert tuple(result.shape) == (batch_sz, d_model)
    np.testing.assert_allclose(result, reference, atol=1e-5)

    # result_weight = ref_attn_weight
    result_weight = result_weight.detach().numpy()
    assert tuple(result_weight.shape) == tuple(ref_attn_weight.shape)
    np.testing.assert_allclose(result_weight, ref_attn_weight, atol=1e-5)

def test_multihead_attn_add_bias_kv():
    _multihead_attn_test_helper(add_bias_kv=True, average_attn_weights=True)

def test_multihead_attn_add_zero_attn():
    _multihead_attn_test_helper(add_zero_attn=True)

def test_multihead_attn_no_masking():
    _multihead_attn_test_helper()

def test_multihead_attn_key_padding_mask():
    _multihead_attn_test_helper(add_key_padding_mask=False, average_attn_weights=True)

def test_multihead_attn_saved_kv():
    _multihead_attn_test_helper(saved_kv=True)

def test_multihead_attn_add_bias_kv_zero_attn():
    _multihead_attn_test_helper(add_key_padding_mask=False, add_bias_kv=True,
                                add_zero_attn=True, average_attn_weights=True)

def test_multihead_attn_all_arguments1():
    _multihead_attn_test_helper(add_key_padding_mask=False, add_zero_attn=True,
                                saved_kv=True, average_attn_weights=True)

def test_multihead_attn_all_arguments2():
    # expected to raise error: The bias_k cannot be added to static_k
    with pytest.raises(ValueError):
        _multihead_attn_test_helper(add_key_padding_mask=True, add_bias_kv=True,
                                    add_zero_attn=True, saved_kv=True, average_attn_weights=True)

def test_multihead_attn_all_arguments3():
    _multihead_attn_test_helper(add_key_padding_mask=False, add_zero_attn=True,
                                saved_kv=True, same_embed_dim=True)

def test_multihead_attn_no_bias():
    embed_dim = 8
    num_heads = 4
    mha = nn.MultiheadAttention(embed_dim, num_heads, bias=False)

    # Verify that bias=False applies to both in and out projection layers.
    assert mha.in_proj_bias is None
    assert mha.out_proj.bias is None

@SKIP_ENV_CPU(reason="[CI] ms2.4.0 0920 still not pass, need to be fixed.")
def test_multihead_attn_bool_mask():
    input = ms_torch.tensor([[[20., 30., 40., 50.]]], device='cpu', dtype=ms_torch.float)
    ms_output = nn.functional.multi_head_attention_forward(input, input, input, embed_dim_to_check=4,
                                                             num_heads=2,
                                                             in_proj_weight=ms_torch.rand(12, 4),
                                                             in_proj_bias=ms_torch.zeros(12),
                                                             bias_k=None, bias_v=None,
                                                             add_zero_attn=False,
                                                             dropout_p=0.,
                                                             out_proj_weight=ms_torch.rand(4, 4),
                                                             out_proj_bias=ms_torch.zeros(4),
                                                             training=True,
                                                             key_padding_mask=ms_torch.tensor([[True]]),
                                                             use_separate_proj_weight=False,
                                                             average_attn_weights=True)
    torch_input = torch.tensor([[[20., 30., 40., 50.]]], device='cpu', dtype=torch.float)
    torch_output = torch.nn.functional.multi_head_attention_forward(torch_input, torch_input, torch_input,
                                                             embed_dim_to_check=4,
                                                             num_heads=2,
                                                             in_proj_weight=torch.rand(12, 4),
                                                             in_proj_bias=torch.zeros(12),
                                                             bias_k=None, bias_v=None,
                                                             add_zero_attn=False,
                                                             dropout_p=0.,
                                                             out_proj_weight=torch.rand(4, 4),
                                                             out_proj_bias=torch.zeros(4),
                                                             training=True,
                                                             key_padding_mask=torch.tensor([[True]]),
                                                             use_separate_proj_weight=False,
                                                             average_attn_weights=True)
    param_compare(ms_output, torch_output, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="key-value assignment only support on pynative mode.")
def test_multi_head_attention_kwargs():
    _embed_dim = 8
    _target_seq_length = 3
    _batch_size = 2
    _source_seq_length = 6
    _num_heads = 1

    ms_net = nn.MultiheadAttention(embed_dim=_embed_dim, num_heads=_num_heads, dropout=0.5)
    torch_net = torch.nn.MultiheadAttention(embed_dim=_embed_dim, num_heads=_num_heads, dropout=0.5)

    query = np.random.randn(_target_seq_length, _batch_size, _embed_dim).astype(np.float32)
    key = np.random.randn(_source_seq_length, _batch_size, _embed_dim).astype(np.float32)
    value = np.random.randn(_source_seq_length, _batch_size, _embed_dim).astype(np.float32)

    torch_query = torch.tensor(query)
    torch_key = torch.tensor(key)
    torch_value = torch.tensor(value)
    torch_output = torch_net(query=torch_query, key=torch_key, value=torch_value, need_weights=False)
    torch_output1 = torch_net(torch_query, torch_key, value=torch_value, need_weights=False)

    ms_query = ms_torch.tensor(query)
    ms_key = ms_torch.tensor(key)
    ms_val = ms_torch.tensor(value)
    ms_output = ms_net(query=ms_query, key=ms_key, value=ms_val, need_weights=False)
    ms_output1 = ms_net(ms_query, ms_key, value=ms_val, need_weights=False)

    type_shape_compare(ms_output[0], torch_output[0].detach())
    type_shape_compare(ms_output1[0], torch_output1[0].detach())


if __name__ == '__main__':
    set_mode_by_env_config()
    test_relu1()
    test_relu2()
    test_hardtanh1()
    test_hardtanh2()
    test_relu6()
    test_silu1()
    test_silu2()
    test_hardswish1()
    test_hardswish2()
    test_leakyReLU1()
    test_leakyReLU2()
    test_sigmoid()
    test_logsigmoid()
    test_elu()
    test_rrelu()
    test_selu()
    test_celu()
    test_gelu1()
    test_gelu2()
    test_mish()
    test_softshrink()
    test_tanh()
    test_tanhshrink1()
    test_tanhshrink2()
    test_threshold1()
    test_threshold2()
    test_softmax1()
    test_softmax2()
    test_softmax3()
    test_softmax4()
    test_logsoftmax1()
    test_logsoftmax2()
    test_logsoftmax3()
    test_softmin1()
    test_softmin2()
    test_softsign_fp32()
    test_softsign_fp64()
    test_glu()
    test_hardshrink()
    test_multi_head_attention1()
    test_multi_head_attention2()
    test_prelu()
    test_softplus()
    test_softplus_no_param()
    test_softmax2d_fp64()
    test_softmax2d_fp32()
    test_prelu_grad()
    test_multihead_attn_add_zero_attn()  # Test MultiheadAttention with add_zero_attn
    test_multihead_attn_add_bias_kv()  # Test MultiheadAttention with add_bias_kv
    test_multihead_attn_no_masking()   # Test MultiheadAttention without masking
    test_multihead_attn_bool_mask()
    # TODO: add_key_padding_mask to be set to True after ms bug fixed
    test_multihead_attn_key_padding_mask()  # Test MultiheadAttention with src lengths
    test_multihead_attn_saved_kv()  # Test MultiheadAttention with static kv.
    test_multihead_attn_add_bias_kv_zero_attn()  # Test MultiheadAttention with bias_kv and zero_attn.
    test_multihead_attn_all_arguments1()  # Test MultiheadAttention with all the argument.
    test_multihead_attn_all_arguments2()  # Test MultiheadAttention with all the argument.
    test_multihead_attn_all_arguments3()  # Test MultiheadAttention with all the argument.
    test_multihead_attn_no_bias()
    test_multi_head_attention_kwargs()
    test_tanh_complex()
    test_tanhshrink_complex()
