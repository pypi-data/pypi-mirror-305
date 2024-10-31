#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_permute():
    tensor = np.random.random((3, 4, 4)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.permute(torch_tensor, (1, 0, 2))
    ms_output = ms_torch.permute(ms_tensor, (1, 0, 2))
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

if __name__ == '__main__':
    set_mode_by_env_config()
    test_permute()