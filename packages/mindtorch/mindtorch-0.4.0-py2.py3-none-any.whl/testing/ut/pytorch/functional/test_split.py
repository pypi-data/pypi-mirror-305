#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_split1():
    np_array = np.random.random((5,2)).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.split(torch_tensor, split_size_or_sections=2)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.split(ms_tensor, split_size_or_sections=2)

    for i in range(len(ms_out)):
        assert np.allclose(ms_out[i].numpy(), torch_out[i].numpy())
        assert ms_out[i].numpy().dtype == torch_out[i].numpy().dtype

def test_split2():
    np_array = np.random.random((5,2)).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.split(torch_tensor, split_size_or_sections=[1,4])

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.split(ms_tensor, split_size_or_sections=[1,4])

    for i in range(len(ms_out)):
        assert np.allclose(ms_out[i].numpy(), torch_out[i].numpy())
        assert ms_out[i].numpy().dtype == torch_out[i].numpy().dtype

def test_split3():
    np_array = np.random.random((5,4)).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.split(torch_tensor, split_size_or_sections=[1,3], dim=1)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.split(ms_tensor, split_size_or_sections=[1,3], dim=1)

    for i in range(len(ms_out)):
        assert np.allclose(ms_out[i].numpy(), torch_out[i].numpy())
        assert ms_out[i].numpy().dtype == torch_out[i].numpy().dtype


def test_split4():
    np_array = np.random.random((3,16,5,4)).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.split(torch_tensor, split_size_or_sections=4, dim=1)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.split(ms_tensor, split_size_or_sections=4, dim=1)

    for i in range(len(ms_out)):
        assert np.allclose(ms_out[i].numpy(), torch_out[i].numpy())
        assert ms_out[i].numpy().dtype == torch_out[i].numpy().dtype

def test_split5():
    np_array = np.random.random((3,16,5,4)).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.split(torch_tensor, split_size_or_sections=[1,2,3,4,6], dim=1)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.split(ms_tensor, split_size_or_sections=[1,2,3,4,6], dim=1)

    for i in range(len(ms_out)):
        assert np.allclose(ms_out[i].numpy(), torch_out[i].numpy())
        assert ms_out[i].numpy().dtype == torch_out[i].numpy().dtype

def test_split_with_sizes():
    np_array = np.random.random((5,2)).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.split_with_sizes(torch_tensor, (2, 3))

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.split_with_sizes(ms_tensor, (2, 3))

    param_compare(torch_out, ms_out)

def test_hsplit():
    tensor = np.random.random((3, 4, 4)).astype(np.float32)
    index_array = [1, 2, 3]
    torch_tensor = torch.tensor(tensor)
    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.hsplit(torch_tensor, index_array)
    ms_output = ms_torch.hsplit(ms_tensor, index_array)
    for i in range(3):
        assert np.allclose(ms_output[i].asnumpy(), torch_output[i].numpy())
        assert ms_output[i].asnumpy().dtype == torch_output[i].numpy().dtype

def test_dsplit():
    tensor = np.random.random((3, 4, 4)).astype(np.float32)
    index_array = (1, 2, 3)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.dsplit(torch_tensor, index_array)
    ms_output = ms_torch.dsplit(ms_tensor, index_array)
    for i in range(3):
        assert np.allclose(ms_output[i].asnumpy(), torch_output[i].numpy())
        assert ms_output[i].asnumpy().dtype == torch_output[i].numpy().dtype

def test_tensor_split():
    tensor = np.random.random((3, 4, 4)).astype(np.float32)
    index_array = [1, 2, 3]
    torch_tensor = torch.tensor(tensor)
    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.tensor_split(torch_tensor, index_array)
    ms_output = ms_torch.tensor_split(ms_tensor, index_array)
    for i in range(3):
        assert np.allclose(ms_output[i].asnumpy(), torch_output[i].numpy())
        assert ms_output[i].asnumpy().dtype == torch_output[i].numpy().dtype

    torch_output = torch.tensor_split(torch_tensor, index_array, dim=2)
    ms_output = ms_torch.tensor_split(ms_tensor, index_array, dim=2)
    for i in range(3):
        assert np.allclose(ms_output[i].asnumpy(), torch_output[i].numpy())
        assert ms_output[i].asnumpy().dtype == torch_output[i].numpy().dtype

def test_vsplit():
    tensor = np.random.random((3, 4, 4)).astype(np.float32)
    index_array = [1, 2]
    torch_tensor = torch.tensor(tensor)
    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.vsplit(torch_tensor, index_array)
    ms_output = ms_torch.vsplit(ms_tensor, index_array)
    for i in range(3):
        assert np.allclose(ms_output[i].asnumpy(), torch_output[i].numpy())
        assert ms_output[i].asnumpy().dtype == torch_output[i].numpy().dtype


if __name__ == '__main__':
    set_mode_by_env_config()
    test_split1()
    test_split2()
    test_split3()
    test_split4()
    test_split5()
    test_hsplit()
    test_dsplit()
    test_tensor_split()
    test_vsplit()