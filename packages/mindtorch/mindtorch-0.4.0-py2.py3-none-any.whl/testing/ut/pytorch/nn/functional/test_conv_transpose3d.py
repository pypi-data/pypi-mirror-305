#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import pytest

import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, is_test_under_ascend_context, is_test_under_gpu_context
set_mode_by_env_config()

_atol = 1e-5
if is_test_under_ascend_context():
    _atol = 8e-2

def test_conv_transpose3d1():
    np_input = np.random.randn(2, 16, 50, 10, 20).astype(np.float32)
    np_weight = np.random.randn(16, 34, 3, 3, 3).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_result = ms_torch.nn.functional.conv_transpose3d(ms_tensor, ms_weight)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_result = torch.nn.functional.conv_transpose3d(torch_tensor, torch_weight)

    if is_test_under_gpu_context():
        assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-3, atol=1e-4)
    else:
        assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-2, atol=_atol)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_conv_transpose3d2():
    np_input = np.random.randn(2, 16, 50, 10, 20).astype(np.float32)
    np_weight = np.random.randn(16, 34, 3, 3, 3).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_result = ms_torch.nn.functional.conv_transpose3d(
        ms_tensor, ms_weight, stride=2, padding=1, groups=1, dilation=1)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_result = torch.nn.functional.conv_transpose3d(
        torch_tensor, torch_weight, stride=2, padding=1, groups=1, dilation=1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-2, atol=_atol)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_conv_transpose3d3():
    np_input = np.random.randn(2, 16, 50, 10, 20).astype(np.float32)
    np_weight = np.random.randn(16, 34, 3, 3, 3).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_result = ms_torch.nn.functional.conv_transpose3d(
        ms_tensor, ms_weight, stride=2, padding=0, output_padding=0, groups=1, dilation=1)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_result = torch.nn.functional.conv_transpose3d(
        torch_tensor, torch_weight, stride=2, padding=0, output_padding=0, groups=1, dilation=1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-2, atol=_atol)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_conv_transpose3d4():
    np_input = np.random.randn(2, 16, 50, 10, 20).astype(np.float32)
    np_weight = np.random.randn(16, 34, 3, 3, 3).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_result = ms_torch.nn.functional.conv_transpose3d(
        ms_tensor, ms_weight, stride=2, padding=(1, 1, 2), groups=1, dilation=1)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_result = torch.nn.functional.conv_transpose3d(
        torch_tensor, torch_weight, stride=2, padding=(1, 1, 2), groups=1, dilation=1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), rtol=1e-2, atol=_atol)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape


def test_conv_transpose3d5():
    np_input = np.random.randn(2, 15, 50).astype(np.float32)
    np_weight = np.random.randn(15, 11, 5).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    with pytest.raises(ValueError):
        ms_result = ms_torch.nn.functional.conv_transpose3d(
            ms_tensor, ms_weight, stride=2, padding=1, groups=3, dilation=2)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    with pytest.raises(RuntimeError):
        torch_result = torch.nn.functional.conv_transpose3d(
            torch_tensor, torch_weight, stride=2, padding=1, groups=3, dilation=2)


if __name__ == "__main__":
    test_conv_transpose3d1()
    test_conv_transpose3d2()
    test_conv_transpose3d3()
    test_conv_transpose3d4()
    test_conv_transpose3d5()
