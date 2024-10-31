#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import torch
import mindtorch.torch as ms_torch

from ...utils import SKIP_ENV_ASCEND, SKIP_ENV_CPU, SKIP_ENV_GPU, set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()


def test_acos_int():
    np_array = np.random.rand(3, 2).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.acos()

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_tensor.acos()

    param_compare(torch_out, ms_out, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_acos_():
    x = [0.3348, -0.5889,  0.2005, -0.1584]
    torch_x = torch.tensor(x)
    torch_x.acos_()

    ms_x = ms_torch.tensor(x)
    ms_x.acos_()
    param_compare(torch_x, ms_x, equal_nan=True)

@SKIP_ENV_ASCEND(reason="Ascend outputs differ from pytorch outputs when input equals to 0")
def test_acosh_int():
    np_array = np.random.rand(2, 3, 2).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.acosh(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.acosh(ms_tensor)

    param_compare(torch_out, ms_out, equal_nan=True)

@SKIP_ENV_CPU(reason="Testcase only used on Ascend")
@SKIP_ENV_GPU(reason="Testcase only used on Ascend")
def test_acosh_int_ascend():
    np_array = (np.random.rand(2, 3, 2) * 5 + 5).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.acosh(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.acosh(ms_tensor)

    param_compare(torch_out, ms_out, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_acosh_():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float64) * 50 + 2

    torch_tensor = torch.tensor(np_array)
    torch_tensor.acosh_()

    ms_tensor = ms_torch.tensor(np_array)
    ms_tensor.acosh_()

    param_compare(torch_tensor, ms_tensor, equal_nan=True)

@SKIP_ENV_ASCEND(reason="When input is not in [-1,1], ascend returns wrong answer")
def test_arccos_int():
    np_array = np.array([1, 2, -3, 100]).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.arccos(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.arccos(ms_tensor)

    param_compare(torch_out, ms_out, equal_nan=True)

@SKIP_ENV_CPU(reason="Testcase only used on Ascend")
@SKIP_ENV_GPU(reason="Testcase only used on Ascend")
def test_arccos_int_ascend():
    np_array = np.array([1, 0, -1]).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.arccos(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.arccos(ms_tensor)

    param_compare(torch_out, ms_out, atol=1e-3, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_arccos_():
    np_array = np.array([0.3348, -0.5889, 0.2005, -0.1584])

    torch_tensor = torch.tensor(np_array)
    torch_tensor.arccos_()

    ms_tensor = ms_torch.tensor(np_array)
    ms_tensor.arccos_()

    param_compare(torch_tensor, ms_tensor, equal_nan=True)

@SKIP_ENV_ASCEND(reason="Ascend outputs differ from pytorch outputs when input equals to 0")
def test_arccosh_int():
    np_array = np.random.rand(1, 4, 3, 2).astype(np.int64)
    np_array[0, 0, 0, 0] = 1
    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.arccosh()

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_tensor.arccosh()
    param_compare(torch_out, ms_out, equal_nan=True)

@SKIP_ENV_CPU(reason="Testcase only used on Ascend")
@SKIP_ENV_GPU(reason="Testcase only used on Ascend")
def test_arccosh_int_ascend():
    np_array = (np.random.rand(1, 4, 3, 2) * 5 + 5).astype(np.int64)
    np_array[0, 0, 0, 0] = 1
    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.arccosh()

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_tensor.arccosh()
    param_compare(torch_out, ms_out, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_arccosh_():
    np_array = np.array([1.3192, 1.9915, 1.9674, 1.7151])

    torch_tensor = torch.tensor(np_array)
    torch_tensor.arccosh_()

    ms_tensor = ms_torch.tensor(np_array)
    ms_tensor.arccosh_()

    param_compare(torch_tensor, ms_tensor, equal_nan=True)

def test_arcsin():
    np_array = np.random.rand(1, 2, 3, 4).astype(np.float64) * 5

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.arcsin()

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_tensor.arcsin()

    param_compare(torch_out, ms_out, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_arcsin_():
    np_array = np.array([-0.5962, 1.4985, -0.4396, 1.4525])

    torch_tensor = torch.tensor(np_array)
    torch_tensor.arcsin_()

    ms_tensor = ms_torch.tensor(np_array)
    ms_tensor.arcsin_()

    param_compare(torch_tensor, ms_tensor, equal_nan=True)

def test_arcsinh_int():
    x = np.array([-5.0, 1.5, 3.0, 100.0])

    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch_x.arcsinh()
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_x.arcsinh()
    param_compare(torch_out, ms_out, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_arcsinh_():
    x = np.array([0.1606, -1.4267, -1.0899, -1.0250])

    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_x.arcsinh_()
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_x.arcsinh_()
    param_compare(ms_x, torch_x, equal_nan=True)

def test_asin_int():
    a1 = np.random.randn(4).astype(np.int32)
    torch_a1 = torch.tensor(a1)
    torch_out1 = torch_a1.asin()
    ms_torch_a1 = ms_torch.tensor(a1)
    ms_torch_out1 = ms_torch_a1.asin()
    param_compare(torch_out1, ms_torch_out1, equal_nan=True, atol=1e-05)

def test_asin():
    a2 = np.random.randn(3, 2).astype(np.float32)
    torch_a2 = torch.tensor(a2)
    torch_out2 = torch_a2.asin()
    ms_torch_a2 = ms_torch.tensor(a2)
    ms_torch_out2 = ms_torch_a2.asin()
    param_compare(torch_out2, torch_out2, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="When input is not in [-1,1], ascend returns wrong answer")
def test_asin_():
    x = np.array([-0.5962, 1.4985, -0.4396, 1.4525])

    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_x.asin_()
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_x.asin_()
    param_compare(ms_x, torch_x, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
@SKIP_ENV_CPU(reason="Testcase only used on Ascend")
@SKIP_ENV_GPU(reason="Testcase only used on Ascend")
def test_asin_ascend():
    x = np.random.uniform(low=-1, high=1, size=5).astype(np.float32)

    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_x.asin_()
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_x.asin_()
    param_compare(ms_x, torch_x, atol=1e-4, equal_nan=True)

def test_asinh_int():
    a2 = np.random.randn(3, 2).astype(np.int32)
    torch_a2 = torch.tensor(a2)
    torch_out2 = torch_a2.asinh()
    ms_torch_a2 = ms_torch.tensor(a2)
    ms_torch_out2 = ms_torch_a2.asinh()
    param_compare(torch_out2, ms_torch_out2, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_asinh_():
    x = [0.1606, -1.4267, -1.0899, -1.0250]
    torch_x = torch.tensor(x)
    torch_x.asinh_()

    ms_x = ms_torch.tensor(x)
    ms_x.asinh_()
    param_compare(ms_x, torch_x, equal_nan=True)

def test_atan_int():
    a1 = np.random.randn(4).astype(np.uint8)
    torch_a1 = torch.tensor(a1)
    torch_out1 = torch_a1.atan()
    ms_torch_a1 = ms_torch.tensor(a1)
    ms_torch_out1 = ms_torch_a1.atan()
    param_compare(torch_out1, ms_torch_out1, equal_nan=True)

def test_atan():
    a2 = np.random.randn(3, 2).astype(np.float32)
    torch_a2 = torch.tensor(a2)
    torch_out2 = torch_a2.atan()
    ms_torch_a2 = ms_torch.tensor(a2)
    ms_torch_out2 = ms_torch_a2.atan()
    param_compare(torch_out2, ms_torch_out2, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_atan_():
    x = [0.2341, 0.2539, -0.6256, -0.6448]
    torch_x = torch.tensor(x)
    torch_x.atan_()

    ms_x = ms_torch.tensor(x)
    ms_x.atan_()
    param_compare(ms_x, torch_x, equal_nan=True)

def test_arctan():
    np_array = np.random.rand(1, 2, 3, 4).astype(np.float32) * 5 - 2

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.arctan()

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_tensor.arctan()
    param_compare(torch_out, ms_out, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_arctan_():
    x = [0.2341, 0.2539, -0.6256, -0.6448]
    torch_x = torch.tensor(x)
    torch_x.arctan_()

    ms_x = ms_torch.tensor(x)
    ms_x.arctan_()
    param_compare(ms_x, torch_x, equal_nan=True)

@SKIP_ENV_ASCEND(reason="Ascend outputs differ from pytorch outputs when inputs contains zero")
def test_atan2_int():
    x = np.random.randn(2).astype(np.int64)
    y = np.random.randn(2, 2).astype(np.int64)
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out1 = torch_x.atan2(torch_y)
    ms_torch_x = ms_torch.tensor(x)
    ms_torch_y = ms_torch.tensor(y)
    ms_torch_out1 = ms_torch_x.atan2(ms_torch_y)
    param_compare(torch_out1, ms_torch_out1, equal_nan=True)

@SKIP_ENV_CPU(reason="Testcase only used on Ascend")
@SKIP_ENV_GPU(reason="Testcase only used on Ascend")
def test_atan2_int_ascend():
    x = (np.random.rand(2) * 2 + 1).astype(np.int64)
    y = (np.random.rand(2, 2) * 2 + 1).astype(np.int64)
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out1 = torch_x.atan2(torch_y)
    ms_torch_x = ms_torch.tensor(x)
    ms_torch_y = ms_torch.tensor(y)
    ms_torch_out1 = ms_torch_x.atan2(ms_torch_y)
    param_compare(torch_out1, ms_torch_out1, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_atan2_():
    x = [0.9041, 0.0196, -0.3108, -2.4423]
    y = [0.9833, 0.0811, -1.9743, -1.4151]
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_x.atan2_(torch_y)

    ms_x = ms_torch.tensor(x)
    ms_y = ms_torch.tensor(y)
    ms_x.atan2_(ms_y)
    param_compare(ms_x, torch_x, equal_nan=True)

def test_arctan2():
    np_array = np.random.rand(1, 4, 5, 6).astype(np.float32)
    np_other = np.random.rand(1, 4, 5, 6).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out = torch_tensor.arctan2(torch_other)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_out = ms_tensor.arctan2(ms_other)
    param_compare(ms_out, torch_out, equal_nan=True, atol=1e-4)


@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_arctan2_():
    y = [0.9041, 0.0196, -0.3108, -2.4423]
    x = [0.9833, 0.0811, -1.9743, -1.4151]
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_x.arctan2_(torch_y)

    ms_x = ms_torch.tensor(x)
    ms_y = ms_torch.tensor(y)
    ms_x.arctan2_(ms_y)
    param_compare(ms_x, torch_x, equal_nan=True)

def test_atanh():
    np_array = np.array([0, -0.5, 0.3, 0.0, 0.99]).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.atanh()

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_tensor.atanh()
    param_compare(torch_out, ms_out, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_atanh_():
    x = [-0.9385, 0.2968, -0.8591, -0.1871]
    torch_x = torch.tensor(x)
    torch_x.atanh_()

    ms_x = ms_torch.tensor(x)
    ms_x.atanh_()
    param_compare(ms_x, torch_x, equal_nan=True)

@SKIP_ENV_ASCEND(reason="-1 or 1 will create inf value, which is not support on Ascend")
def test_arctanh_int():
    x = np.random.randn(2).astype(np.int64)

    torch_x = torch.tensor(x)
    torch_out = torch_x.arctanh()
    ms_x = ms_torch.tensor(x)
    ms_out = ms_x.arctanh()
    param_compare(ms_out, torch_out, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_arctanh_():
    x = np.array([-0.5, 0.3, 0.0, 0.99])

    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_x.arctanh_()
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_x.arctanh_()
    param_compare(torch_x, ms_x, equal_nan=True)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_acos_int()
    test_acos_()
    test_acosh_int()
    test_acosh_int_ascend()
    test_acosh_()
    test_arccos_int()
    test_arccos_int_ascend()
    test_arccos_()
    test_arccosh_int()
    test_arccosh_int_ascend()
    test_arccosh_()
    test_arcsin()
    test_arcsin_()
    test_arcsinh_int()
    test_arcsinh_()
    test_asin_int()
    test_asin()
    test_asin_()
    test_asin_ascend()
    test_asinh_int()
    test_asinh_()
    test_atan_int()
    test_atan()
    test_atan2_int()
    test_atan2_int_ascend()
    test_atan2_()
    test_arctan2()
    test_arctan2_()
    test_atanh()
    test_atanh_()
    test_arctanh_int()
    test_arctanh_()
