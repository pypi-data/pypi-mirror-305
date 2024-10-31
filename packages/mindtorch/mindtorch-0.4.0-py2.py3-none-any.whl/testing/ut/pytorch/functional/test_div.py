#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context
from ...utils import SKIP_ENV_ASCEND, param_compare

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_div1():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.int64)
    np_2 = np.array([[1.0, 2],[3, 4]]).astype(np.int64)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.div(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.div(torch_tensor_1, torch_tensor_2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_div2():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.uint8)
    np_2 = np.array([[1, 2],[3, 4]]).astype(np.uint8)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.div(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.div(torch_tensor_1, torch_tensor_2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_div3():
    np_1 = np.array([[3, 4],[3, 4]]).astype(np.int32)
    np_2 = np.array([[2.0, 2.0],[2.0, 2.0]]).astype(np.float32)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.div(ms_tensor_1, ms_tensor_2, rounding_mode='trunc')

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.div(torch_tensor_1, torch_tensor_2, rounding_mode='trunc')

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

@SKIP_ENV_ASCEND(reason='div not support float64 input on Ascend')
def test_div3_float64():
    np_1 = np.array([[3, 4],[3, 4]]).astype(np.int32)
    np_2 = np.array([[2.0, 2.0],[2.0, 2.0]]).astype(np.float32)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.div(ms_tensor_1, ms_tensor_2, rounding_mode='trunc')

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.div(torch_tensor_1, torch_tensor_2, rounding_mode='trunc')

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_div4():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.int64)
    np_2 = np.array([[2, 2],[2, 2]]).astype(np.int16)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.divide(ms_tensor_1, ms_tensor_2, rounding_mode='floor')

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.divide(torch_tensor_1, torch_tensor_2, rounding_mode='floor')

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_div_scalar():
    ms_result = ms_torch.div(3, 4)
    torch_result = torch.div(3, 4)
    param_compare(ms_result, torch_result)

def test_div_scalar2():
    ms_result = ms_torch.div(2, 1, rounding_mode='floor')
    torch_result = torch.div(2, 1, rounding_mode='floor')
    param_compare(ms_result, torch_result)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_div1()
    test_div2()
    test_div3()
    test_div3_float64()
    test_div4()
    test_div_scalar()
    test_div_scalar2()
