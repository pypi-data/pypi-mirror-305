import numpy as np
import torch
import mindspore as ms
import mindtorch.torch as ms_torch

from ....utils import set_mode_by_env_config
set_mode_by_env_config()


def test_max_pool1d_1():
    N = np.random.randint(1, 33)
    C = np.random.randint(2, 65)
    tensor = np.random.randn(N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = np.random.randint(1, C + 1)

    ms_tensor = ms_torch.tensor(tensor)
    torch_output, torch_indices = torch.nn.functional.max_pool1d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    ms_output, ms_indices = ms_torch.nn.functional.max_pool1d(ms_tensor, kernel_size, stride, padding, return_indices=True)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert np.allclose(ms_indices.asnumpy(), torch_indices.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape


def test_max_pool1d_2():
    #TODO: random error
    np.random.seed(1)
    N = np.random.randint(1, 33)
    C = np.random.randint(2, 65)
    tensor = np.random.randn(N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = np.random.randint(1, C + 1)

    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.nn.functional.max_pool1d(torch_tensor, kernel_size, stride, padding)
    ms_output = ms_torch.nn.functional.max_pool1d(ms_tensor, kernel_size, stride, padding)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape

def test_max_pool1d_3():
    B = np.random.randint(1, 33)
    N = np.random.randint(1, 33)
    C = np.random.randint(2, 65)
    tensor = np.random.randn(B, N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = np.random.randint(1, C + 1)

    ms_tensor = ms_torch.tensor(tensor)
    torch_output, torch_indices = torch.nn.functional.max_pool1d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    ms_output, ms_indices = ms_torch.nn.functional.max_pool1d(ms_tensor, kernel_size, stride, padding, return_indices=True)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert np.allclose(ms_indices.asnumpy(), torch_indices.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape


def test_max_pool1d_4():
    B = np.random.randint(1, 33)
    N = np.random.randint(1, 33)
    C = np.random.randint(2, 65)
    # tensor = np.random.randn(B, N, C).astype(np.float32)
    # now ms.ops.pad is not supported on Ascend, max_pool1d use ms.ops.Pad instead, the pad value is 0.
    # therefore some result at boarder may be wrong when tensor value are smaller than zero.
    # use np.random.random instead of np.random.randn to generate value that are bigger than zero.
    tensor = np.random.random((B, N, C)).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = np.random.randint(1, C + 1)

    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.nn.functional.max_pool1d(torch_tensor, kernel_size, stride, padding)
    ms_output = ms_torch.nn.functional.max_pool1d(ms_tensor, kernel_size, stride, padding)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape

def test_max_pool1d_5():
    B = np.random.randint(1, 33)
    N = np.random.randint(1, 33)
    C = np.random.randint(2, 65)
    tensor = np.random.randn(B, N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = np.random.randint(1, C + 1)

    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.nn.functional.max_pool1d(torch_tensor, kernel_size, stride, padding, ceil_mode=True)
    ms_output = ms_torch.nn.functional.max_pool1d(ms_tensor, kernel_size, stride, padding, ceil_mode=True)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape

def test_max_pool1d_6():
    B = np.random.randint(1, 33)
    N = np.random.randint(1, 33)
    C = np.random.randint(5, 65)
    tensor = np.random.randn(B, N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, (C-1)/2)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = np.random.randint(1, C + 1)

    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.nn.functional.max_pool1d(torch_tensor, kernel_size, stride, padding, dilation=2, ceil_mode=True)
    ms_output = ms_torch.nn.functional.max_pool1d(ms_tensor, kernel_size, stride, padding, dilation=2, ceil_mode=True)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape

def test_max_pool3d_1():
    N = np.random.randint(1, 17)
    C = np.random.randint(2, 33)
    D = np.random.randint(1, 17)
    H = np.random.randint(1, 33)
    W = np.random.randint(1, 33)

    tensor = np.random.randn(N, C, D, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = (np.random.randint(1, D + 1),
                   np.random.randint(1, H + 1),
                   np.random.randint(1, W + 1))
    padding = (np.random.randint(0, kernel_size[0]/2 + 1),
               np.random.randint(0, kernel_size[1]/2 + 1),
               np.random.randint(0, kernel_size[2]/2 + 1))
    stride = (np.random.randint(1, D + 1),
              np.random.randint(1, H + 1),
              np.random.randint(1, W + 1))

    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.nn.functional.max_pool3d(torch_tensor, kernel_size, stride, padding)
    ms_output = ms_torch.nn.functional.max_pool3d(ms_tensor, kernel_size, stride, padding)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape

def test_max_pool3d_2():
    N = np.random.randint(1, 17)
    C = np.random.randint(2, 33)
    D = np.random.randint(1, 17)
    H = np.random.randint(1, 33)
    W = np.random.randint(1, 33)

    tensor = np.random.randn(N, C, D, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = (np.random.randint(1, D + 1),
                   np.random.randint(1, H + 1),
                   np.random.randint(1, W + 1))
    padding = (np.random.randint(0, kernel_size[0]/2 + 1),
               np.random.randint(0, kernel_size[1]/2 + 1),
               np.random.randint(0, kernel_size[2]/2 + 1))
    stride = (np.random.randint(1, D + 1),
              np.random.randint(1, H + 1),
              np.random.randint(1, W + 1))

    ms_tensor = ms_torch.tensor(tensor)
    torch_output, torch_indices = torch.nn.functional.max_pool3d(torch_tensor, kernel_size, stride, padding, return_indices=True)
    ms_output, ms_indices = ms_torch.nn.functional.max_pool3d(ms_tensor, kernel_size, stride, padding, return_indices=True)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert np.allclose(ms_indices.asnumpy(), torch_indices.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape

def test_max_pool3d_3():
    N = np.random.randint(1, 17)
    C = np.random.randint(2, 33)
    D = np.random.randint(5, 17)
    H = np.random.randint(5, 33)
    W = np.random.randint(5, 33)

    tensor = np.random.randn(N, C, D, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = (np.random.randint(1, (D - 1)/2),
                   np.random.randint(1, (H - 1)/2),
                   np.random.randint(1, (W - 1)/2))
    padding = (np.random.randint(0, kernel_size[0]/2 + 1),
               np.random.randint(0, kernel_size[1]/2 + 1),
               np.random.randint(0, kernel_size[2]/2 + 1))
    stride = (np.random.randint(1, D + 1),
              np.random.randint(1, H + 1),
              np.random.randint(1, W + 1))

    ms_tensor = ms_torch.tensor(tensor)
    torch_output, torch_indices = torch.nn.functional.max_pool3d(torch_tensor, kernel_size,
                                                                 stride, padding, dilation=2, return_indices=True)
    ms_output, ms_indices = ms_torch.nn.functional.max_pool3d(ms_tensor, kernel_size, stride,
                                                              padding, dilation=2, return_indices=True)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert np.allclose(ms_indices.asnumpy(), torch_indices.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape

def test_max_pool3d_4():
    N = np.random.randint(1, 17)
    C = np.random.randint(2, 33)
    D = np.random.randint(5, 17)
    H = np.random.randint(5, 33)
    W = np.random.randint(5, 33)

    tensor = np.random.randn(N, C, D, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = (np.random.randint(1, (D - 1)/2),
                   np.random.randint(1, (H - 1)/2),
                   np.random.randint(1, (W - 1)/2))
    padding = (np.random.randint(0, kernel_size[0]/2 + 1),
               np.random.randint(0, kernel_size[1]/2 + 1),
               np.random.randint(0, kernel_size[2]/2 + 1))
    stride = (np.random.randint(1, D + 1),
              np.random.randint(1, H + 1),
              np.random.randint(1, W + 1))

    ms_tensor = ms_torch.tensor(tensor)
    torch_output, torch_indices = torch.nn.functional.max_pool3d(torch_tensor, kernel_size,
                                                                 stride, padding, dilation=2, return_indices=True, ceil_mode=True)
    ms_output, ms_indices = ms_torch.nn.functional.max_pool3d(ms_tensor, kernel_size, stride,
                                                              padding, dilation=2, return_indices=True, ceil_mode=True)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert np.allclose(ms_indices.asnumpy(), torch_indices.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape

def test_max_pool3d_5():
    C = np.random.randint(2, 33)
    D = np.random.randint(5, 17)
    H = np.random.randint(5, 33)
    W = np.random.randint(5, 33)

    tensor = np.random.randn(C, D, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = (np.random.randint(1, (D - 1)/2),
                   np.random.randint(1, (H - 1)/2),
                   np.random.randint(1, (W - 1)/2))
    padding = (np.random.randint(0, kernel_size[0]/2 + 1),
               np.random.randint(0, kernel_size[1]/2 + 1),
               np.random.randint(0, kernel_size[2]/2 + 1))
    stride = (np.random.randint(1, D + 1),
              np.random.randint(1, H + 1),
              np.random.randint(1, W + 1))

    ms_tensor = ms_torch.tensor(tensor)
    torch_output, torch_indices = torch.nn.functional.max_pool3d(torch_tensor, kernel_size,
                                                                 stride, padding, dilation=2, return_indices=True, ceil_mode=True)
    ms_output, ms_indices = ms_torch.nn.functional.max_pool3d(ms_tensor, kernel_size, stride,
                                                              padding, dilation=2, return_indices=True, ceil_mode=True)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert np.allclose(ms_indices.asnumpy(), torch_indices.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape

def test_max_pool3d_6():
    C = np.random.randint(2, 33)
    D = np.random.randint(5, 17)
    H = np.random.randint(5, 33)
    W = np.random.randint(5, 33)

    tensor = np.random.randn(C, D, H, W).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = (np.random.randint(1, (D - 1)/2),
                   np.random.randint(1, (H - 1)/2),
                   np.random.randint(1, (W - 1)/2))
    padding = (np.random.randint(0, kernel_size[0]/2 + 1),
               np.random.randint(0, kernel_size[1]/2 + 1),
               np.random.randint(0, kernel_size[2]/2 + 1))
    stride = (np.random.randint(1, D + 1),
              np.random.randint(1, H + 1),
              np.random.randint(1, W + 1))

    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.nn.functional.max_pool3d(torch_tensor, kernel_size, stride, padding, dilation=2)
    ms_output = ms_torch.nn.functional.max_pool3d(ms_tensor, kernel_size, stride, padding, dilation=2)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().shape == torch_output.numpy().shape

if __name__ == '__main__':
    set_mode_by_env_config()
    test_max_pool3d_1()
    test_max_pool3d_2()
    test_max_pool3d_3()
    test_max_pool3d_4()
    test_max_pool3d_5()
    test_max_pool3d_6()
    test_max_pool1d_1()
    test_max_pool1d_2()
    test_max_pool1d_3()
    test_max_pool1d_4()
    test_max_pool1d_5()
    test_max_pool1d_6()
