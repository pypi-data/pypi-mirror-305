import numpy as np
import torch
import mindspore as ms
import mindtorch.torch as ms_torch

from ....utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()


def test_maxunpool1d_with_2dim():
    N = np.random.randint(1, 33)
    C = np.random.randint(1, 257)
    tensor = np.random.randn(N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool1d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool1d(torch_pooling, torch_indices, kernel_size, stride, padding)

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool1d(ms_pooling, ms_indices, kernel_size, stride, padding)

    param_compare(ms_output, torch_output)

def test_maxunpool1d_with_3dim():
    B = np.random.randint(1, 33)
    N = np.random.randint(1, 33)
    C = np.random.randint(1, 257)
    tensor = np.random.randn(B, N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool1d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool1d(torch_pooling, torch_indices, kernel_size, stride, padding)

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool1d(ms_pooling, ms_indices, kernel_size, stride, padding)

    param_compare(ms_output, torch_output)

def test_maxunpool1d_with_3dim_shape():
    B = np.random.randint(1, 33)
    N = np.random.randint(1, 33)
    C = np.random.randint(1, 257)
    tensor = np.random.randn(B, N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool1d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool1d(torch_pooling, torch_indices, kernel_size, stride, padding, output_size=torch_tensor.size())

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool1d(ms_pooling, ms_indices, kernel_size, stride, padding, tensor.shape)

    param_compare(ms_output, torch_output)

def test_maxunpool1d_with_2dim_shape():
    N = np.random.randint(1, 33)
    C = np.random.randint(1, 257)
    tensor = np.random.randn(N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool1d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool1d(torch_pooling, torch_indices, kernel_size, stride, padding, output_size=[C])

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool1d(ms_pooling, ms_indices, kernel_size, stride, padding, tensor.shape)

    param_compare(ms_output, torch_output)

def test_maxunpool2d_with_3dim():
    H = W = np.random.randint(1, 33)
    C = np.random.randint(1, 257)
    tensor = np.random.randn(C, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, H + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool2d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool2d(torch_pooling, torch_indices, kernel_size, stride, padding)

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool2d(ms_pooling, ms_indices, kernel_size, stride, padding)

    param_compare(ms_output, torch_output)

def test_maxunpool2d_with_3dim_shape():
    H = W = np.random.randint(1, 33)
    C = np.random.randint(1, 257)
    tensor = np.random.randn(C, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, H + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool2d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool2d(torch_pooling, torch_indices, kernel_size, stride, padding, [H, W])

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool2d(ms_pooling, ms_indices, kernel_size, stride, padding,tensor.shape)

    param_compare(ms_output, torch_output)

def test_maxunpool2d_with_4dim():
    H = W = np.random.randint(1, 33)
    C = np.random.randint(1, 129)
    N = np.random.randint(1, 33)
    tensor = np.random.randn(N, C, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, H + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool2d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool2d(torch_pooling, torch_indices, kernel_size, stride, padding)

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool2d(ms_pooling, ms_indices, kernel_size, stride, padding)

    param_compare(ms_output, torch_output)

def test_maxunpool2d_with_4dim_shape():
    H = W = np.random.randint(1, 33)
    C = np.random.randint(1, 129)
    N = np.random.randint(1, 33)
    tensor = np.random.randn(N, C, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, H + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool2d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool2d(torch_pooling, torch_indices, kernel_size, stride, padding, torch_tensor.size())

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool2d(ms_pooling, ms_indices, kernel_size, stride, padding, tensor.shape)

    param_compare(ms_output, torch_output)

def test_maxunpool3d_with_4dim():
    H = W = np.random.randint(1, 33)
    C = np.random.randint(1, 129)
    D = np.random.randint(1, H + 1)
    tensor = np.random.randn(C, D, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, D + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool3d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool3d(torch_pooling, torch_indices, kernel_size, stride, padding)

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool3d(ms_pooling, ms_indices, kernel_size, stride, padding)

    param_compare(ms_output, torch_output)

def test_maxunpool3d_with_4dim_shape():
    H = W = np.random.randint(1, 33)
    C = np.random.randint(1, 129)
    D = np.random.randint(1, H + 1)
    tensor = np.random.randn(C, D, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, D + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool3d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool3d(torch_pooling, torch_indices, kernel_size, stride, padding, [D, H, W])

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool3d(ms_pooling, ms_indices, kernel_size, stride, padding, tensor.shape)

    param_compare(ms_output, torch_output)

def test_maxunpool3d_with_5dim():
    H = W = np.random.randint(1, 33)
    C = np.random.randint(1, 129)
    D = np.random.randint(1, H + 1)
    N = np.random.randint(1, 17)
    tensor = np.random.randn(N, C, D, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, D + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool3d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool3d(torch_pooling, torch_indices, kernel_size, stride, padding)

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool3d(ms_pooling, ms_indices, kernel_size, stride, padding)

    param_compare(ms_output, torch_output)

def test_maxunpool3d_with_5dim_shape():
    H = W = np.random.randint(1, 33)
    C = np.random.randint(1, 129)
    D = np.random.randint(1, H + 1)
    N = np.random.randint(1, 17)
    tensor = np.random.randn(N, C, D, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, D + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool3d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    torch_output = torch.nn.functional.max_unpool3d(torch_pooling, torch_indices, kernel_size, stride, padding, torch_tensor.size())

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool3d(ms_pooling, ms_indices, kernel_size, stride, padding, tensor.shape)

    param_compare(ms_output, torch_output)

def test_maxunpool1d_with_keywords_input():
    N = np.random.randint(1, 33)
    C = np.random.randint(1, 257)
    tensor = np.random.randn(N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    #padding = np.random.randint(0, kernel_size/2 + 1)
    stride = 1

    torch_pooling, torch_indices = torch.nn.functional.max_pool1d(torch_tensor, kernel_size, stride, return_indices=True)
    torch_output = torch.nn.functional.max_unpool1d(torch_pooling, torch_indices, kernel_size, stride)

    ms_pooling = ms_torch.tensor(torch_pooling.numpy())
    ms_indices = ms_torch.tensor(torch_indices.numpy())

    ms_output = ms_torch.nn.functional.max_unpool1d(ms_pooling, ms_indices, kernel_size, stride)

    param_compare(ms_output, torch_output)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_maxunpool1d_with_2dim()
    test_maxunpool1d_with_3dim()
    test_maxunpool2d_with_3dim()
    test_maxunpool2d_with_4dim()
    test_maxunpool3d_with_4dim()
    test_maxunpool3d_with_5dim()
    test_maxunpool1d_with_2dim_shape()
    # test_maxunpool1d_with_3dim_shape()
    test_maxunpool2d_with_3dim_shape()
    test_maxunpool2d_with_4dim_shape()
    test_maxunpool3d_with_4dim_shape()
    test_maxunpool3d_with_5dim_shape()
    test_maxunpool1d_with_keywords_input()
