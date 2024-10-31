#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, SKIP_ENV_ASCEND, param_compare
set_mode_by_env_config()


def test_conv1d1():
    np_input = np.random.randn(33, 16, 30).astype(np.float32)
    np_weight = np.random.randn(20, 16, 5).astype(np.float32)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_out = torch.nn.functional.conv1d(torch_tensor, torch_weight)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_out = ms_torch.nn.functional.conv1d(ms_tensor, ms_weight)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-2, atol=1e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape


def test_conv1d2():
    out_channel = 1
    np_input = np.random.randn(3, 8, 30).astype(np.float32)
    np_weight = np.random.randn(out_channel, 8, 5).astype(np.float32)
    np_bias = np.ones(out_channel).astype(np.float32)*0.5

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_bias = torch.tensor(np_bias)
    torch_out = torch.nn.functional.conv1d(torch_tensor, torch_weight, torch_bias, 7, (3,), (4,), 1)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_bias = ms_torch.tensor(np_bias)
    ms_out = ms_torch.nn.functional.conv1d(ms_tensor, ms_weight, ms_bias, 7, (3,), (4,), 1)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-2, atol=1e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

def test_conv1d3():
    out_channel = 8
    np_input = np.random.randn(15, 32, 30).astype(np.float64)
    np_weight = np.random.randn(out_channel, 8, 5).astype(np.float64)
    np_bias = np.ones(out_channel).astype(np.float32)*0.5

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_bias = torch.tensor(np_bias)
    torch_out = torch.nn.functional.conv1d(torch_tensor, torch_weight, torch_bias, (1,), 'same', (2,), 4)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_bias = ms_torch.tensor(np_bias)
    ms_out = ms_torch.nn.functional.conv1d(ms_tensor, ms_weight, ms_bias, (1,), 'same', (2,), 4)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-2, atol=1e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

def test_conv1d_groups_equal_to_input_channel():
    out_channel = 4
    np_input = np.random.randn(1, 4, 11).astype(np.float64)
    np_weight = np.random.randn(out_channel, 1, 5).astype(np.float64)
    np_bias = np.ones(out_channel).astype(np.float32)*0.5

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_bias = torch.tensor(np_bias)
    torch_out = torch.nn.functional.conv1d(torch_tensor, torch_weight, torch_bias, (1,), 'same', (2,), 4)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_bias = ms_torch.tensor(np_bias)
    ms_out = ms_torch.nn.functional.conv1d(ms_tensor, ms_weight, ms_bias, (1,), 'same', (2,), 4)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-2, atol=1e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape   


def test_conv2d1():
    np_input = np.random.randn(1, 4, 5, 5).astype(np.float32)
    np_weight = np.random.randn(8, 4, 3, 3).astype(np.float32)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_out = torch.nn.functional.conv2d(torch_tensor, torch_weight)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_out = ms_torch.nn.functional.conv2d(ms_tensor, ms_weight)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-2, atol=1e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-4)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape


def test_conv2d2():
    out_channel = 1
    np_input = np.random.randn(3, 8, 9, 9).astype(np.float32)
    np_weight = np.random.randn(out_channel, 8, 3, 5).astype(np.float32)
    np_bias = np.ones(out_channel).astype(np.float32)*0.5

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_bias = torch.tensor(np_bias)
    torch_out = torch.nn.functional.conv2d(torch_tensor, torch_weight, torch_bias, 7, 3, (2,), 1)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_bias = ms_torch.tensor(np_bias)
    ms_out = ms_torch.nn.functional.conv2d(ms_tensor, ms_weight, ms_bias, 7, 3, (2,), 1)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-2, atol=1e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

def test_conv2d3():
    out_channel = 8
    np_input = np.random.randn(4, 16, 8, 8).astype(np.float64)
    np_weight = np.random.randn(out_channel, 4, 3, 3).astype(np.float64)
    np_bias = np.ones(out_channel).astype(np.float64)*0.5

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_bias = torch.tensor(np_bias)
    torch_out = torch.nn.functional.conv2d(torch_tensor, torch_weight, torch_bias, (2, 2), (3, 2), (1, 3), 4)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_bias = ms_torch.tensor(np_bias)
    ms_out = ms_torch.nn.functional.conv2d(ms_tensor, ms_weight, ms_bias, (2, 2), (3, 2), (1, 3), 4)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-2, atol=1e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

def test_conv2d_groups_equal_to_Cin():
    out_channel = 4
    np_input = np.random.randn(1, 4, 8, 8).astype(np.float64)
    np_weight = np.random.randn(out_channel, 1, 3, 3).astype(np.float64)
    np_bias = np.ones(out_channel).astype(np.float64)*0.5

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_bias = torch.tensor(np_bias)
    torch_out = torch.nn.functional.conv2d(torch_tensor, torch_weight, torch_bias, (2, 2), (3, 2), (1, 3), 4)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_bias = ms_torch.tensor(np_bias)
    ms_out = ms_torch.nn.functional.conv2d(ms_tensor, ms_weight, ms_bias, (2, 2), (3, 2), (1, 3), 4)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-2, atol=1e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape


def test_conv3d1():
    np_input = np.random.randn(1, 4, 5, 5, 5).astype(np.float32)
    np_weight = np.random.randn(8, 4, 3, 3, 3).astype(np.float32)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_out = torch.nn.functional.conv3d(torch_tensor, torch_weight)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_out = ms_torch.nn.functional.conv3d(ms_tensor, ms_weight)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-2, atol=1e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape


def test_conv3d2():
    out_channel = 1
    np_input = np.random.randn(3, 8, 9, 9, 9).astype(np.float32)
    np_weight = np.random.randn(out_channel, 8, 3, 5, 4).astype(np.float32)
    np_bias = np.ones(out_channel).astype(np.float32)*0.5

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_bias = torch.tensor(np_bias)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_bias = ms_torch.tensor(np_bias)
    #TODO: Ascend currently not support dilation=1
    if ms.get_context('device_target') == 'Ascend':
        torch_out = torch.nn.functional.conv3d(torch_tensor, torch_weight, torch_bias, 7, 2, 1, 1)
        ms_out = ms_torch.nn.functional.conv3d(ms_tensor, ms_weight, ms_bias, 7, 2, 1, 1)
    else:
        torch_out = torch.nn.functional.conv3d(torch_tensor, torch_weight, torch_bias, 7, 3, (2,), 1)
        ms_out = ms_torch.nn.functional.conv3d(ms_tensor, ms_weight, ms_bias, 7, 3, (2,), 1)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-2, atol=1e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

def test_conv3d3():
    out_channel = 8
    np_input = np.random.randn(4, 16, 18, 18, 18).astype(np.float64)
    np_weight = np.random.randn(out_channel, 4, 5, 5, 5).astype(np.float64)
    np_bias = np.ones(out_channel).astype(np.float32)*0.5

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_bias = torch.tensor(np_bias)
    torch_out = torch.nn.functional.conv3d(torch_tensor, torch_weight, torch_bias, (2, 2, 1), (4, 6, 2), (1, 3, 3), 4)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_bias = ms_torch.tensor(np_bias)
    ms_out = ms_torch.nn.functional.conv3d(ms_tensor, ms_weight, ms_bias, (2, 2, 1), (4, 6, 2), (1, 3, 3), 4)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=2e-2, atol=2e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-4)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape


def test_unfold():
    np_input = np.random.randn(7, 8, 9, 10)

    torch_tensor = torch.tensor(np_input)
    torch_out = torch.nn.functional.unfold(torch_tensor, (2, 3), 1, (1, 2), (2, 1))

    ms_tensor = ms_torch.tensor(np_input)
    ms_out = ms_torch.nn.functional.unfold(ms_tensor, (2, 3), 1, (1, 2), (2, 1))

    param_compare(ms_out, torch_out, rtol=1e-3, atol=1e-5)


def test_fold():
    np_input1 = np.random.randn(7, 8, 24)
    np_input2 = np.random.randn(18, 6)

    torch_tensor1 = torch.tensor(np_input1)
    torch_tensor2 = torch.tensor(np_input2)
    torch_out1 = torch.nn.functional.fold(torch_tensor1, (4, 5), (2, 2), 1, (1, 2), (2, 1))
    torch_out2 = torch.nn.functional.fold(torch_tensor2, (7, 4), 3, 2, 2, 3)

    ms_tensor1 = ms_torch.tensor(np_input1)
    ms_tensor2 = ms_torch.tensor(np_input2)
    ms_out1 = ms_torch.nn.functional.fold(ms_tensor1, (4, 5), (2, 2), 1, (1, 2), (2, 1))
    ms_out2 = ms_torch.nn.functional.fold(ms_tensor2, (7, 4), 3, 2, 2, 3)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert ms_out1.asnumpy().shape == torch_out1.numpy().shape
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert ms_out2.asnumpy().shape == torch_out2.numpy().shape

def test_conv1d_2d():
    np_input = np.random.randn(5, 30).astype(np.float32)
    np_weight = np.random.randn(2, 5, 5).astype(np.float32)

    torch_tensor = torch.tensor(np_input)
    torch_weight = torch.tensor(np_weight)
    torch_out = torch.nn.functional.conv1d(torch_tensor, torch_weight)

    ms_tensor = ms_torch.tensor(np_input)
    ms_weight = ms_torch.tensor(np_weight)
    ms_out = ms_torch.nn.functional.conv1d(ms_tensor, ms_weight)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-2, atol=1e-2)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

if __name__ == '__main__':
    set_mode_by_env_config()
    test_conv1d1()
    test_conv1d2()
    test_conv1d3()
    test_conv1d_groups_equal_to_input_channel()
    test_conv2d1()
    test_conv2d2()
    test_conv2d_groups_equal_to_Cin()
    test_conv2d3()
    test_conv3d1()
    test_conv3d2()
    test_conv3d3()
    test_unfold()
    test_fold()
    test_conv1d_2d()
