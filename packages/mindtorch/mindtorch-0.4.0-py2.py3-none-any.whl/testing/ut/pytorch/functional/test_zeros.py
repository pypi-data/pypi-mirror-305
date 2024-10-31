#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_zeros1():
    ms_result = ms_torch.zeros(1, 2, 3)
    torch_result = torch.zeros(1, 2, 3)
    param_compare(ms_result, torch_result)

def test_zeros2():
    ms_result = ms_torch.zeros((1, 2, 3))
    torch_result = torch.zeros((1, 2, 3))
    param_compare(ms_result, torch_result)

def test_zeros3():
    ms_result = ms_torch.zeros([5], dtype=ms_torch.float64)
    torch_result = torch.zeros([5], dtype=torch.float64)
    param_compare(ms_result, torch_result)

def test_zeros4():
    ms_result = ms_torch.zeros(size=(2, 3), dtype=ms_torch.float64)
    torch_result = torch.zeros(size=(2, 3), dtype=torch.float64)
    param_compare(ms_result, torch_result)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_zeros1()
    test_zeros2()
    test_zeros3()
    test_zeros4()
