#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
from torch.nn.functional import grid_sample
import numpy as np
from mindspore import context

from ....utils import SKIP_ENV_ASCEND, SKIP_ENV_CPU, SKIP_ENV_GPU, set_mode_by_env_config, param_compare
set_mode_by_env_config()


def test_grid_sample():
    data = np.array(np.ones(shape=(2, 2, 2, 2))).astype(np.float32)
    grid_data = np.arange(0.2, 1, 0.1).reshape((2, 2, 1, 2)).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.grid_sample(ms_input, grid=ms_torch.tensor(grid_data))

    torch_input = torch.tensor(data)
    torch_out = grid_sample(torch_input, grid=torch.tensor(grid_data))

    param_compare(ms_out, torch_out)

def test_grid_sample_all_args():
    data = np.array(np.ones(shape=(2, 2, 2, 2))).astype(np.float32)
    grid_data = np.arange(0.2, 1, 0.1).reshape((2, 2, 1, 2)).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.grid_sample(ms_input, grid=ms_torch.tensor(grid_data), \
        mode="nearest", padding_mode="reflection", align_corners=True)

    torch_input = torch.tensor(data)
    torch_out = grid_sample(torch_input, grid=torch.tensor(grid_data), \
        mode="nearest", padding_mode="reflection", align_corners=True)

    param_compare(ms_out, torch_out)

@SKIP_ENV_ASCEND(reason="grid_sample currently not support float64 on Ascend")
def test_grid_sample_all_args_fp64():
    data = np.array(np.ones(shape=(1, 1, 2, 2))).astype(np.float64)
    grid_data = np.arange(0.2, 1, 0.1).reshape((1, 2, 2, 2)).astype(np.float64)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.grid_sample(ms_input, grid=ms_torch.tensor(grid_data), \
        mode="nearest", padding_mode="reflection", align_corners=True)
    torch_input = torch.tensor(data)
    torch_out = grid_sample(torch_input, grid=torch.tensor(grid_data), \
        mode="nearest", padding_mode="reflection", align_corners=True)
    param_compare(ms_out, torch_out)

def test_grid_sample_all_args2():
    data = np.array(np.ones(shape=(2, 2, 2, 2))).astype(np.float32)
    grid_data = np.arange(0.2, 1, 0.1).reshape((2, 2, 1, 2)).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.grid_sample(ms_input, ms_torch.tensor(grid_data), \
        "nearest", "reflection", True)

    torch_input = torch.tensor(data)
    torch_out = grid_sample(torch_input, torch.tensor(grid_data), \
        "nearest", "reflection", True)

    param_compare(ms_out, torch_out)

@SKIP_ENV_ASCEND(reason="grid_sample currently not support float64 on Ascend")
def test_grid_sample_all_args2_fp64():
    data = np.array(np.ones(shape=(2, 2, 2, 2))).astype(np.float64)
    grid_data = np.arange(0.2, 1, 0.1).reshape((2, 2, 1, 2)).astype(np.float64)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.grid_sample(ms_input, ms_torch.tensor(grid_data), \
        "nearest", "reflection", True)

    torch_input = torch.tensor(data)
    torch_out = grid_sample(torch_input, torch.tensor(grid_data), \
        "nearest", "reflection", True)

    param_compare(ms_out, torch_out)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_grid_sample()
    test_grid_sample_all_args()
    test_grid_sample_all_args2()
    test_grid_sample_all_args_fp64()
    test_grid_sample_all_args2_fp64()