#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_unbind():
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch.unbind(torch_x, 0)
    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_torch.unbind(ms_x, 0)
    for ms_out_, torch_out_ in zip(ms_out, torch_out):
        assert np.allclose(ms_out_.numpy(), torch_out_.numpy())

if __name__ == '__main__':
    set_mode_by_env_config()
    test_unbind()