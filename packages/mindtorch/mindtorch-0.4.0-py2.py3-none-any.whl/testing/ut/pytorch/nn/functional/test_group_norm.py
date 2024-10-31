#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms

import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()



def test_group_norm1():
    np_input = np.random.randn(10, 8, 6).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.group_norm(
        ms_input, num_groups=2, weight=ms_weight, bias=ms_bias, eps=1e-5)

    torch_input = torch.tensor(np_input)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.group_norm(
        torch_input, num_groups=2, weight=torch_weight, bias=torch_bias, eps=1e-5)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)


def test_group_norm2():
    np_input = np.random.randn(10, 8, 6).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_result = ms_torch.nn.functional.group_norm(
        ms_input, num_groups=2, eps=1e-5)

    torch_input = torch.tensor(np_input)
    torch_result = torch.nn.functional.group_norm(
        torch_input, num_groups=2, eps=1e-5)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)


def test_group_norm3():
    np_input = np.random.randn(10, 8, 6, 6).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.group_norm(
        ms_input, num_groups=2, bias=ms_bias, eps=1e-5)

    torch_input = torch.tensor(np_input)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.group_norm(
        torch_input, num_groups=2, bias=torch_bias, eps=1e-5)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)


def test_group_norm4():
    np_input = np.random.randn(10, 8, 6, 6, 6).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(weight)
    ms_result = ms_torch.nn.functional.group_norm(
        ms_input, num_groups=2, weight=ms_weight, eps=1e-5)

    torch_input = torch.tensor(np_input)
    torch_weight = torch.tensor(weight)
    torch_result = torch.nn.functional.group_norm(
        torch_input, num_groups=2, weight=torch_weight, eps=1e-5)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)


def test_group_norm_dynamic_shape():
    np_input = np.random.randn(10, 8, 6, 6).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_bias = ms_torch.tensor(bias)

    class Net(ms_torch.nn.Module):
        def __init__(self, num_groups, bias, eps):
            super().__init__()
            self.num_groups = num_groups
            self.bias = bias
            self.eps = eps

        def forward(self, input):
            return ms_torch.nn.functional.group_norm(input, num_groups=self.num_groups, bias=self.bias, eps=self.eps)

    net = Net(2, ms_bias, 1e-5)
    net.set_inputs(ms.Tensor(shape=[None, None, None, None], dtype=ms.float32))
    ms_result = net(ms_input)

    torch_input = torch.tensor(np_input)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.group_norm(
        torch_input, num_groups=2, bias=torch_bias, eps=1e-5)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)

if __name__ == "__main__":
    test_group_norm1()
    test_group_norm2()
    test_group_norm3()
    test_group_norm4()
    test_group_norm_dynamic_shape()
    