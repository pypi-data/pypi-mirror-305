#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindtorch.torch as ms_torch
import torch
import numpy as np

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_flip1():
    np_1 = np.random.randn(4, 4)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.flip(ms_tensor_1, (1, ))

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.flip(torch_tensor_1, (1, ))
    param_compare(ms_result, torch_result)

def test_flip2():
    np_1 = np.random.randn(4, 5, 6, 7)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.flip(ms_tensor_1, [0, 3])

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.flip(torch_tensor_1, [0, 3])
    param_compare(ms_result, torch_result)

def test_flip3():
    np_1 = np.random.randn(3, 4, 5)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.flip(ms_tensor_1, (0, 1))

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.flip(torch_tensor_1, (0, 1))
    param_compare(ms_result, torch_result)


def test_flip4():
    np_1 = np.reshape(np.arange(8), (2, 2, 2))
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.flip(ms_tensor_1, [0, 1])

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.flip(torch_tensor_1, [0, 1])
    param_compare(ms_result, torch_result)

def test_fliplr1():
    np_1 = np.random.randn(4, 4)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.fliplr(ms_tensor_1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.fliplr(torch_tensor_1)
    param_compare(ms_result, torch_result)

def test_fliplr2():
    np_1 = np.random.randn(4, 5, 6, 7)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.fliplr(ms_tensor_1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.fliplr(torch_tensor_1)
    param_compare(ms_result, torch_result)

def test_fliplr3():
    #TODO: numpy higher than 1.20 should use float64 instead of float
    np_1 = np.reshape(np.arange(8), (2, 2, 2)).astype(np.float64)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.fliplr(ms_tensor_1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.fliplr(torch_tensor_1)
    param_compare(ms_result, torch_result)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_flip1()
    test_flip2()
    test_flip3()
    test_flip4()
    test_fliplr1()
    test_fliplr2()
    test_fliplr3()

