#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context
from ...utils import SKIP_ENV_ASCEND

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_cumsum1():
    np_1 = np.random.randn(3, 4).astype(np.float64)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.cumsum(ms_tensor, dim=0)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.cumsum(torch_tensor, dim=0)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_cumsum2():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.cumsum(ms_tensor, dim=0)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.cumsum(torch_tensor, dim=0)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

@SKIP_ENV_ASCEND(reason='cumsum not support int64 input on Ascend')
def test_cumsum3():
    np_1 = np.random.randn(3, 4).astype(np.int64)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.cumsum(ms_tensor, dim=0)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.cumsum(torch_tensor, dim=0)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

@SKIP_ENV_ASCEND(reason='cumsum not support int64 input on Ascend')
def test_cumsum_uint8_overflow():
    data = np.array([66, 66, 66, 66, 66]).astype(np.uint8)

    ms_result = ms_torch.tensor(data).cumsum(0)
    torch_result = torch.tensor(data).cumsum(0)

    param_compare(ms_result, torch_result)

if __name__ == "__main__":
    set_mode_by_env_config()
    test_cumsum1()
    test_cumsum2()
    test_cumsum3()
    test_cumsum_uint8_overflow()
