#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context
from ...utils import SKIP_ENV_ASCEND, is_test_under_ascend_context, is_test_under_cpu_context, is_test_under_gpu_context, \
                     is_test_under_pynative_context, param_compare, grad_test, type_shape_compare, graph_lax_level
from mindtorch.utils import is_under_cpu_context

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, SKIP_ENV_GPU, SKIP_ENV_CPU, SKIP_ENV_PYNATIVE_MODE
set_mode_by_env_config()

def test_round1():
    np_array1 = np.array([[1.501, 0.5, 1000.8],[-0.9, -2.5, -24.49]]).astype(np.float32)
    np_array2 = np.array([[1.501, 0.5, 1000.8],[-0.9, -2.5, -24.49]]).astype(np.float64)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch.round(torch_tensor1)
    torch_out2 = torch.round(torch_tensor2)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_torch.round(ms_tensor1)
    ms_out2 = ms_torch.round(ms_tensor2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)


def test_round2():
    np_array = np.random.randn(20).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.round(torch_tensor, decimals=2)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.round(ms_tensor, decimals=2)

    param_compare(torch_out, ms_out)


def test_round3():
    np_array = np.random.randn(20).astype(np.float32)*10**3

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.round(torch_tensor, decimals=-2)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.round(ms_tensor, decimals=-2)

    param_compare(torch_out, ms_out)


def test_floor1():
    np_array = np.array([[1.501, 0.5, 1000.8],[-0.9, -2.5, -24.49]]).astype(np.float32)
    np_array1 = np.random.randn(2, 3, 5).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.floor(torch_tensor)
    torch_tensor1 = torch.tensor(np_array1)
    torch_out1 = torch.floor(torch_tensor1)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.floor(ms_tensor)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_out1 = ms_torch.floor(ms_tensor1)

    param_compare(torch_out, ms_out)
    param_compare(torch_out1, ms_out1)


def test_ceil1():
    np_array = np.array([[1.501, 0.5, 1000.8],[-0.9, -2.5, -24.49]]).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.ceil(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.ceil(ms_tensor)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_sign1():
    np_array = np.array([[1.1, 0, 0.0], [-0, -0.5, -0.0]]).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.sign(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.sign(ms_tensor)

    param_compare(torch_out, ms_out)



def test_sign2():
    np_array = np.array([0, 1, 5, -2, -9, -0, 5]).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.sign(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.sign(ms_tensor)

    param_compare(torch_out, ms_out)



def test_pow1():
    np_array = np.array([0, 1, 5, -2, -9, -0, 5]).astype(np.float64)
    pow_array = np.array([-2, 2, 1.2, 0, -2, 2, 2]).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_pow_tensor = torch.tensor(pow_array)
    torch_out = torch.pow(torch_tensor,torch_pow_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_pow_tensor = ms_torch.tensor(pow_array)
    ms_out = ms_torch.pow(ms_tensor,ms_pow_tensor)

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="pow currently not support inf and nan input on Ascend")
def test_pow2():
    np_array = np.array([0, 1, 5, -2, -9, -0, 5]).astype(np.int64)
    np_array1 = np.array([0, np.nan, 5, -2, np.nan, -0, 5]).astype(np.int32)
    pow_array = np.array([-2, 2, 1.2, np.inf, -2, 2, np.nan]).astype(np.int64)

    torch_tensor = torch.tensor(np_array)
    torch_tensor1 = torch.tensor(np_array1)
    torch_pow_tensor = torch.tensor(pow_array)
    torch_out = torch.pow(torch_tensor, False)
    torch_out1 = torch.pow(torch_tensor,torch_pow_tensor)
    torch_out2 = torch.pow(torch_tensor1,torch_pow_tensor)
    torch_out3 = torch.pow(0, torch_pow_tensor)
    #TODO: torch has integer wraparound problem
    #torch_out4 = torch.pow(torch_tensor, 2333)

    ms_tensor = ms_torch.tensor(np_array)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_pow_tensor = ms_torch.tensor(pow_array)
    ms_out = ms_torch.pow(ms_tensor, False)
    ms_out1 = ms_torch.pow(ms_tensor,ms_pow_tensor)
    ms_out2 = ms_torch.pow(ms_tensor1,ms_pow_tensor)
    ms_out3 = ms_torch.pow(0, ms_pow_tensor)
    #ms_out4 = ms_torch.pow(ms_tensor, 2333)

    param_compare(torch_out, ms_out)
    #TODO: currently GPU has problem calculating negative inputs
    if not is_test_under_gpu_context():
        param_compare(torch_out1, ms_out1)
        param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)
    #param_compare(torch_out4, ms_out4)

# TODO: On GPU and Ascend not support input above 7-dimentions.
'''
def test_pow3():
    np_array = np.array([[[[[[[[[0, 1, 5, 2, 9, -0, 5]]]]]]]]]).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.pow(torch_tensor, -2.2)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.pow(ms_tensor, -2.2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
'''

def test_pow4():
    np_array = np.array([0, 1.5, 5, 2, -9.5, -0, 5]).astype(np.float16)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.pow(2, torch_tensor)
    torch_out1 = torch.pow(torch_tensor, -2)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.pow(2, ms_tensor)
    ms_out1 = ms_torch.pow(ms_tensor, -2)

    param_compare(torch_out, ms_out)


def test_exp1():
    np_array = np.array([0, 1, 5, 2, 9, -0, 5]).astype(np.double)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.exp(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.exp(ms_tensor)

    param_compare(torch_out, ms_out)


def test_exp2():
    np_array = np.array([0, 1, 5, 2, 9, -0, 5]).astype(np.bool8)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.exp(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.exp(ms_tensor)

    param_compare(torch_out, ms_out)


def test_exp3():
    np_array = np.array([[[[[[[0, 1]]]]]]]).astype(np.int16)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.exp(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.exp(ms_tensor)

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: ms.ops.Mul with int64 input result not correct on Ascend.")
def test_mul1():
    a = np.array([1, 2])
    b = np.array([[3], [4]])

    torch_tensor_a = torch.tensor(a)
    torch_tensor_b = torch.tensor(b)
    torch_out = torch.mul(torch_tensor_a, torch_tensor_b)

    ms_tensor_a = ms_torch.tensor(a)
    ms_tensor_b = ms_torch.tensor(b)
    ms_out = ms_torch.mul(ms_tensor_a, ms_tensor_b)

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: ms.ops.Mul with int64 input result not correct on Ascend.")
def test_multiply():
    a = np.array([1, 2])
    b = np.array([[3], [4]])

    torch_tensor_a = torch.tensor(a)
    torch_tensor_b = torch.tensor(b)
    torch_out1 = torch.multiply(torch_tensor_a, torch_tensor_b)

    ms_tensor_a = ms_torch.tensor(a)
    ms_tensor_b = ms_torch.tensor(b)
    ms_out1 = ms_torch.multiply(ms_tensor_a, ms_tensor_b)

    param_compare(torch_out1, ms_out1)

@SKIP_ENV_ASCEND(reason="mul: ms.ops.mul has bug on Ascend")
def test_mul2():
    b = np.array([[3], [4]])

    torch_tensor_b = torch.tensor(b)
    torch_out = torch.mul(2, torch_tensor_b)
    torch_out1 = torch.multiply(2, torch_tensor_b)

    ms_tensor_b = ms_torch.tensor(b)
    ms_out = ms_torch.mul(2, ms_tensor_b)
    ms_out1 = ms_torch.multiply(2, ms_tensor_b)

    param_compare(torch_out, ms_out)
    param_compare(torch_out1, ms_out1)

def test_absolute():
    np_array = np.array([[0, -1.5, -0.55, 2, 9, -0, 5]]).astype(np.float16)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.absolute(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.absolute(ms_tensor)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_acos():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.acos(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.acos(ms_tensor)

    param_compare(torch_out, ms_out)



def test_arccos():
    np_array = np.random.rand(1, 2, 3, 4).astype(np.float64) * 5

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.arccos(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.arccos(ms_tensor)

    param_compare(torch_out, ms_out, equal_nan=True)



def test_acosh():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.acosh(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.acosh(ms_tensor)

    param_compare(torch_out, ms_out, equal_nan=True)


def test_arccosh():
    np_array = np.random.rand(1, 4, 5, 6).astype(np.float64)
    np_array[0, 0, 0, 0] = 1
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.arccosh(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.arccosh(ms_tensor)

    param_compare(torch_out, ms_out, equal_nan=True)


def test_add():
    np_x = np.random.rand(1, 2, 3, 2).astype(np.int32)
    np_y = np.random.rand(1, 2, 3, 2).astype(np.int32)

    for x_dtype in (np.int16, np.int32, np.uint8, np.half, np.double, np.single):
        for y_dtype in (np.int16, np.int32, np.uint8, np.half, np.double, np.single):
            np_x_ = np_x.astype(x_dtype)
            np_y_ = np_y.astype(y_dtype)
            torch_x = torch.tensor(np_x_)
            torch_y = torch.tensor(np_y_)
            torch_out1 = torch.add(torch_x, 2.1, alpha=2)
            torch_out2 = torch.add(torch_x, torch_y, alpha=2)
            #torch_out2 = torch.add(torch_x, 2, torch_y)
            ms_x = ms_torch.tensor(np_x_)
            ms_y = ms_torch.tensor(np_y_)
            ms_out1 = ms_torch.add(ms_x, 2.1, alpha=2)
            ms_out2 = ms_torch.add(ms_x, ms_y, alpha=2)

            param_compare(torch_out1, ms_out1, equal_nan=True)
            param_compare(torch_out2, ms_out2, equal_nan=True)

def test_addcdiv():
    np_array = np.random.rand(1, 2, 3, 2).astype(np.float32)
    np_x = np.random.rand(1, 2, 3, 2).astype(np.float32)
    np_y = np.random.rand(1, 2, 3, 2).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_x = torch.tensor(np_x)
    torch_y = torch.tensor(np_y)
    torch_out = torch.addcdiv(torch_tensor, torch_x, torch_y, value=2.1)
    #torch_out = torch.addcdiv(torch_tensor, 2.1, torch_x, torch_y)
    ms_tensor = ms_torch.tensor(np_array)
    ms_x = ms_torch.tensor(np_x)
    ms_y = ms_torch.tensor(np_y)
    ms_out = ms_torch.addcdiv(ms_tensor, ms_x, ms_y, value=2.1)

    param_compare(torch_out, ms_out)

def test_addcdiv_fp64():
    np_array = np.random.rand(1, 2, 3, 2).astype(np.float64)
    np_x = np.random.rand(1, 2, 3, 2).astype(np.float64)
    np_y = np.random.rand(1, 2, 3, 2).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_x = torch.tensor(np_x)
    torch_y = torch.tensor(np_y)
    torch_out = torch.addcdiv(torch_tensor, torch_x, torch_y, value=2.1)
    #torch_out = torch.addcdiv(torch_tensor, 2.1, torch_x, torch_y)
    ms_tensor = ms_torch.tensor(np_array)
    ms_x = ms_torch.tensor(np_x)
    ms_y = ms_torch.tensor(np_y)
    ms_out = ms_torch.addcdiv(ms_tensor, ms_x, ms_y, value=2.1)

    param_compare(torch_out, ms_out)


def test_addcmul():
    np_array = np.random.rand(1, 2, 3, 2).astype(np.float32)
    np_x = np.random.rand(1, 2, 3, 2).astype(np.float32)
    np_y = np.random.rand(1, 2, 3, 2).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_x = torch.tensor(np_x)
    torch_y = torch.tensor(np_y)
    torch_out = torch.addcmul(torch_tensor, torch_x, torch_y, value=2.1)

    ms_tensor = ms_torch.tensor(np_array)
    ms_x = ms_torch.tensor(np_x)
    ms_y = ms_torch.tensor(np_y)
    ms_out = ms_torch.addcmul(ms_tensor, ms_x, ms_y, value=2.1)
    param_compare(torch_out, ms_out)

def test_addcmul_fp64():
    np_array = np.random.rand(1, 2, 3, 2).astype(np.float64)
    np_x = np.random.rand(1, 2, 3, 2).astype(np.float64)
    np_y = np.random.rand(1, 2, 3, 2).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_x = torch.tensor(np_x)
    torch_y = torch.tensor(np_y)
    torch_out = torch.addcmul(torch_tensor, torch_x, torch_y, value=2.1)

    ms_tensor = ms_torch.tensor(np_array)
    ms_x = ms_torch.tensor(np_x)
    ms_y = ms_torch.tensor(np_y)
    ms_out = ms_torch.addcmul(ms_tensor, ms_x, ms_y, value=2.1)
    param_compare(torch_out, ms_out)

def test_angle():
    np_array = np.array([[[1, -20, -1j, 0j, -0j, -1+1j], [0, -0, 3-3j, -0-0.6j, -1-0.01j, 1+1.732j]]])

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.angle(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.angle(ms_tensor)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), equal_nan=True)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape


def test_asin():
    np_array = np.random.rand(1, 1, 1, 1, 1, 1, 2, 3, 2).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.asin(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.asin(ms_tensor)

    param_compare(torch_out, ms_out)



def test_arcsin():
    np_array = np.random.rand(1, 2, 3, 4).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.arcsin(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.arcsin(ms_tensor)

    param_compare(torch_out, ms_out)


def test_asinh():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float64)
    np_array = np_array * 100
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.asinh(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.asinh(ms_tensor)

    param_compare(torch_out, ms_out)



def test_arcsinh():
    np_array = np.random.rand(1, 2, 3, 2).astype(np.int32) * 50
    np_array[0, 0, 0, 0] = 0
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.arcsinh(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.arcsinh(ms_tensor)

    param_compare(torch_out, ms_out)


def test_atan():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.atan(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.atan(ms_tensor)

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="Atan currently not support float64 on Ascend")
def test_atan_fp64():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.atan(torch_tensor)
    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.atan(ms_tensor)

    param_compare(torch_out, ms_out)

def test_arctan():
    np_array = np.random.rand(2, 3, 4).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.arctan(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.arctan(ms_tensor)
    if is_test_under_ascend_context():
        param_compare(torch_out, ms_out, atol=1e-5)
    else:
        param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="Arctan currently not support float64 on Ascend")
def test_arctan_fp64():
    np_array = np.random.rand(1, 2, 3, 4).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.arctan(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.arctan(ms_tensor)

    param_compare(torch_out, ms_out)

def test_arctan_int():
    np_array = np.random.rand(3, 4, 5).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.arctan(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.arctan(ms_tensor)

    param_compare(torch_out, ms_out)

def test_atanh():
    #atanh already support float64 on Ascend
    np_array = np.random.rand(2, 3, 2).astype(np.float64)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.atanh(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.atanh(ms_tensor)

    param_compare(torch_out, ms_out)


def test_arctanh():
    #atanh already support float64 on Ascend
    np_array = np.random.rand(1, 4, 5, 6).astype(np.float64)
    np_array[0, 0, 0, 0] = 0
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.arctanh(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.arctanh(ms_tensor)

    param_compare(torch_out, ms_out)


def test_arctan2():
    np_array = np.random.rand(2, 3, 4).astype(np.float32)
    np_other = np.random.rand(2, 3, 4).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out = torch.arctan2(torch_tensor, torch_other)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_out = ms_torch.arctan2(ms_tensor, ms_other)

    param_compare(torch_out, ms_out)


@SKIP_ENV_ASCEND(reason="Arctan2 currently not support float64 on Ascend")
def test_arctan2_fp64():
    np_array = np.random.rand(1, 4, 5, 6).astype(np.float64)
    np_other = np.random.rand(1, 4, 5, 6).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out = torch.arctan2(torch_tensor, torch_other)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_out = ms_torch.arctan2(ms_tensor, ms_other)

    param_compare(torch_out, ms_out)


def test_bitwise_not():
    np_array1 = np.arange(-5, 12).astype(np.uint8)
    np_array2 = np.arange(-10, 10).astype(np.int16)
    np_array3 = np.array([[[False, True, True, False, False]]])

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor3 = torch.tensor(np_array3)
    torch_out1 = torch.bitwise_not(torch_tensor1)
    torch_out2 = torch.bitwise_not(torch_tensor2)
    torch_out3 = torch.bitwise_not(torch_tensor3)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_tensor3 = ms_torch.tensor(np_array3)
    ms_out1 = ms_torch.bitwise_not(ms_tensor1)
    ms_out2 = ms_torch.bitwise_not(ms_tensor2)
    ms_out3 = ms_torch.bitwise_not(ms_tensor3)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)


def test_bitwise():
    np_array1 = np.arange(-5, 11).reshape(1, 2, 2, 4).astype(np.bool8)
    np_array2 = np.arange(-10, 6).reshape(2, 2, 4).astype(np.bool8)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch.bitwise_and(torch_tensor1, torch_tensor2)
    torch_out2 = torch.bitwise_or(torch_tensor1, 3)
    torch_out3 = torch.bitwise_xor(True, torch_tensor2)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_torch.bitwise_and(ms_tensor1, ms_tensor2)
    ms_out2 = ms_torch.bitwise_or(ms_tensor1, 3)
    ms_out3 = ms_torch.bitwise_xor(True, ms_tensor2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)



def test_bitwise_shift():
    np_array1 = np.arange(-5, 11).reshape(2, 2, 4).astype(np.int8)
    np_array2 = np.array([1,2,7,1,2,5,1,2,-1,-3,-4,0,2,1,0,0]).reshape(2, 2, 4).astype(np.int8)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch.bitwise_left_shift(torch_tensor1, torch_tensor2)
    torch_out2 = torch.bitwise_right_shift(torch_tensor1, 3)
    torch_out3 = torch.bitwise_right_shift(True, torch_tensor2)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_torch.bitwise_left_shift(ms_tensor1, ms_tensor2)
    ms_out2 = ms_torch.bitwise_right_shift(ms_tensor1, 3)
    ms_out3 = ms_torch.bitwise_right_shift(True, ms_tensor2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)


def test_clip():
    np_array = np.random.rand(1, 2, 3, 4).astype(np.float32)
    min = 0.35
    max = 0.65
    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.clip(torch_tensor, torch.tensor(min), torch.tensor(max))
    torch_out2 = torch.clip(torch_tensor, 0.85, max)
    torch_out3 = torch.clip(torch_tensor, None, max)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out1 = ms_torch.clip(ms_tensor, ms_torch.tensor(min), ms_torch.tensor(max))
    ms_out2 = ms_torch.clip(ms_tensor, 0.85, max)
    ms_out3 = ms_torch.clip(ms_tensor, None, max)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)


def test_conj_physical():
    np_array1 = np.array([[1, 2, 3, 4]]).astype(np.int16)
    np_array2 = np.array([[1+5j, 2-1j, 3.0, -4j, -0j]])

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch.conj_physical(torch_tensor1)
    torch_out2 = torch.conj_physical(torch_tensor2)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_torch.conj_physical(ms_tensor1)
    ms_out2 = ms_torch.conj_physical(ms_tensor2)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype


def test_copysign():
    np_other = np.array([[0.0, -0.0, 1, 1.5, -0.5, -20]]).astype(np.half)
    np_array = np.array([0, -0, 0, 1, 1, 1]).astype(np.int32)

    for type_input in (np.int32, np.half, np.float32):
        torch_tensor = torch.tensor(np_array.astype(type_input))
        ms_tensor = ms_torch.tensor(np_array.astype(type_input))
        for type_other in (np.half, np.int8, np.int32):
            torch_other = torch.tensor(np_other.astype(type_other))
            torch_out1 = torch.copysign(torch_tensor, torch_other)
            ms_other = ms_torch.tensor(np_other.astype(type_other))
            ms_out1 = ms_torch.copysign(ms_tensor, ms_other)
            assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
            assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
        torch_out2 = torch.copysign(torch_tensor, -0)
        ms_out2 = ms_torch.copysign(ms_tensor, -0)
        assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
        assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype


def test_cosh():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float64) - 0.5
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.cosh(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.cosh(ms_tensor)

    param_compare(torch_out, ms_out)

    np_array = np.random.rand(2, 3, 2).astype(np.int32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.cosh(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.cosh(ms_tensor)

    param_compare(torch_out, ms_out)


def test_deg2rad():
    np_array = np.array([[180, -180, 360, 30, 0, 57, 80]])

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.deg2rad(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.deg2rad(ms_tensor)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape


def test_digamma():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float32) - 0.5
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.digamma(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.digamma(ms_tensor)
    param_compare(torch_out, ms_out, atol=1e-5, equal_nan=True)

@SKIP_ENV_ASCEND(reason="digamma not support float64 on Ascend")
def test_digamma_fp64():
    np_array = np.random.rand(1, 1, 1, 2, 3, 2).astype(np.float64)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.digamma(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.digamma(ms_tensor)
    param_compare(torch_out, ms_out, atol=1e-5, equal_nan=True)


def test_lgamma():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float32) - 0.5
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.lgamma(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.lgamma(ms_tensor)

    param_compare(torch_out, ms_out, atol=1e-5)

@SKIP_ENV_ASCEND(reason="digamma not support float64 on Ascend")
def test_lgamma_fp64():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float64) - 0.5
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.lgamma(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.lgamma(ms_tensor)

    param_compare(torch_out, ms_out, atol=1e-5)

def test_erf():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float32) - 0.5
    np_array = np_array * 4
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.erf(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.erf(ms_tensor)
    if is_test_under_ascend_context():
        param_compare(torch_out, ms_out, atol=1e-4)
    else:
        param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="erf not support float64 on Ascend")
def test_erf_fp64():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float64) - 0.5
    np_array = np_array * 4
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.erf(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.erf(ms_tensor)

    param_compare(torch_out, ms_out)

def test_erfc():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float32) - 0.5
    np_array = np_array * 4
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.erfc(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.erfc(ms_tensor)
    if is_test_under_ascend_context():
        param_compare(torch_out, ms_out, atol=1e-4)
    else:
        param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="erfc not support float64 on Ascend")
def test_erfc_fp64():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float64) - 0.5
    np_array = np_array * 4
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.erfc(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.erfc(ms_tensor)

    param_compare(torch_out, ms_out)

def test_erfinv():
    np_array = np.random.rand(2, 3, 4).astype(np.float32) - 0.5
    #TODO: Inaccurate on Ascend when input is close to 1
    if not is_test_under_ascend_context():
        np_array = np_array * 1.9
        np_array[0, 0, 0:3] = [-1, 1, 0.98]
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.erfinv(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.erfinv(ms_tensor)
    #TODO: Inaccurate for float32 in graph mode
    if is_test_under_ascend_context():
        param_compare(torch_out, ms_out, atol=1e-4)
    else:
        param_compare(torch_out, ms_out)

@SKIP_ENV_GRAPH_MODE(reason='inplace not support graph')
def test_exp2_():
    np_array = np.random.rand(2, 3, 4).astype(np.float64) - 0.5
    np_array = np_array * 10
    np_array[0, 0, 0:3] = [0, 10, 25]

    torch_tensor = torch.tensor(np_array)
    torch.exp2_(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_torch.exp2_(ms_tensor)

    param_compare(torch_tensor, ms_tensor)


def test_expm1():
    np_array = np.random.rand(2, 3, 4).astype(np.float32) - 0.5
    np_array = np_array * 10
    np_array[0, 0, 0:3] = [0, 10, 25]

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.expm1(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.expm1(ms_tensor)

    param_compare(torch_out, ms_out)


def test_fake_quantize():
    np_array = np.random.randn(2, 2, 12).astype(np.float32)*10
    scales = (np.random.randn(2).astype(np.float32) + 1.1) * 0.1
    zero_points = np.array([0, 1]).astype(np.int32)
    axis = 1
    min = 0
    max = 255

    torch_tensor = torch.tensor(np_array)
    torch_scales = torch.tensor(scales)
    torch_zero_points = torch.tensor(zero_points)
    torch_out1 = torch.fake_quantize_per_channel_affine(torch_tensor, torch_scales, torch_zero_points, axis, min, max)
    torch_out2 = torch.fake_quantize_per_tensor_affine(torch_tensor, 0.04, 1, min, max)

    ms_tensor = ms_torch.tensor(np_array)
    ms_scales = ms_torch.tensor(scales)
    ms_zero_points = ms_torch.tensor(zero_points)
    ms_out1 = ms_torch.fake_quantize_per_channel_affine(ms_tensor, ms_scales, ms_zero_points, axis, min, max)
    ms_out2 = ms_torch.fake_quantize_per_tensor_affine(ms_tensor, 0.04, 1, min, max)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert ms_out1.asnumpy().shape == torch_out1.numpy().shape
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert ms_out2.asnumpy().shape == torch_out2.numpy().shape


def test_fix():
    np_array = (np.random.rand(3, 4, 5) * 10 - 5).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.fix(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.fix(ms_tensor)

    param_compare(torch_out, ms_out)

def test_float_power():
    np_array = np.random.rand(3, 4, 5)*5
    np_exponent = np.random.rand(4, 5)*5
    np_array = np_array.astype(np.float32)
    np_exponent = np_exponent.astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_exponent = torch.tensor(np_exponent)
    torch_out1 = torch.float_power(torch_tensor, torch_exponent)
    torch_out2 = torch.float_power(torch_tensor, 2)
    torch_out3 = torch.float_power(2, torch_exponent)

    ms_tensor = ms_torch.tensor(np_array)
    ms_exponent = ms_torch.tensor(np_exponent)
    ms_out1 = ms_torch.float_power(ms_tensor, ms_exponent)
    ms_out2 = ms_torch.float_power(ms_tensor, 2)
    ms_out3 = ms_torch.float_power(2, ms_exponent)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)


# TODO: mindspore.ops.float_power not support complex now
'''
def test_float_power_complex():
    np_array = np.random.rand(3, 4, 5).astype(np.float32)*5
    np_exponent = np.random.rand(4, 5)*5
    np_array = np_array.astype(np.float32)
    np_exponent = np_exponent.astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out2 = torch.float_power(torch_tensor, 2+3j)
    print("torch_out2:", torch_out2)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out2 = ms_torch.float_power(ms_tensor, 2+3j)

    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
'''

@SKIP_ENV_ASCEND(reason="ascend not support inf result")
def test_floor_divide():
    np_array = (np.random.randn(3, 4, 5) * 20).astype(np.int32)
    np_other = (np.random.rand(4, 5) * 20).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out1 = torch.floor_divide(torch_tensor, torch_other)
    torch_out2 = torch.floor_divide(torch_tensor, 2)
    torch_out3 = torch.floor_divide(torch_tensor, 0.)
    try:
        torch_out4 = torch.floor_divide(torch_tensor, 0)
    except RuntimeError as e:
        torch_e = e
    torch_out5 = torch.floor_divide(2, torch_other)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_out1 = ms_torch.floor_divide(ms_tensor, ms_other)
    ms_out2 = ms_torch.floor_divide(ms_tensor, 2)
    ms_out3 = ms_torch.floor_divide(ms_tensor, 0.)
    try:
        ms_out4 = ms_torch.floor_divide(ms_tensor, 0)
    except RuntimeError as e:
        ms_e = e
    ms_out5 = ms_torch.floor_divide(2, ms_other)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3, equal_nan=True)
    param_compare(torch_out5, ms_out5)
    assert str(torch_e) == str(ms_e)

@SKIP_ENV_CPU(reason="testcase for ascend only, because ascend not support inf, cpu test will be cover by test_floor_divide")
@SKIP_ENV_GPU(reason="testcase for ascend only, because ascend not support inf, gpu test will be cover by test_floor_divide")
def test_floor_divide_ascend():
    np_array = (np.random.randn(3, 4, 5) * 20).astype(np.int32)
    np_other = (np.random.rand(4, 5) * 20).astype(np.float32)
    np_other = np.where(np_other == 0, 1, np_other)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out1 = torch.floor_divide(torch_tensor, torch_other)
    torch_out2 = torch.floor_divide(torch_tensor, 2)
    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_out1 = ms_torch.floor_divide(ms_tensor, ms_other)
    ms_out2 = ms_torch.floor_divide(ms_tensor, 2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_frexp():
    for type1 in (np.float16, np.float32):
        np_array = (np.random.randn(1, 4, 4)).astype(type1)
        torch_tensor = torch.tensor(np_array)
        ms_tensor = ms_torch.tensor(np_array)

        torch_out1, torch_out2 = torch.frexp(torch_tensor)
        ms_out1, ms_out2 = ms_torch.frexp(ms_tensor)
        param_compare(torch_out1, ms_out1)
        param_compare(torch_out2, ms_out2)
        if is_test_under_pynative_context():
            torch_out3 = torch.zeros(torch_out1.shape, dtype=torch_out1.dtype)
            torch_out4 = torch.zeros(torch_out2.shape, dtype=torch_out2.dtype)
            ms_out3 = ms_torch.zeros(ms_out1.shape, dtype=ms_out1.dtype)
            ms_out4 = ms_torch.zeros(ms_out2.shape, dtype=ms_out2.dtype)
            torch.frexp(torch_tensor, out=(torch_out3, torch_out4))
            ms_torch.frexp(ms_tensor, out=(ms_out3, ms_out4))
            param_compare(torch_out3, ms_out3)
            param_compare(torch_out4, ms_out4)


@SKIP_ENV_ASCEND(reason="frexp not support float64 on Ascend")
def test_frexp_fp64():
    np_array = np.random.randn(2, 2).astype(np.float64)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = ms_torch.tensor(np_array)

    torch_out1, torch_out2 = torch.frexp(torch_tensor)
    ms_out1, ms_out2 = ms_torch.frexp(ms_tensor)
    if is_test_under_pynative_context():
        torch_out3 = torch.zeros(torch_out1.shape, dtype=torch_out1.dtype)
        torch_out4 = torch.zeros(torch_out2.shape, dtype=torch_out2.dtype)
        ms_out3 = ms_torch.zeros(ms_out1.shape, dtype=ms_out1.dtype)
        ms_out4 = ms_torch.zeros(ms_out2.shape, dtype=ms_out2.dtype)
        torch.frexp(torch_tensor, out=(torch_out3, torch_out4))
        ms_torch.frexp(ms_tensor, out=(ms_out3, ms_out4))
        param_compare(torch_out3, ms_out3)
        param_compare(torch_out4, ms_out4)
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_gradient():
    np_array = np.array([4., 1., 1., 16.]).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.gradient(torch_tensor, spacing=torch.tensor(1))

    ms_tensor = ms_torch.tensor(np_array)
    ms_out1 = ms_torch.gradient(ms_tensor, spacing=ms_torch.tensor(1))

    param_compare(torch_out1, ms_out1)

@SKIP_ENV_ASCEND(reason="gradient currently not support float64 on Ascend")
def test_gradient_fp64():
    np_array = np.random.randn(4)

    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.gradient(torch_tensor, spacing=torch.tensor(1))

    ms_tensor = ms_torch.tensor(np_array)
    ms_out1 = ms_torch.gradient(ms_tensor, spacing=ms_torch.tensor(1))

    param_compare(torch_out1, ms_out1)

def test_imag():
    np_array = np.array([[1+5j, 2-1j, 3.0, -4j, -0j]])

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.imag(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.imag(ms_tensor)

    param_compare(torch_out, ms_out)


def test_ldexp():
    np_array = (np.random.rand(1, 4, 5, 6)*5-2).astype(np.int32)
    np_other = (np.random.rand(1, 4, 5, 6)*5-2).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out = torch.ldexp(torch_tensor, torch_other)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_out = ms_torch.ldexp(ms_tensor, ms_other)

    param_compare(torch_out, ms_out)

def test_lerp():
    np_array = (np.random.rand(1, 4, 5, 5) * 5 - 2).astype(np.float32)
    np_other = (np.random.rand(4, 5, 5) * 5 - 2).astype(np.float32)
    np_weight = (np.random.rand(1, 4, 5, 5) * 5 - 2).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_weight = torch.tensor(np_weight)
    torch_out1 = torch.lerp(torch_tensor, torch_other, torch_weight)
    torch_out2 = torch.lerp(torch_tensor, torch_other, 3)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_weight = ms_torch.tensor(np_weight)
    ms_out1 = ms_torch.lerp(ms_tensor, ms_other, ms_weight)
    ms_out2 = ms_torch.lerp(ms_tensor, ms_other, 3)

    param_compare(torch_out1, ms_out1, atol=1e-6)
    param_compare(torch_out2, ms_out2, atol=1e-6)

@SKIP_ENV_ASCEND(reason="lerp currently not support float64 on Ascend")
def test_lerp_fp64():
    np_array = np.random.rand(2, 2)
    np_other = np.random.rand(2)
    np_weight = np.random.rand(2, 2)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_weight = torch.tensor(np_weight)
    torch_out1 = torch.lerp(torch_tensor, torch_other, torch_weight)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_weight = ms_torch.tensor(np_weight)
    ms_out1 = ms_torch.lerp(ms_tensor, ms_other, ms_weight)

    param_compare(torch_out1, ms_out1, atol=1e-6)

def test_logaddexp():
    np_array = (np.random.rand(1, 4, 5, 6) * 5 - 2).astype(np.float32)
    np_other = (np.random.rand(1, 4, 5, 6) * 5 - 2).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out = torch.logaddexp(torch_tensor, torch_other)
    torch_out2 = torch.logaddexp2(torch_tensor, torch_other)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_out = ms_torch.logaddexp(ms_tensor, ms_other)
    ms_out2 = ms_torch.logaddexp2(ms_tensor, ms_other)

    param_compare(torch_out, ms_out, atol=1e-5)
    param_compare(torch_out2, ms_out2, atol=1e-5)

@SKIP_ENV_ASCEND(reason="logaddexp currently not support float64 on Ascend")
def test_logaddexp_fp64():
    np_array = np.random.rand(2, 3)
    np_other = np.random.rand(2, 3)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out = torch.logaddexp(torch_tensor, torch_other)
    torch_out2 = torch.logaddexp2(torch_tensor, torch_other)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_out = ms_torch.logaddexp(ms_tensor, ms_other)
    ms_out2 = ms_torch.logaddexp2(ms_tensor, ms_other)

    param_compare(torch_out, ms_out)
    param_compare(torch_out2, ms_out2)

def test_logical_and():
    np_array = np.random.randn(120).reshape(2, 2, 6, 5) * 16 - 8
    np_array = np_array.astype(np.int16)
    np_other = np.random.randn(60).reshape(2, 6, 5) * 2
    np_other = np_other.astype(np.bool8)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out = torch.logical_and(torch_tensor, torch_other)
    torch_out2 = torch.logical_or(torch_tensor, torch.tensor(3))
    torch_out3 = torch.logical_xor(torch.tensor(True), torch_other)
    torch_out4 = torch.logical_not(torch_tensor)
    torch_out5 = torch.logical_not(torch_other)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_out = ms_torch.logical_and(ms_tensor, ms_other)
    ms_out2 = ms_torch.logical_or(ms_tensor, ms_torch.tensor(3))
    ms_out3 = ms_torch.logical_xor(ms_torch.tensor(True), ms_other)
    ms_out4 = ms_torch.logical_not(ms_tensor)
    ms_out5 = ms_torch.logical_not(ms_other)

    param_compare(torch_out, ms_out)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)
    param_compare(torch_out4, ms_out4)
    param_compare(torch_out5, ms_out5)


def test_logit():
    np_array = np.random.randn(120).reshape(4, 6, 5) * 3 - 1
    np_array = np_array.astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.logit(torch_tensor, 0.001)
    torch_out2 = torch.logit(torch_tensor, 0.4)
    torch_out3 = torch.logit(torch_tensor)
    torch_out4 = torch.logit(torch_tensor, -0.8)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out1 = ms_torch.logit(ms_tensor, 0.001)
    ms_out2 = ms_torch.logit(ms_tensor, 0.4)
    ms_out3 = ms_torch.logit(ms_tensor)
    ms_out4 = ms_torch.logit(ms_tensor, -0.8)
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3, equal_nan=True)
    param_compare(torch_out4, ms_out4, equal_nan=True)


def test_lu_solve():
    # lu_solve Prim not support float64 on Ascend
    lu_array = np.random.randn(2, 3, 3).astype(np.float32)
    b_array = np.random.randn(2, 3, 1).astype(np.float32)
    p_array = np.random.randint(1, 3, size=(2, 3)).astype(np.int32)

    torch_lu = torch.tensor(lu_array)
    torch_pivot = torch.tensor(p_array)
    torch_b = torch.tensor(b_array)

    ms_lu = ms_torch.tensor(lu_array)
    ms_pivot = ms_torch.tensor(p_array)
    ms_b = ms_torch.tensor(b_array)

    torch_out = torch.lu_solve(torch_b, torch_lu, torch_pivot)
    ms_out = ms_torch.lu_solve(ms_b, ms_lu, ms_pivot)
    param_compare(torch_out, ms_out)
    @ms.jit
    def lu_solve_test(b, lu, pivot):
        out = ms_torch.lu_solve(b, lu, pivot)
        return out
    ms_out1 = lu_solve_test(ms_b, ms_lu, ms_pivot)
    param_compare(torch_out, ms_out1)


@SKIP_ENV_ASCEND(reason='lu_unpack not support on Ascend')
def test_lu_unpack():
    for type1 in (np.float32, np.float64):
        lu_array1 = np.random.randn(2, 3, 3).astype(type1)
        p_array1 = np.random.randint(1, 3, size=(2,3)).astype(np.int32)
        torch_lu1 = torch.tensor(lu_array1)
        ms_lu1 = ms_torch.tensor(lu_array1)
        torch_pivot1 = torch.tensor(p_array1)
        ms_pivot1 = ms_torch.tensor(p_array1)

        torch_p1, torch_l1, torch_u1 = torch.lu_unpack(torch_lu1, torch_pivot1)
        ms_p1, ms_l1, ms_u1 = ms_torch.lu_unpack(ms_lu1, ms_pivot1)

        param_compare(torch_p1, ms_p1)
        param_compare(torch_l1, ms_l1)
        param_compare(torch_u1, ms_u1)

@SKIP_ENV_GRAPH_MODE(reason="nn.cell currently has memcpy problem in graph mode")
def test_lstsq():
    if is_test_under_ascend_context():
        # lstsq Prim not support float64 on Ascend.
        _type = (np.float32,)
    else:
        _type = (np.float32, np.float64)

    for type1 in _type:
        x1 = np.random.randn(5,5).astype(type1)
        A1 = np.random.randn(5,5).astype(type1)
        x2 = np.random.randn(6,7).astype(type1)
        A2 = np.random.randn(6,7).astype(type1)
        torch_a1 = torch.tensor(A1)
        torch_x1 = torch.tensor(x1)
        ms_a1 = ms_torch.tensor(A1)
        ms_x1 = ms_torch.tensor(x1)
        torch_a2 = torch.tensor(A2)
        torch_x2 = torch.tensor(x2)
        ms_a2 = ms_torch.tensor(A2)
        ms_x2 = ms_torch.tensor(x2)

        #TODO: lstsq not support return qr as the second result
        torch_output1, _ = torch.lstsq(torch_a1,torch_x1)
        ms_output1, _ = ms_torch.lstsq(ms_a1, ms_x1)
        torch_output2, _ = torch.lstsq(torch_a2, torch_x2)
        ms_output2, _ = ms_torch.lstsq(ms_a2, ms_x2)
        param_compare(torch_output1, ms_output1, rtol=1e-4, atol=1e-4)
        param_compare(torch_output2, ms_output2, rtol=1e-4, atol=1e-4)
        #TODO: cpu use ops.lstsq, which doe not support bprop
        if not is_under_cpu_context():
            grad_test('lstsq', ms_torch.lstsq, ms_a1, ms_x1)


def test_tanh():
    np_array = np.random.rand(1, 1, 1, 1, 3, 4, 5).astype(np.float64)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.tanh(torch_tensor)
    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.tanh(ms_tensor)
    param_compare(torch_out, ms_out)
    np_array = np.random.rand(1, 3, 4, 5).astype(np.int32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.tanh(torch_tensor)
    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.tanh(ms_tensor)
    param_compare(torch_out, ms_out)

def test_sigmoid():
    np_array = np.random.rand(1, 1, 1, 1, 3, 4, 5).astype(np.float64) - 0.5
    np_array = np_array * 20

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.sigmoid(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.sigmoid(ms_tensor)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

@SKIP_ENV_ASCEND(reason='mindspore.ops.hypot result not correct on ascend.')
def test_hypot():
    np_array = np.random.rand(2, 3, 4, 5).astype(np.double)
    np_other = -np.random.rand(4, 5).astype(np.uint8)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out = torch.hypot(torch_tensor, torch_other)
    torch_out2 = torch.hypot(torch_tensor, torch.tensor(3))

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    ms_out = ms_torch.hypot(ms_tensor, ms_other)
    ms_out2 = ms_torch.hypot(ms_tensor, ms_torch.tensor(3))

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert ms_out2.asnumpy().shape == torch_out2.numpy().shape


def test_i0():
    np_array = np.random.rand(2, 3, 4, 5).astype(np.double)
    np_array2 = np.arange(12).reshape(3, 4) - 6

    torch_tensor = torch.tensor(np_array)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out = torch.i0(torch_tensor)
    torch_out2 = torch.i0(torch_tensor2)

    ms_tensor = ms_torch.tensor(np_array)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out = ms_torch.i0(ms_tensor)
    ms_out2 = ms_torch.i0(ms_tensor2)

    param_compare(torch_out, ms_out)
    param_compare(torch_out2, ms_out2)


def test_igamma():
    np_array = np.random.rand(2, 3, 4, 5) * 3 + 1
    np_other = np.random.rand(4, 5) * 3 + 1

    torch_tensor1 = torch.tensor(np_array.astype(np.float16))
    torch_other1 = torch.tensor(np_other.astype(np.float16))
    torch_tensor2 = torch.tensor(np_array.astype(np.float32))
    torch_other2 = torch.tensor(np_other.astype(np.float64))
    torch_out1 = torch.igamma(torch_tensor1, torch_other1)
    torch_out2 = torch.igamma(torch_tensor2, torch_other2)

    ms_tensor1 = ms_torch.tensor(np_array.astype(np.float16))
    ms_other1 = ms_torch.tensor(np_other.astype(np.float16))
    ms_tensor2 = ms_torch.tensor(np_array.astype(np.float32))
    ms_other2 = ms_torch.tensor(np_other.astype(np.float64))
    ms_out1 = ms_torch.igamma(ms_tensor1, ms_other1)
    ms_out2 = ms_torch.igamma(ms_tensor2, ms_other2)

    param_compare(torch_out1, ms_out1, equal_nan=True, atol=1e-3)
    param_compare(torch_out2, ms_out2, equal_nan=True)


def test_igammac():
    np_array = np.random.rand(2, 3, 4, 5) * 3 + 1
    np_other = np.random.rand(4, 5) * 3 + 1

    torch_tensor1 = torch.tensor(np_array.astype(np.float16))
    torch_other1 = torch.tensor(np_other.astype(np.float16))
    torch_tensor2 = torch.tensor(np_array.astype(np.float32))
    torch_other2 = torch.tensor(np_other.astype(np.float64))
    torch_out1 = torch.igammac(torch_tensor1, torch_other1)
    torch_out2 = torch.igammac(torch_tensor2, torch_other2)

    ms_tensor1 = ms_torch.tensor(np_array.astype(np.float16))
    ms_other1 = ms_torch.tensor(np_other.astype(np.float16))
    ms_tensor2 = ms_torch.tensor(np_array.astype(np.float32))
    ms_other2 = ms_torch.tensor(np_other.astype(np.float64))
    ms_out1 = ms_torch.igammac(ms_tensor1, ms_other1)
    ms_out2 = ms_torch.igammac(ms_tensor2, ms_other2)

    param_compare(torch_out1, ms_out1, equal_nan=True, atol=1e-3)
    param_compare(torch_out2, ms_out2, equal_nan=True)

def test_mvlgamma():
    np_array = np.random.rand(2, 3, 4, 5).astype(np.double)

    for p in (1, 2, 3):
        torch_tensor = torch.tensor(np_array) + (p-1)/2
        ms_tensor = ms_torch.tensor(np_array) + (p-1)/2

        torch_out = torch.mvlgamma(torch_tensor, p)
        ms_out = ms_torch.mvlgamma(ms_tensor, p)

        assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
        assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
        assert ms_out.asnumpy().shape == torch_out.numpy().shape


def test_nan_to_num():
    np_array = np.array([np.nan, np.inf, -np.inf, 3])
    typetest = [np.half, np.float32, np.int32]
    for i in typetest:
        np_array_ = np_array.astype(i)
        torch_tensor = torch.tensor(np_array_)
        ms_tensor = ms_torch.tensor(np_array_)

        torch_out = torch.nan_to_num(torch_tensor)
        ms_out = ms_torch.nan_to_num(ms_tensor)
        param_compare(torch_out, ms_out)

def test_nan_to_num1():
    if is_test_under_ascend_context():
        np_array = np.array([np.nan, np.inf, -np.inf, 3]).astype(np.float32)
    else:
        np_array = np.array([np.nan, np.inf, -np.inf, 3])
    torch_tensor = torch.tensor(np_array)
    ms_tensor = ms_torch.tensor(np_array)
    torch_out = torch.nan_to_num(torch_tensor, 1.1, 2, -1)
    ms_out = ms_torch.nan_to_num(ms_tensor, 1.1, 2, -1)

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="nan_to_num not support float64 on Ascend")
def test_nan_to_num_fp64():
    np_array = np.array([np.nan, np.inf, -np.inf, 3])
    torch_tensor = torch.tensor(np_array.astype(np.float64))
    ms_tensor = ms_torch.tensor(np_array.astype(np.float64))

    torch_out1 = torch.nan_to_num(torch_tensor)
    ms_out1 = ms_torch.nan_to_num(ms_tensor)
    torch_out2 = torch.nan_to_num(torch_tensor, 1.1, 2, -1)
    ms_out2 = ms_torch.nan_to_num(ms_tensor, 1.1, 2, -1)
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_neg():
    np_array1 = np.array([np.nan, np.inf, -np.inf, 3, 0, -0])
    np_array2 = np.array([-0j, 0j, -0.0, -2+3j, 5+2j, 1, 1j])
    np_array3 = np.random.randn(2, 3, 4).astype(np.uint8)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor3 = torch.tensor(np_array3)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_tensor3 = ms_torch.tensor(np_array3)

    torch_out = torch.neg(torch_tensor1)
    ms_out = ms_torch.neg(ms_tensor1)
    torch_out2 = torch.neg(torch_tensor2)
    ms_out2 = ms_torch.neg(ms_tensor2)
    torch_out3 = torch.neg(torch_tensor3)
    ms_out3 = ms_torch.neg(ms_tensor3)
    torch_out4 = torch.negative(torch_tensor1)
    ms_out4 = ms_torch.negative(ms_tensor1)
    torch_out5 = torch.negative(torch_tensor3)
    ms_out5 = ms_torch.negative(ms_tensor3)


    param_compare(torch_out, ms_out, equal_nan=True)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)
    param_compare(torch_out4, ms_out4, equal_nan=True)
    param_compare(torch_out5, ms_out5)


def test_nextafter():
    #TODO: On CPU when dtype is float32, the result of inf, -inf, 0, -0 is different with pytorch
    np_array1 = np.array([np.nan, np.inf, -np.inf, 3, 0, -0]).astype(np.float64)
    np_other = np.array([1, 2, 3, 3, -5, 6]).astype(np.float64)

    torch_tensor1 = torch.tensor(np_array1)
    torch_other = torch.tensor(np_other)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_other = ms_torch.tensor(np_other)

    torch_out = torch.nextafter(torch_tensor1, torch_other)
    ms_out = ms_torch.nextafter(ms_tensor1, ms_other)

    param_compare(torch_out, ms_out, equal_nan=True)

def test_positive():
    np_array1 = np.array([np.nan, np.inf, -np.inf, 3, 0, -0])
    np_array2 = np.array([-0j, 0j, -0.0, -2+3j, 5+2j, 1, 1j])
    np_array3 = np.array([0, 1, 2, 3, 4, 5]).astype(np.uint8)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor3 = torch.tensor(np_array3)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_tensor3 = ms_torch.tensor(np_array3)

    torch_out = torch.positive(torch_tensor1)
    ms_out = ms_torch.positive(ms_tensor1)
    torch_out2 = torch.positive(torch_tensor2)
    ms_out2 = ms_torch.positive(ms_tensor2)
    torch_out3 = torch.positive(torch_tensor3)
    ms_out3 = ms_torch.positive(ms_tensor3)
    assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), equal_nan=True)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy())
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype
    ms_out[0] = 7
    torch_out[0] = 7
    assert np.allclose(ms_tensor1.asnumpy(), torch_tensor1.numpy())
    assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype

@SKIP_ENV_ASCEND(reason='polygamma not support on Ascend')
def test_polygamma():
    for type1 in (np.float32, np.float64):
        np_array = np.random.randn(3, 3).astype(type1)
        torch_tensor = torch.tensor(np_array)
        ms_tensor = ms_torch.tensor(np_array)
        #TODO:polygamma returns -inf on CPU, and zeros on GPU when n=0
        #torch_out1 = torch.polygamma(0, torch_tensor)
        torch_out2 = torch.polygamma(1, torch_tensor)
        torch_out3 = torch.polygamma(3, torch_tensor)
        torch_out4 = torch.polygamma(8, torch_tensor)
        #ms_out1 = ms_torch.polygamma(0, ms_tensor)
        ms_out2 = ms_torch.polygamma(1, ms_tensor)
        ms_out3 = ms_torch.polygamma(3, ms_tensor)
        ms_out4 = ms_torch.polygamma(8, ms_tensor)

        #param_compare(torch_out1, ms_out1, rtol=1e-3, atol=1e-5)
        param_compare(torch_out2, ms_out2, rtol=1e-3, atol=1e-5)
        param_compare(torch_out3, ms_out3, rtol=1e-3, atol=1e-5)
        param_compare(torch_out4, ms_out4, rtol=1e-3, atol=1e-5)


def test_rad2deg():
    np_array = np.array([[3.14, 1.57, 0, -1.57, -1, 20]])

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.rad2deg(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.rad2deg(ms_tensor)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape


def test_real():
    np_array = np.array([[1+5j, 2-1j, 3.0, -4j, -0j]])

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.real(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.real(ms_tensor)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_reciprocal():
    np_array1 = np.array([[1+5j, 2-1j, 3.0, -4j, -0.1j]])
    #TODO: when input is conj value, result on mindspore is inf+nanj/-inf+nanj
    # while torch returns nan+nanj
    #np_array2 = np.array([[0j, -0j, 0, -0, -0-0j, 0+0j]])
    #np_array2 = np.array([[np.inf, -0.0, 1.0, np.nan]])
    np_array2 = np.array([[np.inf, 0.0, 1.0, np.nan]]).astype(np.float32)
    np_array3 = np.array([[1, 1, 2]]).astype(np.int16)
    np_array4 = np.array([[1, -1, 0]]).astype(np.bool_)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor3 = torch.tensor(np_array3)
    torch_tensor4 = torch.tensor(np_array4)
    torch_out1 = torch.reciprocal(torch_tensor1)
    torch_out2 = torch.reciprocal(torch_tensor2)
    torch_out3 = torch.reciprocal(torch_tensor3)
    torch_out4 = torch.reciprocal(torch_tensor4)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_out1 = ms_torch.reciprocal(ms_tensor1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out2 = ms_torch.reciprocal(ms_tensor2)
    ms_tensor3 = ms_torch.tensor(np_array3)
    ms_out3 = ms_torch.reciprocal(ms_tensor3)
    ms_tensor4 = ms_torch.tensor(np_array4)
    ms_out4 = ms_torch.reciprocal(ms_tensor4)


    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2, equal_nan=True)
    param_compare(ms_out3, torch_out3)
    param_compare(ms_out4, torch_out4)

def test_remainder():
    np_array1 = np.array([[-3., -2, -1, 1, 2, 3]]).astype(np.float16)
    np_array2 = np.array([[1, 2, 3, 4, 5]]).astype(np.int16)
    np_other = np.array([[6, 7, 3, 4, 5]]).astype(np.float32)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_other = torch.tensor(np_other)
    torch_out1 = torch.remainder(torch_tensor1, 2)
    torch_out2 = torch.remainder(torch_tensor2, 3)
    torch_out3 = torch.remainder(torch_tensor2, torch_other)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_out1 = ms_torch.remainder(ms_tensor1, 2)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out2 = ms_torch.remainder(ms_tensor2, 3)
    ms_other = ms_torch.tensor(np_other)
    ms_out3 = ms_torch.remainder(ms_tensor2, ms_other)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy())
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

@SKIP_ENV_ASCEND(reason="ascend not support nan result")
def test_rsqrt():
    np_array1 = np.array([[-3, -2, -1, 0, 2, 3]]).astype(np.float32)
    np_array2 = np.array([[1, 2, 3, 4, 5]]).astype(np.int64)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch.rsqrt(torch_tensor1)
    torch_out2 = torch.rsqrt(torch_tensor2)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_torch.rsqrt(ms_tensor1)
    ms_out2 = ms_torch.rsqrt(ms_tensor2)

    param_compare(ms_out1, torch_out1, equal_nan=True)
    param_compare(ms_out2, torch_out2)

@SKIP_ENV_CPU(reason="testcase for ascend only, because ascend not support nan, cpu test will be covered by test_rsqrt.")
@SKIP_ENV_GPU(reason="testcase for ascend only, because ascend not support nan, gpu test will be covered by test_rsqrt.")
def test_rsqrt_ascend():
    np_array1 = np.array([[1, 2, 3, 4, 5]]).astype(np.int64)
    torch_tensor1 = torch.tensor(np_array1)
    torch_out1 = torch.rsqrt(torch_tensor1)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_out1 = ms_torch.rsqrt(ms_tensor1)
    param_compare(ms_out1, torch_out1)

def test_roll():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float32)
    torch_tensor = torch.tensor(x).view(3, 3)
    ms_tensor =ms_torch.tensor(x).view(3, 3)

    torch_out1 = torch.roll(torch_tensor, 1)
    torch_out2 = torch.roll(torch_tensor, 1, 0)
    torch_out3 = torch.roll(torch_tensor,-1, 0)
    torch_out4 = torch.roll(torch_tensor,shifts=(2, 1), dims=(0, 1))

    ms_out1 = ms_torch.roll(ms_tensor, 1)
    ms_out2 = ms_torch.roll(ms_tensor, 1, 0)
    ms_out3 = ms_torch.roll(ms_tensor, -1, 0)
    ms_out4 = ms_torch.roll(ms_tensor, shifts=(2, 1), dims=(0, 1))

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)
    param_compare(ms_out3, torch_out3)
    param_compare(ms_out4, torch_out4)

def test_rot90():
    np_array = np.array([[0, 1],[2, 3]], dtype=np.int32)
    np_array1 = np.random.randn(2, 3, 3).astype(np.float32)
    dims1 = [0, 1]
    dims2 = [1, 0]
    torch_tensor = torch.tensor(np_array)
    torch_tensor1 = torch.tensor(np_array1)
    ms_tensor = ms_torch.tensor(np_array)
    ms_tensor1 = ms_torch.tensor(np_array1)

    torch_out1 = torch.rot90(torch_tensor, 1, dims1)
    torch_out2 = torch.rot90(torch_tensor, 2, dims1)
    torch_out3 = torch.rot90(torch_tensor, -1, dims1)
    torch_out4 = torch.rot90(torch_tensor, 1, dims2)
    torch_out5 = torch.rot90(torch_tensor1, 1, dims2)
    torch_out6 = torch.rot90(torch_tensor)
    ms_out1 = ms_torch.rot90(ms_tensor, 1, dims1)
    ms_out2 = ms_torch.rot90(ms_tensor, 2, dims1)
    ms_out3 = ms_torch.rot90(ms_tensor, -1, dims1)
    ms_out4 = ms_torch.rot90(ms_tensor, 1, dims2)
    ms_out5 = ms_torch.rot90(ms_tensor1, 1, dims2)
    ms_out6 = ms_torch.rot90(ms_tensor)
    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)
    param_compare(ms_out3, torch_out3)
    param_compare(ms_out4, torch_out4)
    param_compare(ms_out5, torch_out5)
    param_compare(ms_out6, torch_out6)

@SKIP_ENV_CPU(reason="[CI] ms2.4.0 0920 still not pass, need to be fixed.")
def test_searchsorted():
    np_seq =  np.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]])
    np_val =  np.array([[3, 6, 9], [3, 6, 9]])
    torch_seq = torch.tensor(np_seq)
    torch_val = torch.tensor(np_val)
    ms_seq = ms_torch.tensor(np_seq)
    ms_val = ms_torch.tensor(np_val)

    torch_out1 = torch.searchsorted(torch_seq, torch_val)
    torch_out2 = torch.searchsorted(torch_seq, torch_val, out_int32=True, right=True)
    torch_out3 = torch.searchsorted(torch_seq, torch_val, side='right')
    ms_out1 = ms_torch.searchsorted(ms_seq, ms_val)
    ms_out2 = ms_torch.searchsorted(ms_seq, ms_val, out_int32=True, right=True)
    ms_out3 = ms_torch.searchsorted(ms_seq, ms_val, side='right')
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

@SKIP_ENV_CPU(reason="[CI] ms2.4.0 0920 still not pass, need to be fixed.")
def test_searchsorted_int():
    np_seq =  np.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]).astype(np.int32)
    np_val =  np.array([[3, 6, 9], [3, 6, 9]]).astype(np.int32)
    torch_seq = torch.tensor(np_seq)
    torch_val = torch.tensor(np_val)
    ms_seq = ms_torch.tensor(np_seq)
    ms_val = ms_torch.tensor(np_val)

    torch_out1 = torch.searchsorted(torch_seq, torch_val)
    torch_out2 = torch.searchsorted(torch_seq, torch_val, out_int32=True, right=True)
    ms_out1 = ms_torch.searchsorted(ms_seq, ms_val)
    ms_out2 = ms_torch.searchsorted(ms_seq, ms_val, out_int32=True, right=True)
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_searchsorted_fp16():
    np_seq =  np.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]).astype(np.float16)
    np_val =  np.array([[3, 6, 9], [3, 6, 9]]).astype(np.float16)
    torch_seq = torch.tensor(np_seq)
    torch_val = torch.tensor(np_val)
    ms_seq = ms_torch.tensor(np_seq)
    ms_val = ms_torch.tensor(np_val)

    torch_out = torch.searchsorted(torch_seq, torch_val)
    ms_out = ms_torch.searchsorted(ms_seq, ms_val)
    param_compare(torch_out, ms_out)

def test_searchsorted_scalar():
    np_seq =  np.array([1, 3, 5, 7, 9]).astype(np.float16)
    val =  3.0
    torch_seq = torch.tensor(np_seq)
    ms_seq = ms_torch.tensor(np_seq)

    torch_out = torch.searchsorted(torch_seq, val)
    ms_out = ms_torch.searchsorted(ms_seq, val)
    assert (torch_out.numpy() == ms_out.numpy()).all()

def test_sgn():
    np_array1 = np.array([[-3, -2, -0.0, 0.0, 2, 3]]).astype(np.float16)
    np_array2 = np.array([[-3, -2, -0, 0, 2, 3]]).astype(np.int16)
    np_array3 = np.array([[1+1j, 2, -0j, 0j, -0, 3-4j, -2+2j, -5j]])

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor3 = torch.tensor(np_array3)
    torch_out1 = torch.sgn(torch_tensor1)
    torch_out2 = torch.sgn(torch_tensor2)
    if not is_test_under_ascend_context():
        torch_out3 = torch.sgn(torch_tensor3)
        ms_tensor3 = ms_torch.tensor(np_array3)
        ms_out3 = ms_torch.sgn(ms_tensor3)
        assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy())
        assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_torch.sgn(ms_tensor1)
    ms_out2 = ms_torch.sgn(ms_tensor2)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype


def test_qr():
    np_array = np.random.randn(2,3).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = ms_torch.tensor(np_array)
    torch_q1, torch_r1 = torch.qr(torch_tensor)
    ms_q1, ms_r1 = ms_torch.qr(ms_tensor)
    torch_q2, torch_r2 = torch.qr(torch_tensor, some=False)
    ms_q2, ms_r2 = ms_torch.qr(ms_tensor, some=False)
    param_compare(torch_q1, ms_q1, atol=1e-6)
    param_compare(torch_q2, ms_q2, atol=1e-6)
    param_compare(torch_r1, ms_r1, atol=1e-6)
    param_compare(torch_r2, ms_r2, atol=1e-6)

def test_signbit():
    np_array1 = np.array([[-3, -2, -0.0, 0.0, 2, 3]]).astype(np.float16)
    np_array2 = np.array([[-3, -2, -0, 0, 2, 3]]).astype(np.int16)
    np_array3 = np.array([[-3, -2, -0, 0, 2, 3]]).astype(np.bool8)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor3 = torch.tensor(np_array3)
    torch_out1 = torch.signbit(torch_tensor1)
    torch_out2 = torch.signbit(torch_tensor2)
    torch_out3 = torch.signbit(torch_tensor3)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_tensor3 = ms_torch.tensor(np_array3)
    ms_out1 = ms_torch.signbit(ms_tensor1)
    ms_out2 = ms_torch.signbit(ms_tensor2)
    ms_out3 = ms_torch.signbit(ms_tensor3)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy())
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype


def test_sinc():
    np_array1 = np.random.randn(10).astype(np.float32)
    np_array2 = np.random.randn(10).astype(np.float64)
    np_array1[0] = 0
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch.sinc(torch_tensor1)
    torch_out2 = torch.sinc(torch_tensor2)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_torch.sinc(ms_tensor1)
    ms_out2 = ms_torch.sinc(ms_tensor2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_sinh():
    np_array1 = np.random.randn(10).astype(np.int32)
    np_array2 = np.random.randn(10).astype(np.float64)
    np_array1[0] = 0
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch.sinh(torch_tensor1)
    torch_out2 = torch.sinh(torch_tensor2)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_torch.sinh(ms_tensor1)
    ms_out2 = ms_torch.sinh(ms_tensor2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)


def test_square():
    np_array1 = np.random.randn(10).astype(np.complex64)
    np_array2 = (np.random.randn(2, 3) * 10).astype(np.float64)
    np_array3 = np.arange(10).astype(np.int64)
    np_array1[0] = 1j
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor3 = torch.tensor(np_array3)
    torch_out1 = torch.square(torch_tensor1)
    torch_out2 = torch.square(torch_tensor2)
    torch_out3 = torch.square(torch_tensor3)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_tensor3 = ms_torch.tensor(np_array3)
    ms_out1 = ms_torch.square(ms_tensor1)
    ms_out2 = ms_torch.square(ms_tensor2)
    ms_out3 = ms_torch.square(ms_tensor3)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)


def test_sub():
    np_x = np.random.rand(1, 2, 3, 2).astype(np.float16)
    np_y = np.random.rand(1, 2, 3, 2).astype(np.float64)

    for x_dtype in (np.int16, np.int32, np.uint8, np.half, np.double, np.single):
        for y_dtype in (np.int16, np.int32, np.uint8, np.half, np.double, np.single):
            np_x_ = np_x.astype(x_dtype)
            np_y_ = np_y.astype(y_dtype)
            torch_x = torch.tensor(np_x_)
            torch_y = torch.tensor(np_y_)
            torch_out1 = torch.sub(torch_x, 2.1, alpha=2)
            torch_out2 = torch.sub(torch_x, torch_y, alpha=2)
            #torch_out2 = torch.sub(torch_x, 2, torch_y)

            ms_x = ms_torch.tensor(np_x_)
            ms_y = ms_torch.tensor(np_y_)
            ms_out1 = ms_torch.sub(ms_x, 2.1, alpha=2)
            ms_out2 = ms_torch.sub(ms_x, ms_y, alpha=2)

            assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
            assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
            assert ms_out1.asnumpy().shape == torch_out1.numpy().shape
            assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), equal_nan=True)
            assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
            assert ms_out2.asnumpy().shape == torch_out2.numpy().shape

def test_sub_complex():
    data_a = np.array(1 + 2j)
    data_b = np.array(2 + 2j)

    ms_x = ms_torch.tensor(data_a)
    ms_y = ms_torch.tensor(data_b)
    ms_out = ms_torch.sub(ms_x, ms_y, alpha=2)

    torch_x = torch.tensor(data_a)
    torch_y = torch.tensor(data_b)
    torch_out1 = torch.sub(torch_x, torch_y, alpha=2)

    param_compare(ms_out, torch_out1)

def test_subtract():
    np_array1 = np.random.rand(1, 2, 3).astype(np.float32)
    np_other1 = np.random.rand(1, 2, 3).astype(np.float32)
    np_array2 = np.arange(10).astype(np.int16)
    np_other2 = np.arange(10, 20).astype(np.uint8)

    torch_tensor1 = torch.tensor(np_array1)
    torch_other1 = torch.tensor(np_other1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_other2 = torch.tensor(np_other2)
    torch_out1 = torch.subtract(torch_tensor1, torch_other1)
    torch_out2 = torch.subtract(torch_tensor2, torch_other2, alpha=3)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_other1 = ms_torch.tensor(np_other1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_other2 = ms_torch.tensor(np_other2)
    ms_out1 = ms_torch.subtract(ms_tensor1, ms_other1)
    ms_out2 = ms_torch.subtract(ms_tensor2, ms_other2, alpha=3)
    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())


def test_tan():
    np_array1 = np.random.randn(10).astype(np.float64)
    np_array2 = np.random.randn(10).astype(np.int32)
    np_array1[0] = 1.57
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch.tan(torch_tensor1)
    torch_out2 = torch.tan(torch_tensor2)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_torch.tan(ms_tensor1)
    ms_out2 = ms_torch.tan(ms_tensor2)
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)


def test_true_divide():
    np_array1 = np.random.randn(10).astype(np.float64) * 5
    np_array2 = np.random.randn(10).astype(np.float32) * 5
    if is_test_under_ascend_context():
        # to prevent 0 divisor, because ascend not support inf and nan.
        np_array2 = np.where(np.abs(np_array2 < 1), 1, np_array2)
    for x_dtype in (np.int16, np.int32, np.uint8, np.half, np.double, np.single):
        np_array1_ = np_array1.astype(x_dtype)
        torch_tensor1 = torch.tensor(np_array1_)
        ms_tensor1 = ms_torch.tensor(np_array1_)
        for y_dtype in (np.int16, np.int32, np.uint8, np.half, np.double, np.single):
            np_array2_ = np_array2.astype(y_dtype)
            torch_tensor2 = torch.tensor(np_array2_)
            ms_tensor2 = ms_torch.tensor(np_array2_)
            torch_out1 = torch.true_divide(torch_tensor1, torch_tensor2)
            ms_out1 = ms_torch.true_divide(ms_tensor1, ms_tensor2)
            assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
            assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
        torch_out2 = torch.true_divide(torch_tensor1, 2)
        torch_out3 = torch.true_divide(torch_tensor1, 2.0)
        torch_out4 = torch.true_divide(2.0, torch_tensor1)
        ms_out2 = ms_torch.true_divide(ms_tensor1, 2)
        ms_out3 = ms_torch.true_divide(ms_tensor1, 2.0)
        ms_out4 = ms_torch.true_divide(2.0, ms_tensor1)
        assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), equal_nan=True)
        assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
        assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy(), equal_nan=True)
        assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype
        assert np.allclose(ms_out4.asnumpy(), torch_out4.numpy(), equal_nan=True)
        assert ms_out4.asnumpy().dtype == torch_out4.numpy().dtype
    torch_out5 = torch.true_divide(2, 2)
    ms_out5 = ms_torch.true_divide(2, 2)
    assert np.allclose(ms_out5.asnumpy(), torch_out5.numpy())
    assert ms_out5.asnumpy().dtype == torch_out5.numpy().dtype


def test_trunc():
    np_array2 = np.random.randn(10).astype(np.float32) * 5
    #np_array3 = np.array([0.0, -0.0, np.inf, -np.inf, np.nan])

    torch_tensor2 = torch.tensor(np_array2)
    #torch_tensor3 = torch.tensor(np_array3)
    torch_out2 = torch.trunc(torch_tensor2)
    #torch_out3 = torch.trunc(torch_tensor3)

    ms_tensor2 = ms_torch.tensor(np_array2)
    #ms_tensor3 = ms_torch.tensor(np_array3)
    ms_out2 = ms_torch.trunc(ms_tensor2)
    #ms_out3 = ms_torch.trunc(ms_tensor3)

    param_compare(torch_out2, ms_out2)

@SKIP_ENV_ASCEND(reason="trunc currently not support float64 on Ascend")
def test_trunc_fp64():
    np_array1 = np.random.randn(10).astype(np.float64) * 5
    #np_array3 = np.array([0.0, -0.0, np.inf, -np.inf, np.nan])

    torch_tensor1 = torch.tensor(np_array1)
    torch_out1 = torch.trunc(torch_tensor1)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_out1 = ms_torch.trunc(ms_tensor1)
    param_compare(torch_out1, ms_out1)

def test_xlogy():
    np_array1 = np.random.randn(10).astype(np.float64) * 5
    if is_test_under_ascend_context():
        # prevent negative and 0 input
        np_array2 = np.random.random(10).astype(np.float32) * 5
    else:
        np_array2 = np.random.randn(10).astype(np.float32) * 5

    if not is_test_under_ascend_context():
        # prevent nan and inf input on ascend, because ascend not support
        np_array1[0:2] = 0
        np_array2[1:3] = np.nan
        np_array2[5] = np.inf
        np_array2[0] = 2

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch.xlogy(torch_tensor1, torch_tensor2)
    torch_out2 = torch.xlogy(2, torch_tensor2)
    torch_out3 = torch.xlogy(torch_tensor1, 3.0)


    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_torch.xlogy(ms_tensor1, ms_tensor2)
    ms_out2 = ms_torch.xlogy(2, ms_tensor2)
    ms_out3 = ms_torch.xlogy(ms_tensor1, 3.0)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), equal_nan=True)
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy(), equal_nan=True)
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype


def test_adjoint():
    np_array = np.random.random((3, 4, 4)).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = ms_torch.tensor(np_array)
    torch_out = torch.adjoint(torch_tensor)
    ms_out = ms_torch.adjoint(ms_tensor)
    assert np.allclose(ms_out.numpy(), torch_out.numpy(), equal_nan=True)


def test_heaviside():
    np_array1 = np.array([-1.5, 0, 2.0]).astype(np.float32)
    np_values1 = np.array([1.2, -2.0, 3.5]).astype(np.float32)
    np_array2 = np.array([-1.5, 0, 2.0]).astype(np.float16)
    np_values2 = np.array([0.5]).astype(np.float16)
    np_array3 = np.array([-2, 0, 3]).astype(np.int16)
    np_values3 = np.array([1, -2, -0]).astype(np.int16)

    torch_tensor1 = torch.tensor(np_array1)
    torch_values1 = torch.tensor(np_values1)
    torch_out1 = torch.heaviside(torch_tensor1, torch_values1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_values2 = torch.tensor(np_values2)
    torch_out2 = torch.heaviside(torch_tensor2, torch_values2)
    torch_tensor3 = torch.tensor(np_array3)
    torch_values3 = torch.tensor(np_values3)
    torch_out3 = torch.heaviside(torch_tensor3, torch_values3)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_values1 = ms_torch.tensor(np_values1)
    ms_out1 = ms_torch.heaviside(ms_tensor1, ms_values1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_values2 = ms_torch.tensor(np_values2)
    ms_out2 = ms_torch.heaviside(ms_tensor2, ms_values2)
    ms_tensor3 = ms_torch.tensor(np_array3)
    ms_values3 = ms_torch.tensor(np_values3)
    ms_out3 = ms_torch.heaviside(ms_tensor3, ms_values3)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), equal_nan=True)
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy(), equal_nan=True)


def test_addbmm():
    np_array = np.random.rand(1, 2).astype(np.float32)
    np_batch1 = np.random.rand(4, 1, 3).astype(np.float32)
    np_batch2 = np.random.rand(4, 3, 2).astype(np.float32)
    beta = np.random.randint(-10,10)
    alpha = np.random.randint(-10,10)

    torch_tensor = torch.tensor(np_array)
    torch_batch1 = torch.tensor(np_batch1)
    torch_batch2 = torch.tensor(np_batch2)

    ms_tensor = ms_torch.tensor(np_array)
    ms_batch1 = ms_torch.tensor(np_batch1)
    ms_batch2 = ms_torch.tensor(np_batch2)

    torch_out1 = torch.addbmm(torch_tensor, torch_batch1, torch_batch2)
    torch_out2 = torch.addbmm(torch_tensor, torch_batch1, torch_batch2, beta=beta, alpha=alpha)
    ms_out1 = ms_torch.addbmm(ms_tensor, ms_batch1, ms_batch2)
    ms_out2 = ms_torch.addbmm(ms_tensor, ms_batch1, ms_batch2, beta=beta, alpha=alpha)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), equal_nan=True)


def test_addmm():
    np_array = np.random.rand(3, 5).astype(np.float32)
    np_mat1 = np.random.rand(3, 4).astype(np.float32)
    np_mat2 = np.random.rand(4, 5).astype(np.float32)
    beta = np.random.randint(-10,10)
    alpha = np.random.randint(-10,10)

    torch_tensor = torch.tensor(np_array)
    torch_mat1 = torch.tensor(np_mat1)
    torch_mat2 = torch.tensor(np_mat2)

    ms_tensor = ms_torch.tensor(np_array)
    ms_mat1 = ms_torch.tensor(np_mat1)
    ms_mat2 = ms_torch.tensor(np_mat2)

    torch_out1 = torch.addmm(torch_tensor, torch_mat1, torch_mat2)
    torch_out2 = torch.addmm(torch_tensor, torch_mat1, torch_mat2, beta=beta, alpha=alpha)
    ms_out1 = ms_torch.addmm(ms_tensor, ms_mat1, ms_mat2)
    ms_out2 = ms_torch.addmm(ms_tensor, ms_mat1, ms_mat2, beta=beta, alpha=alpha)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True, atol=1e-5)
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), equal_nan=True, atol=1e-5)


def test_logdet():
    np_array1 = np.random.rand(3, 3) * 10
    np_array1 = np_array1.astype(np.float32)
    np_array2 = np.random.rand(2, 4, 4).astype(np.float64)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)

    torch_out1 = torch.logdet(torch_tensor1)
    torch_out2 = torch.logdet(torch_tensor2)
    ms_out1 = ms_torch.logdet(ms_tensor1)
    ms_out2 = ms_torch.logdet(ms_tensor2)

    #TODO: logdet not accurate in Graph mode
    if is_test_under_ascend_context():
        # can not prevent nan from input, can only see if nan in output
        if not np.isnan(torch_out1.numpy()).any():
            assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), atol=1e-5, equal_nan=True)
            assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
        if not np.isnan(torch_out2.numpy()).any():
            assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), atol=1e-5, equal_nan=True)
            assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    else:
        assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), atol=1e-5, equal_nan=True)
        assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
        assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), atol=1e-5, equal_nan=True)
        assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype

def test_inner():
    np_array1 = np.random.rand(2, 4).astype(np.float32) * 5
    np_other1 = np.random.rand(1, 3, 4).astype(np.float32) * 5
    torch_tensor1 = torch.tensor(np_array1)
    torch_other1 = torch.tensor(np_other1)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_other1 = ms_torch.tensor(np_other1)

    torch_out1 = torch.inner(torch_tensor1, torch_other1)
    ms_out1 = ms_torch.inner(ms_tensor1, ms_other1)


    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype

@SKIP_ENV_ASCEND(reason="torch.inner doesn't support inputs of int type on Ascend")
def test_inner_int():
    np_array2 = np.array([1, 2, 3]).astype(np.int16)
    np_other2 = np.array([0, 2, 1]).astype(np.int16)
    torch_tensor2 = torch.tensor(np_array2)
    torch_other2 = torch.tensor(np_other2)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_other2 = ms_torch.tensor(np_other2)
    torch_out2 = torch.inner(torch_tensor2, torch_other2)
    ms_out2 = ms_torch.inner(ms_tensor2, ms_other2)
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), equal_nan=True)
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype

def test_inner_scalar():
    torch_out3 = torch.inner(torch.tensor(2), torch.tensor([3.2, 4.1]))
    ms_out3 = ms_torch.inner(ms_torch.tensor(2), ms_torch.tensor([3.2, 4.1]))
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy(), equal_nan=True)
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

def test_repeat_interleave():
    np_array1 = np.array([[1, 2], [3, 4]]).astype(np.int32)
    np_array2 = np.random.rand(1, 3, 4).astype(np.float32) * 5

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch.repeat_interleave(torch_tensor1, 2)
    torch_out2 = torch.repeat_interleave(torch_tensor2, 3, dim=1)
    torch_out3 = torch.repeat_interleave(torch_tensor1, torch.tensor([1, 2]), dim=0)
    torch_out4 = torch.repeat_interleave(torch_tensor2, torch.tensor([2, 1, 3]), dim=1)
    torch_out5 = torch.repeat_interleave(torch_tensor2, torch.tensor([3]))
    torch_out6 = torch.repeat_interleave(torch_tensor2, torch.tensor(3))
    torch_out7 = torch.repeat_interleave(torch_tensor2, torch.tensor(3), dim=1)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_torch.repeat_interleave(ms_tensor1, 2)
    ms_out2 = ms_torch.repeat_interleave(ms_tensor2, 3, dim=1)
    ms_out3 = ms_torch.repeat_interleave(ms_tensor1, ms_torch.tensor([1, 2]), dim=0)
    ms_out4 = ms_torch.repeat_interleave(ms_tensor2, ms_torch.tensor([2, 1, 3]), dim=1)
    ms_out5 = ms_torch.repeat_interleave(ms_tensor2, ms_torch.tensor([3]))
    ms_out6 = ms_torch.repeat_interleave(ms_tensor2, ms_torch.tensor(3))
    ms_out7 = ms_torch.repeat_interleave(ms_tensor2, ms_torch.tensor(3), dim=1)


    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), equal_nan=True)
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy(), equal_nan=True)
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype
    assert np.allclose(ms_out4.asnumpy(), torch_out4.numpy(), equal_nan=True)
    assert ms_out4.asnumpy().dtype == torch_out4.numpy().dtype
    assert np.allclose(ms_out5.asnumpy(), torch_out5.numpy(), equal_nan=True)
    assert ms_out5.asnumpy().dtype == torch_out5.numpy().dtype
    assert np.allclose(ms_out6.asnumpy(), torch_out6.numpy(), equal_nan=True)
    assert ms_out6.asnumpy().dtype == torch_out6.numpy().dtype
    assert np.allclose(ms_out7.asnumpy(), torch_out7.numpy(), equal_nan=True)
    assert ms_out7.asnumpy().dtype == torch_out7.numpy().dtype

def test_matrix_power():
    np_array = np.random.rand(4, 4, 4)
    for type1 in (np.float64, np.float32):
        np_array1 = np_array.astype(type1)
        torch_tensor1 = torch.tensor(np_array1)
        ms_tensor1 = ms_torch.tensor(np_array1)
        torch_out1 = torch.matrix_power(torch_tensor1, 0)
        torch_out2 = torch.matrix_power(torch_tensor1, 3)

        ms_out1 = ms_torch.matrix_power(ms_tensor1, 0)
        ms_out2 = ms_torch.matrix_power(ms_tensor1, 3)
        #TODO: GPU currently not support n < 0
        if not is_test_under_gpu_context():
            torch_out3 = torch.matrix_power(torch_tensor1, -3)
            ms_out3 = ms_torch.matrix_power(ms_tensor1, -3)
            param_compare(ms_out3, torch_out3, rtol=1e-3, atol=1e-4)
        param_compare(ms_out1, torch_out1)
        param_compare(ms_out2, torch_out2)

def test_poisson():
    for type1 in (np.float64, np.float32):
        np_array1 = np.array([[1, 2], [3, 4]]).astype(type1)
        np_array2 = np.random.rand(1, 3, 4).astype(type1) * 5
        torch_tensor1 = torch.tensor(np_array1)
        torch_tensor2 = torch.tensor(np_array2)
        ms_tensor1 = ms_torch.tensor(np_array1)
        ms_tensor2 = ms_torch.tensor(np_array2)

        torch_out1 = torch.poisson(torch_tensor1)
        torch_out2 = torch.poisson(torch_tensor2)
        ms_out1 = ms_torch.poisson(ms_tensor1)
        ms_out2 = ms_torch.poisson(ms_tensor2)
        type_shape_compare(torch_out1, ms_out1)
        type_shape_compare(torch_out2, ms_out2)

    for type2 in (np.int64, np.int32, np.float16):
        np_array3 = np.random.rand(1, 3, 4, 6, 8).astype(type2) * 5
        ms_tensor1 = ms_torch.tensor(np_array3)
        ms.set_seed(10)
        ms_out1 = ms_torch.poisson(ms_tensor1)
        ms_out2 = ms_torch.poisson(ms_tensor1)
        ms.set_seed(10)
        ms_out3 = ms_torch.poisson(ms_tensor1)
        ms_out4 = ms_torch.poisson(ms_tensor1)
        param_compare(ms_out1, ms_out3)
        param_compare(ms_out2, ms_out4)
    #TODO: mindspore has problem supporting numpy trans to ms.Tensor
    '''
    ms.set_seed(10)
    @ms.jit
    def func(a):
        x = ms_torch.poisson(a)
        return x
    ms_out5 = func(ms_tensor1)
    param_compare(ms_out1, ms_out5)
    '''


@SKIP_ENV_GPU(reason="Eig currently not support on GPU")
@SKIP_ENV_ASCEND(reason="testcase not support on Ascend")
def test_eig_fp64():
    np_array1 = np.random.randn(2, 2).astype(np.float64)
    torch_tensor1 = torch.tensor(np_array1)
    ms_tensor1 = ms_torch.tensor(np_array1)
    torch_u1, torch_v1 = torch.linalg.eig(torch_tensor1)
    ms_u1, ms_v1 = ms_torch.eig(ms_tensor1)

    assert np.allclose(np.sort(np.abs(torch_u1.numpy())), np.sort(np.abs(ms_u1.numpy())))
    type_shape_compare(torch_u1, ms_u1)
    assert np.allclose(np.sort(np.abs(torch_v1.numpy())), np.sort(np.abs(ms_v1.numpy())))
    type_shape_compare(torch_v1, ms_v1)

@SKIP_ENV_GPU(reason="Eig currently not support on GPU")
def test_eig_complex():
    np_array1 = np.random.randn(2, 2).astype(np.complex64)
    torch_tensor1 = torch.tensor(np_array1)
    ms_tensor1 = ms_torch.tensor(np_array1)
    torch_u1, torch_v1 = torch.linalg.eig(torch_tensor1)
    ms_u1, ms_v1 = ms_torch.eig(ms_tensor1)

    assert np.allclose(np.sort(np.abs(torch_u1.numpy())), np.sort(np.abs(ms_u1.numpy())))
    type_shape_compare(torch_u1, ms_u1)
    assert np.allclose(np.sort(np.abs(torch_v1.numpy())), np.sort(np.abs(ms_v1.numpy())))
    type_shape_compare(torch_v1, ms_v1)

@SKIP_ENV_GPU(reason="Eig currently not support on GPU")
def test_eig():
    np_array1 = np.array([[1, 2], [3, 4]]).astype(np.float32)
    torch_tensor1 = torch.tensor(np_array1)
    ms_tensor1 = ms_torch.tensor(np_array1)
    torch_u1, torch_v1 = torch.linalg.eig(torch_tensor1)
    ms_u1, ms_v1 = ms_torch.eig(ms_tensor1)
    param_compare(torch_u1, ms_u1)
    param_compare(torch_v1, ms_v1)

def test_vander():
    np_array = [1, 2, 3, 4, 5]
    torch_tensor = torch.tensor(np_array)
    ms_tensor = ms_torch.tensor(np_array)

    torch_out1 = torch.vander(torch_tensor)
    torch_out2 = torch.vander(torch_tensor, N=3)
    torch_out3 = torch.vander(torch_tensor, N=4)
    torch_out4 = torch.vander(torch_tensor, N=4, increasing=True)

    ms_out1 = ms_torch.vander(ms_tensor)
    ms_out2 = ms_torch.vander(ms_tensor, N=3)
    ms_out3 = ms_torch.vander(ms_tensor, N=4)
    ms_out4 = ms_torch.vander(ms_tensor, N=4, increasing=True)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert np.allclose(torch_out4.numpy(), ms_out4.numpy())
    assert torch_out1.numpy().shape, ms_out1.numpy().shape
    assert torch_out2.numpy().shape, ms_out2.numpy().shape
    assert torch_out3.numpy().shape, ms_out3.numpy().shape
    assert torch_out4.numpy().shape, ms_out4.numpy().shape
    assert torch_out1.numpy().dtype, ms_out1.numpy().dtype
    assert torch_out2.numpy().dtype, ms_out2.numpy().dtype
    assert torch_out3.numpy().dtype, ms_out3.numpy().dtype
    assert torch_out4.numpy().dtype, ms_out4.numpy().dtype

def test_histogramdd():
    #TODO: Currently not support float64 dtype
    np_array1 = np.array([[0., 1.], [1., 0.], [2., 0.], [2., 0.]]).astype(np.float32)
    np_array2 = np.array([[0., 0.], [1., 1.], [2., 2.]]).astype(np.float32)
    np_array3 = np.arange(15).reshape(5, 3).astype(np.float64)
    weight = np.array([1., 2., 4., 8.]).astype(np.float32)
    range1 = [0., 1., 0., 1.]

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor3 = torch.tensor(np_array3)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_tensor3 = ms_torch.tensor(np_array3)
    torch_weight = torch.tensor(weight)
    ms_weight = ms_torch.tensor(weight)

    torch_hist1, torch_edge1 = torch.histogramdd(torch_tensor1, bins=(3, 3), weight=torch_weight)
    ms_hist1, ms_edge1 = ms_torch.histogramdd(ms_tensor1, bins=(3, 3), weight=ms_weight)
    torch_hist2, torch_edge2 = torch.histogramdd(torch_tensor2, bins=(2, 2), range=range1, density=True)
    ms_hist2, ms_edge2 = ms_torch.histogramdd(ms_tensor2,  bins=(2, 2), range=range1, density=True)
    torch_hist3, torch_edge3 = torch.histogramdd(torch_tensor3, (2, 3, 4))
    ms_hist3, ms_edge3 = ms_torch.histogramdd(ms_tensor3, (2, 3, 4))
    if is_test_under_pynative_context():
        torch_hist4 = torch.histogramdd(torch_tensor3, (2, 3, 4)).hist
        torch_edge4 = torch.histogramdd(torch_tensor3, (2, 3, 4)).bin_edges
        ms_hist4 = ms_torch.histogramdd(ms_tensor3, (2, 3, 4)).hist
        ms_edge4 = ms_torch.histogramdd(ms_tensor3, (2, 3, 4)).bin_edges
        param_compare(torch_hist4, ms_hist4)
        param_compare(torch_edge4, ms_edge4)

    torch_res = [torch_hist1, torch_hist2, torch_hist3, torch_edge1, torch_edge2, torch_edge3]
    ms_res = [ms_hist1, ms_hist2, ms_hist3, ms_edge1, ms_edge2, ms_edge3]
    for i in range(len(ms_res)):
        param_compare(torch_res[i], ms_res[i])

@SKIP_ENV_ASCEND(reason="pinv currently not support on Ascend")
def test_pinverse():
    np_array1 = np.random.rand(3, 5)
    np_array2 = np.random.rand(2, 6, 3)
    for type1 in (np.float64, np.float32):
        np_array1 = np_array1.astype(type1)
        np_array2 = np_array2.astype(type1)
        torch_tensor1 = torch.tensor(np_array1)
        torch_tensor2 = torch.tensor(np_array2)
        ms_tensor1 = ms_torch.tensor(np_array1)
        ms_tensor2 = ms_torch.tensor(np_array2)
        torch_out1 = torch.pinverse(torch_tensor1)
        torch_out2 = torch.pinverse(torch_tensor2)
        torch_out3 = torch.pinverse(torch_tensor1, rcond=1e-6)
        ms_out1 = ms_torch.pinverse(ms_tensor1)
        ms_out2 = ms_torch.pinverse(ms_tensor2)
        ms_out3 = ms_torch.pinverse(ms_tensor1, rcond=1e-6)

        param_compare(ms_out1, torch_out1, atol=1e-5)
        param_compare(ms_out2, torch_out2, atol=1e-5)
        param_compare(ms_out3, torch_out3, atol=1e-5)

def test_symeig():
    np_array = np.random.randn(5, 5).astype(np.float32)
    torch_tensor1 = torch.tensor(np_array)
    torch_tensor = torch_tensor1 + torch_tensor1.t()
    ms_tensor1 = ms_torch.tensor(np_array)
    ms_tensor = ms_tensor1 + ms_tensor1.t()

    torch_val1, _ = torch.symeig(torch_tensor)
    torch_val2, torch_vec2 = torch.symeig(torch_tensor, eigenvectors=True)
    torch_val3, _ = torch.symeig(torch_tensor, upper=False)

    with graph_lax_level():
        ms_val1, _ = ms_torch.symeig(ms_tensor)
        ms_val2, ms_vec2 = ms_torch.symeig(ms_tensor, eigenvectors=True)
        ms_val3, _ = ms_torch.symeig(ms_tensor, upper=False)

    param_compare(torch_val1, ms_val1)
    param_compare(torch_val2, ms_val2)
    param_compare(torch_val3, ms_val3)
    param_compare(torch_vec2.abs(), ms_vec2.abs(), atol=1e-5)

@SKIP_ENV_ASCEND(reason="symeig currently not support float64 on Ascend")
def test_symeig_fp64():
    np_array = np.random.randn(2, 2)
    torch_tensor1 = torch.tensor(np_array)
    torch_tensor = torch_tensor1 + torch_tensor1.t()
    ms_tensor1 = ms_torch.tensor(np_array)
    ms_tensor = ms_tensor1 + ms_tensor1.t()

    torch_val1, _ = torch.symeig(torch_tensor)
    with graph_lax_level():
        ms_val1, _ = ms_torch.symeig(ms_tensor)

    param_compare(torch_val1, ms_val1)

@SKIP_ENV_GRAPH_MODE(reason="graph mode cannot support collections.namedtuple.")
@SKIP_ENV_ASCEND(reason="Currently not support Eigh on Ascend")
def test_symeig_namedtuple():
    for type1 in (np.float32, np.float64):
        np_array1 = np.random.randn(5, 5).astype(type1)
        torch_tensor_a1 = torch.tensor(np_array1)
        torch_tensor = torch_tensor_a1 + torch_tensor_a1.t().conj()
        ms_tensor_a1 = ms_torch.tensor(np_array1)
        ms_tensor = ms_tensor_a1 + ms_tensor_a1.t().conj()
        torch_val = torch.symeig(torch_tensor, eigenvectors=True).eigenvalues
        torch_val, _ = torch_val.sort()
        torch_vec = torch.symeig(torch_tensor, eigenvectors=True).eigenvectors
        ms_val = ms_torch.symeig(ms_tensor, eigenvectors=True).eigenvalues
        ms_val, _ = ms_val.sort()
        ms_vec = ms_torch.symeig(ms_tensor, eigenvectors=True).eigenvectors
        torch_ret = torch.dist(torch_vec @ torch.diag_embed(torch_val) @ torch_vec.mH, torch_tensor)
        ms_ret = ms_torch.dist(ms_vec @ ms_torch.diag_embed(ms_val) @ ms_vec.mH, ms_tensor)

        torch_t1 = torch.zeros(torch_val.shape, dtype=torch_tensor.dtype)
        torch_t2 = torch.zeros(torch_vec.shape, dtype=torch_tensor.dtype)
        ms_t1 = ms_torch.zeros(ms_val.shape, dtype=ms_tensor.dtype)
        ms_t2 = ms_torch.zeros(ms_vec.shape, dtype=ms_tensor.dtype)
        torch.symeig(torch_tensor, eigenvectors=True, out=(torch_t1, torch_t2))
        ms_torch.symeig(ms_tensor, eigenvectors=True, out=(ms_t1, ms_t2))

        param_compare(torch_val, ms_val, atol=1e-5)
        param_compare(torch_vec.abs(), ms_vec.abs(), atol=1e-5)
        param_compare(torch_t1, ms_t1, atol=1e-5)
        param_compare(torch_t2.abs(), ms_t2.abs(), atol=1e-5)
        param_compare(torch_ret, ms_ret, atol=1e-5)

@SKIP_ENV_GRAPH_MODE(reason="graph mode cannot support collections.namedtuple.")
@SKIP_ENV_ASCEND(reason="Currently not support Eigh on Ascend")
def test_symeig_complex():
    for type1 in (np.complex64, np.complex128):
        np_array = np.array([[ 1.+1.j, -0.-2.j], [ 0.+2.j,  5.+1.j]]).astype(type1)
        torch_tensor_a = torch.tensor(np_array)
        torch_tensor = torch_tensor_a + torch_tensor_a.t().conj()
        ms_tensor_a = ms_torch.tensor(np_array)
        ms_tensor = ms_tensor_a + ms_tensor_a.t().conj()
        torch_val = torch.symeig(torch_tensor, eigenvectors=True).eigenvalues
        torch_vec = torch.symeig(torch_tensor, eigenvectors=True).eigenvectors
        ms_val = ms_torch.symeig(ms_tensor, eigenvectors=True).eigenvalues
        ms_vec = ms_torch.symeig(ms_tensor, eigenvectors=True).eigenvectors

        torch_t1 = torch.zeros(torch_val.shape, dtype=torch_tensor.dtype)
        torch_t2 = torch.zeros(torch_vec.shape, dtype=torch_tensor.dtype)
        ms_t1 = ms_torch.zeros(ms_val.shape, dtype=ms_tensor.dtype)
        ms_t2 = ms_torch.zeros(ms_vec.shape, dtype=ms_tensor.dtype)
        torch.symeig(torch_tensor, eigenvectors=True, out=(torch_t1, torch_t2))
        ms_torch.symeig(ms_tensor, eigenvectors=True, out=(ms_t1, ms_t2))

        param_compare(torch_val, ms_val, atol=1e-5)
        param_compare(torch_vec.abs(), ms_vec.abs(), atol=1e-5)
        param_compare(torch_t1, ms_t1, atol=1e-5)
        param_compare(torch_t2.abs(), ms_t2.abs(), atol=1e-5)

def test_logcumsumexp():
    np_array1 = np.random.randn(10)
    np_array2 = np_array1.reshape(2,5)
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)

    torch_out1 = torch.logcumsumexp(torch_tensor1, dim=0)
    torch_out2 = torch.logcumsumexp(torch_tensor2, dim=0)
    torch_out3 = torch.logcumsumexp(torch_tensor2, dim=1)
    ms_out1 = ms_torch.logcumsumexp(ms_tensor1, dim=0)
    ms_out2 = ms_torch.logcumsumexp(ms_tensor2, dim=0)
    ms_out3 = ms_torch.logcumsumexp(ms_tensor2, dim=1)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

def test_kthvalue():
    np_array1 = np.random.randn(8)
    np_array2 = np_array1.reshape(2, 4)
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)

    torch_val1, torch_indice1 = torch.kthvalue(torch_tensor1, 4)
    torch_val2, torch_indice2 = torch.kthvalue(torch_tensor2, 4)
    torch_val3, torch_indice3 = torch.kthvalue(torch_tensor1, 2, 0, True)
    torch_val4, torch_indice4 = torch.kthvalue(torch_tensor2, 2, 0, True)
    torch_val5, torch_indice5 = torch.kthvalue(torch_tensor2, 2, 1, True)

    ms_val1, ms_indice1 = ms_torch.kthvalue(ms_tensor1, 4)
    ms_val2, ms_indice2 = ms_torch.kthvalue(ms_tensor2, 4)
    ms_val3, ms_indice3 = ms_torch.kthvalue(ms_tensor1, 2, 0, True)
    ms_val4, ms_indice4 = ms_torch.kthvalue(ms_tensor2, 2, 0, True)
    ms_val5, ms_indice5 = ms_torch.kthvalue(ms_tensor2, 2, 1, True)

    if not is_test_under_ascend_context():
        atol = 1e-5
    else:
        atol = 1e-3
    param_compare(torch_val1, ms_val1, atol=atol)
    param_compare(torch_val2, ms_val2, atol=atol)
    param_compare(torch_val3, ms_val3, atol=atol)
    param_compare(torch_val4, ms_val4, atol=atol)
    param_compare(torch_val5, ms_val5, atol=atol)
    param_compare(torch_indice1, ms_indice1)
    param_compare(torch_indice2, ms_indice2)
    param_compare(torch_indice3, ms_indice3)
    param_compare(torch_indice4, ms_indice4)
    param_compare(torch_indice5, ms_indice5)

def test_broadcast_shapes():
    torch_out = torch.broadcast_shapes((2,), (3, 1), (1, 1, 1))
    ms_out = ms_torch.broadcast_shapes((2,), (3, 1), (1, 1, 1))
    assert torch.zeros(torch_out).numpy().shape == ms_torch.zeros(ms_out).numpy().shape

def test_broadcast_tensors():
    np_x = np.arange(3)
    np_y = np.arange(2)
    torch_x = torch.tensor(np_x).view(1, 3)
    torch_y = torch.tensor(np_y).view(2, 1)
    ms_x = ms_torch.tensor(np_x).view(1, 3)
    ms_y = ms_torch.tensor(np_y).view(2, 1)

    torch_a, torch_b = torch.broadcast_tensors(torch_x, torch_y)
    ms_a, ms_b = ms_torch.broadcast_tensors(ms_x, ms_y)

    param_compare(torch_a, ms_a)
    param_compare(torch_b, ms_b)

def test_view_as_complex():
    np_array = np.random.randn(5, 2).astype(np.float32)
    np_array2 = np.random.randn(2, 5, 2).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = ms_torch.tensor(np_array)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor2 = ms_torch.tensor(np_array2)

    torch_out = torch.view_as_complex(torch_tensor)
    ms_out = ms_torch.view_as_complex(ms_tensor)
    torch_out2 = torch.view_as_complex(torch_tensor2)
    ms_out2 = ms_torch.view_as_complex(ms_tensor2)
    param_compare(torch_out, ms_out)
    param_compare(torch_out2, ms_out2)

def test_chain_matmul():
    for type1 in (np.float32, np.int32):
        np_array1 = np.random.randn(2, 3).astype(type1)
        np_array2 = np.random.randn(3, 4).astype(type1)
        np_array3 = np.random.randn(4, 5).astype(type1)
        np_array4 = np.random.randn(5, 6).astype(type1)

        torch_tensor1 = torch.tensor(np_array1)
        torch_tensor2 = torch.tensor(np_array2)
        torch_tensor3 = torch.tensor(np_array3)
        torch_tensor4 = torch.tensor(np_array4)
        ms_tensor1 = ms_torch.tensor(np_array1)
        ms_tensor2 = ms_torch.tensor(np_array2)
        ms_tensor3 = ms_torch.tensor(np_array3)
        ms_tensor4 = ms_torch.tensor(np_array4)

        torch_out = torch.chain_matmul(torch_tensor1, torch_tensor2, torch_tensor3, torch_tensor4)
        ms_out = ms_torch.chain_matmul(ms_tensor1, ms_tensor2, ms_tensor3, ms_tensor4)
        param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: ms.ops.Matmul not support int64 input on Ascend.")
def test_chain_matmul_int64():
    type1 = np.int64
    np_array1 = np.random.randn(2, 3).astype(type1)
    np_array2 = np.random.randn(3, 4).astype(type1)
    np_array3 = np.random.randn(4, 5).astype(type1)
    np_array4 = np.random.randn(5, 6).astype(type1)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor3 = torch.tensor(np_array3)
    torch_tensor4 = torch.tensor(np_array4)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_tensor3 = ms_torch.tensor(np_array3)
    ms_tensor4 = ms_torch.tensor(np_array4)

    torch_out = torch.chain_matmul(torch_tensor1, torch_tensor2, torch_tensor3, torch_tensor4)
    ms_out = ms_torch.chain_matmul(ms_tensor1, ms_tensor2, ms_tensor3, ms_tensor4)
    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="Currently not support float64 on Ascend")
def test_chain_matmul_fp64():
    np_array1 = np.random.randn(4, 5).astype(np.float64)
    np_array2 = np.random.randn(5, 6).astype(np.float64)
    np_array3 = np.random.randn(6, 7).astype(np.float64)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor3 = torch.tensor(np_array3)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_tensor3 = ms_torch.tensor(np_array3)
    torch_out = torch.chain_matmul(torch_tensor1, torch_tensor2, torch_tensor3)
    ms_out = ms_torch.chain_matmul(ms_tensor1, ms_tensor2, ms_tensor3)
    param_compare(torch_out, ms_out)

def test_empty_strided():
    size1 = (2, 3)
    size2 = (1, 2)
    size3 = (4, 3, 3)
    size4 = (1, 2, 2)

    torch_out1 = torch.empty_strided(size1, size2)
    ms_out1 = ms_torch.empty_strided(size1, size2)
    torch_out2 = torch.empty_strided(size3, size4)
    ms_out2 = ms_torch.empty_strided(size3, size4)
    torch_out3 = torch.empty_strided(size3, size4, dtype=torch.int32)
    ms_out3 = ms_torch.empty_strided(size3, size4, dtype=ms.int32)
    type_shape_compare(torch_out1, ms_out1)
    type_shape_compare(torch_out2, ms_out2)
    type_shape_compare(torch_out3, ms_out3)

@SKIP_ENV_CPU(reason="TODO: failed on CI device")
@SKIP_ENV_ASCEND(reason="Currently not support float64 on Ascend")
def test_cumulative_trapezoid_fp64():
    np_array1 = np.array([1, 5, 10]).astype(np.float64)
    np_array2 = np.array([1, 3, 6]).astype(np.float64)
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)

    torch_out1 = torch.cumulative_trapezoid(torch_tensor1)
    torch_out2 = torch.cumulative_trapezoid(torch_tensor1, dx=2)
    torch_out3 = torch.cumulative_trapezoid(torch_tensor1, torch_tensor2)
    ms_out1 = ms_torch.cumulative_trapezoid(ms_tensor1)
    ms_out2 = ms_torch.cumulative_trapezoid(ms_tensor1, dx=2)
    ms_out3 = ms_torch.cumulative_trapezoid(ms_tensor1, ms_tensor2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

@SKIP_ENV_CPU(reason="TODO: failed on CI device")
def test_cumulative_trapezoid():
    for type1 in (np.float32, np.int32, np.int64):
        np_array1 = np.random.randn(3, 3, 3).astype(type1)
        np_array2 = np.array([[1, 2, 3], [1, 3, 5], [1, 4, 7]]).astype(type1)
        torch_tensor1 = torch.tensor(np_array1)
        torch_tensor2 = torch.tensor(np_array2)
        ms_tensor1 = ms_torch.tensor(np_array1)
        ms_tensor2 = ms_torch.tensor(np_array2)

        torch_out1 = torch.cumulative_trapezoid(torch_tensor1)
        torch_out2 = torch.cumulative_trapezoid(torch_tensor1, dim=0)
        torch_out3 = torch.cumulative_trapezoid(torch_tensor1, dim=1)
        torch_out4 = torch.cumulative_trapezoid(torch_tensor1, torch_tensor2)
        torch_out5 = torch.cumulative_trapezoid(torch_tensor1, torch_tensor2, dim=1)
        ms_out1 = ms_torch.cumulative_trapezoid(ms_tensor1)
        ms_out2 = ms_torch.cumulative_trapezoid(ms_tensor1, dim=0)
        ms_out3 = ms_torch.cumulative_trapezoid(ms_tensor1, dim=1)
        ms_out4 = ms_torch.cumulative_trapezoid(ms_tensor1, ms_tensor2)
        ms_out5 = ms_torch.cumulative_trapezoid(ms_tensor1, ms_tensor2, dim=1)

        param_compare(torch_out1, ms_out1)
        param_compare(torch_out2, ms_out2)
        param_compare(torch_out3, ms_out3)
        param_compare(torch_out4, ms_out4)
        param_compare(torch_out5, ms_out5)


@SKIP_ENV_CPU(reason="TODO: failed on CI device")
def test_cumulative_trapezoid1():
    for type1 in (np.float32, np.int32, np.int64):
        np_array1 = np.array([1, 5, 10]).astype(type1)
        np_array2 = np.array([1, 3, 6]).astype(type1)
        torch_tensor1 = torch.tensor(np_array1)
        torch_tensor2 = torch.tensor(np_array2)
        ms_tensor1 = ms_torch.tensor(np_array1)
        ms_tensor2 = ms_torch.tensor(np_array2)

        torch_out1 = torch.cumulative_trapezoid(torch_tensor1)
        torch_out2 = torch.cumulative_trapezoid(torch_tensor1, dx=2)
        torch_out3 = torch.cumulative_trapezoid(torch_tensor1, torch_tensor2)
        ms_out1 = ms_torch.cumulative_trapezoid(ms_tensor1)
        ms_out2 = ms_torch.cumulative_trapezoid(ms_tensor1, dx=2)
        ms_out3 = ms_torch.cumulative_trapezoid(ms_tensor1, ms_tensor2)

        param_compare(torch_out1, ms_out1)
        param_compare(torch_out2, ms_out2)
        param_compare(torch_out3, ms_out3)

def test_log1p():
    if is_test_under_ascend_context():
        x = (np.random.rand(3, 5) - 1).astype(np.float32)
    else:
        x = np.random.randn(3, 5)

    torch_tensor = torch.tensor(x)
    torch_out = torch.log1p(torch_tensor)

    ms_tensor = ms_torch.tensor(x)
    ms_out = ms_torch.log1p(ms_tensor)

    param_compare(torch_out, ms_out, equal_nan=True)

@SKIP_ENV_ASCEND(reason="not support inf on Ascend, func test will be cover in test_log10 in test_tensor.py")
def test_log10():
    x = np.random.rand(3, 5).astype(np.int32)
    torch_tensor1 = torch.tensor(x)
    torch_out1 = torch.log10(torch_tensor1)

    ms_tensor1 = ms_torch.tensor(x)
    ms_out1 = ms_torch.log10(ms_tensor1)

    param_compare(torch_out1, ms_out1)

@SKIP_ENV_ASCEND(reason="not support inf on Ascend, func test will be cover in test_log2 in test_tensor.py")
def test_log2():
    x = np.random.rand(3, 5).astype(np.int32)

    torch_tensor1 = torch.tensor(x)
    torch_out1 = torch.log2(torch_tensor1)

    ms_tensor1 = ms_torch.tensor(x)
    ms_out1 = ms_torch.log2(ms_tensor1)

    param_compare(torch_out1, ms_out1)

def test_narrow_copy():
    x = np.random.randn(4, 5).astype(np.float32)
    x1_pt = torch.tensor(x)
    x1_ms = ms_torch.tensor(x)
    x1_ms_temp = x1_ms
    out1_pt = x1_pt.narrow_copy(0, 1, 2)
    out1_ms = x1_ms.narrow_copy(0, 1, 2)
    out2_pt = x1_pt.narrow_copy(-1, 2, 3)
    out2_ms = x1_ms.narrow_copy(-1, 2, 3)
    param_compare(out1_pt, out1_ms)
    param_compare(out2_pt, out2_ms)
    assert np.allclose(x1_ms_temp.numpy(), x1_ms.numpy())

def test_narrow_copy1():
    x = np.random.randn(4, 5).astype(np.float32)
    x1_ms = ms_torch.tensor(x)
    x1_ms_temp = x1_ms.clone()
    out1_ms = x1_ms.narrow_copy(0, 1, 2)
    out1_ms[0][0] = 1000
    param_compare(x1_ms_temp, x1_ms)

def test_matrix_rank():
    A = np.triu(np.random.randn(4, 4).astype(np.float32))
    A1 = A + A.T
    A_t = torch.tensor(A1)
    A_ms = ms_torch.tensor(A1)
    torch_out1 = torch.matrix_rank(A_t, symmetric=True, tol=1.0)
    ms_out1 = ms_torch.matrix_rank(A_ms, symmetric=True, tol=1.0)
    param_compare(torch_out1, ms_out1)

@SKIP_ENV_ASCEND(reason="matrix_rank currently not support float64 on Ascend")
def test_matrix_rank_fp64():
    A = np.triu(np.random.randn(2, 2))
    A1 = A + A.T
    A_t = torch.tensor(A1)
    A_ms = ms_torch.tensor(A1)
    torch_out1 = torch.matrix_rank(A_t)
    ms_out1 = ms_torch.matrix_rank(A_ms)
    param_compare(torch_out1, ms_out1)

@SKIP_ENV_ASCEND(reason="ormqr currently not support on Ascend")
@SKIP_ENV_CPU(reason="ormqr currently not support on CPU")
def test_ormqr():
    a = np.random.randn(3, 3)
    b = np.random.randn(3)
    c = np.random.randn(3, 3)
    A_t = torch.tensor(a)
    B_t = torch.tensor(b)
    C_t = torch.tensor(c)
    A_ms = ms_torch.tensor(a)
    B_ms = ms_torch.tensor(b)
    C_ms = ms_torch.tensor(c)
    torch_out1 = torch.ormqr(A_t, B_t, C_t)
    torch_out2 = torch.ormqr(A_t, B_t, C_t, left=False, transpose=True)
    ms_out1 = ms_torch.ormqr(A_ms, B_ms, C_ms)
    ms_out2 = ms_torch.ormqr(A_ms, B_ms, C_ms, left=False, transpose=True)
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

@SKIP_ENV_ASCEND(reason="triangular_solve currently not support on Ascend")
def test_triangular_solve():
    np_array1 = np.random.randn(2, 3, 3).astype(np.float32)
    np_array2 = np.random.randn(2, 3, 4).astype(np.float32)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)

    A_t = torch_tensor1.triu()
    A_t1 = torch_tensor1.tril()
    X_t = torch.triangular_solve(torch_tensor2, A_t, transpose=True, upper=True)
    X_t1 = torch.triangular_solve(torch_tensor2, A_t1, upper=False, unitriangular=True)

    A_ms1 = ms_tensor1.tril()
    A_ms = ms_tensor1.triu()
    X_ms = ms_torch.triangular_solve(ms_tensor2, A_ms, transpose=True, upper=True)
    X_ms1 = ms_torch.triangular_solve(ms_tensor2, A_ms1, upper=False, unitriangular=True)

    param_compare(X_t, X_ms)
    param_compare(X_t1, X_ms1)

@SKIP_ENV_GRAPH_MODE(reason='triangular_solve not support namedtuple on graph mode')
@SKIP_ENV_ASCEND(reason="triangular_solve currently not support on Ascend")
def test_triangular_solve_namedtuple():
    np_array1 = np.random.randn(2, 3, 3).astype(np.float32)
    np_array2 = np.random.randn(2, 3, 4).astype(np.float32)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)

    A_t = torch_tensor1.triu()
    X_t = torch.triangular_solve(torch_tensor2, A_t, transpose=True, upper=True)
    t_sol = X_t.solution
    t_coef = X_t.cloned_coefficient
    A_ms = ms_tensor1.triu()
    X_ms = ms_torch.triangular_solve(ms_tensor2, A_ms, transpose=True, upper=True)
    ms_sol = X_ms.solution
    ms_coef = X_ms.cloned_coefficient

    param_compare(t_sol, ms_sol)
    param_compare(t_coef, ms_coef)

def test_relu():
    data = np.random.rand(2, 2, 3)
    torch_input = torch.tensor(data)
    torch_output = torch.relu(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_output = ms_torch.relu(ms_input)
    param_compare(torch_output, ms_output)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_round1()
    test_round2()
    test_round3()
    test_floor1()
    test_ceil1()
    test_sign1()
    test_sign2()
    test_pow1()
    test_pow2()
    # test_pow3()
    test_pow4()
    test_exp1()
    test_exp2()
    test_exp3()
    test_mul1()
    test_multiply()
    test_mul2()
    test_absolute()
    test_acos()
    test_arccos()
    test_acosh()
    test_arccosh()
    test_add()
    test_addcdiv()
    test_addcmul()
    test_angle()
    test_asin()
    test_arcsin()
    test_asinh()
    test_arcsinh()
    test_atan()
    test_arctan()
    test_atanh()
    test_arctanh()
    test_arctan2()
    test_bitwise_not()
    test_bitwise()
    test_bitwise_shift()
    test_clip()
    test_conj_physical()
    test_copysign()
    test_cosh()
    test_deg2rad()
    test_digamma()
    test_lgamma()
    test_erf()
    test_erfc()
    test_erfinv()
    test_exp2_()
    test_expm1()
    test_fake_quantize()
    test_fix()
    test_float_power()
    test_floor_divide()
    test_frexp()
    test_gradient()
    test_imag()
    test_ldexp()
    test_lerp()
    test_logaddexp()
    test_logical_and()
    test_logit()
    test_lu_solve()
    test_lu_unpack()
    test_lstsq()
    test_tanh()
    test_sigmoid()
    test_hypot()
    test_i0()
    test_igamma()
    test_mvlgamma()
    test_nan_to_num()
    test_nan_to_num1()
    test_neg()
    test_nextafter()
    test_positive()
    test_polygamma()
    test_qr()
    test_rad2deg()
    test_real()
    test_reciprocal()
    test_remainder()
    test_rsqrt()
    test_roll()
    test_rot90()
    test_searchsorted()
    test_searchsorted_int()
    test_searchsorted_fp16()
    test_sgn()
    test_signbit()
    test_sinc()
    test_square()
    test_sub()
    test_subtract()
    test_tan()
    test_true_divide()
    test_trunc()
    test_xlogy()
    test_adjoint()
    test_heaviside()
    test_addbmm()
    test_addmm()
    test_logdet()
    test_inner()
    test_inner_int()
    test_inner_scalar()
    test_repeat_interleave()
    test_matrix_power()
    test_poisson()
    test_eig_complex()
    test_eig_fp64()
    test_eig()
    test_vander()
    test_histogramdd()
    test_symeig()
    test_symeig_namedtuple()
    test_symeig_complex()
    test_logcumsumexp()
    test_kthvalue()
    test_broadcast_shapes()
    test_broadcast_tensors()
    test_view_as_complex()
    test_chain_matmul()
    test_chain_matmul_fp64()
    test_empty_strided()
    test_cumulative_trapezoid()
    test_cumulative_trapezoid1()
    test_cumulative_trapezoid_fp64()
    test_frexp_fp64()
    test_nan_to_num_fp64()
    test_atan_fp64()
    test_arctan_fp64()
    test_arctan_int()
    test_arctan2_fp64()
    test_erf_fp64()
    test_erfc_fp64()
    test_lgamma_fp64()
    test_addcmul_fp64()
    test_digamma_fp64()
    test_igammac()
    test_log1p()
    test_log10()
    test_log2()
    test_narrow_copy()
    test_narrow_copy1()
    test_gradient_fp64()
    test_lerp_fp64()
    test_logaddexp_fp64()
    test_symeig_fp64()
    test_trunc_fp64()
    test_matrix_rank()
    test_ormqr()
    test_triangular_solve()
    test_triangular_solve_namedtuple()
