#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()


def test_squeeze1():
    x = np.ones(shape=[3, 2, 1])
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch.squeeze(torch_x)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_torch.squeeze(ms_x)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_squeeze2():
    x = np.ones(shape=[3, 1, 2])
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch.squeeze(torch_x, dim=0)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_torch.squeeze(ms_x, dim=0)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_squeeze3():
    x = np.ones(shape=[3, 1, 2, 1])
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch.squeeze(torch_x)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_torch.squeeze(ms_x)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

if __name__ == '__main__':
    set_mode_by_env_config()
    test_squeeze1()
    test_squeeze2()
    test_squeeze3()