#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import SKIP_ENV_ASCEND, SKIP_ENV_CPU, SKIP_ENV_GPU, param_compare, set_mode_by_env_config, is_test_under_ascend_context
set_mode_by_env_config()

@SKIP_ENV_ASCEND(reason="currently softmax not support float64 on Ascend")
def test_softmax_fp64():
    np_array = np.random.randn(2, 3)

    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.softmax(torch_tensor, -1, torch.float32)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out1 = ms_torch.softmax(ms_tensor, -1, ms_torch.float32)
    param_compare(torch_out1, ms_out1)

def test_softmax():
    np_array = np.random.randn(4, 3, 3, 20).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.softmax(torch_tensor, -1, torch.float32)
    torch_out2 = torch.softmax(torch_tensor, 2)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out1 = ms_torch.softmax(ms_tensor, -1, ms_torch.float32)
    ms_out2 = ms_torch.softmax(ms_tensor, 2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_softmax()
    test_softmax_fp64()