import numpy as np
import torch
import mindspore as ms
from mindspore import context

import mindtorch.torch as ms_pytorch

from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_GPU
set_mode_by_env_config()


def test_constant_pad_1d():
    padding = 3
    value = 3.5
    pt_input_2d = torch.ones(2, 3)
    pt_pad_fun1 = torch.nn.ConstantPad1d(padding, value)
    pt_pad_out1 = pt_pad_fun1(pt_input_2d)
    ms_input_2d = ms_pytorch.ones(2, 3)
    ms_pad_fun1 = ms_pytorch.nn.ConstantPad1d(padding, value)
    ms_pad_out1 = ms_pad_fun1(ms_input_2d)
    param_compare(pt_pad_out1, ms_pad_out1)

    padding = (3, 1)
    value = 2.0
    pt_input_3d = torch.ones(2, 3, 4)
    pt_pad_fun2 = torch.nn.ConstantPad1d(padding, value)
    pt_pad_out2 = pt_pad_fun2(pt_input_3d)
    ms_input_3d = ms_pytorch.ones(2, 3, 4)
    ms_pad_fun2 = ms_pytorch.nn.ConstantPad1d(padding, value)
    ms_pad_out2 = ms_pad_fun2(ms_input_3d)
    param_compare(pt_pad_out2, ms_pad_out2)


def test_constant_pad_2d():
    padding = 2
    value = 2.5
    pt_input_3d = torch.ones(2, 3, 4)
    pt_pad_fun1 = torch.nn.ConstantPad2d(padding, value)
    pt_pad_out1 = pt_pad_fun1(pt_input_3d)
    ms_input_3d = ms_pytorch.ones(2, 3, 4)
    ms_pad_fun1 = ms_pytorch.nn.ConstantPad2d(padding, value)
    ms_pad_out1 = ms_pad_fun1(ms_input_3d)
    param_compare(pt_pad_out1, ms_pad_out1)

@SKIP_ENV_GPU(reason="For PadV3 GPU, the max pad dim only support 6.")
def test_constant_pad_2d_4d_padding():
    padding = (-1, 1, 0, 1, 0, 1, 0, 1)
    value = 2.0
    pt_input_4d = torch.ones(2, 2, 3, 4)
    pt_pad_fun2 = torch.nn.ConstantPad2d(padding, value)
    pt_pad_out2 = pt_pad_fun2(pt_input_4d)
    ms_input_4d = ms_pytorch.ones(2, 2, 3, 4)
    ms_pad_fun2 = ms_pytorch.nn.ConstantPad2d(padding, value)
    ms_pad_out2 = ms_pad_fun2(ms_input_4d)
    param_compare(pt_pad_out2, ms_pad_out2)


def test_constant_pad_3d():
    padding = 1
    value = 2.5
    pt_input_4d = torch.ones(2, 1, 3, 4)
    pt_pad_fun1 = torch.nn.ConstantPad3d(padding, value)
    pt_pad_out1 = pt_pad_fun1(pt_input_4d)
    ms_input_4d = ms_pytorch.ones(2, 1, 3, 4)
    ms_pad_fun1 = ms_pytorch.nn.ConstantPad3d(padding, value)
    ms_pad_out1 = ms_pad_fun1(ms_input_4d)
    param_compare(pt_pad_out1, ms_pad_out1)

    padding = (3, 3, 6, 6, 0, 1)
    value = 2.0
    pt_input_5d = torch.ones(1, 2, 1, 3, 4)
    pt_pad_fun2 = torch.nn.ConstantPad3d(padding, value)
    pt_pad_out2 = pt_pad_fun2(pt_input_5d)
    ms_input_5d = ms_pytorch.ones(1, 2, 1, 3, 4)
    ms_pad_fun2 = ms_pytorch.nn.ConstantPad3d(padding, value)
    ms_pad_out2 = ms_pad_fun2(ms_input_5d)
    param_compare(pt_pad_out2, ms_pad_out2)


def test_reflection_pad_1d():
    padding = 3
    np_input_2d = np.random.rand(2, 6)
    pt_input_2d = torch.tensor(np_input_2d)
    pt_pad_fun1 = torch.nn.ReflectionPad1d(padding)
    pt_pad_out1 = pt_pad_fun1(pt_input_2d)
    ms_input_2d = ms_pytorch.tensor(np_input_2d)
    ms_pad_fun1 = ms_pytorch.nn.ReflectionPad1d(padding)
    ms_pad_out1 = ms_pad_fun1(ms_input_2d)
    param_compare(pt_pad_out1, ms_pad_out1)

    padding = (-2, 1)
    np_3d_input = np.random.rand(2, 3, 4)
    pt_input_3d = torch.tensor(np_3d_input)
    pt_pad_fun2 = torch.nn.ReflectionPad1d(padding)
    pt_pad_out2 = pt_pad_fun2(pt_input_3d)
    ms_input_3d = ms_pytorch.tensor(np_3d_input)
    ms_pad_fun2 = ms_pytorch.nn.ReflectionPad1d(padding)
    ms_pad_out2 = ms_pad_fun2(ms_input_3d)
    param_compare(pt_pad_out2, ms_pad_out2)


def test_reflection_pad_2d():
    padding = 2
    np_input_3d = np.random.rand(2, 4, 3)
    pt_input_3d = torch.tensor(np_input_3d)
    pt_pad_fun1 = torch.nn.ReflectionPad2d(padding)
    pt_pad_out1 = pt_pad_fun1(pt_input_3d)
    ms_input_3d = ms_pytorch.tensor(np_input_3d)
    ms_pad_fun1 = ms_pytorch.nn.ReflectionPad2d(padding)
    ms_pad_out1 = ms_pad_fun1(ms_input_3d)
    param_compare(pt_pad_out1, ms_pad_out1)

    padding = (1, 1, -2, 0)
    np_input_4d = np.random.rand(2, 2, 3, 4)
    pt_input_4d = torch.tensor(np_input_4d)
    pt_pad_fun2 = torch.nn.ReflectionPad2d(padding)
    pt_pad_out2 = pt_pad_fun2(pt_input_4d)
    ms_input_4d = ms_pytorch.tensor(np_input_4d)
    ms_pad_fun2 = ms_pytorch.nn.ReflectionPad2d(padding)
    ms_pad_out2 = ms_pad_fun2(ms_input_4d)
    param_compare(pt_pad_out2, ms_pad_out2)


def test_reflection_pad_3d():
    padding = 2
    np_input_4d = np.random.rand(2, 3, 3, 4)
    pt_input_4d = torch.tensor(np_input_4d)
    pt_pad_fun1 = torch.nn.ReflectionPad3d(padding)
    pt_pad_out1 = pt_pad_fun1(pt_input_4d)
    ms_input_4d = ms_pytorch.tensor(np_input_4d)
    ms_pad_fun1 = ms_pytorch.nn.ReflectionPad3d(padding)
    ms_pad_out1 = ms_pad_fun1(ms_input_4d)
    param_compare(pt_pad_out1, ms_pad_out1)

    padding = (1, 1, 2, 0, 3, 2)
    np_input_5d = np.random.rand(2, 3, 6, 4, 5)
    pt_input_5d = torch.tensor(np_input_5d)
    pt_pad_fun2 = torch.nn.ReflectionPad3d(padding)
    pt_pad_out2 = pt_pad_fun2(pt_input_5d)
    ms_input_5d = ms_pytorch.tensor(np_input_5d)
    ms_pad_fun2 = ms_pytorch.nn.ReflectionPad3d(padding)
    ms_pad_out2 = ms_pad_fun2(ms_input_5d)
    param_compare(pt_pad_out2, ms_pad_out2)


def test_zero_pad_2d():
    padding = 2
    pt_input_3d = torch.ones(1, 3, 3)
    pt_pad_fun1 = torch.nn.ZeroPad2d(padding)
    pt_pad_out1 = pt_pad_fun1(pt_input_3d)
    ms_input_3d = ms_pytorch.ones(1, 3, 3)
    ms_pad_fun1 = ms_pytorch.nn.ZeroPad2d(padding)
    ms_pad_out1 = ms_pad_fun1(ms_input_3d)
    param_compare(pt_pad_out1, ms_pad_out1)

    padding = (1, 1, 2, 0)
    pt_input_4d = torch.ones(1, 1, 3, 3)
    pt_pad_fun2 = torch.nn.ZeroPad2d(padding)
    pt_pad_out2 = pt_pad_fun2(pt_input_4d)
    ms_input_4d = ms_pytorch.ones(1, 1, 3, 3)
    ms_pad_fun2 = ms_pytorch.nn.ZeroPad2d(padding)
    ms_pad_out2 = ms_pad_fun2(ms_input_4d)
    param_compare(pt_pad_out2, ms_pad_out2)

    padding = [1, 1, 2, 0]
    pt_input_4d = torch.ones(1, 1, 3, 3)
    pt_pad_fun2 = torch.nn.ZeroPad2d(padding)
    pt_pad_out2 = pt_pad_fun2(pt_input_4d)
    ms_input_4d = ms_pytorch.ones(1, 1, 3, 3)
    ms_pad_fun2 = ms_pytorch.nn.ZeroPad2d(padding)
    ms_pad_out2 = ms_pad_fun2(ms_input_4d)
    param_compare(pt_pad_out2, ms_pad_out2)

def test_replication_pad_1d():
    padding1 = 3
    np_input_2d = np.random.rand(2, 2)
    pt_input_2d = torch.tensor(np_input_2d)
    ms_input_2d = ms_pytorch.tensor(np_input_2d)
    pt_pad_fun1 = torch.nn.ReplicationPad1d(padding1)
    ms_pad_fun1 = ms_pytorch.nn.ReplicationPad1d(padding1)
    pt_pad_out1 = pt_pad_fun1(pt_input_2d)
    ms_pad_out1 = ms_pad_fun1(ms_input_2d)
    param_compare(pt_pad_out1, ms_pad_out1)

    padding2 = (2, 1)
    np_input_3d = np.random.rand(2, 3, 3)
    pt_input_3d = torch.tensor(np_input_3d)
    ms_input_3d = ms_pytorch.tensor(np_input_3d)
    pt_pad_fun2 = torch.nn.ReplicationPad1d(padding2)
    pt_pad_out2 = pt_pad_fun2(pt_input_3d)
    ms_pad_fun2 = ms_pytorch.nn.ReplicationPad1d(padding2)
    ms_pad_out2 = ms_pad_fun2(ms_input_3d)
    param_compare(pt_pad_out2, ms_pad_out2)


def test_replication_pad_2d():
    padding1 = 3
    np_input_3d = np.random.rand(2, 2, 3)
    pt_input_3d = torch.tensor(np_input_3d)
    ms_input_3d = ms_pytorch.tensor(np_input_3d)
    pt_pad_fun1 = torch.nn.ReplicationPad2d(padding1)
    ms_pad_fun1 = ms_pytorch.nn.ReplicationPad2d(padding1)
    pt_pad_out1 = pt_pad_fun1(pt_input_3d)
    ms_pad_out1 = ms_pad_fun1(ms_input_3d)
    param_compare(pt_pad_out1, ms_pad_out1)

    padding2 = (2, 1, 1, 2, 1, 2)
    np_input_4d = np.random.rand(2, 3, 2, 3)
    pt_input_4d = torch.tensor(np_input_4d)
    ms_input_4d = ms_pytorch.tensor(np_input_4d)
    pt_pad_fun2 = torch.nn.ReplicationPad2d(padding2)
    pt_pad_out2 = pt_pad_fun2(pt_input_4d)
    ms_pad_fun2 = ms_pytorch.nn.ReplicationPad2d(padding2)
    ms_pad_out2 = ms_pad_fun2(ms_input_4d)
    param_compare(pt_pad_out2, ms_pad_out2)


def test_replication_pad_3d():
    padding1 = 3
    np_input_4d = np.random.rand(2, 5, 7, 3)
    pt_input_4d = torch.tensor(np_input_4d)
    ms_input_4d = ms_pytorch.tensor(np_input_4d)

    pt_pad_fun1 = torch.nn.ReplicationPad3d(padding1)
    ms_pad_fun1 = ms_pytorch.nn.ReplicationPad3d(padding1)
    pt_pad_out1 = pt_pad_fun1(pt_input_4d)
    ms_pad_out1 = ms_pad_fun1(ms_input_4d)
    param_compare(pt_pad_out1, ms_pad_out1)

    padding2 = (2, 1, 1, 2, 3, 2)
    np_input_5d = np.random.rand(2, 5, 2, 7, 3)
    pt_input_5d = torch.tensor(np_input_5d)
    ms_input_5d = ms_pytorch.tensor(np_input_5d)
    pt_pad_fun2 = torch.nn.ReplicationPad3d(padding2)
    pt_pad_out2 = pt_pad_fun2(pt_input_5d)
    ms_pad_fun2 = ms_pytorch.nn.ReplicationPad3d(padding2)
    ms_pad_out2 = ms_pad_fun2(ms_input_5d)
    param_compare(pt_pad_out2, ms_pad_out2)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_constant_pad_1d()
    test_constant_pad_2d()
    test_constant_pad_3d()
    test_reflection_pad_1d()
    test_reflection_pad_2d()
    test_reflection_pad_3d()
    test_zero_pad_2d()
    test_replication_pad_1d()
    test_replication_pad_2d()
    test_replication_pad_3d()
