#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import pytest

import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, is_test_under_ascend_context, SKIP_ENV_ASCEND
set_mode_by_env_config()

_atol = 1e-5
if is_test_under_ascend_context():
    _atol = 1e-2

def test_conv_transpose1d1():
    np_input = np.random.randn(1, 16, 50).astype(np.float32)
    np_weight = np.random.randn(16, 33, 5).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_result = ms_torch.nn.functional.conv_transpose1d(ms_tensor, ms_weight)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_result = torch.nn.functional.conv_transpose1d(torch_tensor, torch_weight)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=_atol)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape

@SKIP_ENV_ASCEND(reason="On Ascend, groups can only be 1 or in_channels.")
def test_conv_transpose1d2():
    np_input = np.random.randn(2, 15, 50).astype(np.float32)
    np_weight = np.random.randn(15, 33, 5).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_result = ms_torch.nn.functional.conv_transpose1d(
        ms_tensor, ms_weight, stride=2, padding=1, groups=3, dilation=2)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_result = torch.nn.functional.conv_transpose1d(
        torch_tensor, torch_weight, stride=2, padding=1, groups=3, dilation=2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=_atol)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape

@SKIP_ENV_ASCEND(reason="On Ascend, only support groups == 1 or groups == in_channels == out_channels.")
def test_conv_transpose1d3():
    np_input = np.random.randn(2, 15, 50).astype(np.float32)
    np_weight = np.random.randn(15, 33, 5).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_result = ms_torch.nn.functional.conv_transpose1d(
        ms_tensor, ms_weight, stride=2, padding=0, output_padding=0, groups=3, dilation=2)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_result = torch.nn.functional.conv_transpose1d(
        torch_tensor, torch_weight, stride=2, padding=0, output_padding=0, groups=3, dilation=2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=_atol)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape

def test_conv_transpose1d_group_1():
    np_input = np.random.randn(2, 15, 50).astype(np.float32)
    np_weight = np.random.randn(15, 33, 5).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_result = ms_torch.nn.functional.conv_transpose1d(
        ms_tensor, ms_weight, stride=2, padding=0, output_padding=0, groups=1, dilation=2)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_result = torch.nn.functional.conv_transpose1d(
        torch_tensor, torch_weight, stride=2, padding=0, output_padding=0, groups=1, dilation=2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=_atol)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape

def test_conv_transpose1d_group_inchannels():
    np_input = np.random.randn(2, 15, 50).astype(np.float32)
    np_weight = np.random.randn(15, 1, 5).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_result = ms_torch.nn.functional.conv_transpose1d(
        ms_tensor, ms_weight, stride=2, padding=1, output_padding=0, groups=15, dilation=2)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_result = torch.nn.functional.conv_transpose1d(
        torch_tensor, torch_weight, stride=2, padding=1, output_padding=0, groups=15, dilation=2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=_atol)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape

# TODO: not support `output_padding` now
# def test_conv_transpose1d4():
#     np_input = np.random.randn(1, 3, 50).astype(np.float32)
#     np_weight = np.random.randn(3, 64, 5).astype(np.float32)
#
#     ms_tensor = ms_torch.tensor(np_input)
#     ms_weight = ms_torch.tensor(np_weight)
#     ms_result = ms_torch.nn.functional.conv_transpose1d(
#         ms_tensor, ms_weight, stride=3, padding=2, output_padding=2, bias=None)
#
#     torch_tensor = torch.tensor(np_input)
#     torch_weight = torch.tensor(np_weight)
#     torch_result = torch.nn.functional.conv_transpose1d(
#         torch_tensor, torch_weight, stride=3, padding=2, output_padding=2, bias=None)
#     assert np.allclose(ms_result.asnumpy().round(decimals=1e-4), torch_result.numpy(), rtol=1e-3, atol=1e-5)
#     assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
#     assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_conv_transpose1d5():
    np_input = np.random.randn(2, 16, 50).astype(np.float32)
    np_weight = np.random.randn(16, 33, 5).astype(np.float32)
    np_bias = np.random.randn(np_weight.shape[1]).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_bias = ms_torch.tensor(np_bias)
    ms_result = ms_torch.nn.functional.conv_transpose1d(ms_tensor, ms_weight, bias=ms_bias)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_bias = torch.tensor(np_bias)
    torch_result = torch.nn.functional.conv_transpose1d(torch_tensor, torch_weight, bias=torch_bias)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=_atol)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_conv_transpose1d6():
    np_input = np.random.randn(2, 15, 50, 10).astype(np.float32)
    np_weight = np.random.randn(15, 11, 5, 10).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    with pytest.raises(ValueError):
        ms_result = ms_torch.nn.functional.conv_transpose1d(
            ms_tensor, ms_weight, stride=2, padding=1, groups=3, dilation=2)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    with pytest.raises(RuntimeError):
        torch_result = torch.nn.functional.conv_transpose1d(
            torch_tensor, torch_weight, stride=2, padding=1, groups=3, dilation=2)

def test_conv_transpose1d_same():
    np_input = np.random.randn(2, 3, 9).astype(np.float32)
    np_weight = np.random.randn(3, 4, 5).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_result = ms_torch.nn.functional.conv_transpose1d(ms_tensor, ms_weight, stride=1, padding=2)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_result = torch.nn.functional.conv_transpose1d(torch_tensor, torch_weight, stride=1, padding=2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=_atol)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape

if __name__ == "__main__":
    test_conv_transpose1d1()
    test_conv_transpose1d2()
    # reversed for pad_same
    # test_conv_transpose1d4()
    test_conv_transpose1d5()
    test_conv_transpose1d6()
    test_conv_transpose1d_group_1()
    test_conv_transpose1d_group_inchannels()
    test_conv_transpose1d_same()
