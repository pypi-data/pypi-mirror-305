import numpy as np
import torch
import mindtorch.torch as ms_torch
from mindtorch.torch.nn import Upsample

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()


def test_upsample1():
    tensor = np.arange(1, 5).reshape((1, 1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    torch_upsample = torch.nn.Upsample(scale_factor=2, mode="bilinear", align_corners=True)
    torch_output = torch_upsample(torch_tensor)

    ms_tensor = ms_torch.tensor(tensor)
    ms_upsample = Upsample(scale_factor=2, mode="bilinear", align_corners=True)
    ms_output = ms_upsample(ms_tensor)

    param_compare(ms_output, torch_output)


def test_upsample2():
    tensor = np.arange(1, 5).reshape((1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    torch_upsample = torch.nn.Upsample(size=4, mode="linear", align_corners=False)
    torch_output = torch_upsample(torch_tensor)

    ms_tensor = ms_torch.tensor(tensor)
    ms_upsample = Upsample(size=4, mode="linear", align_corners=False)
    ms_output = ms_upsample(ms_tensor)

    param_compare(ms_output, torch_output)


def test_upsampling_nearest2d():
    input = np.arange(1, 5).reshape((1, 1, 2, 2)).astype(np.float32)

    torch_tensor = torch.tensor(input)
    torch_func = torch.nn.UpsamplingNearest2d(scale_factor=2)
    torch_output = torch_func(torch_tensor)

    ms_torch_tensor = ms_torch.tensor(input)
    ms_torch_func = ms_torch.nn.UpsamplingNearest2d(scale_factor=2)
    ms_torch_output = ms_torch_func(ms_torch_tensor)

    param_compare(ms_torch_output, torch_output)


def test_upsampling_bilinear2d():
    input = np.arange(1, 5).reshape((1, 1, 2, 2)).astype(np.float32)

    torch_tensor = torch.tensor(input)
    torch_func = torch.nn.UpsamplingBilinear2d(scale_factor=2)
    torch_output = torch_func(torch_tensor)

    ms_torch_tensor = ms_torch.tensor(input)
    ms_torch_func = ms_torch.nn.UpsamplingBilinear2d(scale_factor=2)
    ms_torch_output = ms_torch_func(ms_torch_tensor)

    param_compare(ms_torch_output, torch_output)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_upsample1()
    test_upsample2()
    test_upsampling_nearest2d()
    test_upsampling_bilinear2d()

