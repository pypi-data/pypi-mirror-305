#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms

import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import param_compare, set_mode_by_env_config, graph_lax_level
set_mode_by_env_config()



def test_layer_norm1():
    np_input = np.random.randn(10, 8, 6).astype(np.float32)
    normalized_shape = (8, 6)
    weight = np.random.randn(*normalized_shape).astype(np.float32)
    bias = np.random.randn(*normalized_shape).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.layer_norm(
        ms_input, normalized_shape, ms_weight, ms_bias)

    torch_input = torch.tensor(np_input)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.layer_norm(
        torch_input, normalized_shape, torch_weight, torch_bias)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_layer_norm2():
    np_input = np.random.randn(10, 8, 6, 6).astype(np.float32)
    normalized_shape = (8, 6, 6)
    weight = np.random.randn(*normalized_shape).astype(np.float32)
    bias = np.random.randn(*normalized_shape).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.layer_norm(
        ms_input, normalized_shape, ms_weight, ms_bias)

    torch_input = torch.tensor(np_input)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.layer_norm(
        torch_input, normalized_shape, torch_weight, torch_bias)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_layer_norm3():
    np_input = np.random.randn(10, 8, 6, 6, 6).astype(np.float32)
    normalized_shape = (8, 6, 6, 6)
    weight = np.random.randn(*normalized_shape).astype(np.float32)
    bias = np.random.randn(*normalized_shape).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.layer_norm(
        ms_input, normalized_shape, ms_weight, ms_bias)

    torch_input = torch.tensor(np_input)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.layer_norm(
        torch_input, normalized_shape, torch_weight, torch_bias)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-4)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_layer_norm4():
    np_input = np.random.randn(10, 8, 6, 6, 6).astype(np.float32)
    normalized_shape = (8, 6, 6, 6)
    bias = np.random.randn(*normalized_shape).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.layer_norm(
        ms_input, normalized_shape, ms_bias)

    torch_input = torch.tensor(np_input)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.layer_norm(
        torch_input, normalized_shape, torch_bias)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_layer_norm5():
    np_input = np.random.randn(10, 8, 6, 6, 6).astype(np.float32)
    normalized_shape = (8, 6, 6, 6)
    weight = np.random.randn(*normalized_shape).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(weight)
    ms_result = ms_torch.nn.functional.layer_norm(ms_input, normalized_shape, ms_weight)

    torch_input = torch.tensor(np_input)
    torch_weight = torch.tensor(weight)
    torch_result = torch.nn.functional.layer_norm(torch_input, normalized_shape, torch_weight)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_layer_norm6():
    np_input = np.random.randn(10, 8, 6).astype(np.float32)
    normalized_shape = (6,)
    weight = np.random.randn(*normalized_shape).astype(np.float32)
    bias = np.random.randn(*normalized_shape).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.layer_norm(
        ms_input, normalized_shape, ms_weight, ms_bias, eps=1e-7)

    torch_input = torch.tensor(np_input)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.layer_norm(
        torch_input, normalized_shape, torch_weight, torch_bias, eps=1e-7)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape

def test_layer_norm_int_eps():
    np_input = np.random.randn(10, 8, 6).astype(np.float32)
    normalized_shape = (6,)
    weight = np.random.randn(*normalized_shape).astype(np.float32)
    bias = np.random.randn(*normalized_shape).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.layer_norm(
        ms_input, normalized_shape, ms_weight, ms_bias, eps=1)

    torch_input = torch.tensor(np_input)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.layer_norm(
        torch_input, normalized_shape, torch_weight, torch_bias, eps=1)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)

def test_layer_norm_graph_dynamic_shape():
    np_input = np.random.randn(10, 8, 6).astype(np.float32)
    normalized_shape = (8, 6)
    weight = np.random.randn(*normalized_shape).astype(np.float32)
    bias = np.random.randn(*normalized_shape).astype(np.float32)

    class Net(ms_torch.nn.Module):
        def __init__(self, shape, weight, bias):
            super().__init__()
            self.shape = shape
            self.weight = weight
            self.bias = bias

        def forward(self, input):
            return ms_torch.nn.functional.layer_norm(input, self.shape, self.weight, self.bias, eps=1e-7)

    ms_input = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)

    net = Net(normalized_shape, ms_weight, ms_bias)
    input_dyn = ms.Tensor(shape=[None, None, None], dtype=ms.float32)
    net.set_inputs(input_dyn)
    ms_result = net(ms_input)

    torch_input = torch.tensor(np_input)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.layer_norm(
        torch_input, normalized_shape, torch_weight, torch_bias, eps=1e-7)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


if __name__ == "__main__":
    test_layer_norm1()
    test_layer_norm2()
    test_layer_norm3()
    test_layer_norm4()
    test_layer_norm5()
    test_layer_norm6()
    test_layer_norm_graph_dynamic_shape()
    test_layer_norm_int_eps()