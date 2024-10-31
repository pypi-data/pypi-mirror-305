import numpy as np
import torch

import mindtorch.torch as msa_torch
from mindtorch.torch import Tensor
from mindtorch.torch.nn import MaxUnpool1d, MaxUnpool2d, MaxUnpool3d

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()


def test_maxunpool1d_compare1():
    kernel_size, stride, padding = 4, 2, 2
    ms_net = MaxUnpool1d((kernel_size,), [stride], padding)
    torch_net = torch.nn.MaxUnpool1d((kernel_size,), [stride], padding)

    B, N, C = 4, 5, 6
    data = np.random.random([B, N, C])
    indices_range = (C - 1) * stride + kernel_size - 2 * padding
    indices = np.random.choice(indices_range - 1, size=(1, 1, C), replace=False)
    indices = indices.repeat(B, 0).repeat(N, 1)

    ms_input = Tensor(data)
    ms_indices = Tensor(indices).type(msa_torch.int64)
    torch_input = torch.Tensor(data)
    torch_indices = torch.Tensor(indices).type(torch.int64)

    torch_output = torch_net(torch_input, torch_indices)
    ms_output = ms_net(ms_input, ms_indices)
    param_compare(ms_output, torch_output)

def test_maxunpool2d_compare1():
    kernel_size, stride = 3, 2
    ms_net = MaxUnpool2d(kernel_size, stride)
    torch_net = torch.nn.MaxUnpool2d(kernel_size, stride)

    B, N, H, W = 4, 5, 6, 7
    data = np.random.random([B, N, H, W])
    indices_range = (H - 1) * stride + kernel_size
    indices_range = ((W - 1) * stride - 1 + kernel_size) * indices_range
    indices = np.random.choice(indices_range - 1, size=(1, 1, H * W), replace=False)
    indices = indices.repeat(B, 0).repeat(N, 1).reshape(B, N, H, W)
    ms_input = Tensor(data)
    ms_indices = Tensor(indices).type(msa_torch.int64)
    torch_input = torch.Tensor(data)
    torch_indices = torch.Tensor(indices).type(torch.int64)

    torch_output = torch_net(torch_input, torch_indices)
    ms_output = ms_net(ms_input, ms_indices)
    param_compare(ms_output, torch_output)


def test_maxunpool2d_compare2():
    kernel_size, stride, padding = 4, 2, 2
    ms_net = MaxUnpool2d(kernel_size, stride, padding)
    torch_net = torch.nn.MaxUnpool2d(kernel_size, stride, padding)

    B, N, H, W = 6, 7, 8, 9
    data = np.random.random([B, N, H, W])
    indices_range = (H - 1) * stride + kernel_size - 2 * padding
    indices_range = ((W - 1) * stride - 1 + kernel_size - 2 * padding) * indices_range
    indices = np.random.choice(indices_range - 1, size=(1, 1, H * W), replace=False)
    indices = indices.repeat(B, 0).repeat(N, 1).reshape(B, N, H, W)
    ms_input = Tensor(data)
    ms_indices = Tensor(indices).type(msa_torch.int64)
    torch_input = torch.Tensor(data)
    torch_indices = torch.Tensor(indices).type(torch.int64)

    torch_output = torch_net(torch_input, torch_indices)
    ms_output = ms_net(ms_input, ms_indices)
    param_compare(ms_output, torch_output)

def test_maxunpool2d_compare3():
    kernel_size, stride, padding = (3, 5), (3, 1), 0
    ms_net = MaxUnpool2d(kernel_size, stride, padding)
    torch_net = torch.nn.MaxUnpool2d(kernel_size, stride, padding)

    B, N, H, W = 1, 32, 9, 9
    data = np.random.random([B, N, H, W])
    indices_range = (H - 1) * stride[0] + kernel_size[0]
    indices_range = ((W - 1) * stride[1] - 1 + kernel_size[1]) * indices_range

    indices = np.random.choice(indices_range - 1, size=(1, 1, H * W), replace=False)
    indices = indices.repeat(B, 0).repeat(N, 1).reshape(B, N, H, W)
    ms_input = Tensor(data)
    ms_indices = Tensor(indices).type(msa_torch.int64)
    torch_input = torch.Tensor(data)
    torch_indices = torch.Tensor(indices).type(torch.int64)

    torch_output = torch_net(torch_input, torch_indices)
    ms_output = ms_net(ms_input, ms_indices)
    param_compare(ms_output, torch_output)


def test_maxunpool3d_compare1():
    kernel_size, stride, padding = 4, 2, 2
    ms_net = MaxUnpool3d(kernel_size, stride, padding)
    torch_net = torch.nn.MaxUnpool3d(kernel_size, stride, padding)

    B, C, D, H, W = 4, 5, 6, 6, 6
    data = np.random.random([B, C, D, H, W])
    indices_range = (D - 1) * stride + kernel_size - 2 * padding
    indices_range = ((H - 1) * stride - 1 + kernel_size - 2 * padding) * indices_range
    indices_range = ((W - 1) * stride - 1 + kernel_size - 2 * padding) * indices_range

    indices = np.random.choice(indices_range - 1, size=(1, 1,D * H * W), replace=False)
    indices = indices.repeat(B, 0).repeat(C, 1).reshape(B, C, D, H, W)
    ms_indices = Tensor(indices).type(msa_torch.int64)
    torch_indices = torch.Tensor(indices).type(torch.int64)

    ms_input = Tensor(data.astype(np.float32))
    torch_input = torch.Tensor(data)

    torch_output = torch_net(torch_input, torch_indices)
    ms_output = ms_net(ms_input, ms_indices)
    param_compare(ms_output, torch_output)


if __name__ == '__main__':
    set_mode_by_env_config()    
    test_maxunpool1d_compare1()
    test_maxunpool2d_compare1()
    test_maxunpool2d_compare2()
    test_maxunpool2d_compare3()
    test_maxunpool3d_compare1()
