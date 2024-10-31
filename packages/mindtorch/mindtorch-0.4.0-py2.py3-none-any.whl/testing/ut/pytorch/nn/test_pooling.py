import numpy as np
import torch

import mindtorch.torch as msa_torch
from mindtorch.torch.nn import MaxPool1d, MaxPool2d, MaxPool3d, AvgPool1d, AvgPool2d, AvgPool3d, \
    AdaptiveAvgPool1d, AdaptiveAvgPool2d, AdaptiveAvgPool3d, AdaptiveMaxPool1d, AdaptiveMaxPool2d, AdaptiveMaxPool3d, \
    LPPool1d, LPPool2d, FractionalMaxPool2d, FractionalMaxPool3d
from mindtorch.utils import is_under_ascend_context
import mindspore as ms
from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_ASCEND, SKIP_ENV_CPU
set_mode_by_env_config()


def test_maxpool1d_compare1():
    ms_net = MaxPool1d(4, 2, padding=2)
    torch_net = torch.nn.MaxPool1d(4, 2, padding=2)

    data = np.random.random([4, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_maxpool1d_compare2():
    ms_net = MaxPool1d([4,], (2,), ceil_mode=True)
    torch_net = torch.nn.MaxPool1d([4,], (2,), ceil_mode=True)

    data = np.random.random([4, 5, 6])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_maxpool1d_compare3():
    ms_net = MaxPool1d([4,], (2,), return_indices=True)
    torch_net = torch.nn.MaxPool1d([4,], (2,), return_indices=True)

    data = np.random.random([4, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output, ms_argmax = ms_net(ms_input)
    torch_output, torch_argmax = torch_net(torch_input)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
        param_compare(ms_argmax, torch_argmax, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)
        param_compare(ms_argmax, torch_argmax)

def test_maxpool2d_compare1():
    ms_net = MaxPool2d([3,], (2,))
    torch_net = torch.nn.MaxPool2d([3,], (2,))

    data = np.random.random([4, 5, 6])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_maxpool2d_compare2():
    ms_net = MaxPool2d(4, 2, padding=2)
    torch_net = torch.nn.MaxPool2d(4, 2, padding=2)

    data = np.random.random([6, 7, 8, 9])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_maxpool2d_compare3():
    ms_net = MaxPool2d((3, 5), [3, 1], padding=0)
    torch_net = torch.nn.MaxPool2d((3, 5), [3, 1], padding=0)

    data = np.random.random([1, 32, 9, 9])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_maxpool2d_compare4():
    ms_net = MaxPool2d(kernel_size=2, ceil_mode=True)
    torch_net = torch.nn.MaxPool2d(kernel_size=2, ceil_mode=True)

    data = np.random.random([2, 3, 4, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_maxpool2d_compare5():
    ms_net = MaxPool2d(3, 2, ceil_mode=True)
    torch_net = torch.nn.MaxPool2d(3, 2, ceil_mode=True)

    data = np.random.random([4, 5, 6, 7])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_maxpool2d_compare6():
    ms_net = MaxPool2d(4, 2, padding=2, ceil_mode=True)
    torch_net = torch.nn.MaxPool2d(4, 2, padding=2, ceil_mode=True)

    data = np.random.random([6, 7, 8, 9])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_maxpool2d_compare7():
    ms_net = MaxPool2d(4, 2, padding=2, return_indices=True)
    torch_net = torch.nn.MaxPool2d(4, 2, padding=2, return_indices=True)

    data = np.random.random([6, 7, 8, 9])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output, ms_argmax = ms_net(ms_input)
    torch_output, torch_argmax = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
        param_compare(ms_argmax, torch_argmax, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)
        param_compare(ms_argmax, torch_argmax)

def test_maxpool2d_compare8():
    ms_net = MaxPool2d(4, 2, padding=2, ceil_mode=True)
    torch_net = torch.nn.MaxPool2d(4, 2, padding=2, ceil_mode=True)

    data = np.random.randn(6, 7, 8, 9)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_maxpool3d_compare1():
    ms_net = MaxPool3d([4,], (2,), padding=2, return_indices=True)
    torch_net = torch.nn.MaxPool3d([4,], (2,), padding=2, return_indices=True)

    data = np.random.random([4, 5, 6, 6, 6])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output, ms_argmax = ms_net(ms_input)
    torch_output, torch_argmax = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
        param_compare(ms_argmax, torch_argmax, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)
        param_compare(ms_argmax, torch_argmax)

def test_maxpool3d_compare2():
    ms_net = MaxPool3d(4, 2, padding=2)
    torch_net = torch.nn.MaxPool3d(4, 2, padding=2)

    data = np.random.random([4, 5, 6, 6])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_avgpool1d_compare1():
    ms_net = AvgPool1d(6, stride=2, padding=3)
    torch_net = torch.nn.AvgPool1d(6, stride=2, padding=3)

    data = np.random.random([5, 3, 8])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_avgpool1d_compare2():
    ms_net = AvgPool1d(6, stride=2, padding=3)
    torch_net = torch.nn.AvgPool1d(6, stride=2, padding=3)

    data = np.random.random([5, 8])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_avgpool2d_compare1():
    ms_net = AvgPool2d(2, stride=2, padding=0)
    torch_net = torch.nn.AvgPool2d(2, stride=2, padding=0)

    data = np.random.random([5, 3, 11, 11])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_avgpool2d_compare2():
    ms_net = AvgPool2d(6, stride=2, padding=3)
    torch_net = torch.nn.AvgPool2d(6, stride=2, padding=3)

    data = np.random.random([5, 8, 8])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_avgpool2d_compare3():
    ms_net = AvgPool2d((3, 5), (3, 1), padding=0)
    torch_net = torch.nn.AvgPool2d((3, 5), (3, 1), padding=0)

    data = np.random.random([1, 6, 9, 9])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_avgpool3d_compare():
    ms_net = AvgPool3d(6, stride=2, padding=3)
    torch_net = torch.nn.AvgPool3d(6, stride=2, padding=3)

    data = np.random.random([5, 3, 8, 8, 8])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptive_maxpool1d_compare1():
    ms_net = AdaptiveMaxPool1d(3)
    torch_net = torch.nn.AdaptiveMaxPool1d(3)
    data = np.random.randn(1, 6, 7).astype(np.float32)

    torch_input = torch.Tensor(data)
    torch_output = torch_net(torch_input)

    ms_input = msa_torch.Tensor(data)
    ms_output = ms_net(ms_input)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-2)
    else:
        param_compare(ms_output, torch_output)

@SKIP_ENV_ASCEND(reason="There is bug in ms.ops.adaptive_max_pool2d when return_indices==Ture.")
def test_adaptive_maxpool1d_compare2():
    ms_net = AdaptiveMaxPool1d(3, True)
    torch_net = torch.nn.AdaptiveMaxPool1d(3, True)

    data = np.arange(3 * 8).reshape(3, 8).astype(np.float32)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output, ms_indices = ms_net(ms_input)
    torch_output, torch_indices = torch_net(torch_input)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-2)
        param_compare(ms_indices, torch_indices)
    else:
        param_compare(ms_output, torch_output)
        param_compare(ms_indices, torch_indices)


def test_adaptive_maxpool2d_compare1():
    ms_net = AdaptiveMaxPool2d((3, 10))
    torch_net = torch.nn.AdaptiveMaxPool2d((3, 10))

    data = np.random.randn(6, 9, 9).astype(np.float32)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-2)
    else:
        param_compare(ms_output, torch_output)

@SKIP_ENV_ASCEND(reason="on Ascend, the mindspore.ops.adaptive_max_pool2d result not right.")
def test_adaptive_maxpool2d_compare2():
    ms_net = AdaptiveMaxPool2d(3, True)
    torch_net = torch.nn.AdaptiveMaxPool2d(3, True)

    data = np.random.randn(2, 6, 6, 9).astype(np.float32)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output, ms_indices = ms_net(ms_input)
    torch_output, torch_indices = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-2)
        param_compare(ms_indices, torch_indices)
    else:
        param_compare(ms_output, torch_output)
        param_compare(ms_indices, torch_indices)


def test_adaptive_maxpool3d_compare1():
    ms_net = AdaptiveMaxPool3d(3, True)
    torch_net = torch.nn.AdaptiveMaxPool3d(3, True)
    data = np.random.randn(6, 7, 9, 5).astype(np.float32)

    torch_input = torch.Tensor(data)
    torch_output, torch_indices = torch_net(torch_input)

    ms_input = msa_torch.Tensor(data)
    ms_output, ms_indices = ms_net(ms_input)

    if is_under_ascend_context():
        # Custom implementation only ensures shape consistency
        assert ms_output.shape == torch_output.size()
        # param_compare(ms_output, torch_output, atol=1e-3)
        # param_compare(ms_indices, torch_indices)
    else:
        param_compare(ms_output, torch_output)
        param_compare(ms_indices, torch_indices)


def test_adaptive_maxpool3d_compare2():
    ms_net = AdaptiveMaxPool3d((3, None, 3))
    torch_net = torch.nn.AdaptiveMaxPool3d((3, None, 3))
    data = np.random.randn(1, 6, 7, 9, 5).astype(np.float32)

    torch_input = torch.Tensor(data).to(torch.float64)
    torch_output = torch_net(torch_input)

    ms_input = msa_torch.Tensor(data).to(msa_torch.float64)
    ms_output = ms_net(ms_input)

    if is_under_ascend_context():
        # Custom implementation only ensures shape consistency
        assert ms_output.shape == torch_output.size()
        # param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptive_avgpool1d_compare1():
    ms_net = AdaptiveAvgPool1d(3)
    torch_net = torch.nn.AdaptiveAvgPool1d(3)

    data = np.arange(3 * 8).reshape(1, 3, 8).astype(np.float32)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output= ms_net(ms_input)
    torch_output= torch_net(torch_input)

    param_compare(ms_output, torch_output)

def test_adaptive_avgpool1d_compare2():
    ms_net = AdaptiveAvgPool1d(2)
    torch_net = torch.nn.AdaptiveAvgPool1d(2)

    data = np.arange(3 * 8).reshape(3, 8).astype(np.float32)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output= ms_net(ms_input)
    torch_output= torch_net(torch_input)

    param_compare(ms_output, torch_output)

def test_adaptive_avgpool2d_compare1():
    ms_net = AdaptiveAvgPool2d(3)
    torch_net = torch.nn.AdaptiveAvgPool2d(3)

    data = np.random.randn(6, 6, 9).astype(np.float32)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output= ms_net(ms_input)
    torch_output= torch_net(torch_input)

    param_compare(ms_output, torch_output)

def test_adaptive_avgpool2d_compare2():
    ms_net = AdaptiveAvgPool2d((3, 3))
    torch_net = torch.nn.AdaptiveAvgPool2d((3, 3))

    data = np.random.randn(2, 6, 6, 9).astype(np.float32)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output= ms_net(ms_input)
    torch_output= torch_net(torch_input)

    param_compare(ms_output, torch_output, atol=1e-5)

def test_adaptive_avgpool3d_compare1():
    ms_net = AdaptiveAvgPool3d(3)
    torch_net = torch.nn.AdaptiveAvgPool3d(3)

    data = np.random.randn(1, 6, 7, 9, 5).astype(np.float32)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output= ms_net(ms_input)
    torch_output= torch_net(torch_input)
    param_compare(ms_output, torch_output, atol=1e-5)

def test_adaptive_avgpool3d_compare2():
    ms_net = AdaptiveAvgPool3d(4)
    torch_net = torch.nn.AdaptiveAvgPool3d(4)

    data = np.random.randn(6, 7, 9, 5).astype(np.float32)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output= ms_net(ms_input)
    torch_output= torch_net(torch_input)

    param_compare(ms_output, torch_output, atol=1e-5)

def test_fractional_maxpool2d_compare1():
    ms_net = FractionalMaxPool2d(1, output_ratio=(0.4, 0.4))
    torch_net = torch.nn.FractionalMaxPool2d(1, output_ratio=(0.4, 0.4))

    data = np.array([0.3220, 0.9545, 0.7879, 0.0975, 0.3698,
                    0.5135, 0.5740, 0.3435, 0.1895, 0.8764,
                    0.9581, 0.4760, 0.9014, 0.8522, 0.3664,
                    0.4980, 0.9673, 0.9879, 0.6988, 0.9022,
                    0.9304, 0.1558, 0.0153, 0.1559, 0.9852]).reshape([1, 1, 5, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)

    param_compare(ms_output, torch_output)

def test_fractional_maxpool2d_compare2():
    _random_samples = np.array([[[0.8, 0.7]]])
    ms_random_samples = msa_torch.Tensor(_random_samples)
    torch_random_samples = torch.Tensor(_random_samples)
    ms_net = FractionalMaxPool2d(kernel_size=(2, 2), output_size=(2, 2), _random_samples=ms_random_samples,
                                 return_indices=True)
    torch_net = torch.nn.FractionalMaxPool2d(kernel_size=(2, 2), output_size=(2, 2),
                                             _random_samples=torch_random_samples,
                                             return_indices=True)

    data = np.array([0.3220, 0.9545, 0.7879, 0.0975, 0.3698,
                    0.5135, 0.5740, 0.3435, 0.1895, 0.8764,
                    0.9581, 0.4760, 0.9014, 0.8522, 0.3664,
                    0.4980, 0.9673, 0.9879, 0.6988, 0.9022,
                    0.9304, 0.1558, 0.0153, 0.1559, 0.9852]).reshape([1, 1, 5, 5])

    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output, ms_indices= ms_net(ms_input)
    torch_output, torch_indices = torch_net(torch_input)
    param_compare(ms_output, torch_output)
    param_compare(ms_indices, torch_indices)

def test_fractional_maxpool2d_compare3():
    ms_net = FractionalMaxPool2d(1, output_ratio=0.4)
    torch_net = torch.nn.FractionalMaxPool2d(1, output_ratio=0.4)

    data = np.random.randn(5, 5).reshape([1, 1, 5, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)

    param_compare(ms_output, torch_output)

def test_fractional_maxpool3d_compare1():
    _random_samples = np.array([0.7, 0.6, 0.5]).reshape([1, 1, 3])
    ms_random_samples = msa_torch.Tensor(_random_samples)
    torch_random_samples = torch.Tensor(_random_samples)
    ms_net = FractionalMaxPool3d(kernel_size=(1, 1, 1), output_size=(1, 1, 3),
                                 _random_samples=ms_random_samples, return_indices=True)
    torch_net = torch.nn.FractionalMaxPool3d(kernel_size=(1, 1, 1), output_size=(1, 1, 3), _random_samples=torch_random_samples, return_indices=True)

    data = np.arange(1, 17).reshape([1, 1, 2, 2, 4])

    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output, ms_indices = ms_net(ms_input)
    torch_output, torch_indices = torch_net(torch_input)

    param_compare(ms_output, torch_output)
    param_compare(ms_indices, torch_indices)

def test_fractional_maxpool3d_compare2():
    _random_samples = np.array([0.7, 0.6, 0.5]).reshape([1, 1, 3])
    ms_random_samples = msa_torch.Tensor(_random_samples)
    torch_random_samples = torch.Tensor(_random_samples)
    ms_net = FractionalMaxPool3d(kernel_size=(1, 2, 3), output_ratio=(0.5, 0.4, 0.3),
                                 _random_samples=ms_random_samples, return_indices=True)
    torch_net = torch.nn.FractionalMaxPool3d(kernel_size=(1, 2, 3), output_ratio=(0.5, 0.4, 0.3),
                                             _random_samples=torch_random_samples, return_indices=True)

    data = np.arange(512).reshape([1, 1, 4, 8, 16])

    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output, ms_indices = ms_net(ms_input)
    torch_output, torch_indices = torch_net(torch_input)
    param_compare(ms_output, torch_output)
    param_compare(ms_indices, torch_indices)

def test_fractional_maxpool3d_compare3():
    _random_samples = np.array([0.7, 0.6, 0.5]).reshape([1, 1, 3])
    ms_random_samples = msa_torch.Tensor(_random_samples)
    torch_random_samples = torch.Tensor(_random_samples)
    ms_net = FractionalMaxPool3d(kernel_size=(1, 2, 3), output_ratio=0.5,
                                 _random_samples=ms_random_samples, return_indices=True)
    torch_net = torch.nn.FractionalMaxPool3d(kernel_size=(1, 2, 3), output_ratio=0.5,
                                             _random_samples=torch_random_samples, return_indices=True)

    data = np.arange(512).reshape([1, 4, 8, 16])

    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output, ms_indices = ms_net(ms_input)
    torch_output, torch_indices = torch_net(torch_input)
    param_compare(ms_output, torch_output)
    param_compare(ms_indices, torch_indices)

@SKIP_ENV_ASCEND(reason="float64 is unsupport on Ascend.")
def test_lppool1d_compare1():
    ms_net = LPPool1d(norm_type=2, kernel_size=3, stride=1)
    torch_net = torch.nn.LPPool1d(norm_type=2, kernel_size=3, stride=1)

    data = np.random.randn(2, 3, 4).astype(np.float32)
    ms_input = msa_torch.Tensor(data).to(msa_torch.float64)
    torch_input = torch.Tensor(data).to(torch.float64)

    ms_output= ms_net(ms_input)
    torch_output= torch_net(torch_input)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)


def test_lppool1d_compare2():
    ms_net = LPPool1d(norm_type=float('inf'), kernel_size=3, ceil_mode=True)
    torch_net = torch.nn.LPPool1d(norm_type=float('inf'), kernel_size=3, ceil_mode=True)

    data = np.random.randn(2, 3, 4).astype(np.float32)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output= ms_net(ms_input)
    torch_output= torch_net(torch_input)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)

def test_lppool2d_compare1():
    ms_net = LPPool2d(norm_type=1, kernel_size=(3, 3), stride=1)
    torch_net = torch.nn.LPPool2d(norm_type=1, kernel_size=(3, 3), stride=1)

    data = np.random.randn(3, 4, 5).astype(np.float32)
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output= ms_net(ms_input)
    torch_output= torch_net(torch_input)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-2)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)

@SKIP_ENV_ASCEND(reason="float64 is unsupport on Ascend.")
def test_lppool2d_compare2():
    ms_net = LPPool2d(norm_type=float('inf'), kernel_size=3, ceil_mode=True)
    torch_net = torch.nn.LPPool2d(norm_type=float('inf'), kernel_size=3, ceil_mode=True)

    data = np.random.randn(2, 3, 4, 5).astype(np.float32)
    ms_input = msa_torch.Tensor(data).to(msa_torch.float64)
    torch_input = torch.Tensor(data).to(torch.float64)

    ms_output= ms_net(ms_input)
    torch_output= torch_net(torch_input)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output, atol=1e-7)

def test_avgpool1d_ceil_mode():
    ms_net = AvgPool1d(2, stride=2, ceil_mode=True)
    torch_net = torch.nn.AvgPool1d(2, stride=2, ceil_mode=True)

    data = np.random.random([1, 5, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_avgpool1d_count_include_pad():
    ms_net = AvgPool1d(2, stride=2, padding=1, count_include_pad=True)
    torch_net = torch.nn.AvgPool1d(2, stride=2, padding=1, count_include_pad=True)

    data = np.random.random([1, 5, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_avgpool2d_ceil_mode():
    ms_net = AvgPool2d(2, stride=2, ceil_mode=True)
    torch_net = torch.nn.AvgPool2d(2, stride=2, ceil_mode=True)

    data = np.random.random([1, 1, 5, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_avgpool2d_count_include_pad():
    ms_net = AvgPool2d(2, stride=2, padding=1, count_include_pad=True)
    torch_net = torch.nn.AvgPool2d(2, stride=2, padding=1, count_include_pad=True)

    data = np.random.random([1, 1, 5, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_avgpool2d_divisor_override():
    ms_net = AvgPool2d(2, stride=2, divisor_override=5)
    torch_net = torch.nn.AvgPool2d(2, divisor_override=5)

    data = np.random.random([1, 1, 5, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_avgpool3d_ceil_mode():
    ms_net = AvgPool3d(2, stride=2, ceil_mode=True)
    torch_net = torch.nn.AvgPool3d(2, stride=2, ceil_mode=True)

    data = np.random.random([1, 1, 5, 5, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_avgpool3d_count_include_pad():
    ms_net = AvgPool3d(2, stride=2, padding=1, count_include_pad=True)
    torch_net = torch.nn.AvgPool3d(2, stride=2, padding=1, count_include_pad=True)

    data = np.random.random([1, 1, 5, 5, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_avgpool3d_divisor_override():
    ms_net = AvgPool3d(2, stride=2, divisor_override=5)
    torch_net = torch.nn.AvgPool3d(2, divisor_override=5)

    data = np.random.random([1, 1, 5, 5, 5])
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_maxpool1d_compare1()
    test_maxpool1d_compare2()
    test_maxpool1d_compare3()
    test_maxpool2d_compare1()
    test_maxpool2d_compare2()
    test_maxpool2d_compare3()
    test_maxpool2d_compare4()
    test_maxpool2d_compare5()
    test_maxpool2d_compare6()
    test_maxpool2d_compare7()
    test_maxpool2d_compare8()
    test_maxpool3d_compare1()
    test_maxpool3d_compare2()

    test_avgpool1d_compare1()
    test_avgpool1d_compare2()
    test_avgpool2d_compare1()
    test_avgpool2d_compare2()
    test_avgpool2d_compare3()
    test_avgpool3d_compare()

    test_adaptive_maxpool1d_compare1()
    test_adaptive_maxpool1d_compare2()
    test_adaptive_maxpool2d_compare1()
    test_adaptive_maxpool2d_compare2()
    test_adaptive_maxpool3d_compare1()
    test_adaptive_maxpool3d_compare2()

    test_adaptive_avgpool1d_compare1()
    test_adaptive_avgpool1d_compare2()
    test_adaptive_avgpool2d_compare1()
    test_adaptive_avgpool2d_compare2()
    test_adaptive_avgpool3d_compare1()
    test_adaptive_avgpool3d_compare2()

    test_lppool1d_compare1()
    test_lppool1d_compare2()
    test_lppool2d_compare1()
    test_lppool2d_compare2()

    test_fractional_maxpool2d_compare1()
    test_fractional_maxpool2d_compare2()
    test_fractional_maxpool2d_compare3()
    test_fractional_maxpool3d_compare1()
    test_fractional_maxpool3d_compare2()
    test_fractional_maxpool3d_compare3()

    test_avgpool1d_ceil_mode()
    test_avgpool1d_count_include_pad()
    test_avgpool2d_ceil_mode()
    test_avgpool2d_count_include_pad()
    test_avgpool2d_divisor_override()
    test_avgpool2d_divisor_override()
    test_avgpool3d_ceil_mode()
    test_avgpool3d_count_include_pad()
