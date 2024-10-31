#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()


def test_cummin1():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result_1, ms_result_2 = ms_torch.cummin(ms_tensor, dim=0)
    torch_tensor = torch.tensor(np_1)
    torch_result_1, torch_result_2 = torch.cummin(torch_tensor, dim=0)
    assert np.allclose(ms_result_1.asnumpy(), torch_result_1.numpy())
    assert ms_result_1.asnumpy().dtype == torch_result_1.numpy().dtype
    assert np.allclose(ms_result_2.asnumpy(), torch_result_2.numpy())
    assert ms_result_2.asnumpy().dtype == torch_result_2.numpy().dtype


def test_cummin2():
    np_1 = np.random.randn(3, 4).astype(np.int32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result_1, ms_result_2 = ms_torch.cummin(ms_tensor, dim=0)
    torch_tensor = torch.tensor(np_1)
    torch_result_1, torch_result_2 = torch.cummin(torch_tensor, dim=0)
    assert np.allclose(ms_result_1.asnumpy(), torch_result_1.numpy())
    assert ms_result_1.asnumpy().dtype == torch_result_1.numpy().dtype
    assert np.allclose(ms_result_2.asnumpy(), torch_result_2.numpy())
    assert ms_result_2.asnumpy().dtype == torch_result_2.numpy().dtype


def test_cummin3():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result_1, ms_result_2 = ms_torch.cummin(ms_tensor, dim=1)
    torch_tensor = torch.tensor(np_1)
    torch_result_1, torch_result_2 = torch.cummin(torch_tensor, dim=1)
    assert np.allclose(ms_result_1.asnumpy(), torch_result_1.numpy())
    assert ms_result_1.asnumpy().dtype == torch_result_1.numpy().dtype
    assert np.allclose(ms_result_2.asnumpy(), torch_result_2.numpy())
    assert ms_result_2.asnumpy().dtype == torch_result_2.numpy().dtype


def test_cummin4():
    np_1 = np.random.randn(3, 4).astype(np.int32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result_1, ms_result_2 = ms_torch.cummin(ms_tensor, dim=1)
    torch_tensor = torch.tensor(np_1)
    torch_result_1, torch_result_2 = torch.cummin(torch_tensor, dim=1)
    assert np.allclose(ms_result_1.asnumpy(), torch_result_1.numpy())
    assert ms_result_1.asnumpy().dtype == torch_result_1.numpy().dtype
    assert np.allclose(ms_result_2.asnumpy(), torch_result_2.numpy())
    assert ms_result_2.asnumpy().dtype == torch_result_2.numpy().dtype


if __name__ == "__main__":
    set_mode_by_env_config()
    test_cummin1()
    test_cummin2()
    test_cummin3()
    test_cummin4()
