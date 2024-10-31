#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context
from ...utils import SKIP_ENV_ASCEND, SKIP_ENV_GRAPH_MODE, SKIP_ENV_PYNATIVE_MODE, SKIP_ENV_ASCEND_GRAPH_MODE, \
    SKIP_ENV_CPU, SKIP_ENV_GPU
from ...utils import set_mode_by_env_config, param_compare, is_test_under_ascend_context, type_shape_compare, \
    graph_lax_level, enable_backward, number_shape_compare
set_mode_by_env_config()

def test_range1():
    ms_result = ms_torch.range(1, 10)
    torch_result = torch.range(1, 10)
    param_compare(ms_result, torch_result)
    ms_result = ms_torch.range(1, 10, 2)
    torch_result = torch.range(1, 10, 2)
    param_compare(ms_result, torch_result)


def test_range2():
    ms_result = ms_torch.range(1.0, 3, 0.5)
    torch_result = torch.range(1.0, 3, 0.5)
    param_compare(ms_result, torch_result)
    ms_result = ms_torch.range(1.0, 5.5, 0.3)
    torch_result = torch.range(1.0, 5.5, 0.3)
    param_compare(ms_result, torch_result)


def test_astensor():
    a = np.array([1, 2, 3])
    torch_r = torch.as_tensor(a)

    ms_r = ms_torch.as_tensor(a)

    param_compare(torch_r, ms_r)


def test_zeros_like():
    input_t = torch.empty(2, 3)
    torch_r1 = torch.zeros_like(input_t)
    torch_r2 = torch.zeros_like(input_t, dtype=torch.float32)
    torch_r3 = torch.zeros_like(input_t, dtype=torch.int32)

    input_ms = ms_torch.empty(2, 3)
    ms_r1 = ms_torch.zeros_like(input_ms)
    ms_r2 = ms_torch.zeros_like(input_ms, dtype=ms_torch.float32)
    ms_r3 = ms_torch.zeros_like(input_ms, dtype=ms_torch.int32)

    param_compare(torch_r1, ms_r1)
    param_compare(torch_r2, ms_r2)
    param_compare(torch_r3, ms_r3)


def test_ones_like():
    input_t = torch.empty(2, 3)
    torch_r1 = torch.ones_like(input_t)

    input_ms = ms_torch.empty(2, 3)
    ms_r1 = ms_torch.ones_like(input_ms)

    input_t2 = torch.tensor([False, True])
    input_ms2 = ms_torch.tensor([False, True])
    torch_r2 = torch.ones_like(input_t2, dtype=bool)
    ms_r2 = ms_torch.ones_like(input_ms2, dtype=bool)
    torch_r3 = torch.ones_like(input_t2, dtype=torch.float32)
    ms_r3 = ms_torch.ones_like(input_ms2, dtype=ms_torch.float32)
    torch_r4 = torch.ones_like(input_t, dtype=torch.float32)
    ms_r4 = ms_torch.ones_like(input_ms, dtype=ms_torch.float32)
    param_compare(torch_r1, ms_r1)
    param_compare(torch_r2, ms_r2)
    param_compare(torch_r3, ms_r3)
    param_compare(torch_r4, ms_r4)



def test_empty_like():
    np_array1 = np.ones((2, 3)).astype(np.int32)
    input_t = torch.tensor(np_array1)
    torch_r = torch.empty_like(input_t)

    input_ms = ms_torch.tensor(np_array1)
    ms_r = ms_torch.empty_like(input_ms)

    type_shape_compare(torch_r, ms_r)

@SKIP_ENV_ASCEND(reason="empty_like currently not support float64 and complex128 on Ascend")
def test_empty_like_fp64():
    np_array1 = np.ones((2, 3)).astype(np.float64)
    input_t = torch.tensor(np_array1)
    torch_r = torch.empty_like(input_t)

    input_ms = ms_torch.tensor(np_array1)
    ms_r = ms_torch.empty_like(input_ms)

    type_shape_compare(torch_r, ms_r)

def test_full():
    torch_r1 = torch.full((2, 3), 3.141592)
    ms_r1 = ms_torch.full((2, 3), 3.141592)
    torch_r2 = torch.full((2, 3), 3)
    ms_r2 = ms_torch.full((2, 3), 3)
    torch_r3 = torch.full((2, 3), 3, dtype=torch.float32)
    ms_r3 = ms_torch.full((2, 3), 3, dtype=ms_torch.float32)
    param_compare(torch_r1, ms_r1)
    param_compare(torch_r2, ms_r2)
    param_compare(torch_r3, ms_r3)

def test_full_like():
    input_t = torch.full((2, 3), 3.141592)
    torch_r1 = torch.full_like(input_t, 0.5)
    torch_r2 = torch.full_like(input_t, 2)
    torch_r3 = torch.full_like(input_t, 2, dtype=torch.float32)
    torch_r4 = torch.full_like(input_t, 2, dtype=torch.complex64)

    input_ms = ms_torch.full((2, 3), 3.141592)
    ms_r1 = ms_torch.full_like(input_ms, 0.5)
    ms_r2 = ms_torch.full_like(input_ms, 2)
    ms_r3 = ms_torch.full_like(input_ms, 2, dtype=ms_torch.float32)
    ms_r4 = ms_torch.full_like(input_ms, 2, dtype=ms_torch.complex64)
    param_compare(torch_r1, ms_r1)
    param_compare(torch_r2, ms_r2)
    param_compare(torch_r3, ms_r3)
    param_compare(torch_r4, ms_r4)


def test_where():
    x = torch.randn(3, 2).to(torch.float32)
    y = torch.ones(3, 2)
    output1 = torch.where(x > 0, x, y)
    x1 = torch.randn(2, 2, dtype=torch.double)
    output2 = torch.where(x1 > 0, x1, 0.)

    x_m = ms.Tensor(x.numpy())
    y_m = ms.Tensor(y.numpy())
    output1_ms = ms_torch.where(x_m > 0, x_m, y_m)
    x1_m = ms.Tensor(x1.numpy())
    output2_ms = ms_torch.where(x1_m > 0, x1_m, 0.)

    param_compare(output1, output1_ms)
    param_compare(output2, output2_ms)

@SKIP_ENV_ASCEND(reason='where not support float64 input on Ascend')
def test_where_float64():
    x = torch.randn(3, 2)
    y = torch.ones(3, 2)
    output1 = torch.where(x > 0, x, y)
    x1 = torch.randn(2, 2, dtype=torch.double)
    output2 = torch.where(x1 > 0, x1, 0.)

    x_m = ms.Tensor(x.numpy())
    y_m = ms.Tensor(y.numpy())
    output1_ms = ms_torch.where(x_m > 0, x_m, y_m)
    x1_m = ms.Tensor(x1.numpy())
    output2_ms = ms_torch.where(x1_m > 0, x1_m, 0.)

    param_compare(output1, output1_ms)
    param_compare(output2, output2_ms)


def test_where2():
    np_array1 = np.array([[-4, -3, -5],[-6, -7, -8]])
    np_array2 = np.array([1, 1, 2])
    x1 = torch.tensor(np_array1)
    y1 = torch.tensor(np_array2)
    x1_m = ms_torch.tensor(np_array1)
    y1_m = ms_torch.tensor(np_array2)

    output1 = torch.where(x1 > 0)
    output2 = torch.where(x1 > 0, x1, y1)
    output1_ms = ms_torch.where(x1_m > 0)
    output2_ms = ms_torch.where(x1_m > 0, x1_m, y1_m)

    param_compare(output1, output1_ms)
    param_compare(output2, output2_ms)


def test_where3():
    output = torch.where(torch.zeros(2,3, dtype=torch.bool))
    output_ms = ms_torch.where(ms_torch.zeros(2,3, dtype=ms_torch.bool))
    param_compare(output, output_ms)

def test_seed():
    torch.manual_seed(12)
    x = torch.empty((1, 4))
    t_r = torch.nn.init.uniform(x)

    torch.seed()
    t_r1 = torch.nn.init.uniform(x)
    seed_v = torch.initial_seed()

    ms_torch.manual_seed(12)
    ms_r = ms.ops.uniform((1, 4), ms.Tensor(1.0, ms.float32), ms.Tensor(2.0, ms.float32))

    ms_torch.seed()
    ms_r1 = ms.ops.uniform((1, 4), ms.Tensor(1.0, ms.float32), ms.Tensor(2.0, ms.float32))

    assert np.allclose(t_r.shape, ms_r.shape)
    assert np.allclose(t_r1.shape, ms_r1.shape)



def test_rand():
    t_r1 = torch.rand(4)
    t_r2 = torch.rand(2, 3)
    t_r3 = torch.rand((2, 3))
    t_r4 = torch.rand([2, 3])

    ms_r1 = ms_torch.rand(4)
    ms_r2 = ms_torch.rand(2, 3)
    ms_r3 = ms_torch.rand((2, 3))
    ms_r4 = ms_torch.rand([2, 3])

    type_shape_compare(t_r1, ms_r1)
    type_shape_compare(t_r2, ms_r2)
    type_shape_compare(t_r3, ms_r3)
    type_shape_compare(t_r4, ms_r4)

def test_rand_size():
    t_r1 = torch.rand((2, 3, 3))
    t_r2 = torch.rand(size=(2, 3, 3))
    ms_r1 = ms_torch.rand((2, 3, 3))
    ms_r2 = ms_torch.rand(size=(2, 3, 3))
    type_shape_compare(t_r1, ms_r1)
    type_shape_compare(t_r2, ms_r2)

def test_linspace():
    t_r1 = torch.linspace(3, 10, steps=5)
    t_r2 = torch.linspace(-10, 10, steps=5)
    t_r3 = torch.linspace(start=-10, end=10, steps=5)
    t_r4 = torch.linspace(start=-10, end=10, steps=1)

    ms_r1 = ms_torch.linspace(3, 10, steps=5)
    ms_r2 = ms_torch.linspace(-10, 10, steps=5)
    ms_r3 = ms_torch.linspace(start=-10, end=10, steps=5)
    ms_r4 = ms_torch.linspace(start=-10, end=10, steps=1)

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r3, ms_r3)
    param_compare(t_r4, ms_r4)

def test_linspace_tensor_input():
    t_r1 = torch.linspace(torch.tensor(3), torch.tensor(10), steps=5)
    t_r2 = torch.linspace(torch.tensor(-10), torch.tensor(10), steps=5)
    t_r3 = torch.linspace(torch.tensor(-10), torch.tensor(10), steps=5, dtype=torch.int64)

    ms_r1 = ms_torch.linspace(ms_torch.tensor(3), ms_torch.tensor(10), steps=5)
    ms_r2 = ms_torch.linspace(ms_torch.tensor(-10), ms_torch.tensor(10), steps=5)
    ms_r3 = ms_torch.linspace(ms_torch.tensor(-10), ms_torch.tensor(10), steps=5, dtype=ms_torch.int64)

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r3, ms_r3)


def test_take():
    src = torch.tensor([[4, 3, 5],
                        [6, 7, 8]])
    output_t = torch.take(src, torch.tensor([0, 2, 5]))

    ms_src = ms_torch.tensor([[4, 3, 5], [6, 7, 8]])
    output_ms = ms_torch.take(ms_src, ms_torch.tensor([0, 2, 5]))

    param_compare(output_t, output_ms)


def test_abs():
    x = (np.random.randn(2, 3, 4) * 20).astype(np.float32)
    torch_x = torch.tensor(x)
    ms_x = ms_torch.tensor(x)
    torch_out = torch.abs(torch_x)
    ms_out = ms_torch.abs(ms_x)
    param_compare(torch_out, ms_out)

def test_abs_int():
    x = (np.random.randn(2, 3, 4) * 20).astype(np.int32)
    torch_x = torch.tensor(x)
    ms_x = ms_torch.tensor(x)
    torch_out = torch.abs(torch_x)
    ms_out = ms_torch.abs(ms_x)
    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason='abs not support float64 and int16 input on Ascend')
def test_abs_fp64():
    x = np.random.randn(2, 3, 4)
    x1 = x.astype(np.float64)
    x2 = x.astype(np.int16)
    torch_x1 = torch.tensor(x1)
    torch_x2 = torch.tensor(x2)
    ms_x1 = ms_torch.tensor(x1)
    ms_x2 = ms_torch.tensor(x2)
    torch_out1 = torch.abs(torch_x1)
    torch_out2 = torch.abs(torch_x2)
    ms_out1 = ms_torch.abs(ms_x1)
    ms_out2 = ms_torch.abs(ms_x2)
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_atan2():
    x = np.random.randn(2).astype(np.int32)
    y = np.random.randn(2, 2).astype(np.float32)
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    ms_x = ms_torch.tensor(x)
    ms_y = ms_torch.tensor(y)
    t_r = torch.atan2(torch_x, torch_y)
    ms_r = ms_torch.atan2(ms_x, ms_y)

    param_compare(t_r, ms_r)

@SKIP_ENV_ASCEND(reason='atan2 do not support float64 input on Ascend')
def test_atan2_fp64():
    x = np.random.randn(2).astype(np.float64)
    y = np.random.randn(2, 2).astype(np.float64)
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    ms_x = ms_torch.tensor(x)
    ms_y = ms_torch.tensor(y)
    t_r = torch.atan2(torch_x, torch_y)
    ms_r = ms_torch.atan2(ms_x, ms_y)

    param_compare(t_r, ms_r)

def test_clamp():
    a = torch.tensor([[1., 25., 5., 7.], [4., 11., 6., 21.]], dtype=torch.int32)
    t_r = torch.clamp(a, min=5, max=20.)

    input = ms_torch.tensor(np.array([[1., 25., 5., 7.], [4., 11., 6., 21.]]), ms_torch.int32)
    ms_r = ms_torch.clamp(input, min=5, max=20.)

    param_compare(t_r, ms_r)

def test_cos():
    x = torch.tensor([0.24, 0.83, 0.31, 0.09], dtype=torch.float32)
    t_r = torch.cos(x)

    y = ms_torch.tensor([0.24, 0.83, 0.31, 0.09], ms_torch.float32)
    ms_r = ms_torch.cos(y)

    assert np.allclose(t_r.numpy(), ms_r.numpy())
    x = torch.tensor([1, 2, 3, 4], dtype=torch.int32)
    t_r = torch.cos(x)

    y = ms_torch.tensor([1, 2, 3, 4], dtype=ms_torch.int32)
    ms_r = ms_torch.cos(y)

    param_compare(t_r, ms_r)


@SKIP_ENV_GRAPH_MODE(reason="fft currently not support graph mode")
def test_fft():
    t = torch.arange(0, 4).to(torch.int32)
    t_r = torch.fft.fft(t)

    ms_t = ms_torch.arange(0, 4).to(ms_torch.int32)
    ms_r = ms_torch.fft.fft(ms_t)

    #TODO: torch and ms func tensor return type are different
    # ms astype not support complex type input, thus transform the torch tensor type
    t1 = torch.tensor([0. + 1.j, 2. + 3.j, 4. + 5.j, 6. + 7.j]).to(torch.complex128)
    t_r1 = torch.fft.fft(t1)

    t1_ms = ms_torch.tensor([0. + 1.j, 2. + 3.j, 4. + 5.j, 6. + 7.j])
    ms_r1 = ms_torch.fft.fft(t1_ms)

    np_array = np.random.randn(2, 3).astype(np.complex64)
    t_r2 = torch.fft.fft(torch.tensor(np_array))
    ms_r2 = ms_torch.fft.fft(ms_torch.tensor(np_array))
    param_compare(t_r, ms_r)
    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)

def test_fmod():
    t_r = torch.fmod(torch.tensor([-3., -2, -1, 1, 2, 3]), 2)
    t_r1 = torch.fmod(torch.tensor([1, 2, 3, 4, 5]), -1.5)

    ms_r = ms_torch.fmod(ms_torch.tensor([-3., -2, -1, 1, 2, 3]), 2)
    ms_r1 = ms_torch.fmod(ms_torch.tensor([1, 2, 3, 4, 5]), -1.5)

    param_compare(t_r, ms_r)
    param_compare(t_r1, ms_r1)

@SKIP_ENV_ASCEND(reason="ascend not support inf result, result will not be correct")
def test_fmod_inf_nan():
    np_array = (np.random.randn(2, 3) * 20).astype(np.float32)
    t_r2 = torch.fmod(torch.tensor(np_array), 0)
    ms_r2 = ms_torch.fmod(ms_torch.tensor(np_array), 0)

    param_compare(t_r2, ms_r2, equal_nan=True)

def test_frac():
    t_r = torch.frac(torch.tensor([1, 2.5, -3.2]))
    ms_r = ms_torch.frac(ms_torch.tensor([1, 2.5, -3.2]))

    np_array = np.random.rand(2, 3).astype(np.float16)
    t_r1 = torch.frac(torch.tensor(np_array))
    ms_r1 = ms_torch.frac(ms_torch.tensor(np_array))
    param_compare(t_r, ms_r)
    param_compare(t_r1, ms_r1)

def test_log():
    x = torch.tensor([0.24, 0.83, 0.31, 0.09], dtype=torch.float32)
    t_r = torch.log10(x)
    t_r1 = torch.log1p(x)
    t_r2 = torch.log2(x)

    y = ms_torch.tensor([0.24, 0.83, 0.31, 0.09], ms_torch.float32)
    ms_r = ms_torch.log10(y)
    ms_r1 = ms_torch.log1p(y)
    ms_r2 = ms_torch.log2(y)

    param_compare(t_r, ms_r, atol=1e-3)
    param_compare(t_r1, ms_r1, atol=1e-3)
    param_compare(t_r2, ms_r2, atol=1e-3)


def test_sin():
    x = torch.tensor([0.24, 0.83, 0.31, 0.09], dtype=torch.float32)
    t_r = torch.sin(x)

    y = ms_torch.tensor([0.24, 0.83, 0.31, 0.09], ms_torch.float32)
    ms_r = ms_torch.sin(y)

    param_compare(t_r, ms_r)
    x = torch.tensor([1, 2, 3, 4], dtype=torch.int32)
    t_r = torch.sin(x)

    y = ms_torch.tensor([1, 2, 3, 4], dtype=ms_torch.int32)
    ms_r = ms_torch.sin(y)

    param_compare(t_r, ms_r)

def test_norm_p_inf():
    data = np.random.randn(3).astype(np.float32)
    x = torch.tensor(data)
    t_r1 = torch.norm(x, p=float('inf'))
    y = torch.tensor(data)
    ms_r1 = ms_torch.norm(y, p=float('inf'))
    param_compare(t_r1, ms_r1)

    data = np.random.randn(1, 2, 3).astype(np.float32)
    x = torch.tensor(data)
    t_r1 = torch.norm(x, p=float('inf'))
    y = torch.tensor(data)
    ms_r1 = ms_torch.norm(y, p=float('inf'))
    param_compare(t_r1, ms_r1)

def test_norm_p_minus_inf():
    data = np.random.randn(3).astype(np.float32)
    x = torch.tensor(data)
    t_r1 = torch.norm(x, p=float('-inf'))
    y = torch.tensor(data)
    ms_r1 = ms_torch.norm(y, p=float('-inf'))
    param_compare(t_r1, ms_r1)

    data = np.random.randn(1, 2, 3).astype(np.float32)
    x = torch.tensor(data)
    t_r1 = torch.norm(x, p=float('-inf'))
    y = torch.tensor(data)
    ms_r1 = ms_torch.norm(y, p=float('-inf'))
    param_compare(t_r1, ms_r1)

def test_norm_fro():
    x = torch.tensor(1.)
    t_r = torch.norm(x)

    y = ms_torch.tensor(1.)
    ms_r = ms_torch.norm(y)

    param_compare(t_r, ms_r)

    x = torch.tensor([1., 2, 3])
    t_r = torch.norm(x)

    y = ms_torch.tensor([1., 2, 3])
    ms_r = ms_torch.norm(y)

    param_compare(t_r, ms_r)

    x = torch.tensor([[1., 2, 3], [4, 5, 6]])
    t_r = torch.norm(x)

    y = ms_torch.tensor([[1., 2, 3], [4, 5, 6]])
    ms_r = ms_torch.norm(y)

    param_compare(t_r, ms_r)

    data = np.random.randn(2, 3, 4)
    x = torch.tensor(data)
    t_r = torch.norm(x)
    y = ms_torch.tensor(data)
    ms_r = ms_torch.norm(y)
    param_compare(t_r, ms_r)

    data = np.random.randn(2, 3, 4)
    x = torch.tensor(data)
    t_r = torch.norm(x, dim=-1)
    y = ms_torch.tensor(data)
    ms_r = ms_torch.norm(y, dim=-1)
    param_compare(t_r, ms_r)

    data = np.random.randn(2, 3, 4)
    x = torch.tensor(data)
    t_r = torch.norm(x, dim=(1, 2))
    y = ms_torch.tensor(data)
    ms_r = ms_torch.norm(y, dim=(1, 2))
    param_compare(t_r, ms_r)

def test_norm_p_2():
    data = np.random.randn(1, 2, 3).astype(np.float32)
    x = torch.tensor(data)
    t_r1 = torch.norm(x, p=2)
    t_r2 = torch.norm(x, p=2, dim=0)
    t_r3 = torch.norm(x, p=2, dim=(1, 2))

    y = ms_torch.tensor(data)
    ms_r1 = ms_torch.norm(y, p=2)
    ms_r2 = ms_torch.norm(x, p=2, dim=0)
    ms_r3 = ms_torch.norm(x, p=2, dim=(1, 2))

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r3, ms_r3)

def test_norm_p_2_jit():
    data = np.random.randn(1, 2, 3).astype(np.float32)
    x = torch.tensor(data)
    t_r1 = torch.norm(x, p=2)
    @ms.jit
    def func(input):
        return input.norm(p=2)
    y = ms_torch.tensor(data)
    ms_r1 = func(y)
    param_compare(t_r1, ms_r1)

def test_norm_p_0():
    data = np.random.randn(3).astype(np.float32)
    x = torch.tensor(data)
    t_r1 = torch.norm(x, p=0)
    y = ms_torch.tensor(data)
    ms_r1 = ms_torch.norm(y, p=0)
    param_compare(t_r1, ms_r1)

    # ms.ops.norm not support matric 0 norm now
    # data = np.random.randn(2, 3)
    # x = torch.tensor(data)
    # t_r1 = torch.norm(x, p=0)
    # y = ms_torch.tensor(data)
    # ms_r1 = ms_torch.norm(y, p=0)
    # param_compare(t_r1, ms_r1)

def test_norm_p_1():
    # no support float64
    data = np.random.randn(3).astype(np.float32)
    x = torch.tensor(data)
    t_r1 = torch.norm(x, p=1)
    y = ms_torch.tensor(data)
    ms_r1 = ms_torch.norm(y, p=1)
    param_compare(t_r1, ms_r1)

    # ms.ops.norm matrix 1-norm result is not the same as torch
    # data = np.random.randn(2, 3).astype(np.float32)
    # x = torch.tensor(data)
    # t_r1 = torch.norm(x, p=1)
    # y = ms_torch.tensor(data)
    # ms_r1 = ms_torch.norm(y, p=1)
    # param_compare(t_r1, ms_r1)

def test_norm_p_minus_1():
    # no support float64
    data = np.random.randn(3).astype(np.float32)
    x = torch.tensor(data)
    t_r1 = torch.norm(x, p=-1)
    y = ms_torch.tensor(data)
    ms_r1 = ms_torch.norm(y, p=-1)
    param_compare(t_r1, ms_r1)

    # ms.ops.norm matrix minus-1-norm result is not the same as torch
    # data = np.random.randn(2, 3).astype(np.float32)
    # x = torch.tensor(data)
    # t_r1 = torch.norm(x, p=-1)
    # y = ms_torch.tensor(data)
    # ms_r1 = ms_torch.norm(y, p=-1)
    # param_compare(t_r1, ms_r1)

def test_norm_p_minus_2():
    # no support float64
    data = np.random.randn(3).astype(np.float32)
    x = torch.tensor(data)
    t_r1 = torch.norm(x, p=-2)
    y = ms_torch.tensor(data)
    ms_r1 = ms_torch.norm(y, p=-2)
    param_compare(t_r1, ms_r1)

    # ms.ops.norm matrix minus-2-norm result is not the same as torch
    # data = np.random.randn(2, 3).astype(np.float32)
    # x = torch.tensor(data)
    # t_r1 = torch.norm(x, p=-1)
    # y = ms_torch.tensor(data)
    # ms_r1 = ms_torch.norm(y, p=-1)
    # param_compare(t_r1, ms_r1)


def test_bartlett_window():
    t_r = torch.bartlett_window(5)
    ms_r = ms_torch.bartlett_window(5)
    t_r1 = torch.bartlett_window(5, False)
    ms_r1 = ms_torch.bartlett_window(5, False)
    t_r2 = torch.bartlett_window(5, dtype=torch.float64)
    ms_r2 = ms_torch.bartlett_window(5, dtype=ms_torch.float64)

    param_compare(t_r, ms_r)
    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)


def test_hamming_window():
    t_r1 = torch.hamming_window(12)
    t_r2 = torch.hamming_window(20, periodic=True, alpha=0.54, beta=0.46, dtype=torch.float32)
    ms_r1 = ms_torch.hamming_window(12)
    ms_r2 = ms_torch.hamming_window(20, periodic=True, alpha=0.54, beta=0.46, dtype=ms_torch.float32)

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)


def test_hann_windoww():
    t_r = torch.hann_window(12, periodic=False)
    ms_r = ms_torch.hann_window(12, periodic=False)

    param_compare(t_r, ms_r)


def test_cumsum():
    x = torch.tensor([0.24, 0.83, 0.31, 0.09], dtype=torch.float32)
    t_r = torch.cumsum(x, dim=0)

    y = ms_torch.tensor([0.24, 0.83, 0.31, 0.09], ms_torch.float32)
    ms_r = ms_torch.cumsum(y, dim=0)

    param_compare(t_r, ms_r)

@SKIP_ENV_ASCEND(reason="ms.ops.einsum only support GPU")
@SKIP_ENV_CPU(reason="ms.ops.einsum only support GPU")
def test_einsum():
    # trace
    in_1 = torch.randn(4, 4)
    t_r = torch.einsum('ii', in_1)
    ms_r = ms_torch.einsum('ii', ms_torch.tensor(in_1.numpy()))
    param_compare(ms_r, t_r)

    # diagonal
    in_1 = torch.randn(4, 4)
    t_r = torch.einsum('ii->i', in_1)
    ms_r = ms_torch.einsum('ii->i', ms_torch.tensor(in_1.numpy()))
    param_compare(ms_r, t_r)

    # outer product
    x = torch.randn(5)
    y = torch.randn(4)
    t_r = torch.einsum('i,j->ij', x, y)
    ms_r = ms_torch.einsum('i,j->ij', ms_torch.tensor(x.numpy()), ms_torch.tensor(y.numpy()))
    param_compare(ms_r, t_r)

    # batch matrix multiplication
    As = torch.randn(3, 2, 5)
    Bs = torch.randn(3, 5, 4)
    t_r = torch.einsum('bij,bjk->bik', As, Bs)
    ms_r = ms_torch.einsum('bij,bjk->bik', ms_torch.tensor(As.numpy()), ms_torch.tensor(Bs.numpy()))
    param_compare(ms_r, t_r)

    # with sublist format and ellipsis
    t_r = torch.einsum(As, [..., 0, 1], Bs, [..., 1, 2], [..., 0, 2])
    ms_r = ms_torch.einsum(ms_torch.tensor(As.numpy()), [..., 0, 1], ms_torch.tensor(Bs.numpy()),
                           [..., 1, 2], [..., 0, 2])
    param_compare(ms_r, t_r)

    # batch permute
    A = torch.randn(2, 3, 4, 5)
    t_r = torch.einsum('...ij->...ji', A)
    ms_r = ms_torch.einsum('...ij->...ji', ms_torch.tensor(A.numpy()))
    param_compare(ms_r, t_r)

    # equivalent to torch.nn.functional.bilinear
    A = torch.randn(3, 5, 4)
    l = torch.randn(2, 5)
    r = torch.randn(2, 4)
    t_r = torch.einsum('bn,anm,bm->ba', l, A, r)
    ms_r = ms_torch.einsum('bn,anm,bm->ba', ms_torch.tensor(l.numpy()),
                           ms_torch.tensor(A.numpy()), ms_torch.tensor(r.numpy()))
    param_compare(ms_r, t_r)


    A = torch.randn(4, 4, 64)
    l = torch.randn(4, 4, 64)
    t_r = torch.einsum('nct,ncp->ntp', (A, l))
    ms_r = ms_torch.einsum('nct,ncp->ntp', ms_torch.tensor(A.numpy()),
                           ms_torch.tensor(l.numpy()))
    param_compare(ms_r, t_r, atol=1e-5)

    A = torch.randn(3, 2)
    B = torch.randn(3, 3)
    t_r = torch.einsum(A, [...,1], B, [...,2])
    ms_r = ms_torch.einsum(ms_torch.tensor(A.numpy()), [...,1], ms_torch.tensor(B.numpy()), [...,2])
    param_compare(ms_r, t_r, atol=1e-5)

def test_histc():
    data1 = np.array([1, 2, 1, 0, -1, -2, 2, 2, 3, 3, 4, 5, 6]).astype(np.float32)
    t_r1 = torch.histc(torch.tensor(data1), bins=4, min=3, max=3)
    ms_r1 = ms_torch.histc(ms_torch.tensor(data1), bins=4, min=3, max=3)
    t_r2 = torch.histc(torch.tensor([[1., 2, 1, 0, -1, -2, 2.1, 2.9, 3, 3.1, 4, 5, 6]]), bins=4, min=0, max=3)
    ms_r2 = ms_torch.histc(ms_torch.tensor([[1., 2, 1, 0, -1, -2, 2.1, 2.9, 3, 3.1, 4, 5, 6]]), bins=4, min=0, max=3)
    t_r3 = torch.histc(torch.tensor([1., 1, 1]), bins=4, min=3, max=3)
    ms_r3 = ms_torch.histc(ms_torch.tensor([1., 1, 1]), bins=4, min=3, max=3)

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r3, ms_r3)


def test_histogram():
    n1 = random.randint(1, 50)
    data1 = np.random.randn(n1).astype(np.float32)
    bins1 = random.randint(1, 50)
    range1_0 = random.randint(1, 50)
    range1_1 = random.randint(1, 50)
    if range1_0 >= range1_1:
        range1 = (range1_1, range1_0)
    else:
        range1 = (range1_0, range1_1)
    weight1 = np.random.randint(low=20, size=n1).astype(np.float32)

    torch_out1 = torch.histogram(torch.tensor(data1), bins=bins1, range=range1, weight=torch.tensor(weight1))
    torch_out2 = torch.histogram(torch.tensor(data1), bins=bins1, range=range1, weight=torch.tensor(weight1), density=True)

    ms_out1 = ms_torch.histogram(ms_torch.tensor(data1), bins=bins1, range=range1, weight=ms_torch.tensor(weight1))
    ms_out2 = ms_torch.histogram(ms_torch.tensor(data1), bins=bins1, range=range1, weight=ms_torch.tensor(weight1), density=True)

    param_compare(torch_out1, ms_out1, equal_nan=True)
    param_compare(torch_out2, ms_out2, equal_nan=True)


def test_triu():
    a = np.random.randn(3, 3).astype(np.int32)
    a1 = np.random.randn(3, 3).astype(np.float32)
    t1 = torch.tensor(a)
    t2 = torch.tensor(a1)
    ms1 = ms_torch.tensor(a)
    ms2 = ms_torch.tensor(a1)
    t_r = torch.triu(t1)
    t_r1 = torch.triu(t1, diagonal=1)
    t_r2 = torch.triu(t1, diagonal=-1)
    t_r3 = torch.triu(t2)

    ms_r = ms_torch.triu(ms1)
    ms_r1 = ms_torch.triu(ms1, diagonal=1)
    ms_r2 = ms_torch.triu(ms1, diagonal=-1)
    ms_r3 = ms_torch.triu(ms2)

    param_compare(ms_r, t_r)
    param_compare(ms_r1, t_r1)
    param_compare(ms_r2, t_r2)
    param_compare(ms_r3, t_r3)


def test_index_select():
    data = np.random.randn(3, 4 ,5)

    x_torch = torch.tensor(data)
    indices = torch.tensor([0, 2])
    torch_out = torch.index_select(x_torch, 1, indices)
    x_ms = ms_torch.tensor(data)
    indices = ms_torch.tensor([0, 2])
    ms_out = ms_torch.index_select(x_ms, 1, indices)

    param_compare(ms_out, torch_out)

@SKIP_ENV_ASCEND(reason="bmm currently not support float64 on Ascend")
def test_bmm_fp64():
    input = np.random.randn(1, 3, 4)
    mat2 = np.random.randn(1, 4, 5)

    torch_input = torch.tensor(input)
    torch_mat2 = torch.tensor(mat2)
    torch_out = torch.bmm(torch_input, torch_mat2)

    ms_input = ms_torch.tensor(input)
    ms_mat2 = ms_torch.tensor(mat2)
    ms_out = ms_torch.bmm(ms_input, ms_mat2)
    param_compare(torch_out, ms_out)

def test_bmm():
    input = np.random.randn(3, 5, 6).astype(np.float32)
    mat2 = np.random.randn(3, 6, 8).astype(np.float32)

    torch_input = torch.tensor(input)
    torch_mat2 = torch.tensor(mat2)
    torch_out = torch.bmm(torch_input, torch_mat2)

    ms_input = ms_torch.tensor(input)
    ms_mat2 = ms_torch.tensor(mat2)
    ms_out = ms_torch.bmm(ms_input, ms_mat2)
    param_compare(torch_out, ms_out, atol=1e-2)

@SKIP_ENV_ASCEND(reason="baddbmm currently not support float64 on Ascend")
def test_baddbmm_fp64():
    x = np.random.randn(1, 3, 5)
    b1 = np.random.randn(1, 3, 4)
    b2 = np.random.randn(1, 4, 5)

    torch_input = torch.tensor(x)
    torch_batch1 = torch.tensor(b1)
    torch_batch2 = torch.tensor(b2)
    torch_out = torch.baddbmm(torch_input, torch_batch1, torch_batch2, beta=2, alpha=1.5)

    ms_torch_input = ms_torch.tensor(x)
    ms_torch_batch1 = ms_torch.tensor(b1)
    ms_torch_batch2 = ms_torch.tensor(b2)
    ms_torch_out = ms_torch.baddbmm(ms_torch_input, ms_torch_batch1, ms_torch_batch2, beta=2, alpha=1.5)
    param_compare(torch_out, ms_torch_out, atol=1e-4)

def test_baddbmm():
    x = np.random.randn(10, 3, 5).astype(np.float32)
    b1 = np.random.randn(10, 3, 4).astype(np.float32)
    b2 = np.random.randn(10, 4, 5).astype(np.float32)

    torch_input = torch.tensor(x)
    torch_batch1 = torch.tensor(b1)
    torch_batch2 = torch.tensor(b2)
    torch_out = torch.baddbmm(torch_input, torch_batch1, torch_batch2, beta=2., alpha=1.5)

    ms_torch_input = ms_torch.tensor(x)
    ms_torch_batch1 = ms_torch.tensor(b1)
    ms_torch_batch2 = ms_torch.tensor(b2)
    ms_torch_out = ms_torch.baddbmm(ms_torch_input, ms_torch_batch1, ms_torch_batch2, beta=2., alpha=1.5)
    param_compare(torch_out, ms_torch_out, atol=1e-2)

def test_argmin():
    x = np.random.randn(2, 3, 2)
    torch_x = torch.tensor(x)
    torch_out = torch.argmin(torch_x, 1, False)
    ms_x = ms_torch.tensor(x)
    ms_out = ms_torch.argmin(ms_x, 1, False)

    number_shape_compare(torch_out, ms_out)  #dtype diff: torch.int64 vs ms.int32


def test_argmax():
    x = np.random.randn(2, 3, 2)
    torch_x = torch.tensor(x)
    torch_out = torch.argmax(torch_x, 1, False)
    ms_x = ms_torch.tensor(x)
    ms_out = ms_torch.argmax(ms_x, 1, False)

    param_compare(torch_out, ms_out)

def test_broadcast_to():
    torch_x = torch.tensor([1])
    torch_out1 = torch.broadcast_to(torch_x, (2,2))
    torch_out2 = torch.broadcast_to(torch_x, [2,2])
    ms_x = ms_torch.tensor([1])
    ms_out1 = ms_torch.broadcast_to(ms_x, (2,2))
    ms_out2 = ms_torch.broadcast_to(ms_x, [2,2])

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_ravel():
    x = np.random.randn(2, 1, 2)
    torch_x = torch.tensor(x, dtype=torch.bool)
    torch_out = torch.ravel(torch_x)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.bool)
    ms_out = ms_torch.ravel(ms_x)

    param_compare(torch_out, ms_out)

def test_numel():
    tensor = np.zeros((1, 2, 3, 1, 2)).astype(np.int32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.numel(torch_tensor)
    ms_output = ms_torch.numel(ms_tensor)
    assert torch_output == ms_output  # scaler


def test_logsumexp():
    x = np.random.randn(3, 4, 5).astype(np.float32)
    torch_x = torch.tensor(x)
    torch_out = torch.logsumexp(torch_x, dim=2, keepdim=True)
    ms_torch_x = ms_torch.tensor(x)
    ms_torch_out = ms_torch.logsumexp(ms_torch_x, dim=2, keepdim=True)
    param_compare(torch_out, ms_torch_out, atol=1e-5)

def test_addmv():
    M = np.random.randn(2).astype(np.float32)
    mat = np.random.randn(2, 3).astype(np.float32)
    vec = np.random.randn(3).astype(np.float32)

    torch_M = torch.tensor(M)
    torch_mat = torch.tensor(mat)
    torch_vec = torch.tensor(vec)
    torch_out = torch.addmv(torch_M, torch_mat, torch_vec, beta=False, alpha=0.5)

    ms_torch_M = ms_torch.tensor(M)
    ms_torch_mat = ms_torch.tensor(mat)
    ms_torch_vec = ms_torch.tensor(vec)
    ms_torch_out = ms_torch.addmv(ms_torch_M, ms_torch_mat, ms_torch_vec, beta=False, alpha=0.5)
    atol=1e-3 if is_test_under_ascend_context() else 1e-8
    param_compare(torch_out, ms_torch_out, atol=atol)

def test_dot():
    x = [2, 3, 1]
    y = [2, 1, 2]
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch.dot(torch_x, torch_y)
    ms_torch_x = ms_torch.tensor(x)
    ms_torch_y = ms_torch.tensor(y)
    ms_torch_out = ms_torch.dot(ms_torch_x, ms_torch_y)
    param_compare(torch_out, ms_torch_out)

def test_inverse():
    A1 = np.random.randn(4, 4).astype(np.float32)
    torch_A1 = torch.tensor(A1)
    torch_out1 = torch.inverse(torch_A1)
    ms_torch_A1 = ms_torch.tensor(A1)
    ms_torch_out1 = ms_torch.inverse(ms_torch_A1)
    param_compare(torch_out1, ms_torch_out1, rtol=2e-5)

def test_scatter_1():
    ms_out = ms_torch.scatter(ms_torch.full((2, 4), 2.), 1, ms_torch.tensor([[2], [3]]), 1.23)

    torch_out = torch.scatter(torch.full((2, 4), 2.), 1, torch.tensor([[2], [3]]), 1.23)
    param_compare(ms_out, torch_out)

def test_topk():
    x = np.random.randn(10).astype(np.float32)
    torch_x = torch.tensor(x)
    torch_v, torch_i = torch.topk(torch_x, 3)
    ms_x = ms_torch.tensor(x)
    ms_v, ms_i = ms_torch.topk(ms_x, 3)
    if is_test_under_ascend_context():
        param_compare(torch_v, ms_v, atol=1e-3)
    else:
        param_compare(torch_v, ms_v)
    number_shape_compare(torch_i, ms_i)  #dtype diff: torch.int64 vs ms.int32

def test_topk_with_dim():
    y = np.random.randn(3, 3).astype(np.float32)
    torch_y = torch.tensor(y)
    # when sorted = False, the order of result will not be guaranteed, which is normal
    torch_v, torch_i = torch.topk(torch_y, 2, dim=1, largest=False, sorted=True)
    ms_y = ms_torch.tensor(y)
    ms_v, ms_i = ms_torch.topk(ms_y, 2, dim=1, largest=False, sorted=True)
    if is_test_under_ascend_context():
        param_compare(torch_v, ms_v, atol=1e-3)
    else:
        param_compare(torch_v, ms_v)
    number_shape_compare(torch_i, ms_i)  #dtype diff: torch.int64 vs ms.int32


@SKIP_ENV_ASCEND(reason="addbmm currently not support float64 on Ascend")
def test_addbmm_fp64():
    M_ = np.random.randn(3, 5)
    batch1_ = np.random.randn(1, 3, 4)
    batch2_ = np.random.randn(1, 4, 5)

    M = torch.tensor(M_)
    batch1 = torch.tensor(batch1_)
    batch2 = torch.tensor(batch2_)
    torch_output = torch.addbmm(M, batch1, batch2, alpha=2, beta=3)

    M = ms_torch.tensor(M_)
    batch1 = ms_torch.tensor(batch1_)
    batch2 = ms_torch.tensor(batch2_)
    ms_output = ms_torch.addbmm(M, batch1, batch2, alpha=2, beta=3)
    param_compare(torch_output, ms_output)

def test_addbmm():
    M_ = np.random.randn(3, 5).astype(np.float32)
    batch1_ = np.random.randn(4, 3, 4).astype(np.float32)
    batch2_ = np.random.randn(4, 4, 5).astype(np.float32)

    M = torch.tensor(M_)
    batch1 = torch.tensor(batch1_)
    batch2 = torch.tensor(batch2_)
    torch_output = torch.addbmm(M, batch1, batch2, alpha=2.5, beta=3.5)

    M = ms_torch.tensor(M_)
    batch1 = ms_torch.tensor(batch1_)
    batch2 = ms_torch.tensor(batch2_)
    ms_output = ms_torch.addbmm(M, batch1, batch2, alpha=2.5, beta=3.5)
    atol=1e-2 if is_test_under_ascend_context() else 1e-8
    param_compare(torch_output, ms_output, atol=atol)

def test_addr():
    vec1 = torch.arange(1., 4.)
    vec2 = torch.arange(1., 3.)
    M = torch.zeros(3, 2)
    torch_output = torch.addr(M, vec1, vec2)

    vec1 = ms_torch.arange(1., 4.)
    vec2 = ms_torch.arange(1., 3.)
    M = ms_torch.zeros(3, 2)
    ms_output = ms_torch.addr(M, vec1, vec2)

    param_compare(torch_output, ms_output)

def test_allclose():
    a1 = ms_torch.allclose(ms_torch.tensor([10000., 1e-07]), ms_torch.tensor([10000.1, 1e-08]), equal_nan=True)
    b1 = ms_torch.allclose(ms_torch.tensor([10000., 1e-08]), ms_torch.tensor([10000.1, 1e-09]), equal_nan=True)
    d1 = ms_torch.allclose(ms_torch.tensor([1.0, float('nan')]), ms_torch.tensor([1.0, float('nan')]), equal_nan=True)

    d2 = torch.allclose(torch.tensor([1.0, float('nan')]), torch.tensor([1.0, float('nan')]), equal_nan=True)
    a2 = torch.allclose(torch.tensor([10000., 1e-07]), torch.tensor([10000.1, 1e-08]), equal_nan=True)
    b2 = torch.allclose(torch.tensor([10000., 1e-08]), torch.tensor([10000.1, 1e-09]), equal_nan=True)

    assert a1 == a2
    # ms.ops.isclose() has bug on Ascend in r2.3-0429
    if not is_test_under_ascend_context():
        assert b1 == b2
    assert d1 == d2

@SKIP_ENV_ASCEND(reason='allclose not support equal_nan=False on Ascend')
def test_allclose_equal_nan_false():
    c1 = ms_torch.allclose(ms_torch.tensor([1.0, float('nan')]), ms_torch.tensor([1.0, float('nan')]))
    c2 = torch.allclose(torch.tensor([1.0, float('nan')]), torch.tensor([1.0, float('nan')]))
    assert c1 == c2

@SKIP_ENV_ASCEND(reason='isclose not support equal_nan=False on Ascend')
def test_isclose_equal_nan_false():
    a1 = ms_torch.isclose(ms_torch.tensor((1., 2, 3)), ms_torch.tensor((1 + 1e-10, 3, 4)))
    b1 = ms_torch.isclose(ms_torch.tensor((float('inf'), 4)), ms_torch.tensor((float('inf'), 6)), rtol=.5)

    a2 = torch.isclose(torch.tensor((1., 2, 3)), torch.tensor((1 + 1e-10, 3, 4)))
    b2 = torch.isclose(torch.tensor((float('inf'), 4)), torch.tensor((float('inf'), 6)), rtol=.5)

    param_compare(a1, a2)
    param_compare(b1, b2)

def test_isclose():
    a1 = ms_torch.isclose(ms_torch.tensor((1., 2, 3)), ms_torch.tensor((1 + 1e-10, 3, 4)), equal_nan=True)
    a2 = torch.isclose(torch.tensor((1., 2, 3)), torch.tensor((1 + 1e-10, 3, 4)), equal_nan=True)
    assert np.allclose(a1.numpy(), a2.numpy())

@SKIP_ENV_ASCEND(reason="isclose not support inf on Ascend")
def test_isclose_inf():
    b1 = ms_torch.isclose(ms_torch.tensor((float('inf'), 4)), ms_torch.tensor((float('inf'), 6)), rtol=.5, equal_nan=True)
    b2 = torch.isclose(torch.tensor((float('inf'), 4)), torch.tensor((float('inf'), 6)), rtol=.5, equal_nan=True)
    assert np.allclose(b1.numpy(), b2.numpy())

@SKIP_ENV_ASCEND(reason="baddbmm currently not support float64 on Ascend")
def test_addmm_fp64():
    _M = np.random.randn(1, 2)
    _mat1 = np.random.randn(1, 2)
    _mat2 = np.random.randn(2, 2)

    M = ms_torch.tensor(_M)
    mat1 = ms_torch.tensor(_mat1)
    mat2 = ms_torch.tensor(_mat2)
    a1 = ms_torch.addmm(M, mat1, mat2, alpha=2, beta=3)

    M = torch.tensor(_M)
    mat1 = torch.tensor(_mat1)
    mat2 = torch.tensor(_mat2)
    a2 = torch.addmm(M, mat1, mat2, alpha=2, beta=3)

    param_compare(a1, a2)

def test_addmm():
    _M = np.random.randn(2, 3).astype(np.float32)
    _mat1 = np.random.randn(2, 3).astype(np.float32)
    _mat2 = np.random.randn(3, 3).astype(np.float32)

    M = ms_torch.tensor(_M)
    mat1 = ms_torch.tensor(_mat1)
    mat2 = ms_torch.tensor(_mat2)
    a1 = ms_torch.addmm(M, mat1, mat2, alpha=2.5, beta=3.5)

    M = torch.tensor(_M)
    mat1 = torch.tensor(_mat1)
    mat2 = torch.tensor(_mat2)
    a2 = torch.addmm(M, mat1, mat2, alpha=2.5, beta=3.5)

    atol = 1e-2 if is_test_under_ascend_context() else 1e-8
    param_compare(a1, a2, atol=atol)


@SKIP_ENV_ASCEND(reason="cholesky currently not support float64 on Ascend")
def test_cholesky_fp64():
    _data1 = np.random.randn(3, 3)

    a = torch.tensor(_data1)
    a = a @ a.mT + 1e-3
    torch_out1 = torch.cholesky(a)

    a = ms_torch.tensor(_data1)
    a = a @ a.mT + 1e-3
    ms_out1 = ms_torch.cholesky(a)

    param_compare(ms_out1, torch_out1, atol=1e-4)

def test_cholesky():
    _data1 = np.random.randn(4, 4).astype(np.float32)
    _data2 = np.random.randn(5, 2, 2).astype(np.float32)

    a = torch.tensor(_data1)
    a = a @ a.mT + 1e-3
    torch_out1 = torch.cholesky(a)

    a = torch.tensor(_data2)
    a = a @ a.mT + 1e-03
    torch_out2 = torch.cholesky(a)

    a = ms_torch.tensor(_data1)
    a = a @ a.mT + 1e-3
    ms_out1 = ms_torch.cholesky(a)

    a = ms_torch.tensor(_data2)
    a = a @ a.mT + 1e-03
    ms_out2 = ms_torch.cholesky(a)

    param_compare(ms_out1, torch_out1, atol=1e-3)
    param_compare(ms_out2, torch_out2, atol=1e-3)

def test_dist():
    _data1 = np.random.randn(4)
    _data2 = np.random.randn(4)

    x = torch.tensor(_data1)
    y = torch.tensor(_data2)

    # TODO: Not support float p yet
    #a1 = torch.dist(x, y, 3.5)
    b1 = torch.dist(x, y, 3)
    c1 = torch.dist(x, y, 0)
    d1 = torch.dist(x, y, 1)

    x = ms_torch.tensor(_data1)
    y = ms_torch.tensor(_data2)
    #a2 = ms_torch.dist(x, y, 3.5)
    b2 = ms_torch.dist(x, y, 3)
    c2 = ms_torch.dist(x, y, 0)
    d2 = ms_torch.dist(x, y, 1)

    #assert np.allclose(a1.numpy(), a2.numpy())
    param_compare(b1, b2)
    param_compare(c1, c2)
    param_compare(d1, d2)

def test_aminmax():
    a1, b1 = torch.aminmax(torch.tensor([1, -3, 5]))
    a2, b2 = ms_torch.aminmax(ms_torch.tensor([1, -3, 5]))
    param_compare(a1, a2)
    param_compare(b1, b2)

def test_any():
    data1 = np.random.randn(1, 2)
    data2 = np.random.randn(4, 2)

    a = torch.tensor(data1).bool()
    a1 = torch.any(a)
    a = torch.arange(0, 3)
    b1 = torch.any(a)
    a = torch.tensor(data2) < 0
    c1 = torch.any(a, 1)
    d1 = torch.any(a, 0)

    a = torch.tensor(data1).bool()
    a2 = torch.any(a)
    a = torch.arange(0, 3)
    b2 = torch.any(a)
    a = torch.tensor(data2) < 0
    c2 = torch.any(a, 1)
    d2 = torch.any(a, 0)

    param_compare(a1, a2)
    param_compare(b1, b2)
    param_compare(c1, c2)
    param_compare(d1, d2)

@SKIP_ENV_GPU(reason="Unsupport on GPU.")
@SKIP_ENV_ASCEND(reason="baddbmm currently not support float64 on Ascend")
def test_cholesky_inverse_fp64():
    _data = np.random.randn(2, 2)

    a = torch.tensor(_data)
    a = torch.mm(a, a.t()) + 1e-05 * torch.eye(2)
    u = torch.cholesky(a)
    torch_out = torch.cholesky_inverse(u)

    a = ms_torch.tensor(_data)
    a = ms_torch.mm(a, a.t()) + 1e-05 * ms_torch.eye(2)
    u = ms_torch.cholesky(a)
    ms_out = ms_torch.cholesky_inverse(u)
    param_compare(torch_out, ms_out, rtol=1e-2, atol=1e-5)

@SKIP_ENV_GPU(reason="cholesky_inverse currently not support on GPU.")
def test_cholesky_inverse():
    _data = np.random.randn(4, 4).astype(np.float32)

    a = torch.tensor(_data)
    a = torch.mm(a, a.t()) + 1e-05 * torch.eye(4)
    u = torch.cholesky(a)
    torch_out = torch.cholesky_inverse(u)

    a = ms_torch.tensor(_data)
    a = ms_torch.mm(a, a.t()) + 1e-05 * ms_torch.eye(4)
    u = ms_torch.cholesky(a)
    ms_out = ms_torch.cholesky_inverse(u)
    param_compare(torch_out, ms_out, rtol=1e-2, atol=1e-5)

def test_cholesky_solve():
    data1 = np.random.randn(3, 2).astype(np.float32)
    data2 = np.random.randn(3, 3).astype(np.float32)

    a_t = torch.tensor(data1)
    b_t = torch.tensor(data2)
    a_t = torch.mm(a_t, a_t.t()) + 1e-05 * torch.eye(3)
    u_t = torch.cholesky(a_t)
    torch_out1 = torch.cholesky_solve(u_t, b_t)
    torch_out2 = torch.cholesky_solve(u_t, b_t, True)

    a_ms = ms_torch.tensor(data1)
    b_ms = ms_torch.tensor(data2)
    a_ms = ms_torch.mm(a_ms, a_ms.t()) + 1e-05 * ms_torch.eye(3)
    u_ms = ms_torch.cholesky(a_ms)
    ms_out1 = ms_torch.cholesky_solve(u_ms, b_ms)
    ms_out2 = ms_torch.cholesky_solve(u_ms, b_ms, True)
    param_compare(torch_out1, ms_out1, rtol=1e-2, atol=1e-4)
    param_compare(torch_out2, ms_out2, rtol=1e-2, atol=1e-4)

@SKIP_ENV_ASCEND(reason="cholesky_solve currently not support float64 on Ascend")
def test_cholesky_solve_fp64():
    data1 = np.random.randn(2, 3)
    data2 = np.random.randn(2, 2)

    a_t = torch.tensor(data1)
    b_t = torch.tensor(data2)
    torch_out1 = torch.cholesky_solve(a_t, b_t)

    a_ms = ms_torch.tensor(data1)
    b_ms = ms_torch.tensor(data2)
    ms_out1 = ms_torch.cholesky_solve(a_ms, b_ms)
    param_compare(torch_out1, ms_out1)

def test_iscomplex():
    a = ms_torch.tensor([1+1j, 2, 3])
    assert ms_torch.is_complex(a) == True
    a = ms_torch.tensor([1, 2, 3])
    assert ms_torch.is_complex(a) == False

def test_isinf():
    data = [1, float('inf'), 2, float('-inf'), float('nan')]
    a = torch.isinf(torch.tensor(data))
    b = ms_torch.isinf(ms_torch.tensor(data))
    assert np.allclose(a.numpy(), b.numpy())
    assert a.numpy().dtype == b.numpy().dtype

def test_isneginf():
    data = [-float('inf'), float('inf'), 1.2]
    a = torch.isneginf(torch.tensor(data))
    b = ms_torch.isneginf(ms_torch.tensor(data))
    assert np.allclose(a.numpy(), b.numpy())
    assert a.numpy().dtype == b.numpy().dtype

def test_isposinf():
    data = [-float('inf'), float('inf'), 1.2]
    a = torch.isposinf(torch.tensor(data))
    b = ms_torch.isposinf(ms_torch.tensor(data))
    assert np.allclose(a.numpy(), b.numpy())
    assert a.numpy().dtype == b.numpy().dtype

def test_isreal():
    data = [1, 1+1j, 2+0j]
    a = torch.isreal(torch.tensor(data))
    b = ms_torch.isreal(ms_torch.tensor(data))
    assert np.allclose(a.numpy(), b.numpy())
    assert a.numpy().dtype == b.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="fft currently not support graph mode")
def test_rfft():
    t = torch.arange(0, 4)
    t_r = torch.fft.rfft(t)

    ms_t = ms_torch.arange(0, 4)
    ms_r = ms_torch.fft.rfft(ms_t)

    assert np.allclose(t_r.numpy(), ms_r.numpy())

    t = torch.arange(0, 4)
    t_r = torch.fft.rfft(t, n=5)

    ms_t = ms_torch.arange(0, 4)
    ms_r = ms_torch.fft.rfft(ms_t, n=5)

    assert np.allclose(t_r.numpy(), ms_r.numpy())

    np_array = np.random.randn(2, 3).astype(np.float64)
    t_r1 = torch.fft.rfft(torch.tensor(np_array))
    ms_r1 = ms_torch.fft.rfft(ms_torch.tensor(np_array))
    param_compare(t_r1, ms_r1)

def test_polar():
    abs = np.array([1, 2]).astype(np.float32)
    angle = np.array([np.pi / 2, 5 * np.pi / 4]).astype(np.float32)

    torch_abs = torch.tensor(abs)
    torch_angle = torch.tensor(angle)
    z = torch.polar(torch_abs, torch_angle)

    ms_abs = ms_torch.tensor(abs)
    ms_angle = ms_torch.tensor(angle)
    z_ms = ms_torch.polar(ms_abs, ms_angle)
    assert np.allclose(z.numpy(), z_ms.numpy())
    assert z.numpy().dtype == z_ms.numpy().dtype

    abs = np.array([1, 2]).astype(np.float64)
    angle = np.array([np.pi / 2, 5 * np.pi / 4]).astype(np.float64)

    torch_abs = torch.tensor(abs)
    torch_angle = torch.tensor(angle)
    z = torch.polar(torch_abs, torch_angle)

    ms_abs = ms_torch.tensor(abs)
    ms_angle = ms_torch.tensor(angle)
    z_ms = ms_torch.polar(ms_abs, ms_angle)
    assert np.allclose(z.numpy(), z_ms.numpy())
    assert z.numpy().dtype == z_ms.numpy().dtype

def test_narrow():
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    x1_pt = torch.tensor(x)
    out1_pt = torch.narrow(x1_pt, 0, 0, 2)
    x1_ms = ms_torch.tensor(x)
    out1_ms = ms_torch.narrow(x1_ms, 0, 0, 2)
    assert np.allclose(out1_pt.numpy(), out1_ms.numpy())

    x2_pt = torch.tensor(x, dtype=torch.float32)
    dim = torch.tensor(1)
    start = torch.tensor(1)
    length = torch.tensor(2)
    out2_pt = torch.narrow(x2_pt, dim, start, length)

    dim = ms_torch.tensor(1)
    start = ms_torch.tensor(1)
    length = ms_torch.tensor(2)
    x2_ms = ms_torch.tensor(x, dtype=ms_torch.float32)
    out2_ms = ms_torch.narrow(x2_ms, dim, start, length)
    assert np.allclose(out2_pt.numpy(), out2_ms.numpy())

@SKIP_ENV_ASCEND(reason='vdot do not support float64 input on Ascend')
def test_vdot_float64():
    data1_1 = np.array([2., 3, 4])
    data1_2 = np.array([1, 2., 3])

    a = torch.tensor(data1_1)
    b = torch.tensor(data1_2)
    torch_out = torch.vdot(a, b)

    a = ms_torch.tensor(data1_1)
    b = ms_torch.tensor(data1_2)
    ms_out = ms_torch.vdot(a, b)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


@SKIP_ENV_GPU(reason="Unsupport int type on GPU.")
def test_vdot_int():
    data1_1 = np.array([2., 3, 4])
    data1_2 = np.array([1, 2., 3])

    a = torch.tensor(data1_1)
    b = torch.tensor(data1_2)
    torch_out = torch.vdot(a, b)

    a = ms_torch.tensor(data1_1)
    b = ms_torch.tensor(data1_2)
    ms_out = ms_torch.vdot(a, b)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

    data1_1 = np.array([2])
    data1_2 = np.array([3])

    a = torch.tensor(data1_1)
    b = torch.tensor(data1_2)
    torch_out = torch.vdot(a, b)

    a = ms_torch.tensor(data1_1)
    b = ms_torch.tensor(data1_2)
    ms_out = ms_torch.vdot(a, b)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_ASCEND(reason='ms.ops.vdot not support complex input on Ascend')
def test_vdot_complex():
    data1_1 = np.array([2, 3+1j, 4])
    data1_2 = np.array([1, 2+1j, 3])

    a = torch.tensor(data1_1)
    b = torch.tensor(data1_2)
    torch_out = torch.vdot(a, b)

    a = ms_torch.tensor(data1_1)
    b = ms_torch.tensor(data1_2)
    ms_out = ms_torch.vdot(a, b)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_amax():
    x = np.random.randn(2, 3, 4, 5).astype(np.float32)
    x_pt = torch.tensor(x)
    x_ms = ms_torch.tensor(x)
    out1_pt = torch.amax(x_pt, 0, keepdim=True)
    out1_ms = ms_torch.amax(x_ms, 0, keepdim=True)
    assert np.allclose(out1_pt.numpy(), out1_ms.numpy())

    out2_pt = torch.amax(x_pt, 1, keepdim=True)
    out2_ms = ms_torch.amax(x_ms, 1, keepdim=True)
    assert np.allclose(out2_pt.numpy(), out2_ms.numpy())

    out3_pt = torch.amax(x_pt, 2, keepdim=True)
    out3_ms = ms_torch.amax(x_ms, 2, keepdim=True)
    assert np.allclose(out3_pt.numpy(), out3_ms.numpy())

@SKIP_ENV_ASCEND(reason='ms.ops.amax not support float64 input on Ascend')
def test_amax_float64():
    y = np.random.randn(4, 4)
    y_pt = torch.tensor(y)
    y_ms = ms_torch.tensor(y)
    out4_pt = torch.amax(y_pt, 1)
    out4_ms = ms_torch.amax(y_ms, 1)
    param_compare(out4_pt, out4_ms)


def test_amin():
    x = np.random.randn(2, 3, 4, 5).astype(np.float32)
    x_pt = torch.tensor(x)
    x_ms = ms_torch.tensor(x)
    out1_pt = torch.amin(x_pt, 0, keepdim=True)
    out1_ms = ms_torch.amin(x_ms, 0, keepdim=True)
    assert np.allclose(out1_pt.numpy(), out1_ms.numpy())

    out2_pt = torch.amin(x_pt, 1, keepdim=True)
    out2_ms = ms_torch.amin(x_ms, 1, keepdim=True)
    assert np.allclose(out2_pt.numpy(), out2_ms.numpy())

    out3_pt = torch.amin(x_pt, 2, keepdim=True)
    out3_ms = ms_torch.amin(x_ms, 2, keepdim=True)
    assert np.allclose(out3_pt.numpy(), out3_ms.numpy())

@SKIP_ENV_ASCEND(reason='ms.ops.amin not support on Ascend')
def test_amin_float64():
    y = np.random.randn(4, 4)
    y_pt = torch.tensor(y)
    y_ms = ms_torch.tensor(y)
    out4_pt = torch.amin(y_pt, 1)
    out4_ms = ms_torch.amin(y_ms, 1)
    param_compare(out4_pt, out4_ms)


def test_nanmean():
    x = np.array([[float('nan'), 1, 2], [1, 2, 3]]).astype(np.float32)
    x_pt = torch.tensor(x)
    out1_pt = torch.nanmean(x_pt)
    x_ms = ms_torch.tensor(x)
    out1_ms = ms_torch.nanmean(x_ms)
    param_compare(out1_pt, out1_ms)

    out2_pt = torch.nanmean(x_pt, 0)
    out2_ms = ms_torch.nanmean(x_ms, 0)
    param_compare(out2_pt, out2_ms)

    out3_pt = torch.nanmean(torch.tensor([torch.nan]))
    out3_ms = ms_torch.nanmean(ms_torch.tensor([ms_torch.nan]))
    param_compare(out3_pt, out3_ms, equal_nan=True)


def test_nansum():
    a = np.array([1., 2., float('nan'), 4.]).astype(np.float32)
    a_pt = torch.tensor(a)
    out1_pt = torch.nansum(a_pt)
    a_ms = ms_torch.tensor(a)
    out1_ms = ms_torch.nansum(a_ms)
    param_compare(out1_pt, out1_ms, equal_nan=True)

    out2_pt = torch.nansum(torch.tensor([1., float("nan")]))
    out2_ms = ms_torch.nansum(ms_torch.tensor([1., float("nan")]))
    param_compare(out2_pt, out2_ms, equal_nan=True)

    b = np.array([[1, 2], [3., float("nan")]]).astype(np.float32)
    b_pt = torch.tensor(b)
    out3_pt = torch.nansum(b_pt)
    b_ms = ms_torch.tensor(b)
    out3_ms = ms_torch.nansum(b_ms)
    assert np.allclose(out3_pt.numpy(), out3_ms.numpy())

    out4_pt = torch.nansum(b_pt, dim=0)
    out4_ms = ms_torch.nansum(b_ms, dim=0)
    assert np.allclose(out4_pt.numpy(), out4_ms.numpy())


def test_std():
    x = np.random.randn(1,3).astype(np.float32)
    x_pt = torch.tensor(x)
    x_ms = ms_torch.tensor(x)
    out1_pt = torch.std(x_pt)
    out1_ms = ms_torch.std(x_ms)
    assert np.allclose(out1_pt.numpy(), out1_ms.numpy())

    out2_pt = torch.std(x_pt, unbiased=False)
    out2_ms = ms_torch.std(x_ms, unbiased=False)
    assert np.allclose(out2_pt.numpy(), out2_ms.numpy())

    y = np.random.randn(2,3).astype(np.float16)
    y_pt = torch.tensor(y)
    y_ms = ms_torch.tensor(y)
    out3_pt = torch.std(y_pt, dim=1, unbiased=True, keepdim=True)
    out3_ms = ms_torch.std(y_ms, dim=1, unbiased=True, keepdim=True)
    assert np.allclose(out3_pt.numpy(), out3_ms.numpy(), rtol=.4)

def test_tile():
    x1 = np.array([1, 2, 3]).astype(np.int16)
    x2 = np.array([[1, 2], [3, 4]]).astype(np.float32)
    torch_tensor1 = torch.tensor(x1)
    torch_tensor2 = torch.tensor(x2)
    torch_out1 = torch.tile(torch_tensor1, (2,))
    torch_out2 = torch.tile(torch_tensor2, (2, 2))
    torch_out3 = torch.tile(torch_tensor2, (1, 2, 3, 4))
    torch_out4 = torch.tile(torch_tensor2, (2,))

    ms_tensor1 = ms_torch.tensor(x1)
    ms_tensor2 = ms_torch.tensor(x2)
    ms_out1 = ms_torch.tile(ms_tensor1, (2,))
    ms_out2 = ms_torch.tile(ms_tensor2, (2, 2))
    ms_out3 = ms_torch.tile(ms_tensor2, (1, 2, 3, 4))
    ms_out4 = ms_torch.tile(ms_tensor2, (2,))

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype
    assert np.allclose(torch_out4.numpy(), ms_out4.numpy())
    assert torch_out4.numpy().dtype == ms_out4.numpy().dtype

def test_vstack():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    a2 = np.array([[1],[2],[3]])
    b2 = np.array([[4],[5],[6]])

    torch_tensor1 = torch.tensor(a)
    torch_tensor2 = torch.tensor(b)
    torch_tensor3 = torch.tensor(a2)
    torch_tensor4 = torch.tensor(b2)
    torch_out1 = torch.vstack((torch_tensor1.byte(), torch_tensor2.int()))
    torch_out2 = torch.vstack((torch_tensor3.float(), torch_tensor4.float()))
    torch_out4 = torch.vstack([torch_tensor3.short(), torch_tensor4.int()])

    ms_tensor1 = ms_torch.tensor(a)
    ms_tensor2 = ms_torch.tensor(b)
    ms_tensor3 = ms_torch.tensor(a2)
    ms_tensor4 = ms_torch.tensor(b2)
    ms_out1 = ms_torch.vstack((ms_tensor1.byte(), ms_tensor2.int()))
    ms_out2 = ms_torch.vstack((ms_tensor3.float(), ms_tensor4.float()))
    ms_out4 = ms_torch.vstack([ms_tensor3.short(), ms_tensor4.int()])

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out4, ms_out4)

@SKIP_ENV_ASCEND(reason="vstack currently not support float64 on Ascend")
def test_vstack_fp64():
    a = np.random.randn(3, 1)
    b = np.random.randn(3, 1)

    torch_tensor1 = torch.tensor(a)
    torch_tensor2 = torch.tensor(b)
    torch_out1 = torch.vstack((torch_tensor1.long(), torch_tensor2.double()))

    ms_tensor1 = ms_torch.tensor(a)
    ms_tensor2 = ms_torch.tensor(b)
    ms_out1 = ms_torch.vstack((ms_tensor1.long(), ms_tensor2.double()))

    param_compare(torch_out1, ms_out1)

def test_flipud():
    x = np.arange(4).reshape(2, 2).astype(np.int16)
    x2 = np.arange(1, 9).reshape((2, 2, 2)).astype(np.float32)

    torch_x1 = torch.tensor(x)
    torch_x2 = torch.tensor(x2)
    torch_out1 = torch.flipud(torch_x1)
    torch_out2 = torch.flipud(torch_x2)

    ms_x1 = ms_torch.tensor(x)
    ms_x2 = ms_torch.tensor(x2)
    ms_out1 = ms_torch.flipud(ms_x1)
    ms_out2 = ms_torch.flipud(ms_x2)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

def test_det():
    torch_x1 = torch.randn((3, 3), dtype=torch.double)
    torch_x2 = torch.randn((3, 2, 2), dtype=torch.float)
    torch_out1 = torch.det(torch_x1)
    torch_out2 = torch.det(torch_x2)

    ms_x1 = ms_torch.tensor(torch_x1.numpy(), dtype=torch.double)
    ms_x2 = ms_torch.tensor(torch_x2.numpy(), dtype=torch.float)
    ms_out1 = ms_torch.det(ms_x1)
    ms_out2 = ms_torch.det(ms_x2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_outer():
    v1 = np.arange(1., 5.)
    v2 = np.arange(1., 4.)
    v3 = np.array([1, 2, 3], dtype=np.int32)
    v4 = np.array([-1, -2, -3], dtype=np.int32)

    torch_v1 = torch.tensor(v1)
    torch_v2 = torch.tensor(v2)
    torch_v3 = torch.tensor(v3)
    torch_v4 = torch.tensor(v4)
    torch_out1 = torch.outer(torch_v1, torch_v2)
    torch_out2 = torch.outer(torch_v3, torch_v4)

    ms_v1 = ms_torch.tensor(v1)
    ms_v2 = ms_torch.tensor(v2)
    ms_v3 = ms_torch.tensor(v3)
    ms_v4 = ms_torch.tensor(v4)
    ms_out1 = ms_torch.outer(ms_v1, ms_v2)
    ms_out2 = ms_torch.outer(ms_v3, ms_v4)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

def test_along_dim():
    data = np.random.randn(2, 3).astype(np.float32)

    a = torch.tensor(data)
    torch_out1 = torch.take_along_dim(a, torch.tensor([0, 5]))
    torch_out2 = torch.take_along_dim(a, torch.tensor([[0], [2]]), dim=1)

    b = ms_torch.tensor(data)
    ms_out1 = ms_torch.take_along_dim(b, ms_torch.tensor([0, 5]))
    ms_out2 = ms_torch.take_along_dim(b, ms_torch.tensor([[0], [2]]), dim=1)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())


@SKIP_ENV_ASCEND(reason='mindspore.ops.unique_consecutive has some problem on ascend.')
def test_unique_consecutive():
    x = np.array([1, 1, 2, 2, 3, 1, 1, 2])

    torch_tensor1 = torch.tensor(x)
    torch_out1 = torch.unique_consecutive(torch_tensor1)
    torch_out2, torch_indices = torch.unique_consecutive(torch_tensor1, return_inverse=True)
    torch_out3, torch_counts = torch.unique_consecutive(torch_tensor1, return_counts=True)

    ms_tensor1 = ms_torch.tensor(x)
    ms_out1 = ms_torch.unique_consecutive(ms_tensor1)
    ms_out2, ms_indices = ms_torch.unique_consecutive(ms_tensor1, return_inverse=True)
    ms_out3, ms_counts = ms_torch.unique_consecutive(ms_tensor1, return_counts=True)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert np.allclose(torch_indices.numpy(), ms_indices.numpy())
    assert np.allclose(torch_counts.numpy(), ms_counts.numpy())


@SKIP_ENV_ASCEND_GRAPH_MODE("Ascend encapsulate numpy func, which has PyInterpret problem on Graph mode")
def test_svd():
    data = np.random.randn(5, 3).astype(np.float32)
    a1 = torch.tensor(data)
    a2 = ms_torch.tensor(data)
    u1, s1, v1 = torch.svd(a1)
    u2, s2, v2 = ms_torch.svd(a2)

    dist1 = torch.dist(a1, torch.mm(torch.mm(u1, torch.diag(s1)), v1.t()))
    dist2 = ms_torch.dist(a2, ms_torch.mm(ms_torch.mm(u2, ms_torch.diag(s2)), v2.t()))

    atol=1e-2 if is_test_under_ascend_context() else 3e-6
    param_compare(dist1, dist2, atol=atol)

def test_trace():
    data = np.random.randn(5, 3).astype(np.float32)
    a1 = torch.tensor(data)
    a2 = ms_torch.tensor(data)
    torch_out = torch.trace(a1)
    ms_out = ms_torch.trace(a2)
    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())

def test_tril():
    a = torch.randn(3, 3)
    t_r = torch.tril(a)
    t_r1 = torch.tril(a, 1)
    t_r2 = torch.tril(a, -1)

    a = ms_torch.tensor(a.numpy())
    ms_r = ms_torch.tril(a)
    ms_r1 = ms_torch.tril(a, 1)
    ms_r2 = ms_torch.tril(a, -1)

    assert np.allclose(t_r.numpy(), ms_r.numpy())
    assert np.allclose(t_r1.numpy(), ms_r1.numpy())
    assert np.allclose(t_r2.numpy(), ms_r2.numpy())

def test_conj():
    x = torch.tensor([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_out = torch.conj(x)

    y = ms_torch.tensor(x.numpy())
    ms_out = ms_torch.conj(y)

    assert np.allclose(torch_out.resolve_conj().numpy(), ms_out.numpy())

def test_is_conj():
    x = np.array([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_tensor = torch.tensor(x)
    ms_tensor = ms_torch.tensor(x)
    torch_out = torch.conj(torch_tensor)
    ms_out = ms_torch.conj(ms_tensor)

    assert np.allclose(torch_out.resolve_conj().numpy(), ms_out.numpy())
    assert ms_torch.is_conj(ms_out) == torch.is_conj(torch_out)

@SKIP_ENV_GRAPH_MODE("graph mode not support assigning attr to tensor")
@SKIP_ENV_PYNATIVE_MODE("ms.jit forced to use graph mode, which not support assigning attr to tensor")
def test_is_conj_jit():
    x = np.array([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_tensor = torch.tensor(x)
    ms_tensor = ms_torch.tensor(x)
    torch_out = torch.conj(torch_tensor)

    @ms.jit
    def conj_func(ms_tensor):
        ms_out = ms_torch.conj(ms_tensor)
        return ms_out

    ms_out = conj_func(ms_tensor)
    assert np.allclose(torch_out.resolve_conj().numpy(), ms_out.numpy())
    assert ms_torch.is_conj(ms_out) == torch.is_conj(torch_out)

def test_resolve_conj():
    x = np.array([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_tensor = torch.tensor(x)
    ms_tensor = ms_torch.tensor(x)
    torch_out = torch.conj(torch_tensor)
    torch_out1 = torch.resolve_conj(torch_out)
    ms_out = ms_torch.conj(ms_tensor)
    ms_out1 = ms_torch.resolve_conj(ms_out)

    assert np.allclose(torch_out1.resolve_conj().numpy(), ms_out1.numpy())
    assert ms_torch.is_conj(ms_out1) == torch.is_conj(torch_out1)

@SKIP_ENV_GRAPH_MODE("graph mode not support assigning attr to tensor")
@SKIP_ENV_PYNATIVE_MODE("ms.jit forced to use graph mode, which not support assigning attr to tensor")
def test_resolve_conj_jit():
    x = np.array([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_tensor = torch.tensor(x)
    ms_tensor = ms_torch.tensor(x)
    torch_out = torch.conj(torch_tensor)
    torch_out1 = torch.resolve_conj(torch_out)

    @ms.jit
    def conj_func(ms_tensor):
        ms_out = ms_torch.conj(ms_tensor)
        ms_out1 = ms_torch.resolve_conj(ms_out)
        return ms_out1

    ms_out1 = conj_func(ms_tensor)
    assert np.allclose(torch_out1.resolve_conj().numpy(), ms_out1.numpy())
    assert ms_torch.is_conj(ms_out1) == torch.is_conj(torch_out1)

def test_ger():
    v1 = torch.arange(1., 5.)
    v2 = torch.arange(1., 4.)
    torch_out = torch.ger(v1, v2)

    k1 = ms_torch.tensor(v1.numpy())
    k2 = ms_torch.tensor(v2.numpy())
    ms_out = ms_torch.ger(k1, k2)

    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().dtype == ms_out.numpy().dtype

    v1 = torch.arange(1, 5)
    v2 = torch.arange(1, 4)
    torch_out = torch.ger(v1, v2)

    k1 = ms_torch.tensor(v1.numpy())
    k2 = ms_torch.tensor(v2.numpy())
    ms_out = ms_torch.ger(k1, k2)

    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().dtype == ms_out.numpy().dtype

def test_block_diag():
    a = np.array([[0, 1], [1, 0]])
    b = np.array([[3, 4, 5], [6, 7, 8]])
    c = np.array(7)
    d = np.array([1, 2, 3])
    e = np.array([[4], [5], [6]])

    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_c = torch.tensor(c)
    torch_d = torch.tensor(d)
    torch_e = torch.tensor(e)
    torch_out1 = torch.block_diag(torch_a, torch_b, torch_c, torch_d, torch_e)

    ms_a = ms_torch.tensor(a)
    ms_b = ms_torch.tensor(b)
    ms_c = ms_torch.tensor(c)
    ms_d = ms_torch.tensor(d)
    ms_e = ms_torch.tensor(e)
    ms_out1 = ms_torch.block_diag(ms_a, ms_b, ms_c, ms_d, ms_e)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())


def test_logspace():
    torch_out2 = torch.logspace(start=0.1, end=1.0, steps=5, dtype=torch.float32)
    torch_out3 = torch.logspace(start=0.1, end=1.0, steps=1, dtype=torch.int64)
    torch_out4 = torch.logspace(start=2, end=2, steps=1, base=2)

    ms_out2 = ms_torch.logspace(start=0.1, end=1.0, steps=5, dtype= ms_torch.float32)
    ms_out3 = ms_torch.logspace(start=0.1, end=1.0, steps=1, dtype=ms_torch.int64)
    ms_out4 = ms_torch.logspace(start=2, end=2, steps=1, base=2)

    param_compare(ms_out2, torch_out2)
    param_compare(ms_out3, torch_out3)
    param_compare(ms_out4, torch_out4)

@SKIP_ENV_GPU(reason='ms.ops.logspace has bug on GPU')
def test_logspace_skip_gpu():
    # TODO: for end=10, the result will be 1e10, which exceeds the upper limit of int16 and int32,
    # and result in inconsistent behavior between pytorch and mindspore.
    # Thus, change end=10 to end=8 for better maintainability
    torch_out1 = torch.logspace(start=-10, end=8, steps=5, dtype=torch.int16)
    ms_out1 = ms_torch.logspace(start=-10, end=8, steps=5, dtype=ms_torch.int16)
    param_compare(ms_out1, torch_out1)

def test_column_stack():
    x1 = np.array([1, 2, 3])
    y1 = np.array([4, 5, 6])
    x2 = np.arange(5)
    y2 = np.arange(10).reshape(5, 2)

    torch_x1 = torch.tensor(x1)
    torch_y1 = torch.tensor(y1)
    torch_x2 = torch.tensor(x2)
    torch_y2 = torch.tensor(y2)
    torch_out1 = torch.column_stack([torch_x1.short(), torch_y1.bool()])
    torch_out2 = torch.column_stack([torch_x1.float(), torch_y1.int()])
    torch_out3 = torch.column_stack([torch_x2.byte(), torch_y2.bool()])

    ms_x1 = ms_torch.tensor(x1)
    ms_y1 = ms_torch.tensor(y1)
    ms_x2 = ms_torch.tensor(x2)
    ms_y2 = ms_torch.tensor(y2)
    ms_out1 = ms_torch.column_stack([ms_x1.short(), ms_y1.bool()])
    ms_out2 = ms_torch.column_stack([ms_x1.float(), ms_y1.int()])
    ms_out3 = ms_torch.column_stack([ms_x2.byte(), ms_y2.bool()])

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)
    param_compare(ms_out3, torch_out3)

@SKIP_ENV_ASCEND(reason="column_stack currently not support float64 on Ascend")
def test_column_stack_fp64():
    x1 = np.arange(5)
    y1 = np.arange(10).reshape(5, 2)

    torch_x1 = torch.tensor(x1)
    torch_y1 = torch.tensor(y1)

    ms_x1 = ms_torch.tensor(x1)
    ms_y1 = ms_torch.tensor(y1)
    torch_out1 = torch.column_stack((torch_x1.float(), torch_y1.float(), torch_y1.double()))
    ms_out1 = ms_torch.column_stack((ms_x1.float(), ms_y1.float(), ms_y1.double()))
    param_compare(ms_out1, torch_out1)

@SKIP_ENV_ASCEND(reason='not support complex input on Ascend')
def test_column_stack_complex():
    real = np.random.randn(2, 3).astype(np.float32)
    img = np.random.randn(2, 3).astype(np.float32)
    input_np = (real + 1j * img).astype(np.complex64)

    torch_x1 = torch.tensor(input_np)
    torch_y1 = torch.tensor(real)

    ms_x1 = ms_torch.tensor(input_np)
    ms_y1 = ms_torch.tensor(real)
    torch_out1 = torch.column_stack((torch_x1, torch_y1))
    ms_out1 = ms_torch.column_stack((ms_x1, ms_y1))

    param_compare(ms_out1, torch_out1)

def test_hstack():
    x1 = np.array([1, 2, 3])
    y1 = np.array([4, 5, 6])
    x2 = np.array([[1],[2],[3]])
    y2 = np.array([[4],[5],[6]])

    torch_x1 = torch.tensor(x1)
    torch_y1 = torch.tensor(y1)
    torch_x2 = torch.tensor(x2)
    torch_y2 = torch.tensor(y2)

    torch_out1 = torch.hstack((torch_x1.float(), torch_y1.short()))
    torch_out2 = torch.hstack((torch_x2.byte(), torch_y2.int()))

    ms_x1 = ms_torch.tensor(x1)
    ms_y1 = ms_torch.tensor(y1)
    ms_x2 = ms_torch.tensor(x2)
    ms_y2 = ms_torch.tensor(y2)

    ms_out1 = ms_torch.hstack((ms_x1.float(), ms_y1.short()))
    ms_out2 = ms_torch.hstack((ms_x2.byte(), ms_y2.int()))

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

@SKIP_ENV_ASCEND(reason="hstack currently not support float64 on Ascend")
def test_hstack_fp64():
    x1 = np.random.randn(1, 3)
    y1 = np.random.randn(1, 3)

    torch_x1 = torch.tensor(x1)
    torch_y1 = torch.tensor(y1)

    ms_x1 = ms_torch.tensor(x1)
    ms_y1 = ms_torch.tensor(y1)

    torch_out1 = torch.hstack([torch_x1.float(), torch_y1.double()])
    ms_out1 = ms_torch.hstack([ms_x1.float(), ms_y1.double()])
    param_compare(ms_out1, torch_out1)

def test_movedim():
    t = np.random.randn(3,2,1)
    torch_t = torch.tensor(t)
    torch_out1 = torch.movedim(torch_t, 1, 0)
    torch_out2 = torch.movedim(torch_t, (1, 2), (0, 1))

    ms_t = ms_torch.tensor(t)
    ms_out1 = ms_torch.movedim(ms_t, 1, 0)
    ms_out2 = ms_torch.movedim(ms_t, (1, 2), (0, 1))

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

def test_moveaxis():
    t = np.random.randn(2, 5, 4).astype(np.int16)
    torch_t = torch.tensor(t)
    torch_out1 = torch.moveaxis(torch_t, -1, 0)
    torch_out2 = torch.moveaxis(torch_t, (-1, -2), (0, -1))

    ms_t = ms_torch.tensor(t)
    ms_out1 = ms_torch.moveaxis(ms_t, -1, 0)
    ms_out2 = ms_torch.moveaxis(ms_t, (-1, -2), (0, -1))

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

def test_swapdims():
    x1 = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])

    torch_tensor1 = torch.tensor(x1)
    torch_out1 = torch.swapdims(torch_tensor1, 0, 1)
    torch_out2 = torch.swapdims(torch_tensor1, 0, 2)

    ms_tensor1 = ms_torch.tensor(x1)
    ms_out1 = ms_torch.swapdims(ms_tensor1, 0, 1)
    ms_out2 = ms_torch.swapdims(ms_tensor1, 0, 2)

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

def test_swapaxes():
    x1 = np.array([[[0,1],[2,3]],[[4,5],[6,7]]]).astype(np.float32)

    torch_tensor1 = torch.tensor(x1)
    torch_out1 = torch.swapaxes(torch_tensor1, 0, 1)
    torch_out2 = torch.swapaxes(torch_tensor1, 0, 2)

    ms_tensor1 = ms_torch.tensor(x1)
    ms_out1 = ms_torch.swapaxes(ms_tensor1, 0, 1)
    ms_out2 = ms_torch.swapaxes(ms_tensor1, 0, 2)

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

@SKIP_ENV_ASCEND(reason='ms tensor of shape 0 not supported on Ascend')
def test_swapaxes2():
    torch_tensor1 = torch.randn(2, 3, 0, 1)
    torch_out1 = torch.swapaxes(torch_tensor1, 0, 1)
    torch_out2 = torch.swapaxes(torch_tensor1, 0, 2)

    ms_tensor1 = ms_torch.randn(2, 3, 0, 1)
    ms_out1 = ms_torch.swapaxes(ms_tensor1, 0, 1)
    ms_out2 = ms_torch.swapaxes(ms_tensor1, 0, 2)

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

def test_row_stack():
    a = np.random.randn(2, 3) * 20
    b = np.random.randn(3, 3) * 20

    torch_tensor1 = torch.tensor(a)
    torch_tensor2 = torch.tensor(b)
    torch_out1 = torch.row_stack((torch_tensor1.int(), torch_tensor2.float()))
    torch_out2 = torch.row_stack([torch_tensor1.float(), torch_tensor2.float()])

    ms_tensor1 = ms_torch.tensor(a)
    ms_tensor2 = ms_torch.tensor(b)
    ms_out1 = ms_torch.row_stack((ms_tensor1.int(), ms_tensor2.float()))
    ms_out2 = ms_torch.row_stack([ms_tensor1.float(), ms_tensor2.float()])

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

#TODO:Unsupported op [MatrixExp] on CPU
'''
def test_matrix_exp():
    A = np.empty([2, 2, 2])
    A[0, :, :] = np.eye(2, 2)
    A[1, :, :] = 2 * np.eye(2, 2)

    torch_A = torch.tensor(A)
    torch_out = torch.matrix_exp(torch_A)

    ms_A = ms_torch.tensor(A)
    ms_out = ms_torch.matrix_exp(ms_A)

    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().dtype == ms_out.numpy().dtype
'''

def test_mv():
    mat = np.random.randn(2, 3).astype(np.float32)
    vec = np.random.randn(3).astype(np.float32)
    torch_mat = torch.tensor(mat)
    torch_vec = torch.tensor(vec)
    torch_out1 = torch.mv(torch_mat, torch_vec)
    torch_out2 = torch.mv(torch_mat.float(), torch_vec.float())

    ms_mat = ms_torch.tensor(mat)
    ms_vec = ms_torch.tensor(vec)
    ms_out1 = ms_torch.mv(ms_mat, ms_vec)
    ms_out2 = ms_torch.mv(ms_mat.float(), ms_vec.float())

    atol=1e-3 if is_test_under_ascend_context() else 1e-8
    param_compare(torch_out1, ms_out1, atol=atol)
    param_compare(torch_out2, ms_out2, atol=atol)


@SKIP_ENV_ASCEND(reason='ms.ops.mv not support on Ascend')
def test_mv_float64():
    mat = np.random.randn(2, 3)
    vec = np.random.randn(3)
    torch_mat = torch.tensor(mat)
    torch_vec = torch.tensor(vec)
    torch_out1 = torch.mv(torch_mat, torch_vec)
    torch_out2 = torch.mv(torch_mat.float(), torch_vec.float())

    ms_mat = ms_torch.tensor(mat)
    ms_vec = ms_torch.tensor(vec)
    ms_out1 = ms_torch.mv(ms_mat, ms_vec)
    ms_out2 = ms_torch.mv(ms_mat.float(), ms_vec.float())

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_blackman_window():
    torch_out1 = torch.blackman_window(5)
    torch_out2 = torch.blackman_window(1)
    torch_out3 = torch.blackman_window(5, periodic=False)

    ms_out1 = ms_torch.blackman_window(5)
    ms_out2 = ms_torch.blackman_window(1)
    ms_out3 = ms_torch.blackman_window(5, periodic=False)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy(), atol=1e-6)
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy(), atol=1e-6)
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy(), atol=1e-6)
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype

def test_tril_indices():
    torch_out1 = torch.tril_indices(3, 3)
    torch_out2 = torch.tril_indices(4, 3, -1, dtype=torch.float64)
    torch_out3 = torch.tril_indices(4, 3, 1, dtype=torch.int8)

    ms_out1 = ms_torch.tril_indices(3, 3)
    ms_out2 = ms_torch.tril_indices(4, 3, -1, dtype=ms_torch.float64)
    ms_out3 = ms_torch.tril_indices(4, 3, 1, dtype=ms_torch.int8)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype

def test_triu_indices():
    torch_out1 = torch.triu_indices(3, 3)
    torch_out2 = torch.triu_indices(4, 3, -1, dtype=torch.float32)
    torch_out3 = torch.triu_indices(4, 3, 1, dtype=torch.uint8)

    ms_out1 = ms_torch.triu_indices(3, 3)
    ms_out2 = ms_torch.triu_indices(4, 3, -1, dtype=ms_torch.float32)
    ms_out3 = ms_torch.triu_indices(4, 3, 1, dtype=ms_torch.uint8)

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)
    param_compare(ms_out3, torch_out3)


def test_argwhere():
    data = np.array([[1, 0, 1], [2, 3, 4]])

    a = torch.tensor(data)
    torch_out = torch.argwhere(a)

    a = ms_torch.tensor(data)
    ms_out = ms_torch.argwhere(a)

    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_geqrf():
    x1 = np.array([[-2.0, -1.0], [1.0, 2.0]]).astype(np.float32)
    x2 = np.random.randn(3, 5).astype(np.float64)

    torch_x1 = torch.tensor(x1)
    torch_x2 = torch.tensor(x2)
    torch_out1 = torch.geqrf(torch_x1)
    torch_out2 = torch.geqrf(torch_x2)

    ms_x1 = ms_torch.tensor(x1)
    ms_x2 = ms_torch.tensor(x2)
    ms_out1 = ms_torch.geqrf(ms_x1)
    ms_out2 = ms_torch.geqrf(ms_x2)

    assert np.allclose(torch_out1[0].numpy(), ms_out1[0].numpy())
    assert torch_out1[0].numpy().dtype == ms_out1[0].numpy().dtype
    assert np.allclose(torch_out1[1].numpy(), ms_out1[1].numpy())
    assert torch_out1[1].numpy().dtype == ms_out1[1].numpy().dtype
    assert np.allclose(torch_out2[0].numpy(), ms_out2[0].numpy())
    assert torch_out2[0].numpy().dtype == ms_out2[0].numpy().dtype
    assert np.allclose(torch_out2[1].numpy(), ms_out2[1].numpy())
    assert torch_out2[1].numpy().dtype == ms_out2[1].numpy().dtype

def test_trapz():
    y1 = np.array([1, 5, 10]).astype(np.float16)
    x1 = np.array([1, 3, 6]).astype(np.float16)
    y2 = np.arange(9).reshape(3, 3)

    torch_y1 = torch.tensor(y1)
    torch_x1 = torch.tensor(x1)
    torch_y2 = torch.tensor(y2)
    torch_out1 = torch.trapz(torch_y1)
    torch_out3 = torch.trapz(torch_y1, torch_x1)
    torch_out4 = torch.trapz(torch_y2)
    torch_out5 = torch.trapz(torch_y2, dim=0)

    ms_y1 = ms_torch.tensor(y1)
    ms_y2 = ms_torch.tensor(y2)
    ms_x1 = ms_torch.tensor(x1)
    ms_out1 = ms_torch.trapz(ms_y1)
    ms_out3 = ms_torch.trapz(ms_y1, ms_x1)
    ms_out4 = ms_torch.trapz(ms_y2)
    ms_out5 = ms_torch.trapz(ms_y2, dim=0)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out3, ms_out3)
    param_compare(torch_out4, ms_out4)
    param_compare(torch_out5, ms_out5)

def test_trapz1():
    y = np.random.randn(3)

    torch_y = torch.tensor(y)
    torch_out = torch.trapz(torch_y, dx=2.5)
    ms_y = ms_torch.tensor(y)
    ms_out = ms_torch.trapz(ms_y, dx=2.5)

    param_compare(torch_out, ms_out)


def test_trapezoid():
    y1 = np.array([1, 5, 10]).astype(np.float16)
    # y3 = np.ones((3, 3))
    y3 = np.ones((3, 3)).astype(np.float32)
    x3 = np.array([1, 3, 6]).astype(np.int32)
    y4 = np.ones((3, 3)).astype(np.int16)
    x4 = np.array([[1, 2, 3], [1, 3, 5], [1, 4, 7]]).astype(np.float16)
    y5 = np.random.randn(2, 3, 4)


    torch_y1 = torch.tensor(y1)
    torch_y3 = torch.tensor(y3)
    torch_y4 = torch.tensor(y4)
    torch_x3 = torch.tensor(x3)
    torch_x4 = torch.tensor(x4)
    torch_y5 = torch.tensor(y5)
    torch_out2 = torch.trapezoid(torch_y1, dx=2)
    torch_out6 = torch.trapezoid(torch_y3, torch_x3)
    torch_out7 = torch.trapezoid(torch_y4, torch_x4)
    torch_out8 = torch.trapezoid(torch_y5)

    ms_y1 = ms_torch.tensor(y1)
    ms_y3 = ms_torch.tensor(y3)
    ms_y4 = ms_torch.tensor(y4)
    ms_x3 = ms_torch.tensor(x3)
    ms_x4 = ms_torch.tensor(x4)
    ms_y5 = ms_torch.tensor(y5)
    ms_out2 = ms_torch.trapezoid(ms_y1, dx=2)
    ms_out6 = ms_torch.trapezoid(ms_y3, ms_x3)
    ms_out7 = ms_torch.trapezoid(ms_y4, ms_x4)
    ms_out8 = ms_torch.trapezoid(ms_y5)

    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out6.numpy(), ms_out6.numpy())
    assert torch_out6.numpy().dtype == ms_out6.numpy().dtype
    assert np.allclose(torch_out7.numpy(), ms_out7.numpy())
    assert torch_out7.numpy().dtype == ms_out7.numpy().dtype
    assert np.allclose(torch_out8.numpy(), ms_out8.numpy())
    assert torch_out8.numpy().dtype == ms_out8.numpy().dtype

def test_bucketize():
    boundaries1 = np.array([1, 3, 5, 7, 9])
    boundaries2 = np.array([-9.004112, 3.4471533, 4.094589, 6.938159, 12.685098])
    v1 = np.array([[3, 6, 9], [3, 6, 9]])

    torch_boundaries1 = torch.tensor(boundaries1)
    torch_boundaries2 = torch.tensor(boundaries2)
    torch_v1 = torch.tensor(v1)
    torch_out1 = torch.bucketize(torch_v1, torch_boundaries1)
    torch_out2 = torch.bucketize(torch_v1, torch_boundaries1, right=True)
    torch_out3 = torch.bucketize(torch_v1, torch_boundaries2)
    torch_out4 = torch.bucketize(torch_v1, torch_boundaries2, right=True)

    ms_boundaries1 = ms_torch.tensor(boundaries1)
    ms_boundaries2 = ms_torch.tensor(boundaries2)
    ms_v1 = ms_torch.tensor(v1)
    ms_out1 = ms_torch.bucketize(ms_v1, ms_boundaries1)
    ms_out2 = ms_torch.bucketize(ms_v1, ms_boundaries1, right=True)
    ms_out3 = ms_torch.bucketize(ms_v1, ms_boundaries2)
    ms_out4 = ms_torch.bucketize(ms_v1, ms_boundaries2, right=True)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype
    assert np.allclose(torch_out4.numpy(), ms_out4.numpy())
    assert torch_out4.numpy().dtype == ms_out4.numpy().dtype

def test_bucketize_random():
    boundaries = np.random.rand(4).astype(np.float32)
    boundaries.sort()
    v = np.random.randn(64).astype(np.float32)

    pt_boundaries = torch.tensor(boundaries)
    pt_v = torch.tensor(v)
    pt_out1 = torch.bucketize(pt_v, pt_boundaries, right=True)

    ms_boundaries = ms_torch.tensor(boundaries)
    ms_v = ms_torch.tensor(v)
    ms_out = ms_torch.bucketize(ms_v, ms_boundaries, right=True)

    param_compare(pt_out1, ms_out)

    pt_boundaries = torch.tensor(boundaries)
    pt_v = torch.tensor(v)
    pt_out1 = torch.bucketize(pt_v, pt_boundaries)

    ms_boundaries = ms_torch.tensor(boundaries)
    ms_v = ms_torch.tensor(v)
    ms_out = ms_torch.bucketize(ms_v, ms_boundaries)

    param_compare(pt_out1, ms_out)

def test_lcm():
    a = np.array([5, 10, 15])
    b = np.array([3, 4, 5])
    c = np.array([3])

    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_c = torch.tensor(c)
    torch_out1 = torch.lcm(torch_a, torch_b)
    torch_out2 = torch.lcm(torch_a, torch_c)
    torch_out3 = torch.lcm(torch.tensor(0), torch.tensor(0))
    torch_out4 = torch.lcm(torch.tensor(0), torch_a)

    ms_a = ms_torch.tensor(a)
    ms_b = ms_torch.tensor(b)
    ms_c = ms_torch.tensor(c)
    ms_out1 = ms_torch.lcm(ms_a, ms_b)
    ms_out2 = ms_torch.lcm(ms_a, ms_c)
    ms_out3 = ms_torch.lcm(ms_torch.tensor(0), ms_torch.tensor(0))
    ms_out4 = ms_torch.lcm(ms_torch.tensor(0), ms_a)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype
    assert np.allclose(torch_out4.numpy(), ms_out4.numpy())
    assert torch_out4.numpy().dtype == ms_out4.numpy().dtype

def test_renorm():
    x = np.ones((3, 3)).astype(np.float32)
    x[1].fill(2)
    x[2].fill(3)

    torch_x = torch.tensor(x)
    torch_out1 = torch.renorm(torch_x, 1, 0, 5)
    torch_out2 = torch.renorm(torch_x, 2, 1, 2)
    torch_out3 = torch.renorm(torch_x, 2., 1, 2.)
    ms_x = ms_torch.tensor(x)
    ms_out1 = ms_torch.renorm(ms_x, 1, 0, 5)
    ms_out2 = ms_torch.renorm(ms_x, 2, 1, 2)
    ms_out3 = ms_torch.renorm(ms_x, 2., 1, 2.)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

@SKIP_ENV_ASCEND(reason='vdot do not support float64 input on Ascend')
def test_renorm_fp64():
    x = np.ones((2, 2))
    x[0].fill(2)
    x[1].fill(3)

    torch_x = torch.tensor(x)
    torch_out1 = torch.renorm(torch_x, 1, 0, 5)
    torch_out2 = torch.renorm(torch_x.double(), 2, 1, 2)
    ms_x = ms_torch.tensor(x)
    ms_out1 = ms_torch.renorm(ms_x, 1, 0, 5)
    ms_out2 = ms_torch.renorm(ms_x.double(), 2, 1, 2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_tensordot():
    a1 = np.arange(60.).reshape(3, 4, 5).astype(np.float32)
    b1 = np.arange(24.).reshape(4, 3, 2).astype(np.float32)
    a2 = np.random.randn(3, 4, 5).astype(np.float32)
    b2 = np.random.randn(4, 5, 6).astype(np.float32)

    torch_a1 = torch.tensor(a1)
    torch_b1 = torch.tensor(b1)
    torch_a2 = torch.tensor(a2)
    torch_b2 = torch.tensor(b2)

    ms_a1 = ms_torch.tensor(a1)
    ms_b1 = ms_torch.tensor(b1)
    ms_a2 = ms_torch.tensor(a2)
    ms_b2 = ms_torch.tensor(b2)

    torch_out1 = torch.tensordot(torch_a1, torch_b1, dims=([1, 0], [0, 1]))
    torch_out2 = torch.tensordot(torch_a2, torch_b2, dims=2)
    ms_out1 = ms_torch.tensordot(ms_a1, ms_b1, dims=([1, 0], [0, 1]))
    ms_out2 = ms_torch.tensordot(ms_a2, ms_b2, dims=2)

    param_compare(torch_out1, ms_out1)
    atol=1e-2 if is_test_under_ascend_context() else 1e-4
    param_compare(torch_out2, ms_out2, atol=atol)

@SKIP_ENV_GPU(reason="tensordot currently not support int on Ascend")
def test_tensordot_int():
    a1 = np.random.randn(3, 4, 5).astype(np.int32)
    b1 = np.random.randn(4, 3, 2).astype(np.int32)

    torch_a1 = torch.tensor(a1)
    torch_b1 = torch.tensor(b1)

    ms_a1 = ms_torch.tensor(a1)
    ms_b1 = ms_torch.tensor(b1)

    torch_out1 = torch.tensordot(torch_a1, torch_b1, dims=([1, 0], [0, 1]))
    ms_out1 = ms_torch.tensordot(ms_a1, ms_b1, dims=([1, 0], [0, 1]))

    param_compare(torch_out1, ms_out1)

@SKIP_ENV_ASCEND(reason="tensordot currently not support float64 on Ascend")
def test_tensordot_fp64():
    a1 = np.random.randn(3, 4, 5)
    b1 = np.random.randn(4, 3, 2)

    torch_a1 = torch.tensor(a1)
    torch_b1 = torch.tensor(b1)
    ms_a1 = ms_torch.tensor(a1)
    ms_b1 = ms_torch.tensor(b1)

    torch_out1 = torch.tensordot(torch_a1, torch_b1, dims=([1, 0],[0, 1]))
    ms_out1 = ms_torch.tensordot(ms_a1, ms_b1, dims=([1, 0],[0, 1]))

    param_compare(torch_out1, ms_out1)

def test_randn_like():
    x = np.ones((2, 3, 4))
    x2 = np.arange(15).astype('float32')

    torch_x = torch.tensor(x)
    torch_x2 = torch.tensor(x2)
    torch_out1 = torch.randn_like(torch_x, dtype=torch.float64)
    torch_out2 = torch.randn_like(torch_x2)

    ms_x = ms_torch.tensor(x)
    ms_x2 = ms_torch.tensor(x2)
    ms_out1 = ms_torch.randn_like(ms_x, dtype=ms.float64)
    ms_out2 = ms_torch.randn_like(ms_x2)

    assert np.allclose(torch_out1.shape, ms_out1.shape)
    assert np.allclose(torch_out2.shape, ms_out2.shape)
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

    ms.set_seed(0)
    ms_out1 = ms_torch.randn_like(ms_x, dtype=ms.float64)
    ms_out2 = ms_torch.randn_like(ms_x, dtype=ms.float64)
    ms.set_seed(0)
    ms_out3 = ms_torch.randn_like(ms_x, dtype=ms.float64)
    ms_out4 = ms_torch.randn_like(ms_x, dtype=ms.float64)
    ms.set_seed(5)
    ms_out5 = ms_torch.randn_like(ms_x2)
    ms_out6 = ms_torch.randn_like(ms_x2)
    ms.set_seed(5)
    ms_out7 = ms_torch.randn_like(ms_x2)
    ms_out8 = ms_torch.randn_like(ms_x2)

    assert np.allclose(ms_out1.numpy(), ms_out3.numpy())
    assert ms_out1.numpy().dtype == ms_out3.numpy().dtype
    assert np.allclose(ms_out2.numpy(), ms_out4.numpy())
    assert ms_out2.numpy().dtype == ms_out4.numpy().dtype
    assert np.allclose(ms_out5.numpy(), ms_out7.numpy())
    assert ms_out5.numpy().dtype == ms_out7.numpy().dtype
    assert np.allclose(ms_out6.numpy(), ms_out8.numpy())
    assert ms_out6.numpy().dtype == ms_out8.numpy().dtype

def test_rand_like():
    x = np.ones((2, 3, 4))
    x2 = np.arange(15).astype('float32')

    torch_x = torch.tensor(x)
    torch_x2 = torch.tensor(x2)
    torch_out1 = torch.rand_like(torch_x, dtype=torch.float64)
    torch_out2 = torch.rand_like(torch_x2)

    ms_x = ms_torch.tensor(x)
    ms_x2 = ms_torch.tensor(x2)
    ms_out1 = ms_torch.rand_like(ms_x, dtype=ms.float64)
    ms_out2 = ms_torch.rand_like(ms_x2)

    assert np.allclose(torch_out1.shape, ms_out1.shape)
    assert np.allclose(torch_out2.shape, ms_out2.shape)
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

    ms.set_seed(1234)
    ms_out1 = ms_torch.rand_like(ms_x, dtype=ms.float32)
    ms_out2 = ms_torch.rand_like(ms_x, dtype=ms.float32)
    ms.set_seed(1234)
    ms_out3 = ms_torch.rand_like(ms_x, dtype=ms.float32)
    ms_out4 = ms_torch.rand_like(ms_x, dtype=ms.float32)

    assert np.allclose(ms_out1.numpy(), ms_out3.numpy())
    assert ms_out1.numpy().dtype == ms_out3.numpy().dtype
    assert np.allclose(ms_out2.numpy(), ms_out4.numpy())
    assert ms_out2.numpy().dtype == ms_out4.numpy().dtype

def test_kron():
    mat1 = np.eye(2).astype(np.complex128)
    # mat2 = np.ones((2, 2)).astype(np.float64)
    mat2 = np.ones((2, 2)).astype(np.complex128)
    mat3 = np.eye(2)
    mat4 = np.arange(1, 5).reshape(2, 2)

    torch_mat1 = torch.tensor(mat1)
    torch_mat2 = torch.tensor(mat2)
    torch_mat3 = torch.tensor(mat3)
    torch_mat4 = torch.tensor(mat4)
    torch_out1 = torch.kron(torch_mat1, torch_mat2)
    torch_out2 = torch.kron(torch_mat3, torch_mat4)

    ms_mat1 = ms_torch.tensor(mat1)
    ms_mat2 = ms_torch.tensor(mat2)
    ms_mat3 = ms_torch.tensor(mat3)
    ms_mat4 = ms_torch.tensor(mat4)
    ms_out1 = ms_torch.kron(ms_mat1, ms_mat2)
    ms_out2 = ms_torch.kron(ms_mat3, ms_mat4)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

def test_gcd():
    a = np.array([5, 10, 15])
    b = np.array([3, 4, 5])
    c = np.array([3])

    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_c = torch.tensor(c)
    torch_out1 = torch.gcd(torch_a, torch_b)
    torch_out2 = torch.gcd(torch_a, torch_c)
    torch_out3 = torch.gcd(torch.tensor(0), torch.tensor(0))

    ms_a = ms_torch.tensor(a)
    ms_b = ms_torch.tensor(b)
    ms_c = ms_torch.tensor(c)
    ms_out1 = ms_torch.gcd(ms_a, ms_b)
    ms_out2 = ms_torch.gcd(ms_a, ms_c)
    ms_out3 = ms_torch.gcd(ms_torch.tensor(0), ms_torch.tensor(0))

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype

def test_index_add():
    x = np.ones((5, 3), dtype=np.int64)
    t = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int64)
    index = np.array([0, 4, 2])

    torch_x = torch.tensor(x)
    torch_t = torch.tensor(t)
    torch_index = torch.tensor(index)
    torch_out1 = torch.index_add(torch_x, 0, torch_index, torch_t)
    torch_out2 = torch.index_add(torch_x, 0, torch_index, torch_t, alpha=-1)

    ms_x = ms_torch.tensor(x)
    ms_t = ms_torch.tensor(t)
    ms_index = ms_torch.tensor(index)
    ms_out1 = ms_torch.index_add(ms_x, 0, ms_index, ms_t)
    ms_out2 = ms_torch.index_add(ms_x, 0, ms_index, ms_t, alpha=-1)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

# TODO: index_add to support input of more than 2-D & dim >= 1
# test fails on Ascend
@SKIP_ENV_ASCEND(reason="index_add doesn't support input of more than 2-D & dim >= 1 on Ascend")
def test_index_add_dim2():
    x2 = np.ones((1, 1, 2), dtype=np.int64)
    t2 = np.array([[[2, 5, 4]]], dtype=np.int64)
    index2 = np.array([0, 1, 0])

    torch_x2 = torch.tensor(x2)
    torch_t2 = torch.tensor(t2)
    torch_index2 = torch.tensor(index2)
    torch_out3 = torch.index_add(torch_x2, 2, torch_index2, torch_t2)

    ms_x2 = ms_torch.tensor(x2)
    ms_t2 = ms_torch.tensor(t2)
    ms_index2 = ms_torch.tensor(index2)
    ms_out3 = ms_torch.index_add(ms_x2, 2, ms_index2, ms_t2)

    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype

def test_index_copy():
    x = np.ones((5, 3), dtype=np.int64)
    t1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int64)
    t2 = np.arange(25).reshape(5,5).astype('int64')
    index1 = np.array([0, 4, 2])
    index2 = np.array([0, 2, 1, 1, 2])

    torch_x = torch.tensor(x)
    torch_t1 = torch.tensor(t1)
    torch_t2 = torch.tensor(t2)
    torch_index1 = torch.tensor(index1)
    torch_index2 = torch.tensor(index2)
    torch_out1 = torch.index_copy(torch_x, 0, torch_index1, torch_t1)
    torch_out2 = torch.index_copy(torch_x, 1, torch_index2, torch_t2)

    ms_x = ms_torch.tensor(x)
    ms_t1 = ms_torch.tensor(t1)
    ms_t2 = ms_torch.tensor(t2)
    ms_index1 = ms_torch.tensor(index1)
    ms_index2 = ms_torch.tensor(index2)
    ms_out1 = ms_torch.index_copy(ms_x, 0, ms_index1, ms_t1)
    ms_out2 = ms_torch.index_copy(ms_x, 1, ms_index2, ms_t2)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    # TODO: ms.ops.index_add to support dim >= 1
    # assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    # assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

@SKIP_ENV_ASCEND(reason="scatter_add requires updates_shape=indices_shape + input_x_shape[1:] on ascend")
def test_scatter_add():
    src_np1 = np.ones((2, 5))
    index_np1 = np.array([[0, 1, 2, 0, 0], [0, 1, 2, 0, 0]])
    # index_np1 = np.array([[0, 1, 2, 0, 0]])
    input_np1 = np.zeros((3, 5), dtype=src_np1.dtype)

    torch_src1 = torch.tensor(src_np1)
    torch_index1 = torch.tensor(index_np1)
    torch_input1 = torch.tensor(input_np1)
    torch_out1 = torch.scatter_add(torch_input1, 0, torch_index1, torch_src1)

    ms_src1 = ms_torch.tensor(src_np1)
    ms_index1 = ms_torch.tensor(index_np1)
    ms_input1 = ms_torch.tensor(input_np1)
    ms_out1 = ms_torch.scatter_add(ms_input1, 0, ms_index1, ms_src1)

    param_compare(ms_out1, torch_out1)

def test_std_mean():
    a1 = np.array([[-0.8166, -1.3802, -0.3560]])
    a2 = np.random.randn(1, 3, 4)
    torch_a1 = torch.tensor(a1)
    torch_a2 = torch.tensor(a2)
    ms_a1 = ms_torch.tensor(a1)
    ms_a2 = ms_torch.tensor(a2)
    torch_out1 =  torch.std_mean(torch_a1)
    torch_out2 =  torch.std_mean(torch_a1.float(), unbiased=True)
    torch_out3 =  torch.std_mean(torch_a2, dim=(0,2), unbiased=True, keepdim=True)
    torch_out4 =  torch.std_mean(torch_a2, dim=[0,2], unbiased=True, keepdim=False)
    ms_out1 =  ms_torch.std_mean(ms_a1)
    ms_out2 =  ms_torch.std_mean(ms_a1.float(), unbiased=True)
    ms_out3 =  ms_torch.std_mean(ms_a2, dim=(0,2), unbiased=True, keepdim=True)
    ms_out4 =  ms_torch.std_mean(ms_a2, dim=[0,2], unbiased=True, keepdim=False)
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)
    param_compare(torch_out4, ms_out4)

def test_clone():
    def torch_fun(x):
        y = torch.clone(x)
        return y ** 2

    def ms_fun(x):
        y = ms_torch.clone(x)
        return y ** 2

    torch_a = torch.tensor(1.0, requires_grad=True)
    torch_out1 = torch_fun(torch_a)
    torch_out1.backward()

    ms_a = ms_torch.tensor(1.0, requires_grad=True)
    ms_out1 = ms_fun(ms_a)

    assert np.allclose(torch_out1.detach().numpy(), ms_out1.numpy())

    # Automatic differentiation method 1
    assert np.allclose(torch_a.grad.detach().numpy(), ms.grad(ms_fun)(ms_a).numpy())
    assert torch_a.grad.detach().numpy().dtype == ms.grad(ms_fun)(ms_a).numpy().dtype

def test_slice_scatter():
    a = torch.zeros(8, 8)
    # TODO: to use b = torch.ones(8) as testcase on pytorch documents after pytorch fix slice_scatter.
    b = torch.ones(2, 8)
    torch_out1 = torch.slice_scatter(a, b, start=6, step=1)

    b = torch.ones(8, 2)
    torch_out2 = torch.slice_scatter(a, b, dim=1, start=2, end=6, step=2)

    a = torch.zeros(2, 3, 4, 5)
    b = torch.ones(2, 1, 4, 5)
    torch_out3 = torch.slice_scatter(a, b, start=2, dim=1, step=1)

    a = ms_torch.zeros(8, 8)
    b = ms_torch.ones(8)
    ms_out1 = ms_torch.slice_scatter(a, b, start=6)

    b = ms_torch.ones(2)
    ms_out2 = ms_torch.slice_scatter(a, b, dim=1, start=2, end=6, step=2)

    a = ms_torch.zeros(2, 3, 4, 5)
    b = ms_torch.ones(4, 5)
    ms_out3 = ms_torch.slice_scatter(a, b, start=2, dim=1)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy())
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

def test_select_scatter():
    a = torch.zeros(2, 2)
    b = torch.ones(2)
    torch_out1 = torch.select_scatter(a, b, 0, 0)

    a = ms_torch.zeros(2, 2)
    b = ms_torch.ones(2)
    ms_out1 = ms_torch.select_scatter(a, b, 0, 0)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype

def test_dstack():
    a1 = np.array([1, 2, 3])
    b1 = np.array([4, 5, 6])

    torch_a1 = torch.tensor(a1)
    torch_b1 = torch.tensor(b1)
    torch_out1 = torch.dstack([torch_a1.byte(), torch_b1.char()])
    ms_a1 = ms_torch.tensor(a1)
    ms_b1 = ms_torch.tensor(b1)
    ms_out1 = ms_torch.dstack([ms_a1.byte(), ms_b1.char()])

    a2 = np.array([[1],[2],[3]]).astype(np.float64)
    b2 = np.array([[4],[5],[6]]).astype(np.float64)

    torch_a2 = torch.tensor(a2)
    torch_b2 = torch.tensor(b2)
    torch_out2 = torch.dstack((torch_a2.float(), torch_b2.long()))
    ms_a2 = ms_torch.tensor(a2)
    ms_b2 = ms_torch.tensor(b2)
    ms_out2 = ms_torch.dstack((ms_a2.float(), ms_b2.long()))

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

def test_randint_like():
    a = np.random.rand(3, 2, 1)

    torch_a = torch.tensor(a)
    torch_out1 = torch.randint_like(torch_a, high=10)
    torch_out2 = torch.randint_like(torch_a, 10, dtype=torch.float16)
    torch_out3 = torch.randint_like(torch_a, -5, 10)
    torch_out4 = torch.randint_like(torch_a, low=-5, high=10)

    ms_a = ms_torch.tensor(a)
    ms_out1 = ms_torch.randint_like(ms_a, high=10)
    ms_out2 = ms_torch.randint_like(ms_a, 10, dtype=ms.float16)
    ms_out3 = ms_torch.randint_like(ms_a, -5, 10)
    ms_out4 = ms_torch.randint_like(ms_a, low=-5, high=10)

    assert np.allclose(torch_out1.shape, ms_out1.shape)
    assert np.allclose(torch_out2.shape, ms_out2.shape)
    assert np.allclose(torch_out3.shape, ms_out3.shape)
    assert np.allclose(torch_out4.shape, ms_out4.shape)
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype
    assert torch_out4.numpy().dtype == ms_out4.numpy().dtype

    ms.set_seed(15)
    ms_out1 = ms_torch.randint_like(ms_a, 10, 18, dtype=ms.int16)
    ms_out2 = ms_torch.randint_like(ms_a, 10, 18, dtype=ms.int16)
    ms.set_seed(15)
    ms_out3 = ms_torch.randint_like(ms_a, 10, 18, dtype=ms.int16)
    ms_out4 = ms_torch.randint_like(ms_a, 10, 18, dtype=ms.int16)

    assert np.allclose(ms_out1.numpy(), ms_out3.numpy())
    assert ms_out1.numpy().dtype == ms_out3.numpy().dtype
    assert np.allclose(ms_out2.numpy(), ms_out4.numpy())
    assert ms_out2.numpy().dtype == ms_out4.numpy().dtype

def test_kaiser_window():
    torch_out1 = torch.kaiser_window(12)
    torch_out2 = torch.kaiser_window(8, periodic=False, beta=10, dtype=torch.float32)
    torch_out3 = torch.kaiser_window(1, periodic=False, dtype=torch.float16)
    ms_out1 = ms_torch.kaiser_window(12)
    ms_out2 = ms_torch.kaiser_window(8, periodic=False, beta=10, dtype=ms_torch.float32)
    ms_out3 = ms_torch.kaiser_window(1, periodic=False, dtype=ms_torch.float16)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy(), rtol=1e-3)
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype

def test_cartesian_prod():
    a = [1, 2, 3]
    b = [4, 5]
    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_out1 = torch.cartesian_prod(torch_a, torch_b, torch_a)

    ms_a = ms_torch.tensor(a)
    ms_b = ms_torch.tensor(b)
    ms_out1 = ms_torch.cartesian_prod(ms_a, ms_b, ms_a)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype

def test_combinations():
    a = [1, 2, 3]
    torch_a = torch.tensor(a)
    torch_out1 = torch.combinations(torch_a)


    ms_a = ms_torch.tensor(a)
    ms_out1 = ms_torch.combinations(ms_a)
    torch_out2 = torch.combinations(torch_a.byte(), r=3)
    torch_out3 = torch.combinations(torch_a.float(), with_replacement=True)
    ms_out2 = ms_torch.combinations(ms_a.byte(), r=3)
    ms_out3 = ms_torch.combinations(ms_a.float(), with_replacement=True)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

@SKIP_ENV_ASCEND(reason="combinations currently not support float64 and int16 on Ascend")
def test_combinations_fp64():
    a = np.random.randn(3)
    torch_a = torch.tensor(a)
    ms_a = ms_torch.tensor(a)
    torch_out1 = torch.combinations(torch_a.double(), with_replacement=True)
    torch_out2 = torch.combinations(torch_a.short(), r=3)
    ms_out1 = ms_torch.combinations(ms_a.double(), with_replacement=True)
    ms_out2 = ms_torch.combinations(ms_a.short(), r=3)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_fmax():
    a = torch.tensor([1., float('nan'), 3, float('nan')])
    b = torch.tensor([float('nan'), 2., 1., float('nan')])
    torch_output = torch.fmax(a, b)

    a = ms_torch.tensor([1., float('nan'), 3, float('nan')])
    b = ms_torch.tensor([float('nan'), 2., 1., float('nan')])
    with graph_lax_level():
        ms_out = ms_torch.fmax(a, b)

    assert np.allclose(torch_output.numpy(), ms_out.numpy(), equal_nan=True)

def test_fmin():
    a = torch.tensor([1., float('nan'), 3, float('nan')])
    b = torch.tensor([float('nan'), 2., 1., float('nan')])
    torch_output = torch.fmin(a, b)

    a = ms_torch.tensor([1., float('nan'), 3, float('nan')])
    b = ms_torch.tensor([float('nan'), 2., 1., float('nan')])
    with graph_lax_level():
        ms_out = ms_torch.fmin(a, b)

    assert np.allclose(torch_output.numpy(), ms_out.numpy(), equal_nan=True)

def test_var_mean():
    a = np.array([[-0.8166, -1.3802, -0.3560]])

    torch_a = torch.tensor(a)
    torch_out1 = torch.var_mean(torch_a, unbiased=False)
    torch_out2 = torch.var_mean(torch_a, [1,])
    torch_out3 = torch.var_mean(torch_a, 0, keepdim=True)

    ms_a = ms_torch.tensor(a)
    ms_out1 = ms_torch.var_mean(ms_a, unbiased=False)
    ms_out2 = ms_torch.var_mean(ms_a, [1,])
    ms_out3 = ms_torch.var_mean(ms_a, 0, keepdim=True)

    assert np.allclose(torch_out1[0].numpy(), ms_out1[0].numpy())
    assert torch_out1[0].numpy().dtype == ms_out1[0].numpy().dtype
    assert np.allclose(torch_out1[1].numpy(), ms_out1[1].numpy())
    assert torch_out1[1].numpy().dtype == ms_out1[1].numpy().dtype
    assert np.allclose(torch_out2[0].numpy(), ms_out2[0].numpy())
    assert torch_out2[0].numpy().dtype == ms_out2[0].numpy().dtype
    assert np.allclose(torch_out2[1].numpy(), ms_out2[1].numpy())
    assert torch_out2[1].numpy().dtype == ms_out2[1].numpy().dtype
    assert np.allclose(torch_out3[0].numpy(), ms_out3[0].numpy(), equal_nan=True)
    assert torch_out3[0].numpy().dtype == ms_out3[0].numpy().dtype
    assert np.allclose(torch_out3[1].numpy(), ms_out3[1].numpy())
    assert torch_out3[1].numpy().dtype == ms_out3[1].numpy().dtype

def test_is_nonzero():
    torch_out1 = torch.is_nonzero(torch.tensor([0.]))
    torch_out2 = torch.is_nonzero(torch.tensor([1.5]))
    torch_out3 = torch.is_nonzero(torch.tensor([False]))
    torch_out4 = torch.is_nonzero(torch.tensor([3]))

    ms_out1 = ms_torch.is_nonzero(ms.Tensor([0.]))
    ms_out2 = ms_torch.is_nonzero(ms.Tensor([1.5]))
    ms_out3 = ms_torch.is_nonzero(ms.Tensor([False]))
    ms_out4 = ms_torch.is_nonzero(ms.Tensor([3]))

    assert torch_out1 == ms_out1
    assert torch_out2 == ms_out2
    assert torch_out3 == ms_out3
    assert torch_out4 == ms_out4

def test_isin():
    np_arr = np.random.randint(1, 5, (2, 5))

    torch_tensor = torch.tensor(np_arr)
    torch_out1 = torch.isin(torch.tensor([[1, 2], [3, 4]]), torch.tensor([2, 3]))
    torch_out2 = torch.isin(torch_tensor, torch.tensor([2, 3]), invert=True)

    ms_tensor = ms_torch.tensor(np_arr)
    ms_out1 = ms_torch.isin(ms.Tensor([[1, 2], [3, 4]]), ms.Tensor([2, 3]))
    ms_out2 = ms_torch.isin(ms_tensor, ms.Tensor([2, 3]), invert=True)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

def test_normal():
    # TODO: ms.ops.normal doesn't take float64 inputs
    mean1 = np.arange(1., 11.)
    mean1 = np.arange(1., 11.).astype(np.float32)
    std1 = np.arange(1, 0, -0.1).astype(np.float16)
    std2 = np.arange(1., 6.).astype(np.float16)
    mean2 = np.arange(1., 6.).astype(np.float16)

    torch_mean1 = torch.tensor(mean1)
    torch_mean2 = torch.tensor(mean2)
    torch_std1 = torch.tensor(std1)
    torch_std2 = torch.tensor(std2)

    ms_mean1 = ms_torch.tensor(mean1)
    ms_mean2 = ms_torch.tensor(mean2)
    ms_std1 = ms_torch.tensor(std1)
    ms_std2 = ms_torch.tensor(std2)

    torch_out1 = torch.normal(mean=torch_mean1, std=torch_std1)
    torch_out2 = torch.normal(mean=0.5, std=torch_std2)
    torch_out3 = torch.normal(mean=torch_mean2)
    torch_out4 = torch.normal(torch_mean2)
    torch_out5 = torch.normal(torch_mean2, std=2.0)
    torch_out6 = torch.normal(mean=torch_mean2, std=2)

    ms_out1 = ms_torch.normal(mean=ms_mean1, std=ms_std1)
    ms_out2 = ms_torch.normal(mean=0.5, std=ms_std2)
    ms.set_seed(1)
    ms_out3 = ms_torch.normal(mean=ms_mean2)
    ms.set_seed(1)
    ms_out4 = ms_torch.normal(ms_mean2)
    ms.set_seed(5)
    ms_out5 = ms_torch.normal(ms_mean2, 2.0)
    ms.set_seed(5)
    ms_out6 = ms_torch.normal(mean=ms_mean2, std=2)

    assert np.allclose(torch_out1.shape, ms_out1.shape)
    assert np.allclose(torch_out2.shape, ms_out2.shape)
    assert np.allclose(torch_out3.shape, ms_out3.shape)
    assert np.allclose(torch_out4.shape, ms_out4.shape)
    assert np.allclose(torch_out5.shape, ms_out5.shape)
    assert np.allclose(torch_out6.shape, ms_out6.shape)
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype
    assert torch_out4.numpy().dtype == ms_out4.numpy().dtype
    assert torch_out5.numpy().dtype == ms_out5.numpy().dtype
    assert torch_out6.numpy().dtype == ms_out6.numpy().dtype

    assert np.allclose(ms_out3.numpy(), ms_out4.numpy())
    assert np.allclose(ms_out5.numpy(), ms_out6.numpy())

def test_normal2():
    torch_out1 = torch.normal(2, 3, size=(1, 4, 3))
    torch_out2 = torch.normal(2, 3, size=[1, 4, 3])
    ms.set_seed(2)
    ms_out1 = ms_torch.normal(2, 3, size=(1, 4, 3))
    ms.set_seed(2)
    ms_out2 = ms_torch.normal(2, 3, size=[1, 4, 3])

    assert np.allclose(torch_out1.shape, ms_out1.shape)
    assert np.allclose(torch_out2.shape, ms_out2.shape)
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(ms_out1.numpy(), ms_out2.numpy())

def test_orgqr():
    h = np.random.randn(5, 4, 3, 2, 1).astype(np.float64)
    tau = np.random.randn(5, 4, 3, 1).astype(np.float64)

    torch_h = torch.tensor(h)
    torch_tau = torch.tensor(tau)
    torch_out1 = torch.orgqr(torch_h, torch_tau)

    ms_h = ms_torch.tensor(h)
    ms_tau = ms_torch.tensor(tau)
    ms_out1 = ms_torch.orgqr(ms_h, ms_tau)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype

def test_bernoulli():
    a = ms_torch.empty(3, 3).uniform_adapter(0, 1)  # generate a uniform random matrix with range [0, 1]
    assert ms_torch.bernoulli(a).shape == (3, 3)

    a = ms_torch.ones(3, 3) # probability of drawing "1" is 1
    b = torch.tensor(a.numpy())
    assert np.allclose(ms_torch.bernoulli(a).numpy(), ms_torch.ones_like(a).numpy())
    assert np.allclose(ms_torch.bernoulli(a).numpy(), torch.bernoulli(b).numpy())

    a = ms_torch.zeros(3, 3) # probability of drawing "1" is 1
    b = torch.tensor(a.numpy())
    assert np.allclose(ms_torch.bernoulli(a).numpy(), ms_torch.zeros_like(a).numpy()) # probability of drawing "1" is 0
    assert np.allclose(ms_torch.bernoulli(a).numpy(), torch.bernoulli(b).numpy())

@SKIP_ENV_GRAPH_MODE(reason='1.isintance(a, tuple) not support on 3.27. 2. uniform_ not support on GRAPH_MODE')
def test_bernoulli_grad():
    class torch_Net(torch.nn.Module):
        def forward(self, input):
            output = torch.bernoulli(input)
            output = torch.sum(output)
            return output

    input = torch.empty(3, 3).uniform_(0, 1).requires_grad_(True)
    net = torch_Net()
    output = net(input)
    output.backward()
    torch_gradient = input.grad

    class ms_Net(ms_torch.nn.Module):
        def forward(self, input):
            output = ms_torch.bernoulli(input)
            output = ms_torch.sum(output)
            return output

    input = ms_torch.tensor(input.detach().numpy()).requires_grad_(True)
    net = ms_Net()

    # Automatic differentiation method 1
    ms_gradient = ms.grad(net)(input)
    assert np.allclose(ms_gradient.numpy(), torch_gradient.numpy())
    assert np.allclose(ms_gradient.numpy(), np.zeros(ms_gradient.shape))

def test_scatter_reduce_sum():
    torch_src = torch.tensor([1., 2., 3., 4., 5., 6.])
    torch_index = torch.tensor([0, 1, 0, 1, 2, 1])
    torch_input = torch.tensor([1., 2., 3., 4.])
    torch_out1 = torch.scatter_reduce(torch_input, 0, torch_index, torch_src, reduce="sum")
    torch_out2 = torch.scatter_reduce(torch_input, 0, torch_index, torch_src, reduce="sum", include_self=False)

    ms_src = ms_torch.tensor([1., 2., 3., 4., 5., 6.])
    ms_index = ms_torch.tensor([0, 1, 0, 1, 2, 1])
    ms_input = ms_torch.tensor([1., 2., 3., 4.])
    ms_out1 = ms_torch.scatter_reduce(ms_input, 0, ms_index, ms_src, reduce="sum")
    ms_out2 = ms_torch.scatter_reduce(ms_input, 0, ms_index, ms_src, reduce="sum", include_self=False)

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

def test_scatter_reduce_amax():
    torch_src = torch.tensor([1., 2., 3., 4., 5., 6.])
    torch_index = torch.tensor([0, 1, 0, 1, 2, 1])
    torch_input2 = torch.tensor([5., 4., 3., 2.])
    torch_out3 = torch.scatter_reduce(torch_input2, 0, torch_index, torch_src, reduce="amax")
    torch_out4 = torch.scatter_reduce(torch_input2, 0, torch_index, torch_src, reduce="amax", include_self=False)

    ms_src = ms_torch.tensor([1., 2., 3., 4., 5., 6.])
    ms_index = ms_torch.tensor([0, 1, 0, 1, 2, 1])
    ms_input2 = ms_torch.tensor([5., 4., 3., 2.])
    ms_out3 = ms_torch.scatter_reduce(ms_input2, 0, ms_index, ms_src, reduce="amax")
    ms_out4 = ms_torch.scatter_reduce(ms_input2, 0, ms_index, ms_src, reduce="amax", include_self=False)

    param_compare(ms_out3, torch_out3)
    param_compare(ms_out4, torch_out4)

def test_scatter_reduce_amin():
    torch_src = torch.tensor([1., 2., 3., 4., 5., 6.])
    torch_index = torch.tensor([0, 1, 0, 1, 2, 1])
    torch_input = torch.tensor([1., 2., 3., 4.])
    torch_out7 = torch.scatter_reduce(torch_input, 0, torch_index, torch_src, reduce="amin")
    torch_out8 = torch.scatter_reduce(torch_input, 0, torch_index, torch_src, reduce="amin", include_self=False)

    ms_src = ms_torch.tensor([1., 2., 3., 4., 5., 6.])
    ms_index = ms_torch.tensor([0, 1, 0, 1, 2, 1])
    ms_input = ms_torch.tensor([1., 2., 3., 4.])
    ms_out7 = ms_torch.scatter_reduce(ms_input, 0, ms_index, ms_src, reduce="amin")
    ms_out8 = ms_torch.scatter_reduce(ms_input, 0, ms_index, ms_src, reduce="amin", include_self=False)

    param_compare(ms_out7, torch_out7)
    param_compare(ms_out8, torch_out8)

def test_scatter_reduce_prod():
    torch_src = torch.tensor([1., 2., 3., 4., 5., 6.])
    torch_index = torch.tensor([0, 1, 0, 1, 2, 1])
    torch_input = torch.tensor([1., 2., 3., 4.])
    torch_out5 = torch.scatter_reduce(torch_input, 0, torch_index, torch_src, reduce="prod")
    torch_out6 = torch.scatter_reduce(torch_input, 0, torch_index, torch_src, reduce="prod", include_self=False)

    ms_src = ms_torch.tensor([1., 2., 3., 4., 5., 6.])
    ms_index = ms_torch.tensor([0, 1, 0, 1, 2, 1])
    ms_input = ms_torch.tensor([1., 2., 3., 4.])
    ms_out5 = ms_torch.scatter_reduce(ms_input, 0, ms_index, ms_src, reduce="prod")
    ms_out6 = ms_torch.scatter_reduce(ms_input, 0, ms_index, ms_src, reduce="prod", include_self=False)

    param_compare(ms_out5, torch_out5)
    param_compare(ms_out6, torch_out6)

def test_asarray():
    array = ms.numpy.array([1, 2, 3])
    scalar = 0.5
    ms_tensor = ms_torch.tensor(array)
    ms_scalar = ms_torch.tensor(scalar)
    ms_out1 = ms_torch.asarray(ms_tensor)
    ms_out2 = ms_torch.asarray(array)
    ms_a2 = ms_torch.tensor([1, 2, 3], requires_grad=True).astype(ms.int32)
    ms_out3 = ms_torch.asarray(ms_a2)
    ms_out4 = ms_torch.asarray(ms_scalar)

    assert ms_tensor.dtype == ms_out1.dtype
    assert ms_tensor.dtype == ms_out2.dtype
    assert ms_tensor.dtype == ms_out3.dtype
    assert ms_scalar.dtype == ms_out4.dtype

def test_result_type():
    for type1 in [np.bool_, np.uint8, np.int8, np.int16, np.int32, \
        np.int64, np.float32, np.float64, np.complex64, np.complex128]:
        for type2 in [np.bool_, np.uint8, np.int8, np.int16, np.int32, \
            np.int64, np.float32, np.float64, np.complex64, np.complex128]:
            array1 = np.array([1, 2, 3]).astype(type1)
            array2 = np.array([1, 2, 3]).astype(type2)
            torch_tensor1 = torch.tensor(array1)
            ms_tensor1 = ms_torch.tensor(array1)
            torch_tensor2 = torch.tensor(array2)
            ms_tensor2 = ms_torch.tensor(array2)

            torch_out1 = torch.result_type(torch_tensor1, torch_tensor2)
            ms_out1 = ms_torch.result_type(ms_tensor1, ms_tensor2)
            assert str(ms_out1).upper() == str(torch_out1)[6:].upper()

        torch_out2 = torch.result_type(torch_tensor1, 1.0)
        ms_out2 = ms_torch.result_type(ms_tensor1, 1.0)
        assert str(ms_out2).upper() == str(torch_out2)[6:].upper()

def test_promote_types():
    for type1 in [bool, np.bool_, np.uint8, np.int8, np.int16, np.int32, int, \
        np.int64, np.float16, np.float32, np.float64, float, np.complex64, np.complex128]:
        for type2 in [np.bool_, np.uint8, np.int8, np.int16, np.int32, int, \
            np.int64, np.float32, np.float64, float, np.complex64, np.complex128]:
            t_type1 = torch.tensor(np.array([1]).astype(type1)).dtype
            t_type2 = torch.tensor(np.array([1]).astype(type2)).dtype
            ms_type1 = ms_torch.tensor(np.array([1]).astype(type1)).dtype
            ms_type2 = ms_torch.tensor(np.array([1]).astype(type2)).dtype
            torch_out1 = torch.promote_types(t_type1, t_type2)
            ms_out1 = ms_torch.promote_types(ms_type1, ms_type2)
            assert str(ms_out1).upper() == str(torch_out1)[6:].upper()
    @ms.jit
    def my_test(ms_type1, ms_type2):
        ms_out = ms_torch.promote_types(ms_type1, ms_type2)
        return ms_out
    ms_out1 = my_test(ms_type1, ms_type2)
    assert str(ms_out1).upper() == str(torch_out1)[6:].upper()

def test_complex():
    for type1 in (np.float32, np.float64):
        real_array1 = np.random.randn(3, 3).astype(type1)
        real_array2 = np.random.randn(2, 3).astype(type1)
        imag_array1 = np.random.randn(3, 3).astype(type1)
        imag_array2 = np.random.randn(2, 3).astype(type1)

        torch_real1 = torch.tensor(real_array1)
        torch_real2 = torch.tensor(real_array2)
        torch_imag1 = torch.tensor(imag_array1)
        torch_imag2 = torch.tensor(imag_array2)
        ms_real1 = ms_torch.tensor(real_array1)
        ms_real2 = ms_torch.tensor(real_array2)
        ms_imag1 = ms_torch.tensor(imag_array1)
        ms_imag2 = ms_torch.tensor(imag_array2)

        torch_out1 = torch.complex(torch_real1, torch_imag1)
        torch_out2 = torch.complex(torch_real2, torch_imag2)
        ms_out1 = ms_torch.complex(ms_real1, ms_imag1)
        ms_out2 = ms_torch.complex(ms_real2, ms_imag2)

        param_compare(torch_out1, ms_out1)
        param_compare(torch_out2, ms_out2)

@SKIP_ENV_ASCEND(reason='ms.ops.index_reduce not support float64 input on Ascend')
def test_index_reduce_amin_float64():
    torch_out = torch.index_reduce(torch.full((5,), 2, dtype=torch.float64), 0, torch.tensor([1, 2, 3]),
                                   torch.arange(-4, -1, dtype=torch.float64), 'amin')
    ms_out = ms_torch.index_reduce(ms_torch.full((5,), 2, dtype=ms_torch.float64), 0, ms_torch.tensor([1, 2, 3]),
                                   ms_torch.arange(-4, -1, dtype=ms_torch.float64), 'amin')
    param_compare(ms_out, torch_out)

def test_index_reduce_amin():
    torch_out2 = torch.index_reduce(torch.full((5,), 3, dtype=torch.float32), 0, torch.tensor([0, 1, 3]),
                                   torch.arange(2, 5, dtype=torch.float32), 'amin', include_self=False)
    ms_out2 = ms_torch.index_reduce(ms_torch.full((5,), 3, dtype=ms_torch.float32), 0, ms_torch.tensor([0, 1, 3]),
                                   ms_torch.arange(2, 5, dtype=ms_torch.float32), 'amin', include_self=False)
    param_compare(ms_out2, torch_out2)

@SKIP_ENV_PYNATIVE_MODE(reason="[CI] ms2.4.0 0920 still not pass, need to be fixed.")
def test_index_reduce_amax():
    torch_out = torch.index_reduce(torch.full((2, 3, 4, 5), 10, dtype=torch.float16), 3,
                                   torch.tensor([1, 0, 3]), torch.arange(1, 73).half().reshape(2,3,4,3), 'amax')
    ms_out = ms_torch.index_reduce(ms_torch.full((2, 3, 4, 5), 10, dtype=ms_torch.float16), 3,
                                   ms_torch.tensor([1, 0, 3]), ms_torch.arange(1, 73).half().reshape(2,3,4,3), 'amax')
    param_compare(ms_out, torch_out)

@SKIP_ENV_PYNATIVE_MODE(reason="[CI] ms2.4.0 0920 still not pass, need to be fixed.")
def test_index_reduce_prod():
    torch_out = torch.index_reduce(torch.full((2, 3, 4, 5), 10, dtype=torch.float16), 3,
                                   torch.tensor([1, 0, 3]), torch.arange(1, 73).half().reshape(2,3,4,3), 'prod',
                                   include_self=False)
    ms_out = ms_torch.index_reduce(ms_torch.full((2, 3, 4, 5), 10, dtype=ms_torch.float16), 3,
                                   ms_torch.tensor([1, 0, 3]), ms_torch.arange(1, 73).half().reshape(2,3,4,3), 'prod',
                                   include_self=False)
    param_compare(ms_out, torch_out)

def test_can_cast():
    for type1 in [np.bool_, np.uint8, np.int8, np.int16, np.int32, \
        np.int64, float, np.float16, np.float32, np.float64, np.complex64, np.complex128]:
        for type2 in [np.bool_, np.uint8, np.int8, np.int16, np.int32, \
            np.int64, float, np.float16, np.float32, np.float64, np.complex64, np.complex128]:
            array1 = np.array([1, 2, 3]).astype(type1)
            array2 = np.array([1, 2, 3]).astype(type2)
            torch_tensor1 = torch.tensor(array1)
            ms_tensor1 = ms_torch.tensor(array1)
            torch_tensor2 = torch.tensor(array2)
            ms_tensor2 = ms_torch.tensor(array2)
            torch_out1 = torch.can_cast(torch_tensor1.dtype, torch_tensor2.dtype)
            ms_out1 = ms_torch.can_cast(ms_tensor1.dtype, ms_tensor2.dtype)
            assert torch_out1 == ms_out1

def _check_deterministic_enabled():
    get_out = ms_torch.get_deterministic_debug_mode()
    enabled_out = ms_torch.are_deterministic_algorithms_enabled()
    assert get_out == 1
    assert enabled_out == True

def _check_deterministic_disabled():
    get_out = ms_torch.get_deterministic_debug_mode()
    enabled_out = ms_torch.are_deterministic_algorithms_enabled()
    assert get_out == 0
    assert enabled_out == False

@SKIP_ENV_CPU(reason='deterministic-mode-related apis are not supported on CPU')
@SKIP_ENV_GPU(reason='deterministic-mode-related apis are not supported on GPU')
def test_deterministic_apis():
    default = ms.context.get_context("deterministic")

    ms_torch.use_deterministic_algorithms(True)
    _check_deterministic_enabled()

    ms_torch.use_deterministic_algorithms(False)
    _check_deterministic_disabled()

    ms_torch.set_deterministic_debug_mode("default")
    _check_deterministic_disabled

    ms_torch.set_deterministic_debug_mode(1)
    _check_deterministic_enabled()

    assert ms_torch.is_deterministic_algorithms_warn_only_enabled() == False

    ms.context.set_context(deterministic=default)

def test_diagonal_scatter():
    a = ms_torch.zeros(3, 3)
    ms_out1 = ms_torch.diagonal_scatter(a, ms_torch.ones(3), 0)
    ms_out2 = ms_torch.diagonal_scatter(a, ms_torch.ones(2), 1)

    a = torch.zeros(3, 3)
    torch_out1 = torch.diagonal_scatter(a, torch.ones(3), 0)
    torch_out2 = torch.diagonal_scatter(a, torch.ones(2), 1)

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

@SKIP_ENV_GPU(reason="nanmedian is not supported on GPU")
@SKIP_ENV_ASCEND(reason="nanmedian is not supported on Ascend")
def test_nanmedian1():
    torch_a = torch.tensor([[2, 3, 1], [float('nan'), 1, float('nan')]])
    torch_out = torch.nanmedian(torch_a, 1, keepdim=True)
    ms_a = ms_torch.tensor([[2, 3, 1], [float('nan'), 1, float('nan')]])
    ms_out = ms_torch.nanmedian(ms_a, 1, keepdim=True)
    param_compare(torch_out[0], ms_out[0], equal_nan=True)
    param_compare(torch_out[1], ms_out[1])

@SKIP_ENV_GPU(reason="nanmedian is not supported on GPU")
@SKIP_ENV_ASCEND(reason="nanmedian is not supported on Ascend")
def test_nanmedian2():
    x = np.random.randint(0, 5, (2, 3, 4)).astype(np.float32)
    mask = np.random.randint(0, 2, (2, 3, 4)).astype(np.bool8)

    torch_x = torch.tensor(x)
    torch_mask = torch.tensor(mask)
    torch_in = torch_x.masked_fill(torch_mask, float('nan'))
    ms_x = ms_torch.tensor(x)
    ms_mask = ms_torch.tensor(mask)
    ms_in = ms_x.masked_fill(ms_mask, float('nan'))

    torch_out2 = torch.nanmedian(torch_in, 2, keepdim=True)
    ms_out2 = ms_torch.nanmedian(ms_in, 2, keepdim=True)

    param_compare(torch_out2[0], ms_out2[0], equal_nan=True)
    param_compare(torch_out2[1], ms_out2[1])

    torch_out3 = torch.nanmedian(torch_in)
    ms_out3 = ms_torch.nanmedian(ms_in)
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy(), equal_nan=True)
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype

@SKIP_ENV_CPU(reason="[CI] ms2.4.0 0920 still not pass, Unsupported op [ReduceAll] on CPU under this dtype.")
def test_all1():
    data = np.array([[0, 1], [2, 3]])
    torch_input = torch.tensor(data)
    torch_out = torch.all(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.all(ms_input)
    param_compare(torch_out, ms_out)

@SKIP_ENV_CPU(reason="[CI] ms2.4.0 0920 still not pass, Unsupported op [ReduceAll] on CPU under this dtype.")
def test_all2():
    data = np.array([[0., 1.], [2., 3.]])
    torch_input = torch.tensor(data)
    torch_out = torch.all(torch_input, dim=0)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.all(ms_input, dim=0)
    param_compare(torch_out, ms_out)

def test_randn():
    size = ()
    torch_out = torch.randn(size)
    ms_out = ms_torch.randn(size)
    type_shape_compare(torch_out, ms_out)

@SKIP_ENV_GRAPH_MODE(reason='`out` not support graph mode')
def test_randn_out():
    size = (2, 3)
    ms_tensor = ms_torch.tensor(2.)
    torch_tensor = torch.tensor(2.)

    torch.randn(size, out=torch_tensor)
    ms_torch.randn(size, out=ms_tensor)
    type_shape_compare(torch_tensor, ms_tensor)

def test_clamp_max():
    input = np.array([[1.0, 5.0],[10.0, 20.0]]).astype(np.float32)
    py_tensor = torch.tensor(input)
    torch_out = torch.clamp_max(py_tensor, 10.0)

    ms_tensor = ms_torch.tensor(input)
    ms_out = ms_torch.clamp_max(ms_tensor, 10.0)
    param_compare(torch_out, ms_out)

def test_clamp_min():
    input = np.array([[1.0, 5.0],[10.0, 20.0]]).astype(np.float32)
    py_tensor = torch.tensor(input)
    torch_out = torch.clamp_min(py_tensor, 5.0)

    ms_tensor = ms_torch.tensor(input)
    ms_out = ms_torch.clamp_min(ms_tensor, 5.0)
    param_compare(torch_out, ms_out)

@SKIP_ENV_GRAPH_MODE(reason='inplace not support graph')
def test_clamp_max_():
    input = np.array([[1.0, 5.0],[10.0, 20.0]]).astype(np.float32)
    py_tensor = torch.tensor(input)
    torch.clamp_max_(py_tensor, 10.0)

    ms_tensor = ms_torch.tensor(input)
    ms_torch.clamp_max_(ms_tensor, 10.0)
    param_compare(py_tensor, ms_tensor)

@SKIP_ENV_GRAPH_MODE(reason='inplace not support graph')
def test_clamp_min_():
    input = np.array([[1.0, 5.0],[10.0, 20.0]]).astype(np.float32)
    py_tensor = torch.tensor(input)
    torch.clamp_min_(py_tensor, 5.0)

    ms_tensor = ms_torch.tensor(input)
    ms_torch.clamp_min_(ms_tensor, 5.0)
    param_compare(py_tensor, ms_tensor)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_range1()
    test_range2()
    test_range_requires_grad()
    test_astensor()
    test_zeros_like()
    test_ones_like()
    test_empty_like()
    test_full()
    test_full_like()
    test_where()
    test_where2()
    test_where3()
    test_seed()
    test_rand()
    test_linspace()
    test_take()
    test_abs()
    test_abs1()
    test_atan2()
    test_clamp()
    test_cos()
    test_fft()
    test_fmod()
    test_frac()
    test_log()
    test_sin()
    test_norm_p_inf()
    test_norm_p_minus_inf()
    test_norm_p_minus_1()
    test_norm_p_minus_2()
    test_norm_fro()
    test_norm_p_0()
    test_norm_p_1()
    test_norm_p_2()
    test_norm_p_2_jit()
    test_bartlett_window()
    test_hamming_window()
    test_hann_windoww()
    test_cumsum()
    test_einsum()
    test_histc()
    test_triu()
    test_index_select()
    test_bmm()
    test_baddbmm()
    test_argmin()
    test_argmax()
    test_broadcast_to()
    test_ravel()
    test_numel()
    test_logsumexp()
    test_addmv()
    test_dot()
    test_inverse()
    test_scatter_1()
    test_topk()
    test_topk_with_dim()
    test_addbmm()
    test_allclose()
    test_allclose_equal_nan_false()
    test_isclose()
    test_isclose_equal_nan_false()
    test_addmm()
    test_cholesky()
    test_dist()
    test_aminmax()
    test_any()
    test_cholesky_inverse()
    test_isinf()
    test_isneginf()
    test_isposinf()
    test_isreal()
    test_rfft()
    test_polar()
    test_narrow()
    test_vdot_float64()
    test_vdot_int()
    test_vdot_complex()
    test_amax()
    test_amax_float64()
    test_amin()
    test_amin_float64()
    test_nanmean()
    test_nansum()
    test_std()
    test_tile()
    test_vstack()
    test_flipud()
    test_det()
    test_outer()
    test_unique_consecutive()
    test_block_diag()
    test_logspace()
    test_column_stack()
    test_hstack()
    test_movedim()
    test_moveaxis()
    test_swapdims()
    test_swapaxes()
    test_swapaxes2()
    test_row_stack()
    #test_matrix_exp()
    test_argwhere()
    test_mv()
    test_blackman_window()
    test_tril_indices()
    test_triu_indices()
    test_geqrf()
    test_trapz()
    test_trapezoid()
    test_bucketize()
    test_lcm()
    test_renorm()
    test_tensordot()
    test_randn_like()
    test_rand_like()
    test_kron()
    test_gcd()
    test_index_add()
    test_index_add_dim2()
    test_index_copy()
    test_scatter_add()
    test_std_mean()
    test_clone()
    test_dstack()
    test_randint_like()
    test_kaiser_window()
    test_cartesian_prod()
    test_combinations()
    test_histc()
    test_fmax()
    test_fmin()
    test_var_mean()
    test_is_nonzero()
    test_isin()
    test_normal()
    # test_normal2()
    test_orgqr()
    test_bernoulli()
    test_bernoulli_grad()
    test_is_conj()
    test_resolve_conj()
    test_is_conj_jit()
    test_resolve_conj_jit()
    test_scatter_reduce_amax()
    test_scatter_reduce_amin()
    test_scatter_reduce_prod()
    test_scatter_reduce_sum()
    test_asarray()
    test_result_type()
    test_complex()
    test_linspace_tensor_input()
    test_index_reduce_amax()
    test_index_reduce_amin()
    test_index_reduce_prod()
    test_can_cast()
    test_deterministic_apis()
    test_diagonal_scatter()
    test_empty_like_fp64()
    test_all1()
    test_all2()
    test_nanmedian1()
    test_nanmedian2()
    test_cholesky_solve()
    test_cholesky_solve_fp64()
    test_renorm_fp64()
    test_bmm_fp64()
    test_baddbmm_fp64()
    test_addbmm_fp64()
    test_addmm_fp64()
    test_cholesky_fp64()
    test_cholesky_inverse_fp64()
    test_vstack_fp64()
    test_column_stack_fp64()
    test_hstack_fp64()
    test_combinations_fp64()
    test_abs_fp64()
    test_abs_int()
    test_promote_types()
    test_tensordot_int()
    test_randn()
    test_rand_size()
    test_bucketize_random()
    test_column_stack_complex()
    test_trapz1()
    test_randn_out()
    test_clamp_max()
    test_clamp_max_()
    test_clamp_min()
    test_clamp_min_()
