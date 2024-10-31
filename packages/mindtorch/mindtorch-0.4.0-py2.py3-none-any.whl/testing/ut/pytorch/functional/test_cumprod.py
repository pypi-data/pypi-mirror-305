#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_cumprod1():
    np_1 = np.random.randn(3, 4).astype(np.float64)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.cumprod(ms_tensor, dim=0)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.cumprod(torch_tensor, dim=0)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_cumprod2():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.cumprod(ms_tensor, dim=0)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.cumprod(torch_tensor, dim=0)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_cumprod3():
    np_1 = np.random.randn(3, 4).astype(np.int64)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.cumprod(ms_tensor, dim=0)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.cumprod(torch_tensor, dim=0)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


if __name__ == "__main__":
    set_mode_by_env_config()
    test_cumprod1()
    test_cumprod2()
    test_cumprod3()
    