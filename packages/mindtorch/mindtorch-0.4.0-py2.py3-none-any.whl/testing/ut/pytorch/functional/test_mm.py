#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np

from ...utils import SKIP_ENV_ASCEND, param_compare, set_mode_by_env_config, SKIP_ENV_GPU
set_mode_by_env_config()

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: ms.ops.Matmul not support int64 input on Ascend.")
def test_mm1():
    np_1 = np.array([[1, 2],[3, 4]])
    np_2 = np.array([[-1, 2],[3, 4]])
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.mm(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.mm(torch_tensor_1, torch_tensor_2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_mm2():
    np_1 = np.array([[1., 2],[3, 4]]).astype(np.float32)
    np_2 = np.array([[1, 2.],[3, 4]]).astype(np.float32)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.mm(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.mm(torch_tensor_1, torch_tensor_2)

    param_compare(ms_result, torch_result)

@SKIP_ENV_ASCEND(reason="mm currently not support float64 on Ascend")
def test_mm2_fp64():
    np_1 = np.random.randn(2, 2)
    np_2 = np.random.randn(2, 2)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.mm(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.mm(torch_tensor_1, torch_tensor_2)

    param_compare(ms_result, torch_result)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_mm1()
    test_mm2()
    test_mm2_fp64()