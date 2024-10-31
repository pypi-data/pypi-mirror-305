#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_transpose1():
    np_1 = np.random.randn(1, 2, 3)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.transpose(ms_tensor, 0, 1)

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.transpose(torch_tensor, 0, 1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_transpose2():
    np_1 = np.random.randn(1, 2, 3)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.transpose(ms_tensor, 0, -1)

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.transpose(torch_tensor, 0, -1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_transpose3():
    np_1 = np.random.randn(1, 2, 3)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.transpose(ms_tensor, 0, -3)

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.transpose(torch_tensor, 0, -3)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_transpose4():
    np_1 = np.random.randn(1, 2, 3)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.transpose(ms_tensor, -1, -2)

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.transpose(torch_tensor, -1, -2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_transpose5():
    ms_tensor = ms_torch.rand(1, 2, 0, 3)
    ms_result = ms_torch.transpose(ms_tensor, -1, -2)

    torch_tensor = torch.rand(1, 2, 0, 3)
    torch_result = torch.transpose(torch_tensor, -1, -2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
    assert ms_result.asnumpy().shape == torch_result.numpy().shape

if __name__ == '__main__':
    set_mode_by_env_config()
    test_transpose1()
    test_transpose2()
    test_transpose3()
    test_transpose4()
    test_transpose5()