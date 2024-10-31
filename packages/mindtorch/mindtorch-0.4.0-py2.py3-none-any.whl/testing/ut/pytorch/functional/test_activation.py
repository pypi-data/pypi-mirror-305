#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torch.nn.functional as t_fun
import torch
import numpy as np
from mindspore import context
import mindtorch.torch as ms_torch
import mindtorch.torch.nn.functional as msa_fun

from ...utils import SKIP_ENV_ASCEND, set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, param_compare, \
                     is_test_under_ascend_context, TestNet

set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_rrelu():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.rrelu(torch_input, inplace=True)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.rrelu)
    ms_output = msa_net(ms_input, inplace=True)
    param_compare(torch_output, ms_output)

@SKIP_ENV_GRAPH_MODE(reason="inpalce operation only support on pynative mode.")
def test_rrelu_():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    _ = t_fun.rrelu_(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.rrelu_)
    _ = msa_net(ms_input)
    param_compare(torch_input, ms_input)

@SKIP_ENV_ASCEND(reason="selu currently not support float64 on Ascend")
def test_selu_fp64():
    data = np.random.rand(2, 2).astype(np.float64)

    torch_input = torch.tensor(data)
    torch_output = t_fun.selu(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.selu)
    ms_output = msa_net(ms_input)
    param_compare(ms_output, torch_output)

def test_selu():
    data = np.random.rand(3, 5).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.selu(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.selu)
    ms_output = msa_net(ms_input)
    param_compare(ms_output, torch_output)

@SKIP_ENV_GRAPH_MODE(reason="nn.selu() inpalce operation only support on pynative mode.")
@SKIP_ENV_ASCEND(reason="selu currently not support float64 on Ascend")
def test_selu_inplace_fp64():
    data = np.random.rand(2, 3).astype(np.float64)

    torch_input = torch.tensor(data)
    _ = t_fun.selu(torch_input, True)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.selu)
    _ = msa_net(ms_input, True)
    param_compare(ms_input, torch_input)

@SKIP_ENV_GRAPH_MODE(reason="nn.selu() inpalce operation only support on pynative mode.")
def test_selu_inplace():
    data = np.random.rand(3, 5).astype(np.float32)

    torch_input = torch.tensor(data)
    _ = t_fun.selu(torch_input, True)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.selu)
    _ = msa_net(ms_input, True)
    param_compare(ms_input, torch_input)

def test_celu():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.celu(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.celu)
    ms_output = msa_net(ms_input)
    param_compare(ms_output, torch_output)

def test_celu_alpha():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.celu(torch_input, -2)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.celu)
    ms_output = msa_net(ms_input, -2)
    param_compare(ms_output, torch_output)

@SKIP_ENV_GRAPH_MODE(reason="nn.celu() inpalce operation only support on pynative mode.")
def test_celu_alpha_inplace():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    _ = t_fun.celu(torch_input, -2, True)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.celu)
    _ = msa_net(ms_input, -2, True)
    param_compare(ms_input, torch_input)

def test_gelu():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.gelu(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.gelu)
    ms_output = msa_net(ms_input)
    if is_test_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-4)
    else:
        param_compare(ms_output, torch_output)

@SKIP_ENV_ASCEND(reason="selu currently not support float64 on Ascend")
def test_gelu_tanh_fp64():
    data = np.random.rand(2, 2).astype(np.float64)

    torch_input = torch.tensor(data)
    torch_output = t_fun.gelu(torch_input, approximate='tanh')

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.gelu)
    ms_output = msa_net(ms_input, approximate='tanh')
    param_compare(ms_output, torch_output)

def test_gelu_tanh():
    data = np.random.rand(3, 5).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.gelu(torch_input, approximate='tanh')

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.gelu)
    ms_output = msa_net(ms_input, approximate='tanh')
    param_compare(ms_output, torch_output)

def test_mish():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.mish(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.mish)
    ms_output = msa_net(ms_input)
    if context.get_context('device_target') == 'Ascend':
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_softshrink():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.softshrink(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.softshrink)
    ms_output = msa_net(ms_input)
    param_compare(ms_output, torch_output)


def test_relu():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.relu(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.relu)
    ms_output = msa_net(ms_input)
    param_compare(ms_output, torch_output)


@SKIP_ENV_GRAPH_MODE(reason="inpalce operation only support on pynative mode.")
def test_relu_():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    _ = t_fun.relu_(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.relu_)
    _ = msa_net(ms_input)
    param_compare(torch_input, ms_input)

def test_hardtanh():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.hardtanh(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.hardtanh)
    ms_output = msa_net(ms_input)
    param_compare(ms_output, torch_output)

@SKIP_ENV_GRAPH_MODE(reason="inpalce operation only support on pynative mode.")
def test_hardtanh_():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    _ = t_fun.hardtanh_(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.hardtanh_)
    _ = msa_net(ms_input)
    param_compare(torch_input, ms_input)


def test_hardswish():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.hardswish(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.hardswish)
    ms_output = msa_net(ms_input)
    param_compare(ms_output, torch_output)


def test_relu6():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.relu6(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.relu6)
    ms_output = msa_net(ms_input)
    param_compare(ms_output, torch_output)


def test_leaky_relu():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = t_fun.leaky_relu(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.leaky_relu)
    ms_output = msa_net(ms_input)
    param_compare(ms_output, torch_output)

@SKIP_ENV_GRAPH_MODE(reason="inpalce operation only support on pynative mode.")
def test_leaky_relu_():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    _ = t_fun.leaky_relu_(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.leaky_relu_)
    _ = msa_net(ms_input)
    param_compare(torch_input, ms_input)

def test_prelu():
    input = np.random.rand(1, 3, 32, 32).astype(np.float32)
    weight = np.random.rand(1).astype(np.float32)

    torch_input = torch.tensor(input)
    torch_weight = torch.tensor(weight)
    torch_output = t_fun.prelu(torch_input, torch_weight)
    ms_input = ms_torch.tensor(input)
    ms_weight = ms_torch.tensor(weight)
    msa_net = TestNet(msa_fun.prelu)
    ms_output = msa_net(ms_input, ms_weight)
    param_compare(ms_output, torch_output)

@SKIP_ENV_GRAPH_MODE(reason="inpalce operation only support on pynative mode.")
def test_elu_():
    data = np.random.rand(2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    _ = t_fun.elu_(torch_input)

    ms_input = ms_torch.tensor(data)
    msa_net = TestNet(msa_fun.elu_)
    _ = msa_net(ms_input)

    param_compare(torch_input, ms_input, atol=1e-5)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_rrelu()
    test_selu()
    test_selu_fp64()
    test_selu_inplace()
    test_selu_inplace_fp64()
    test_celu()
    test_gelu()
    test_mish()
    test_softshrink()
    test_relu()
    test_hardtanh()
    test_prelu()
    test_elu_()
    test_leaky_relu_()
    test_relu_()
    test_rrelu_()
    test_gelu_tanh()
    test_gelu_tanh_fp64()