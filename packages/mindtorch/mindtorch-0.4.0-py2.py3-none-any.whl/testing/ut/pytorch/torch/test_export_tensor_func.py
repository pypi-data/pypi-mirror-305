import os
import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()

@SKIP_ENV_GRAPH_MODE(reason="inplace not support graph mode")
def test_asin_():
    ms_tensor = ms_torch.tensor(0.2)
    ms_torch.asin_(ms_tensor)

    pt_tensor = torch.tensor(0.2)
    torch.asin_(pt_tensor)

    param_compare(ms_tensor, pt_tensor)

@SKIP_ENV_GRAPH_MODE(reason="inplace not support graph mode")
def test_asinh_():
    ms_tensor = ms_torch.tensor(0.2)
    ms_torch.asinh_(ms_tensor)

    pt_tensor = torch.tensor(0.2)
    torch.asinh_(pt_tensor)

    param_compare(ms_tensor, pt_tensor)

@SKIP_ENV_GRAPH_MODE(reason="inplace not support graph mode")
def test_atan_():
    ms_tensor = ms_torch.tensor(0.2)
    ms_torch.atan_(ms_tensor)

    pt_tensor = torch.tensor(0.2)
    torch.atan_(pt_tensor)

    param_compare(ms_tensor, pt_tensor)

@SKIP_ENV_GRAPH_MODE(reason="inplace not support graph mode")
def test_atanh_():
    ms_tensor = ms_torch.tensor(0.2)
    ms_torch.atanh_(ms_tensor)

    pt_tensor = torch.tensor(0.2)
    torch.atanh_(pt_tensor)

    param_compare(ms_tensor, pt_tensor)

if __name__ == '__main__':
    test_asin_()
    test_asinh_()
    test_atan_()
    test_atanh_()