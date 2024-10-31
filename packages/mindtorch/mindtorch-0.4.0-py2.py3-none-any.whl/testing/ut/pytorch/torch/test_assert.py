#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, SKIP_ENV_PYNATIVE_MODE, SKIP_ENV_CPU
set_mode_by_env_config()

def test_torch_assert1():
    try:
        ms_torch._assert(1 == 2, 'assert fail')
    except:
        return 0
    return 1

def test_torch_assert2():
    try:
        ms_torch._assert(1 == 1, 'assert fail')
    except:
        return 1
    return 0

def test_is_tensor():
    x = [1, 2, -1, 2, 0, -3.5]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch.is_tensor(torch_x)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_torch.is_tensor(ms_x)
    assert np.allclose(ms_out, torch_out)
    torch_out = torch.is_tensor(x)
    ms_out = ms_torch.is_tensor(x)
    assert np.allclose(ms_out, torch_out)

def test_is_floating_point():
    x = [1, 2, -1, 2, 0, -3.5]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch.is_floating_point(torch_x)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_torch.is_floating_point(ms_x)
    assert np.allclose(ms_out, torch_out)

def test_isfinite():
    x = [1, float('inf'), 2, float('-inf'), float('nan')]
    torch_x = torch.tensor(x)
    torch_out = torch.isfinite(torch_x)
    ms_x = ms_torch.tensor(x)
    ms_out = ms_torch.isfinite(ms_x)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_isnan():
    x = [1, float('nan'), 2]
    torch_x = torch.tensor(x)
    torch_out = torch.isnan(torch_x)
    ms_x = ms_torch.tensor(x)
    ms_out = ms_torch.isnan(ms_x)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())


if __name__ == '__main__':
    set_mode_by_env_config()
    test_torch_assert1()
    test_torch_assert2()
    test_is_tensor()
    test_is_floating_point()
    test_isfinite()
    test_isnan()
