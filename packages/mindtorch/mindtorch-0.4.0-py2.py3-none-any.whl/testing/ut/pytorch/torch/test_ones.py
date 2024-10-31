#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_ones1():
    ms_result = ms_torch.ones(1, 2, 3, dtype=ms_torch.float32)
    torch_result = torch.ones(1, 2, 3, dtype=torch.float32)

    param_compare(ms_result, torch_result)

def test_ones2():
    ms_result = ms_torch.ones((1, 2, 3), dtype=ms_torch.float32)
    torch_result = torch.ones((1, 2, 3), dtype=torch.float32)

    param_compare(ms_result, torch_result)

def test_ones3():
    ms_result = ms_torch.ones([2, 3])
    torch_result = torch.ones([2, 3])

    param_compare(ms_result, torch_result)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_ones1()
    test_ones2()
    test_ones3()