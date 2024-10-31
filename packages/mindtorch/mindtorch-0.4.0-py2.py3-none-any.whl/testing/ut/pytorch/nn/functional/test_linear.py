#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindtorch.torch as ms_torch
import torch
import numpy as np

from ....utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()


def test_linear1():
    data = np.ones((1, 2, 5)).astype(np.float32)
    weight = np.ones((3, 5)).astype(np.float32)

    ms_data = ms_torch.tensor(data)
    ms_weight = ms_torch.tensor(weight)
    ms_out = ms_torch.nn.functional.linear(ms_data, ms_weight)

    torch_data = torch.tensor(data)
    torch_weight = torch.tensor(weight)
    torch_out = torch.nn.functional.linear(torch_data, torch_weight)

    param_compare(ms_out, torch_out)

def test_linear2():
    data = np.ones((1, 2, 5)).astype(np.float32)
    weight = np.ones((3, 5)).astype(np.float32)
    bias = np.ones((3)).astype(np.float32)

    ms_data = ms_torch.tensor(data)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_out = ms_torch.nn.functional.linear(ms_data, ms_weight, bias=ms_bias)

    torch_data = torch.tensor(data)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_out = torch.nn.functional.linear(torch_data, torch_weight, bias=torch_bias)

    param_compare(ms_out, torch_out)


def test_linear3():
    data = np.ones((1, 2, 5)).astype(np.float32)
    weight = np.ones((5)).astype(np.float32)

    ms_data = ms_torch.tensor(data)
    ms_weight = ms_torch.tensor(weight)
    ms_out = ms_torch.nn.functional.linear(ms_data, ms_weight)

    torch_data = torch.tensor(data)
    torch_weight = torch.tensor(weight)
    torch_out = torch.nn.functional.linear(torch_data, torch_weight)

    param_compare(ms_out, torch_out)


def test_bilinear():
    data1 = np.random.randn(2, 2, 3)
    data2 = np.random.randn(2, 2, 5)
    weight = np.random.randn(4, 3, 5)
    bias = np.random.randn(4)

    torch_input1 = torch.Tensor(data1)
    torch_input2 = torch.Tensor(data2)
    torch_weight = torch.Tensor(weight)
    torch_bias = torch.Tensor(bias)
    torch_out = torch.nn.functional.bilinear(torch_input1, torch_input2, torch_weight, torch_bias)

    ms_input1 = ms_torch.Tensor(data1)
    ms_input2 = ms_torch.Tensor(data2)
    ms_weight = ms_torch.Tensor(weight)
    ms_bias = ms_torch.Tensor(bias)
    ms_out = ms_torch.nn.functional.bilinear(ms_input1, ms_input2, ms_weight, ms_bias)

    param_compare(ms_out, torch_out, atol=1e-4, rtol=1e-4)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_linear1()
    test_linear2()
    test_linear3()
    test_bilinear()
