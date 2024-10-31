import numpy as np
import torch
import mindspore as ms
import mindtorch.torch as ms_torch
from mindtorch.utils import is_under_ascend_context, is_under_gpu_context
from ....utils import set_mode_by_env_config, param_compare, SKIP_ENV_ASCEND
set_mode_by_env_config()


def test_avg_pool1d_1():
    N = np.random.randint(1, 33)
    C = np.random.randint(2, 65)
    tensor = np.random.randn(N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = np.random.randint(1, C + 1)

    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.nn.functional.avg_pool1d(torch_tensor, kernel_size, stride, padding)
    ms_output = ms_torch.nn.functional.avg_pool1d(ms_tensor, kernel_size, stride, padding)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_avg_pool1d_2():
    B = np.random.randint(1, 33)
    N = np.random.randint(1, 33)
    C = np.random.randint(2, 62)  # when ceil_mode=True, stride<=63
    tensor = np.random.randn(B, N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = (np.random.randint(1, C + 1), )
    padding = np.random.randint(0, 1)
    stride = (np.random.randint(1, C + 1), )

    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.nn.functional.avg_pool1d(torch_tensor, kernel_size, stride, padding, ceil_mode=True, count_include_pad=False)
    ms_output = ms_torch.nn.functional.avg_pool1d(ms_tensor, kernel_size, stride, padding, ceil_mode=True, count_include_pad=False)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-2)
    else:
        param_compare(ms_output, torch_output)


def test_avg_pool1d_3():
    B = np.random.randint(1, 33)
    N = np.random.randint(1, 33)
    C = np.random.randint(2, 65)
    tensor = np.random.randn(B, N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = np.random.randint(1, C + 1)
    padding = np.random.randint(0, kernel_size/2 + 1)
    stride = np.random.randint(1, C + 1)

    ms_tensor = ms_torch.tensor(tensor)
    torch_output = torch.nn.functional.avg_pool1d(torch_tensor, kernel_size, stride, padding, count_include_pad=True)
    ms_output = ms_torch.nn.functional.avg_pool1d(ms_tensor, kernel_size, stride, padding, count_include_pad=True)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)



def test_avg_pool1d_4():
    tensor = np.random.randn(1, 3, 150).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.avg_pool1d(torch_tensor, kernel_size=(128,), padding=(1,), stride=65)

    ms_tensor = ms_torch.tensor(tensor)

    @ms.jit
    def ms_fun(ms_tensor):
        return ms_torch.nn.functional.avg_pool1d(ms_tensor, kernel_size=(128,), padding=(1,), stride=65)
    ms_output = ms_fun(ms_tensor)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)
    
def test_avg_pool1d_5():
    B = np.random.randint(1, 33)
    N = np.random.randint(1, 33)
    C = np.random.randint(2, 62)
    tensor = np.random.randn(B, N, C).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    kernel_size = (np.random.randint(1, C + 1), )
    stride = (np.random.randint(1, C + 1), )

    ms_tensor = ms_torch.tensor(tensor)
    torch_output1 = torch.nn.functional.avg_pool1d(torch_tensor, kernel_size, stride, padding=0, ceil_mode=True,
        count_include_pad=False)
    torch_output2 = torch.nn.functional.avg_pool1d(torch_tensor, kernel_size, stride, padding=[0], ceil_mode=True,
        count_include_pad=False)
    ms_output1 = ms_torch.nn.functional.avg_pool1d(ms_tensor, kernel_size, stride, padding=0, ceil_mode=True,
        count_include_pad=False)
    ms_output2 = ms_torch.nn.functional.avg_pool1d(ms_tensor, kernel_size, stride, padding=[0], ceil_mode=True,
        count_include_pad=False)

    if is_under_ascend_context():
        param_compare(ms_output1, torch_output1, atol=1e-2)
        param_compare(ms_output2, torch_output2, atol=1e-2)
    else:
        param_compare(ms_output1, torch_output1)
        param_compare(ms_output2, torch_output2)

def test_avg_pool3d_1():
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
    torch_output = torch.nn.functional.avg_pool3d(torch_tensor, kernel_size, stride, padding)
    ms_output = ms_torch.nn.functional.avg_pool3d(ms_tensor, kernel_size, stride, padding)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)


def test_avg_pool3d_2():
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
    torch_output = torch.nn.functional.avg_pool3d(torch_tensor, kernel_size, stride, padding, ceil_mode=True)
    ms_output = ms_torch.nn.functional.avg_pool3d(ms_tensor, kernel_size, stride, padding, ceil_mode=True)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-2)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)

def test_avg_pool3d_3():
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
    torch_output = torch.nn.functional.avg_pool3d(torch_tensor, kernel_size, stride, padding, count_include_pad=True)
    ms_output = ms_torch.nn.functional.avg_pool3d(ms_tensor, kernel_size, stride, padding, count_include_pad=True)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)

def test_avg_pool3d_4():
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
    torch_output = torch.nn.functional.avg_pool3d(torch_tensor, kernel_size, stride, padding, divisor_override=2)
    ms_output = ms_torch.nn.functional.avg_pool3d(ms_tensor, kernel_size, stride, padding, divisor_override=2)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-2)
    elif is_under_gpu_context():
        param_compare(ms_output, torch_output, atol=1e-5)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)

def test_avg_pool3d_5():
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
    padding = [np.random.randint(0, kernel_size[0]/2 + 1),
               np.random.randint(0, kernel_size[1]/2 + 1),
               np.random.randint(0, kernel_size[2]/2 + 1)]
    stride = (np.random.randint(1, D + 1),
              np.random.randint(1, H + 1),
              np.random.randint(1, W + 1))

    ms_tensor = ms_torch.tensor(tensor)
    torch_output1 = torch.nn.functional.avg_pool3d(torch_tensor, kernel_size, stride, padding)
    torch_output2 = torch.nn.functional.avg_pool3d(torch_tensor, kernel_size, stride, padding=0)
    torch_output3 = torch.nn.functional.avg_pool3d(torch_tensor, kernel_size, stride, padding=(0,))
    ms_output1 = ms_torch.nn.functional.avg_pool3d(ms_tensor, kernel_size, stride, padding)
    ms_output2 = ms_torch.nn.functional.avg_pool3d(ms_tensor, kernel_size, stride, padding=0)
    ms_output3 = ms_torch.nn.functional.avg_pool3d(ms_tensor, kernel_size, stride, padding=(0,))

    if is_under_ascend_context():
        param_compare(ms_output1, torch_output1, atol=1e-3)
        param_compare(ms_output2, torch_output2, atol=1e-3)
        param_compare(ms_output3, torch_output3, atol=1e-3)
    else:
        param_compare(ms_output1, torch_output1, atol=1e-7)
        param_compare(ms_output2, torch_output2, atol=1e-7)
        param_compare(ms_output3, torch_output3, atol=1e-7)

def test_avg_pool2d_1():
    tensor = np.random.randn(1, 32, 9, 9).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.avg_pool2d(torch_tensor, (3, 5), stride=None)

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = ms_torch.nn.functional.avg_pool2d(ms_tensor, (3, 5), stride=None)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)


@SKIP_ENV_ASCEND(reason="window_h * window_w should be <= 255 on Ascend.")
def test_avg_pool2d_2():
    tensor = np.random.randn(1, 3, 150, 150).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.avg_pool2d(torch_tensor, kernel_size=(128, 128), padding=(1, 0), stride=65)

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = ms_torch.nn.functional.avg_pool2d(ms_tensor, kernel_size=(128, 128), padding=(1, 0), stride=65)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)


def test_avg_pool2d_3():
    tensor = np.random.randn(32, 9, 9).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.avg_pool2d(torch_tensor, (2, 3), stride=1)

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = ms_torch.nn.functional.avg_pool2d(ms_tensor, (2, 3), stride=1)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)



def test_avg_pool2d_4():
    x = np.random.randn(1, 16, 4, 4).astype(np.float32)

    torch_tensor = torch.tensor(x)
    torch_output = torch.nn.functional.avg_pool2d(torch_tensor, ceil_mode=True, count_include_pad=True, 
                                                  kernel_size=(1, 2), padding=(0, 1), stride=2)

    ms_tensor = ms_torch.tensor(x)
    @ms.jit
    def ms_fun(ms_tensor):
        return ms_torch.nn.functional.avg_pool2d(ms_tensor, ceil_mode=True, count_include_pad=True, 
                                                 kernel_size=(1, 2), padding=(0, 1), stride=2)
    ms_output = ms_fun(ms_tensor)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=3e-3)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)

def test_avg_pool2d_5():
    tensor = np.random.randn(32, 9, 9).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    torch_output1 = torch.nn.functional.avg_pool2d(torch_tensor, (3, 5), stride=None, padding=1)
    torch_output2 = torch.nn.functional.avg_pool2d(torch_tensor, (3, 5), stride=None, padding=[1])
    torch_output3 = torch.nn.functional.avg_pool2d(torch_tensor, (3, 5), stride=None, padding=[1, 0])

    ms_tensor = ms_torch.tensor(tensor)
    ms_output1 = ms_torch.nn.functional.avg_pool2d(ms_tensor, (3, 5), stride=None, padding=1)
    ms_output2 = ms_torch.nn.functional.avg_pool2d(ms_tensor, (3, 5), stride=None, padding=[1])
    ms_output3 = ms_torch.nn.functional.avg_pool2d(ms_tensor, (3, 5), stride=None, padding=[1, 0])

    if is_under_ascend_context():
        param_compare(ms_output1, torch_output1, atol=1e-3)
        param_compare(ms_output2, torch_output2, atol=1e-3)
        param_compare(ms_output3, torch_output3, atol=1e-3)
    else:
        param_compare(ms_output1, torch_output1, atol=1e-7)
        param_compare(ms_output2, torch_output2, atol=1e-7)
        param_compare(ms_output3, torch_output3, atol=1e-7)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_avg_pool1d_1()
    test_avg_pool1d_2()
    test_avg_pool1d_3()
    test_avg_pool1d_4()
    test_avg_pool1d_5()
    test_avg_pool3d_1()
    test_avg_pool3d_2()
    test_avg_pool3d_3()
    test_avg_pool3d_4()
    test_avg_pool3d_5()
    test_avg_pool2d_1()
    test_avg_pool2d_2()
    test_avg_pool2d_3()
    test_avg_pool2d_4()
    test_avg_pool2d_5()
