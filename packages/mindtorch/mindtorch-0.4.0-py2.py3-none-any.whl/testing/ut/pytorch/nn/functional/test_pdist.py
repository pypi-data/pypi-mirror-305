#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, param_compare, SKIP_ENV_ASCEND
set_mode_by_env_config()


def test_pdist1():
    data = np.arange(0, 12).reshape(4, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.pdist(torch_input, 3.1)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.pdist(ms_input, 3.1)

    param_compare(ms_out, torch_out)


def test_pdist2():
    data = np.arange(0, 12).reshape(4, 3).astype(np.float64)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.pdist(torch_input, 0)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.pdist(ms_input, 0)

    param_compare(ms_out, torch_out)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_pdist1()
    test_pdist2()
