#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, SKIP_ENV_ASCEND, SKIP_ENV_CPU
set_mode_by_env_config()

def test_diag1():
    np_1 = np.array([1, 2, 3])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.diag(ms_tensor_1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.diag(torch_tensor_1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_diag2():
    np_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.diag(ms_tensor_1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.diag(torch_tensor_1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

# TODO: undo skipping after bug fixed
@SKIP_ENV_ASCEND(reason="ms.numpy.diag has bug on Ascend")
def test_diag3():
    np_1 = np.array([1, 2, 3])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.diag(ms_tensor_1, 1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.diag(torch_tensor_1, 1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_diagonal1():
    np_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.diagonal(ms_tensor_1, 0)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.diagonal(torch_tensor_1, 0)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_diagonal2():
    np_1 = np.random.randn(2, 5, 4, 2)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.diagonal(ms_tensor_1, offset=-1, dim1=1, dim2=2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.diagonal(torch_tensor_1, offset=-1, dim1=1, dim2=2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_diagonal3():
    np_1 = np.random.randn(3, 3)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.diagonal(ms_tensor_1, 0)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.diagonal(torch_tensor_1, 0)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_diagonal4():
    np_1 = np.random.randn(4, 5, 6, 7)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.diagonal(ms_tensor_1, offset=2, dim1=1, dim2=2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.diagonal(torch_tensor_1, offset=2, dim1=1, dim2=2)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

if __name__ == '__main__':
    set_mode_by_env_config()
    test_diag1()
    test_diag2()
    test_diag3()
    test_diagonal1()
    test_diagonal2()
    test_diagonal3()
    test_diagonal4()
