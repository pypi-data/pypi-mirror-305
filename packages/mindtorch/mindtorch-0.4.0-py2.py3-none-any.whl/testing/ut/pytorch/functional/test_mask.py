#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_masked_select():
    x = np.random.random((3,4)).astype(np.float32)

    torch_tensor = torch.tensor(x)
    torch_mask = torch_tensor.ge(0.5)
    torch_out = torch.masked_select(torch_tensor, torch_mask)
    ms_tensor = ms_torch.tensor(x)
    ms_mask = ms_tensor.ge(0.5)
    ms_out = ms_torch.masked_select(ms_tensor, ms_mask)

    param_compare(ms_out, torch_out)

def test_masked_select1():
    x = np.random.random((3,4)).astype(np.float32)

    torch_tensor = torch.tensor(x)
    torch_mask = torch_tensor.to(torch.uint8)
    torch_out = torch.masked_select(torch_tensor, torch_mask)
    ms_tensor = ms_torch.tensor(x)
    ms_mask = ms_tensor.to(ms_torch.uint8)
    ms_out = ms_torch.masked_select(ms_tensor, ms_mask)

    param_compare(ms_out, torch_out)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_masked_select()
    test_masked_select1()
