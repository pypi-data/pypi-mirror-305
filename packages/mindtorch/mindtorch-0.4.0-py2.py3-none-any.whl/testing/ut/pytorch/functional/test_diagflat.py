#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()


def test_diagflat1():
    np_1 = np.random.randn(8).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.diagflat(ms_tensor, offset=-1)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.diagflat(torch_tensor, offset=-1)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_diagflat2():
    np_1 = np.random.randn(8).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.diagflat(ms_tensor, offset=0)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.diagflat(torch_tensor, offset=0)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_diagflat3():
    np_1 = np.random.randn(8).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.diagflat(ms_tensor, offset=2)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.diagflat(torch_tensor, offset=2)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_diagflat4():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.diagflat(ms_tensor, offset=-1)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.diagflat(torch_tensor, offset=-1)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_diagflat5():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.diagflat(ms_tensor, offset=0)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.diagflat(torch_tensor, offset=0)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_diagflat6():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.diagflat(ms_tensor, offset=2)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.diagflat(torch_tensor, offset=2)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


if __name__ == "__main__":
    set_mode_by_env_config()
    test_diagflat1()
    test_diagflat2()
    test_diagflat3()
    test_diagflat4()
    test_diagflat5()
    test_diagflat6()
