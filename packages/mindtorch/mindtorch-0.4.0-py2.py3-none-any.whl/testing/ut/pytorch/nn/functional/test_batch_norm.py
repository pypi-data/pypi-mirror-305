#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms

import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason='In GRAPH MODE, running_mean and running_var not support')
def test_batch_norm1():
    np_input = np.random.randn(8, 8, 6).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.batch_norm(
        ms_input, ms_running_mean, ms_running_var, ms_weight, ms_bias, training=True)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.batch_norm(
        torch_input, torch_running_mean, torch_running_var, torch_weight, torch_bias, training=True)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)

@SKIP_ENV_GRAPH_MODE(reason='In GRAPH MODE, running_mean and running_var not support')
def test_batch_norm2():
    np_input = np.random.randn(4, 8, 6, 5).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_result = ms_torch.nn.functional.batch_norm(
        ms_input, ms_running_mean, ms_running_var, training=True)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_result = torch.nn.functional.batch_norm(
        torch_input, torch_running_mean, torch_running_var, training=True)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)

def test_batch_norm3():
    np_input = np.random.randn(4, 8, 6, 5, 4).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_weight = ms_torch.tensor(weight)
    ms_result = ms_torch.nn.functional.batch_norm(
        ms_input, ms_running_mean, ms_running_var, weight=ms_weight, training=False)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_weight = torch.tensor(weight)
    torch_result = torch.nn.functional.batch_norm(
        torch_input, torch_running_mean, torch_running_var, weight=torch_weight, training=False)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)

@SKIP_ENV_GRAPH_MODE(reason='In GRAPH MODE, running_mean and running_var not support')
def test_batch_norm4():
    np_input = np.random.randn(10, 8, 6).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.batch_norm(
        ms_input, ms_running_mean, ms_running_var, bias=ms_bias, training=True)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.batch_norm(
        torch_input, torch_running_mean, torch_running_var, bias=torch_bias, training=True)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)

@SKIP_ENV_GRAPH_MODE(reason='In GRAPH MODE, running_mean and running_var not support')
def test_batch_norm5():
    np_input = np.random.randn(10, 8, 6).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_result = ms_torch.nn.functional.batch_norm(
        ms_input, ms_running_mean, ms_running_var, training=True)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_result = torch.nn.functional.batch_norm(
        torch_input, torch_running_mean, torch_running_var, training=True)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)

@SKIP_ENV_GRAPH_MODE(reason='In GRAPH MODE, running_mean and running_var not support')
def test_batch_norm6():
    np_input = np.random.randn(4, 8, 6, 5).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_result = ms_torch.nn.functional.batch_norm(
        ms_input, ms_running_mean, ms_running_var, training=True, momentum=0.01, eps=1e-4)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_result = torch.nn.functional.batch_norm(
        torch_input, torch_running_mean, torch_running_var, training=True, momentum=0.01, eps=1e-4)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)

def test_batch_norm_input_6d():
    np_input = np.random.randn(1, 2, 3, 4, 5, 6).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_weight = ms_torch.tensor(weight)
    ms_result = ms_torch.nn.functional.batch_norm(
        ms_input, ms_running_mean, ms_running_var, weight=ms_weight, training=False)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_weight = torch.tensor(weight)
    torch_result = torch.nn.functional.batch_norm(
        torch_input, torch_running_mean, torch_running_var, weight=torch_weight, training=False)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)


def test_batch_norm_input_running_mean_var_None():
    np_input = np.random.randn(1, 2, 3, 4).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_result = ms_torch.nn.functional.batch_norm(
        ms_input, None, None, training=True)

    torch_input = torch.tensor(np_input)
    torch_result = torch.nn.functional.batch_norm(
        torch_input, None, None, training=True)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)

def test_batch_norm_input_jit():
    np_input = np.random.randn(1, 2, 3, 4).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    @ms.jit
    def func(input, mean, var, weight, bias):
        return ms_torch.nn.functional.batch_norm(input, mean, var, weight, bias, training=True)
    ms_result = func(ms_input, None, None, None, None)

    torch_input = torch.tensor(np_input)
    torch_result = torch.nn.functional.batch_norm(
        torch_input, None, None, training=True)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)

#TODO: assign_value not support in jit
# @SKIP_ENV_GRAPH_MODE(reason='In GRAPH MODE, running_mean and running_var not support')
# def test_batch_norm_input_running_mean_var_jit():
#     np_input = np.random.randn(1, 2, 3, 4).astype(np.float32)
#     running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
#     running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
#     weight = np.random.randn(np_input.shape[1]).astype(np.float32)
#     bias = np.random.randn(np_input.shape[1]).astype(np.float32)

#     ms_input = ms_torch.tensor(np_input)
#     ms_running_mean = ms_torch.tensor(running_mean)
#     ms_running_var = ms_torch.tensor(running_var)
#     ms_weight = ms_torch.tensor(weight)
#     ms_bias = ms_torch.tensor(bias)
#     @ms.jit
#     def func(input, mean, var, weight, bias):
#         return ms_torch.nn.functional.batch_norm(input, mean, var, weight, bias, training=True)
#     ms_result = func(ms_input, ms_running_mean, ms_running_var, ms_weight, ms_bias)

#     torch_input = torch.tensor(np_input)
#     torch_running_mean = torch.tensor(running_mean)
#     torch_running_var = torch.tensor(running_var)
#     torch_weight = torch.tensor(weight)
#     torch_bias = torch.tensor(bias)
#     torch_result = torch.nn.functional.batch_norm(
#         torch_input, torch_running_mean, torch_running_var, torch_weight, torch_bias, training=True)

#     param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)

@SKIP_ENV_GRAPH_MODE(reason='In GRAPH MODE, running_mean and running_var not support')
def test_batch_norm_check_running_mean_var():
    np_input = np.random.randn(4, 8, 6, 5).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_result = ms_torch.nn.functional.batch_norm(
        ms_input, ms_running_mean, ms_running_var, training=True, momentum=0.01, eps=1e-4)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_result = torch.nn.functional.batch_norm(
        torch_input, torch_running_mean, torch_running_var, training=True, momentum=0.01, eps=1e-4)

    param_compare(ms_running_mean, torch_running_mean, rtol=1e-3, atol=1e-5)
    param_compare(ms_running_var, torch_running_var, rtol=1e-3, atol=1e-4)

def test_batch_norm_all_tensor_training_false():
    np_input = np.random.randn(1, 2, 3, 3, 3).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.tensor(running_mean)
    ms_running_var = ms_torch.tensor(running_var)
    ms_weight = ms_torch.tensor(weight)
    ms_bias = ms_torch.tensor(bias)
    ms_result = ms_torch.nn.functional.batch_norm(
        ms_input, ms_running_mean, ms_running_var, ms_weight, ms_bias, training=False)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.tensor(running_mean)
    torch_running_var = torch.tensor(running_var)
    torch_weight = torch.tensor(weight)
    torch_bias = torch.tensor(bias)
    torch_result = torch.nn.functional.batch_norm(
        torch_input, torch_running_mean, torch_running_var, torch_weight, torch_bias, training=False)

    param_compare(ms_result, torch_result, rtol=1e-3, atol=1e-5)


def test_batch_norm_all_parameter_training_True():
    np_input = np.random.randn(1, 2, 3, 3, 3).astype(np.float32)
    running_mean = np.random.randn(np_input.shape[1]).astype(np.float32)
    running_var = np.abs(np.random.randn(np_input.shape[1])).astype(np.float32)
    weight = np.random.randn(np_input.shape[1]).astype(np.float32)
    bias = np.random.randn(np_input.shape[1]).astype(np.float32)

    ms_input = ms_torch.tensor(np_input)
    ms_running_mean = ms_torch.nn.Parameter(running_mean)
    ms_running_var = ms_torch.nn.Parameter(running_var)
    ms_weight = ms_torch.nn.Parameter(weight)
    ms_bias = ms_torch.nn.Parameter(bias)
    ms_result = ms_torch.nn.functional.batch_norm(
        ms_input, ms_running_mean, ms_running_var, ms_weight, ms_bias, training=True)

    torch_input = torch.tensor(np_input)
    torch_running_mean = torch.nn.Parameter(torch.tensor(running_mean), requires_grad=False)
    torch_running_var = torch.nn.Parameter(torch.tensor(running_var), requires_grad=False)
    torch_weight = torch.nn.Parameter(torch.tensor(weight))
    torch_bias = torch.nn.Parameter(torch.tensor(bias))
    torch_result = torch.nn.functional.batch_norm(
        torch_input, torch_running_mean, torch_running_var, torch_weight, torch_bias, training=True)

    param_compare(ms_result, torch_result.detach(), rtol=1e-3, atol=1e-5)

if __name__ == "__main__":
    test_batch_norm1()
    test_batch_norm2()
    test_batch_norm3()
    test_batch_norm4()
    test_batch_norm5()
    test_batch_norm6()
    test_batch_norm_input_6d()
    test_batch_norm_input_running_mean_var_None()
    test_batch_norm_input_jit()
    test_batch_norm_input_running_mean_var_jit()
    test_batch_norm_check_running_mean_var()
    test_batch_norm_all_tensor_training_false()
    test_batch_norm_all_parameter_training_True()
