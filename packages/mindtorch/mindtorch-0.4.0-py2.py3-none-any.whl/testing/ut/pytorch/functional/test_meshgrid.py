#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_meshgrid1():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([5, 6, 7, 8])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.meshgrid(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.meshgrid(torch_tensor_1, torch_tensor_2)

    assert np.allclose(ms_result[0].asnumpy(), torch_result[0].numpy())
    assert ms_result[0].asnumpy().dtype == torch_result[0].numpy().dtype
    assert np.allclose(ms_result[1].asnumpy(), torch_result[1].numpy())
    assert ms_result[1].asnumpy().dtype == torch_result[1].numpy().dtype

def test_meshgrid2():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([5, 6, 7, 8])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.meshgrid([ms_tensor_1, ms_tensor_2])

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.meshgrid([torch_tensor_1, torch_tensor_2])

    assert np.allclose(ms_result[0].asnumpy(), torch_result[0].numpy())
    assert ms_result[0].asnumpy().dtype == torch_result[0].numpy().dtype
    assert np.allclose(ms_result[1].asnumpy(), torch_result[1].numpy())
    assert ms_result[1].asnumpy().dtype == torch_result[1].numpy().dtype

def test_meshgrid3():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([5, 6, 7, 8])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.meshgrid((ms_tensor_1, ms_tensor_2))

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.meshgrid((torch_tensor_1, torch_tensor_2))

    assert np.allclose(ms_result[0].asnumpy(), torch_result[0].numpy())
    assert ms_result[0].asnumpy().dtype == torch_result[0].numpy().dtype
    assert np.allclose(ms_result[1].asnumpy(), torch_result[1].numpy())
    assert ms_result[1].asnumpy().dtype == torch_result[1].numpy().dtype

def test_meshgrid4():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([5, 6, 7, 8])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.meshgrid(ms_tensor_1, ms_tensor_2, indexing='xy')

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.meshgrid(torch_tensor_1, torch_tensor_2, indexing='xy')

    assert np.allclose(ms_result[0].asnumpy(), torch_result[0].numpy())
    assert ms_result[0].asnumpy().dtype == torch_result[0].numpy().dtype
    assert np.allclose(ms_result[1].asnumpy(), torch_result[1].numpy())
    assert ms_result[1].asnumpy().dtype == torch_result[1].numpy().dtype

if __name__ == '__main__':
    set_mode_by_env_config()
    test_meshgrid1()
    test_meshgrid2()
    test_meshgrid3()
    test_meshgrid4()
