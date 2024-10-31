#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import torch
import mindspore as ms
from mindspore import context
import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_sort():
    x = [0, 1] * 9
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out1, torch_out2 = torch.sort(torch_x, dim=-1, descending=False, stable=True)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out1, ms_out2 = ms_torch.sort(ms_x)
    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())

    torch_out1, torch_out2 = torch.sort(torch_x, dim=0, descending=True, stable=True)
    ms_out1, ms_out2 = ms_torch.sort(ms_x, 0, True)
    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())

def test_msort():
    x = [0, 1] * 9
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch.msort(torch_x)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_torch.msort(ms_x)
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_argsort():
    x = [0, 1] * 9
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch.argsort(torch_x, -1, True)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_torch.argsort(ms_x, -1, True)
    #assert np.allclose(torch_out.numpy(), ms_out.numpy())  # 'stable' is different


if __name__ == '__main__':
    set_mode_by_env_config()
    test_sort()
    test_msort()
    test_argsort()