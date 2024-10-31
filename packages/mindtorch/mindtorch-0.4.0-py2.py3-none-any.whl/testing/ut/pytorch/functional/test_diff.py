#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import SKIP_ENV_ASCEND, SKIP_ENV_CPU, SKIP_ENV_GPU, param_compare, set_mode_by_env_config
set_mode_by_env_config()

def test_diff1():
    np_1 = np.random.randn(4, 5, 6, 7)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.diff(ms_tensor_1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.diff(torch_tensor_1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), atol=1e-6)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_diff2():
    np_1 = np.random.randn(3, 4, 5)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.diff(ms_tensor_1, dim=0)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.diff(torch_tensor_1, dim=0)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), atol=1e-6)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_diff3():
    np_1 = np.random.randn(4, 5)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.diff(ms_tensor_1, dim=1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.diff(torch_tensor_1, dim=1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), atol=1e-6)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


@SKIP_ENV_ASCEND(reason="diff currently not support float64 on Ascend")
def test_diff4():
    np_1 = np.random.randn(7, 8)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result1 = ms_torch.diff(ms_tensor_1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result1 = torch.diff(torch_tensor_1)

    param_compare(ms_result1, torch_result1)

def test_diff5():
    np_1 = np.random.randn(3, 4, 5).astype(np.float32)
    np_2 = np.random.randn(3, 4, 5).astype(np.float32)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result1 = ms_torch.diff(ms_tensor_1, dim=-1, append=ms_tensor_2)
    ms_result2 = ms_torch.diff(ms_tensor_1, n=3, dim=-1, append=ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result1 = torch.diff(torch_tensor_1, dim=-1, append=torch_tensor_2)
    torch_result2 = torch.diff(torch_tensor_1, n=3, dim=-1, append=torch_tensor_2)
    param_compare(ms_result1, torch_result1)
    param_compare(ms_result2, torch_result2)

def test_diff6():
    np_1 = np.random.randn(3, 4).astype(np.complex64)
    np_2 = (np.random.randn(3, 4) * 1j).astype(np.complex64)
    ms_tensor = ms_torch.tensor(np_1 + np_2)
    ms_result1 = ms_torch.diff(ms_tensor, dim=-1)
    # TODO: n=3 will call the function ms.numpy.diff,
    # which will truncates the imaginary parts of the complex results and returns wrong outputs
    #ms_result2 = ms_torch.diff(ms_tensor, n=3, dim=-1)

    torch_tensor = torch.tensor(np_1 + np_2)
    torch_result1 = torch.diff(torch_tensor, dim=-1)
    #torch_result2 = torch.diff(torch_tensor, n=3, dim=-1)
    param_compare(ms_result1, torch_result1)
    #param_compare(ms_result2, torch_result2)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_diff1()
    test_diff2()
    test_diff3()
    test_diff4()
    test_diff5()
    test_diff6()