#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, SKIP_ENV_ASCEND
set_mode_by_env_config()


def test_t1():
    x = np.random.randn(3, 4)
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch.t(torch_x)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_torch.t(ms_x)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_t2():
    x = np.random.randn(4)
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch.t(torch_x)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_torch.t(ms_x)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())


if __name__ == '__main__':
    set_mode_by_env_config()
    test_t1()
    test_t2()