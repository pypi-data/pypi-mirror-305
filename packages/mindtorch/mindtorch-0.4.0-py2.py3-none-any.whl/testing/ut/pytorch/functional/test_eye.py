#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_eye1():
    ms_result = ms_torch.eye(n=2, m=3, dtype=ms_torch.float32)
    torch_result = torch.eye(n=2, m=3, dtype=torch.float32)
    param_compare(ms_result, torch_result)

def test_eye2():
    ms_result = ms_torch.eye(n=2, dtype=ms_torch.int64)
    torch_result = torch.eye(n=2, dtype=torch.int64)
    param_compare(ms_result, torch_result)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_eye1()
    test_eye2()
