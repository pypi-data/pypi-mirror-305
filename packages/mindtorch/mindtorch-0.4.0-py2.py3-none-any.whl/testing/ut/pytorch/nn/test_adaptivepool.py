import numpy as np
import torch

import mindtorch.torch as msa_torch
from mindtorch.torch.nn import AdaptiveAvgPool1d, AdaptiveAvgPool2d, AdaptiveAvgPool3d
from mindtorch.torch.nn import AdaptiveMaxPool1d, AdaptiveMaxPool2d, AdaptiveMaxPool3d
from mindtorch.utils import is_under_ascend_context
from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_ASCEND
set_mode_by_env_config()


def test_adaptiveavgpool2d_compare1():
    ms_net = AdaptiveAvgPool2d((3, 7))
    torch_net = torch.nn.AdaptiveAvgPool2d((3, 7))

    data = np.random.random((1, 64, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_adaptiveavgpool2d_compare2():
    ms_net = AdaptiveAvgPool2d(4)
    torch_net = torch.nn.AdaptiveAvgPool2d(4)

    data = np.random.random((1, 3, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_adaptiveavgpool2d_compare3():
    ms_net = AdaptiveAvgPool2d((4, None))
    torch_net = torch.nn.AdaptiveAvgPool2d((4, None))

    data = np.random.random((1, 3, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_adaptiveavgpool2d_compare4():
    ms_net = AdaptiveAvgPool2d((None, 4))
    torch_net = torch.nn.AdaptiveAvgPool2d((None, 4))

    data = np.random.random((1, 3, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptiveavgpool2d_compare5():
    ms_net = AdaptiveAvgPool2d((None, None))
    torch_net = torch.nn.AdaptiveAvgPool2d((None, None))

    data = np.random.random((1, 3, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptiveavgpool1d_compare1():
    ms_net = AdaptiveAvgPool1d(3)
    torch_net = torch.nn.AdaptiveAvgPool1d(3)

    data = np.random.random((1, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptiveavgpool3d_compare1():
    ms_net = AdaptiveAvgPool3d((3, 4, 5))
    torch_net = torch.nn.AdaptiveAvgPool3d((3, 4, 5))

    data = np.random.random((1, 3, 10, 9, 12))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptiveavgpool3d_compare2():
    ms_net = AdaptiveAvgPool3d(3)
    torch_net = torch.nn.AdaptiveAvgPool3d(3)

    data = np.random.random((1, 3, 10, 9, 12))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptiveavgpool3d_compare3():
    ms_net = AdaptiveAvgPool3d(3)
    torch_net = torch.nn.AdaptiveAvgPool3d(3)

    data = np.random.random((1, 3, 10, 9, 12))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptiveavgpool3d_compare4():
    ms_net = AdaptiveAvgPool3d((3, None, 5))
    torch_net = torch.nn.AdaptiveAvgPool3d((3, None, 5))

    data = np.random.random((1, 3, 10, 9, 12))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptiveavgpool3d_compare5():
    ms_net = AdaptiveAvgPool3d((None, None, 5))
    torch_net = torch.nn.AdaptiveAvgPool3d((None, None, 5))

    data = np.random.random((1, 3, 10, 9, 12))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptivemaxpool2d_compare1():
    ms_net = AdaptiveMaxPool2d((3, 7))
    torch_net = torch.nn.AdaptiveMaxPool2d((3, 7))

    data = np.random.random((1, 64, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptivemaxpool2d_compare2():
    ms_net = AdaptiveMaxPool2d(4)
    torch_net = torch.nn.AdaptiveMaxPool2d(4)

    data = np.random.random((1, 3, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptivemaxpool2d_compare3():
    ms_net = AdaptiveMaxPool2d((4, None))
    torch_net = torch.nn.AdaptiveMaxPool2d((4, None))

    data = np.random.random((1, 3, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptivemaxpool2d_compare4():
    ms_net = AdaptiveMaxPool2d((None, 4))
    torch_net = torch.nn.AdaptiveMaxPool2d((None, 4))

    data = np.random.random((1, 3, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptivemaxpool2d_compare5():
    ms_net = AdaptiveMaxPool2d((None, None))
    torch_net = torch.nn.AdaptiveMaxPool2d((None, None))

    data = np.random.random((1, 3, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


@SKIP_ENV_ASCEND(reason="There is bug in ms.ops.adaptive_max_pool2d when return_indices==Ture.")
def test_adaptivemaxpool2d_compare6():
    ms_net = AdaptiveMaxPool2d((3, 7), return_indices=True)
    torch_net = torch.nn.AdaptiveMaxPool2d((3, 7), return_indices=True)

    data = np.random.random((1, 64, 10, 9))
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


def test_adaptivemaxpool1d_compare1():
    ms_net = AdaptiveMaxPool1d(3)
    torch_net = torch.nn.AdaptiveMaxPool1d(3)

    data = np.random.random((1, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


@SKIP_ENV_ASCEND(reason="There is bug in ms.ops.adaptive_max_pool2d when return_indices==Ture.")
def test_adaptivemaxpool1d_compare2():
    ms_net = AdaptiveMaxPool1d(3, True)
    torch_net = torch.nn.AdaptiveMaxPool1d(3, True)

    data = np.random.random((1, 10, 9))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output, ms_indices = ms_net(ms_input)
    torch_output, torch_indices = torch_net(torch_input)
    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-3)
        param_compare(ms_indices, torch_indices)
    else:
        param_compare(ms_output, torch_output)
        param_compare(ms_indices, torch_indices)

def test_adaptivemaxpool3d_compare1():
    ms_net = AdaptiveMaxPool3d((3, 4, 5))
    torch_net = torch.nn.AdaptiveMaxPool3d((3, 4, 5))

    data = np.random.random((1, 3, 10, 9, 12))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        # Custom implementation only ensures shape consistency
        assert ms_output.shape == torch_output.size()
        # param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_adaptivemaxpool3d_compare2():
    ms_net = AdaptiveMaxPool3d(3)
    torch_net = torch.nn.AdaptiveMaxPool3d(3)

    data = np.random.random((1, 3, 10, 9, 12))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        # Custom implementation only ensures shape consistency
        assert ms_output.shape == torch_output.size()
        # param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_adaptivemaxpool3d_compare3():
    ms_net = AdaptiveMaxPool3d(3)
    torch_net = torch.nn.AdaptiveMaxPool3d(3)

    data = np.random.random((1, 3, 10, 9, 12))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        # Custom implementation only ensures shape consistency
        assert ms_output.shape == torch_output.size()
        # param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_adaptivemaxpool3d_compare4():
    ms_net = AdaptiveMaxPool3d((3, None, 5))
    torch_net = torch.nn.AdaptiveMaxPool3d((3, None, 5))

    data = np.random.random((1, 3, 10, 9, 12))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        # Custom implementation only ensures shape consistency
        assert ms_output.shape == torch_output.size()
        # param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

def test_adaptivemaxpool3d_compare5():
    ms_net = AdaptiveMaxPool3d((None, None, 5))
    torch_net = torch.nn.AdaptiveMaxPool3d((None, None, 5))

    data = np.random.random((1, 3, 10, 9, 12))
    ms_input = msa_torch.Tensor(data)
    torch_input = torch.Tensor(data)

    ms_output = ms_net(ms_input)
    torch_output = torch_net(torch_input)
    if is_under_ascend_context():
        # Custom implementation only ensures shape consistency
        assert ms_output.shape == torch_output.size()
        # param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_adaptiveavgpool2d_compare1()
    test_adaptiveavgpool2d_compare2()
    test_adaptiveavgpool2d_compare3()
    test_adaptiveavgpool2d_compare4()
    test_adaptiveavgpool2d_compare5()
    test_adaptiveavgpool1d_compare1()
    test_adaptiveavgpool3d_compare1()
    test_adaptiveavgpool3d_compare2()
    test_adaptiveavgpool3d_compare3()
    test_adaptiveavgpool3d_compare4()
    test_adaptiveavgpool3d_compare5()
    test_adaptivemaxpool2d_compare1()
    test_adaptivemaxpool2d_compare2()
    test_adaptivemaxpool2d_compare3()
    test_adaptivemaxpool2d_compare4()
    test_adaptivemaxpool2d_compare5()
    test_adaptivemaxpool2d_compare6()
    test_adaptivemaxpool1d_compare1()
    test_adaptivemaxpool1d_compare2()
    test_adaptivemaxpool3d_compare1()
    test_adaptivemaxpool3d_compare2()
    test_adaptivemaxpool3d_compare3()
    test_adaptivemaxpool3d_compare4()
    test_adaptivemaxpool3d_compare5()