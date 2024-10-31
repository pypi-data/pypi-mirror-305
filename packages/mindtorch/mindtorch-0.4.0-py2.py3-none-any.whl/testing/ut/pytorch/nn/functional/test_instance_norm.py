#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms

import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, param_compare
set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason='In GRAPH MODE, running_mean and running_var not support')
def test_instance_norm1():
    np_input = np.random.randn(2, 3, 4).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.instance_norm(
        ms_input, ms_running_mean, ms_running_var, ms_weight, ms_bias, use_input_stats=True)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.instance_norm(
        torch_input, torch_running_mean, torch_running_var, torch_weight, torch_bias, use_input_stats=True)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)
    param_compare(ms_running_mean, torch_running_mean, rtol=1e-3, atol=1e-5)
    param_compare(ms_running_var, torch_running_var, rtol=1e-3, atol=1e-5)


def test_instance_norm2():
    np_input = np.random.randn(2, 3, 4, 4).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.instance_norm(
        ms_input, ms_running_mean, ms_running_var, ms_weight, ms_bias, use_input_stats=False)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.instance_norm(
        torch_input, torch_running_mean, torch_running_var, torch_weight, torch_bias, use_input_stats=False)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_instance_norm3():
    np_input = np.random.randn(2, 3, 4, 4).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_result = ms_torch.nn.functional.instance_norm(
        ms_input, ms_running_mean, ms_running_var, use_input_stats=False)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_result = torch.nn.functional.instance_norm(
        torch_input, torch_running_mean, torch_running_var, use_input_stats=False)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_instance_norm4():
    np_input = np.random.randn(2, 3, 4, 4, 4).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.instance_norm(
        ms_input, ms_running_mean, ms_running_var, ms_bias, use_input_stats=False)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.instance_norm(
        torch_input, torch_running_mean, torch_running_var, torch_bias, use_input_stats=False)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_instance_norm5():
    np_input = np.random.randn(2, 3, 4, 4, 4).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_weight = ms_torch.tensor(weight)
    ms_result = ms_torch.nn.functional.instance_norm(
        ms_input, ms_running_mean, ms_running_var, ms_weight, use_input_stats=False)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_weight = torch.tensor(weight)
    torch_result = torch.nn.functional.instance_norm(
        torch_input, torch_running_mean, torch_running_var, torch_weight, use_input_stats=False)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape

@SKIP_ENV_GRAPH_MODE(reason='In GRAPH MODE, running_mean and running_var not support')
def test_instance_norm6():
    np_input = np.random.randn(2, 3, 4).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.instance_norm(
        ms_input, ms_running_mean, ms_running_var, ms_weight, ms_bias,
        use_input_stats=True, momentum=0.2, eps=1e-7)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.instance_norm(
        torch_input, torch_running_mean, torch_running_var, torch_weight, torch_bias,
        use_input_stats=True, momentum=0.2, eps=1e-7)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_instance_norm_running_mean_var_None():
    np_input = np.random.randn(2, 3, 4).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.instance_norm(
        ms_input, None, None, ms_weight, ms_bias, use_input_stats=True)

    torch_input = torch.tensor(np_input)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.instance_norm(
        torch_input, None, None, torch_weight, torch_bias, use_input_stats=True)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape

@SKIP_ENV_GRAPH_MODE(reason="assign running_mean inplace don't take effect under graph mode or jit")
def test_instance_norm_value_and_grad():
    np_input = np.random.randn(2, 3, 4).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    def _func(input, running_mean, running_var, weight, bias):
        return ms_torch.nn.functional.instance_norm(
            input, running_mean, running_var, weight, bias, use_input_stats=True)
    fun = ms.ops.value_and_grad(_func)
    ms_result, _ = fun(ms_input, ms_running_mean, ms_running_var, ms_weight, ms_bias)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.instance_norm(
        torch_input, torch_running_mean, torch_running_var, torch_weight, torch_bias, use_input_stats=True)

    assert np.allclose(ms_running_mean.numpy(), torch_running_mean.numpy())
    assert np.allclose(ms_running_var.numpy(), torch_running_var.numpy())
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape

if __name__ == "__main__":
    test_instance_norm1()
    test_instance_norm2()
    test_instance_norm3()
    test_instance_norm4()
    test_instance_norm5()
    test_instance_norm6()
    test_instance_norm_running_mean_var_None()
    test_instance_norm_value_and_grad()
