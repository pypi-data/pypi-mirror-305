#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindtorch.torch as ms_torch
import torch
import numpy as np

from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_ASCEND, is_test_under_ascend_context
set_mode_by_env_config()

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: ms.ops.Matmul not support int64 input on Ascend.")
def test_matmul1():
    np_1 = np.array([1, 2, 3, 4]).astype(np.int64)
    np_2 = np.array([5, 6, 7, 8]).astype(np.int64)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_out = ms_torch.matmul(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch.matmul(torch_tensor_1, torch_tensor_2)

    param_compare(torch_out, ms_out)


def test_matmul2():
    np_1 = np.array([1, 2]).astype(np.float32)
    np_2 = np.array([[5, 6], [7, 8]]).astype(np.float32)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_out = ms_torch.matmul(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch.matmul(torch_tensor_1, torch_tensor_2)

    param_compare(torch_out, ms_out)


def test_matmul3():
    np_1 = np.arange(0, 36).reshape(3, 1, 6, 2).astype(np.int32)
    np_2 = np.arange(0, 40).reshape(5, 2, 4).astype(np.int32)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_out = ms_torch.matmul(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch.matmul(torch_tensor_1, torch_tensor_2)

    param_compare(torch_out, ms_out)


def test_matmul4():
    np_1 = np.arange(0, 12).reshape(3, 1, 2, 2).astype(np.int32)
    np_2 = np.arange(0, 20).reshape(5, 2, 2).astype(np.int32)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_out = ms_torch.matmul(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch.matmul(torch_tensor_1, torch_tensor_2)

    param_compare(torch_out, ms_out)

def test_matmul_broadcast():
    np_1 = np.random.randn(4, 4, 1, 4, 4).astype(np.float32)
    np_2 = np.random.randn(4, 1, 4, 4, 1).astype(np.float32)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_out = ms_torch.matmul(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch.matmul(torch_tensor_1, torch_tensor_2)

    if is_test_under_ascend_context():
        param_compare(torch_out, ms_out, atol=3e-3, rtol=3e-3)
    else:
        param_compare(torch_out, ms_out)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_matmul1()
    test_matmul2()
    test_matmul3()
    test_matmul4()
    test_matmul_broadcast()
