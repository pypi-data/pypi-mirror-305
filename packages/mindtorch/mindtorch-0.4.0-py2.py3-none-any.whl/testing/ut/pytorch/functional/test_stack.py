#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_stack1():
    np_1 = np.array([[1, 2], [3, 4]])
    np_2 = np.array([[5, 6], [7, 8]])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.stack((ms_tensor_1, ms_tensor_2), dim=1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.stack((torch_tensor_1, torch_tensor_2), dim=1)

    param_compare(ms_result, torch_result)

def test_stack2():
    np_1 = np.array([[1, 2], [3, 4]])
    np_2 = np.array([[5, 6], [7, 8]])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.stack((ms_tensor_1, ms_tensor_2))

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.stack((torch_tensor_1, torch_tensor_2))

    param_compare(ms_result, torch_result)

def test_stack3():
    np_1 = np.array([[0, 1], [1, 1]])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.stack((ms_tensor_1.byte(), ms_tensor_1.char()))

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.stack((torch_tensor_1.byte(), torch_tensor_1.char()))

    param_compare(ms_result, torch_result)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_stack1()
    test_stack2()
    test_stack3()
