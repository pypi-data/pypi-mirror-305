#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import torch

from mindspore import context
import mindspore as ms

import mindtorch

from mindtorch.torch.nn import Module
from mindtorch.torch.nn import BatchNorm1d, BatchNorm2d, BatchNorm3d
from mindtorch.torch.nn import SyncBatchNorm, InstanceNorm1d, InstanceNorm2d, InstanceNorm3d
from mindtorch.torch import tensor

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, SKIP_ENV_ASCEND, SKIP_ENV_CPU, param_compare
set_mode_by_env_config()


def test_bn():
    class BnModel1d(Module):
        def __init__(self):
            super(BnModel1d, self).__init__()
            self.bn1 = BatchNorm1d(num_features=4)
            self.bn2 = BatchNorm1d(4, affine=False)

        def forward(self, inputs):
            x = self.bn1(inputs)
            x = self.bn2(x)
            return x

    class BnModel2d(Module):
        def __init__(self):
            super(BnModel2d, self).__init__()
            self.bn1 = BatchNorm2d(num_features=4)
            self.bn2 = BatchNorm2d(4, affine=False)

        def forward(self, inputs):
            x = self.bn1(inputs)
            x = self.bn2(x)
            return x

    class BnModel3d(Module):
        def __init__(self):
            super(BnModel3d, self).__init__()
            self.bn1 = BatchNorm3d(num_features=4)
            self.bn2 = BatchNorm3d(4, affine=False)

        def forward(self, inputs):
            x = self.bn1(inputs)
            x = self.bn2(x)
            return x

    model1d = BnModel1d()
    model2d = BnModel2d()
    model3d = BnModel3d()

    inputs1d = tensor(np.ones(shape=(5, 4)), ms.float32)
    output1d = model1d(inputs1d)
    assert output1d.shape == (5, 4)

    # 3D testcase
    inputs1d = tensor(np.ones(shape=(5, 4, 2)), ms.float32)
    output1d = model1d(inputs1d)
    assert output1d.shape == (5, 4, 2)

    inputs2d = tensor(np.ones(shape=(5, 4, 5, 5)), ms.float32)
    output2d = model2d(inputs2d)
    assert output2d.shape == (5, 4, 5, 5)

    inputs3d = tensor(np.ones(shape=(5, 4, 5, 5, 5)), ms.float32)
    output3d = model3d(inputs3d)
    assert output3d.shape == (5, 4, 5, 5, 5)

class MSBnModel(Module):
    def __init__(self, mode, num_features, eps, momentum, affine, track_running_stats):
        super(MSBnModel, self).__init__()
        if mode == "2d":
            self.bn = BatchNorm2d(num_features, eps, momentum, affine, track_running_stats)
        elif mode == "3d":
            self.bn = BatchNorm3d(num_features, eps, momentum, affine, track_running_stats)
        else:
            self.bn = BatchNorm1d(num_features, eps, momentum, affine, track_running_stats)

    def forward(self, inputs):
        x = self.bn(inputs)
        x = self.bn(x)
        return x

class PTBnModel(torch.nn.Module):
    def __init__(self, mode, num_features, eps, momentum, affine, track_running_stats):
        super(PTBnModel, self).__init__()
        if mode == "2d":
            self.bn = torch.nn.BatchNorm2d(num_features, eps, momentum, affine, track_running_stats)
        elif mode == "3d":
            self.bn = torch.nn.BatchNorm3d(num_features, eps, momentum, affine, track_running_stats)
        else:
            self.bn = torch.nn.BatchNorm1d(num_features, eps, momentum, affine, track_running_stats)


    def forward(self, inputs):
        x = self.bn(inputs)
        x = self.bn(x)
        return x

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: when input is 2D, ms.ops.BatchNorm sequential result not correct.")
def test_bn1d_momentum():
    input = np.arange(5 * 3).reshape(5, 3).astype(np.float32)
    pt_model = PTBnModel("1d", 3, 1e-5, 0.1, True, True)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("1d", 3, 1e-5, 0.1, True, True)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)

    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: when input is 2D, ms.ops.BatchNorm sequential result not correct.")
def test_bn1d_affine():
    input = np.arange(5 * 3).reshape(5, 3).astype(np.float32)
    pt_model = PTBnModel("1d", 3, 1e-5, 0.1, False, True)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("1d", 3, 1e-5, 0.1, False, True)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)

    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: when input is 2D, ms.ops.BatchNorm sequential result not correct.")
def test_bn1d_train():
    input = np.arange(5 * 3).reshape(5, 3).astype(np.float32)
    pt_model = PTBnModel("1d", 3, 1e-5, 0.1, False, True)
    pt_model.train(mode=False)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("1d", 3, 1e-5, 0.1, False, True)
    ms_model.train(mode=False)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)

    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())

    np.random.seed(123)
    input2 = np.random.randn(5, 3).astype(np.float32)
    pt_input2 = torch.Tensor(input2)
    ms_inputs2 = mindtorch.torch.Tensor(input2)
    pt_output2 = pt_model(pt_input2)
    ms_output2 = ms_model(ms_inputs2)

    assert np.allclose(ms_output2.asnumpy(), pt_output2.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: when input is 2D, ms.ops.BatchNorm sequential result not correct.")
def test_bn1d_track_running_stats():
    input = np.arange(5 * 3).reshape(5, 3).astype(np.float32)
    pt_model = PTBnModel("1d", 3, 1e-5, 0.5, True, False)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("1d", 3, 1e-5, 0.5, True, False)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)
    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)

    np.random.seed(123)
    input2 = np.random.randn(5, 3).astype(np.float32)
    pt_input2 = torch.Tensor(input2)
    ms_inputs2 = mindtorch.torch.Tensor(input2)
    pt_output2 = pt_model(pt_input2)
    ms_output2 = ms_model(ms_inputs2)

    assert np.allclose(ms_output2.asnumpy(), pt_output2.detach().numpy(), atol=1e-5)

    # 3D testcase
    input3 = np.random.randn(5, 3, 2).astype(np.float32)
    pt_input3 = torch.Tensor(input3)
    ms_inputs3 = mindtorch.torch.Tensor(input3)
    pt_output3 = pt_model(pt_input3)
    ms_output3 = ms_model(ms_inputs3)

    assert np.allclose(ms_output3.asnumpy(), pt_output3.detach().numpy(), atol=1e-5)

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: when input is 2D, ms.ops.BatchNorm sequential result not correct.")
def test_bn1d_train_and_track_running_stats():
    input = np.arange(5 * 3).reshape(5, 3).astype(np.float32)
    pt_model = PTBnModel("1d", 3, 1e-5, 0.5, True, False)
    pt_model.train(mode=False)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("1d", 3, 1e-5, 0.5, True, False)
    ms_model.train(mode=False)

    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)
    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)

    np.random.seed(123)
    input2 = np.random.randn(5, 3).astype(np.float32)
    pt_input2 = torch.Tensor(input2)
    ms_inputs2 = mindtorch.torch.Tensor(input2)
    pt_output2 = pt_model(pt_input2)
    ms_output2 = ms_model(ms_inputs2)
    assert np.allclose(ms_output2.asnumpy(), pt_output2.detach().numpy(), atol=1e-5)

    # 3D testcase
    input3 = np.random.randn(5, 3, 2).astype(np.float32)
    pt_input3 = torch.Tensor(input3)
    ms_inputs3 = mindtorch.torch.Tensor(input3)
    pt_output3 = pt_model(pt_input3)
    ms_output3 = ms_model(ms_inputs3)
    assert np.allclose(ms_output3.asnumpy(), pt_output3.detach().numpy(), atol=1e-5)

def test_bn2d_momentum():
    input = np.arange(5 * 3 * 3 * 3).reshape(5, 3, 3, 3).astype(np.float32)
    pt_model = PTBnModel("2d", 3, 1e-5, 0.1, True, True)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("2d", 3, 1e-5, 0.1, True, True)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)

    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())

def test_bn2d_momentum_int():
    input = np.arange(5 * 3 * 3 * 3).reshape(5, 3, 3, 3).astype(np.float32)
    pt_model = PTBnModel("2d", 3, 1e-5, 1, True, True)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("2d", 3, 1e-5, 1, True, True)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)

    param_compare(pt_output.detach(), ms_output, atol=1e-5)
    param_compare(ms_model.bn.running_mean, pt_model.bn.running_mean, atol=1e-5)

def test_bn2d_affine():
    input = np.arange(5 * 3 * 3 * 3).reshape(5, 3, 3, 3).astype(np.float32)
    pt_model = PTBnModel("2d", 3, 1e-5, 0.1, False, True)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("2d", 3, 1e-5, 0.1, False, True)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)

    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())

def test_bn2d_train():
    input = np.arange(5 * 3 * 3 * 3).reshape(5, 3, 3, 3).astype(np.float32)
    pt_model = PTBnModel("2d", 3, 1e-5, 0.1, False, True)
    pt_model.train(mode=False)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("2d", 3, 1e-5, 0.1, False, True)
    ms_model.train(mode=False)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)

    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())

    np.random.seed(123)
    input2 = np.random.randn(5, 3, 3, 3).astype(np.float32)
    pt_input2 = torch.Tensor(input2)
    ms_inputs2 = mindtorch.torch.Tensor(input2)
    pt_output2 = pt_model(pt_input2)
    ms_output2 = ms_model(ms_inputs2)

    assert np.allclose(ms_output2.asnumpy(), pt_output2.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())

def test_bn2d_track_running_stats():
    input = np.arange(5 * 3 * 3 * 3).reshape(5, 3, 3, 3).astype(np.float32)
    pt_model = PTBnModel("2d", 3, 1e-5, 0.1, False, False)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("2d", 3, 1e-5, 0.1, False, False)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)
    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)

    np.random.seed(123)
    input2 = np.random.randn(5, 3, 3, 3).astype(np.float32)
    pt_input2 = torch.Tensor(input2)
    ms_inputs2 = mindtorch.torch.Tensor(input2)
    pt_output2 = pt_model(pt_input2)
    ms_output2 = ms_model(ms_inputs2)
    assert np.allclose(ms_output2.asnumpy(), pt_output2.detach().numpy(), atol=1e-5)

def test_bn2d_train_and_track_running_stats():
    input = np.arange(5 * 3 * 3 * 3).reshape(5, 3, 3, 3).astype(np.float32)
    pt_model = PTBnModel("2d", 3, 1e-5, 0.1, True, False)
    pt_model.train(mode=False)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("2d", 3, 1e-5, 0.1, True, False)
    ms_model.train(mode=False)

    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)
    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)

    np.random.seed(123)
    input2 = np.random.randn(5, 3, 3, 3).astype(np.float32)
    pt_input2 = torch.Tensor(input2)
    ms_inputs2 = mindtorch.torch.Tensor(input2)
    pt_output2 = pt_model(pt_input2)
    ms_output2 = ms_model(ms_inputs2)
    assert np.allclose(ms_output2.asnumpy(), pt_output2.detach().numpy(), atol=1e-5)

def test_bn3d_momentum():
    input = np.arange(5 * 3 * 3 * 3 * 3).reshape(5, 3, 3, 3, 3).astype(np.float32)
    pt_model = PTBnModel("3d", 3, 1e-5, 0.1, True, True)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("3d", 3, 1e-5, 0.1, True, True)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)

    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())

def test_bn3d_affine():
    input = np.arange(5 * 3 * 3 * 3 * 3).reshape(5, 3, 3, 3, 3).astype(np.float32)
    pt_model = PTBnModel("3d", 3, 1e-5, 0.1, False, True)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("3d", 3, 1e-5, 0.1, False, True)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)

    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())

def test_bn3d_train():
    input = np.arange(5 * 3 * 3 * 3 * 3).reshape(5, 3, 3, 3, 3).astype(np.float32)
    pt_model = PTBnModel("3d", 3, 1e-5, 0.1, False, True)
    pt_model.train(mode=False)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("3d", 3, 1e-5, 0.1, False, True)
    ms_model.train(mode=False)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)

    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())

    np.random.seed(123)
    input2 = np.random.randn(5, 3, 3, 3, 3).astype(np.float32)
    pt_input2 = torch.Tensor(input2)
    ms_inputs2 = mindtorch.torch.Tensor(input2)
    pt_output2 = pt_model(pt_input2)
    ms_output2 = ms_model(ms_inputs2)

    assert np.allclose(ms_output2.asnumpy(), pt_output2.detach().numpy(), atol=1e-5)
    assert np.allclose(ms_model.bn.running_mean.asnumpy(), pt_model.bn.running_mean.numpy())


def test_bn3d_track_running_stats():
    input = np.arange(5 * 3 * 3 * 3 * 3).reshape(5, 3, 3, 3, 3).astype(np.float32)
    pt_model = PTBnModel("3d", 3, 1e-5, 0.1, False, False)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("3d", 3, 1e-5, 0.1, False, False)
    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)
    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)

    np.random.seed(123)
    input2 = np.random.randn(5, 3, 3, 3, 3).astype(np.float32)
    pt_input2 = torch.Tensor(input2)
    ms_inputs2 = mindtorch.torch.Tensor(input2)
    pt_output2 = pt_model(pt_input2)
    ms_output2 = ms_model(ms_inputs2)
    assert np.allclose(ms_output2.asnumpy(), pt_output2.detach().numpy(), atol=1e-5)

def test_bn3d_train_and_track_running_stats():
    input = np.arange(5 * 3 * 3 * 3 * 3).reshape(5, 3, 3, 3, 3).astype(np.float32)
    pt_model = PTBnModel("3d", 3, 1e-5, 0.9, False, False)
    pt_model.train(mode=False)
    pt_input = torch.Tensor(input)
    pt_output = pt_model(pt_input)

    ms_model = MSBnModel("3d", 3, 1e-5, 0.9, False, False)
    ms_model.train(mode=False)

    ms_inputs = mindtorch.torch.Tensor(input)
    ms_output = ms_model(ms_inputs)
    assert np.allclose(ms_output.asnumpy(), pt_output.detach().numpy(), atol=1e-5)

    np.random.seed(123)
    input2 = np.random.randn(5, 3, 3, 3, 3).astype(np.float32)
    pt_input2 = torch.Tensor(input2)
    ms_inputs2 = mindtorch.torch.Tensor(input2)
    pt_output2 = pt_model(pt_input2)
    ms_output2 = ms_model(ms_inputs2)
    assert np.allclose(ms_output2.asnumpy(), pt_output2.detach().numpy(), atol=1e-5)

# def test_sbn_track_runing_status():
#     input = np.arange(5 * 3 * 3 * 3).reshape(5, 3, 3, 3).astype(np.float32)
#     pt_input = torch.Tensor(input)
#     ms_inputs = mindtorch.torch.Tensor(input)
#
#     pt_model = torch.nn.SyncBatchNorm(num_features=10)
#
#     from mindspore.communication import init
#     init()
#     ms.reset_auto_parallel_context()
#     ms.set_auto_parallel_context(parallel_mode=ms.ParallelMode.DATA_PARALLEL)
#     ms_model = SyncBatchNorm(num_features=10)
#
#     pt_output = pt_model(pt_input)
#     ms_output = ms_model(ms_inputs)
#     print(ms_output.asnumpy())
#     print(pt_output.detach().numpy())
#
#
@SKIP_ENV_ASCEND(reason="ms.ops.operations.InstanceNorm not support on Ascend")
@SKIP_ENV_CPU(reason="ms.ops.operations.InstanceNorm not support on CPU")
def test_insn1d_track_runing_status():
    input = np.arange(5 * 3 * 3 ).reshape(5, 3, 3).astype(np.float32)
    pt_input = torch.Tensor(input)
    ms_inputs = mindtorch.torch.Tensor(input)

    pt_model = torch.nn.InstanceNorm1d(num_features=3)
    ms_model = InstanceNorm1d(num_features=3)

    pt_output = pt_model(pt_input)
    ms_output = ms_model(ms_inputs)

    param_compare(pt_output, ms_output, atol=1e-5)

@SKIP_ENV_ASCEND(reason="ms.ops.operations.InstanceNorm not support on Ascend")
@SKIP_ENV_CPU(reason="ms.ops.operations.InstanceNorm not support on CPU")
def test_insn2d_track_runing_status():
    input = np.arange(5 * 3 * 3 *3).reshape(5, 3, 3, 3).astype(np.float32)
    pt_input = torch.Tensor(input)
    ms_inputs = mindtorch.torch.Tensor(input)

    pt_model = torch.nn.InstanceNorm2d(num_features=3)
    ms_model = InstanceNorm2d(num_features=3)

    pt_output = pt_model(pt_input)
    ms_output = ms_model(ms_inputs)

    param_compare(pt_output, ms_output)

@SKIP_ENV_ASCEND(reason="ms.ops.operations.InstanceNorm not support on Ascend")
@SKIP_ENV_CPU(reason="ms.ops.operations.InstanceNorm not support on CPU")
def test_insn3d_track_runing_status():
    input = np.arange(5 * 3 * 3 * 3 * 3).reshape(5, 3, 3, 3, 3).astype(np.float32)
    pt_input = torch.Tensor(input)
    ms_inputs = mindtorch.torch.Tensor(input)

    pt_model = torch.nn.InstanceNorm3d(num_features=3)
    ms_model = InstanceNorm3d(num_features=3)

    pt_output = pt_model(pt_input)
    ms_output = ms_model(ms_inputs)

    param_compare(pt_output, ms_output)

@SKIP_ENV_ASCEND(reason="ms.ops.operations.InstanceNorm not support on Ascend")
@SKIP_ENV_CPU(reason="ms.ops.operations.InstanceNorm not support on CPU")
def test_insn1d_track_runing_status_input_2d():
    input = np.arange(3 * 2).reshape(3, 2).astype(np.float32)
    pt_input = torch.Tensor(input)
    ms_inputs = mindtorch.torch.Tensor(input)

    pt_model = torch.nn.InstanceNorm1d(num_features=3)
    ms_model = InstanceNorm1d(num_features=3)

    pt_output = pt_model(pt_input)
    ms_output = ms_model(ms_inputs)

    param_compare(pt_output, ms_output)

@SKIP_ENV_ASCEND(reason="ms.ops.operations.InstanceNorm not support on Ascend")
@SKIP_ENV_CPU(reason="ms.ops.operations.InstanceNorm not support on CPU")
def test_insn2d_track_runing_status_input_3d():
    input = np.arange(3 * 2 * 2).reshape(3, 2, 2).astype(np.float32)
    pt_input = torch.Tensor(input)
    ms_inputs = mindtorch.torch.Tensor(input)

    pt_model = torch.nn.InstanceNorm2d(num_features=3)
    ms_model = InstanceNorm2d(num_features=3)

    pt_output = pt_model(pt_input)
    ms_output = ms_model(ms_inputs)

    param_compare(pt_output, ms_output)

@SKIP_ENV_ASCEND(reason="ms.ops.operations.InstanceNorm not support on Ascend")
@SKIP_ENV_CPU(reason="ms.ops.operations.InstanceNorm not support on CPU")
def test_insn3d_track_runing_status_input_4d():
    input = np.arange(3 * 2 * 2 * 2).reshape(3, 2, 2, 2).astype(np.float32)
    pt_input = torch.Tensor(input)
    ms_inputs = mindtorch.torch.Tensor(input)

    pt_model = torch.nn.InstanceNorm3d(num_features=3)
    ms_model = InstanceNorm3d(num_features=3)

    pt_output = pt_model(pt_input)
    ms_output = ms_model(ms_inputs)

    param_compare(pt_output, ms_output)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_bn()
    test_bn1d_momentum()
    test_bn1d_affine()
    test_bn1d_train()
    test_bn1d_track_running_stats()
    test_bn1d_train_and_track_running_stats()

    test_bn2d_momentum()
    test_bn2d_affine()
    test_bn2d_train()
    test_bn2d_track_running_stats()
    test_bn2d_train_and_track_running_stats()

    test_bn3d_momentum()
    test_bn3d_affine()
    test_bn3d_train()
    test_bn3d_track_running_stats()
    test_bn3d_train_and_track_running_stats()

    # test_sbn_track_runing_status() # Only Ascend is supported.

    test_insn1d_track_runing_status() # Only GPU is supported.
    test_insn2d_track_runing_status() # Only GPU is supported.
    test_insn3d_track_runing_status() # Only GPU is supported.
    test_insn1d_track_runing_status_input_2d() # Only GPU is supported.
    test_insn2d_track_runing_status_input_3d() # Only GPU is supported.
    test_insn3d_track_runing_status_input_4d() # Only GPU is supported.
    test_bn2d_momentum_int()
