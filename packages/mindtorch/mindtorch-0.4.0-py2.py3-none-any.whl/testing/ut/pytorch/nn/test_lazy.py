#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.torch.nn.parameter import UninitializedParameter, UninitializedBuffer
import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, SKIP_ENV_CPU, param_compare
set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason="LazyLinear is not supported in GRAPH_MODE")
def test_lazylinear():
    module = ms_torch.nn.LazyLinear(10)
    assert isinstance(module.weight, UninitializedParameter)
    assert isinstance(module.bias, UninitializedParameter)
    input = ms_torch.ones(5, 5)
    module(input)
    assert isinstance(module, ms_torch.nn.Linear)
    assert not isinstance(module, ms_torch.nn.LazyLinear)
    assert module.weight.shape == (10, 5)
    assert module.bias.shape == (10,)
    y = module(input)
    expect_y = ms_torch.nn.functional.linear(input, module.weight, module.bias)
    param_compare(expect_y, y)


def _check_lazy_norm(cls, lazy_cls, input_shape):
    for affine in [True, False]:
        for track_running_stats in [True, False]:
            lazy_module = lazy_cls(affine=affine, track_running_stats=track_running_stats)

            assert isinstance(lazy_module.weight, UninitializedParameter)
            assert isinstance(lazy_module.bias, UninitializedParameter)
            assert isinstance(lazy_module.running_mean, UninitializedParameter)
            assert isinstance(lazy_module.running_var, UninitializedParameter)

            input = ms_torch.ones(*input_shape)
            lazy_output = lazy_module(input)
            assert isinstance(lazy_module, cls)
            assert not isinstance(lazy_module, lazy_cls)

            num_features = input_shape[1]
            module = cls(num_features, affine=affine, track_running_stats=track_running_stats)
            expected_output = module(input)

            assert lazy_module.momentum == module.momentum
            assert lazy_module.training  == module.training
            assert lazy_module.affine == module.affine
            assert lazy_module.track_running_stats == module.track_running_stats

            param_compare(lazy_output, expected_output)
            if module.weight is not None:
                param_compare(lazy_module.weight, module.weight)
            if module.bias is not None:
                param_compare(lazy_module.bias, module.bias)
            if module.running_mean is not None:
                param_compare(lazy_module.running_mean, module.running_mean)
            if module.running_var is not None:
                param_compare(lazy_module.running_var, module.running_var)


@SKIP_ENV_GRAPH_MODE(reason="LazyBatchNorm is not supported in GRAPH_MODE")
def test_lazy_batchnorm():
    _check_lazy_norm(ms_torch.nn.BatchNorm1d, ms_torch.nn.LazyBatchNorm1d, (8, 3, 6))
    _check_lazy_norm(ms_torch.nn.BatchNorm2d, ms_torch.nn.LazyBatchNorm2d, (8, 3, 6, 7))
    _check_lazy_norm(ms_torch.nn.BatchNorm3d, ms_torch.nn.LazyBatchNorm3d, (8, 3, 6, 7, 8))


@SKIP_ENV_GRAPH_MODE(reason="InstanceNorm is not supported in GRAPH_MODE")
@SKIP_ENV_CPU(reason="InstanceNorm not support on CPU")
def test_lazy_instance_norm():
    _check_lazy_norm(ms_torch.nn.InstanceNorm1d, ms_torch.nn.LazyInstanceNorm1d, (8, 3, 6))
    _check_lazy_norm(ms_torch.nn.InstanceNorm2d, ms_torch.nn.LazyInstanceNorm2d, (8, 3, 6, 7))
    _check_lazy_norm(ms_torch.nn.InstanceNorm3d, ms_torch.nn.LazyInstanceNorm3d, (8, 3, 6, 7, 8))


def _check_lazy_conv(cls, lazy_cls, func, init_args, input_shape, expected_weight_shape, expected_bias_shape):
    module = lazy_cls(*init_args)
    assert isinstance(module.weight, UninitializedParameter)
    if module.bias is not None:
        assert isinstance(module.bias, UninitializedParameter)
    input = ms_torch.ones(*input_shape)
    module(input)
    assert isinstance(module, cls)
    assert not isinstance(module, lazy_cls)
    assert module.weight.shape == expected_weight_shape
    if module.bias is not None:
        assert module.bias.shape == expected_bias_shape
    y = module(input)
    assert ms_torch.equal(func(input, module.weight, module.bias), y)


@SKIP_ENV_GRAPH_MODE(reason="LazyConv is not supported in GRAPH_MODE")
def test_lazy_conv():
    _check_lazy_conv(ms_torch.nn.Conv1d, ms_torch.nn.LazyConv1d, ms_torch.nn.functional.conv1d,
                     (32, 2), (192, 16, 50), (32, 16, 2), (32,))
    _check_lazy_conv(ms_torch.nn.Conv2d, ms_torch.nn.LazyConv2d, ms_torch.nn.functional.conv2d,
                     (32, 2), (192, 16, 8, 6), (32, 16, 2, 2), (32,))
    _check_lazy_conv(ms_torch.nn.Conv3d, ms_torch.nn.LazyConv3d, ms_torch.nn.functional.conv3d,
                     (32, 2), (192, 16, 8, 7, 6), (32, 16, 2, 2, 2), (32,))


@SKIP_ENV_GRAPH_MODE(reason="LazyConvTranspose is not supported in GRAPH_MODE")
def test_lazy_conv_transpose():
    _check_lazy_conv(ms_torch.nn.ConvTranspose1d, ms_torch.nn.LazyConvTranspose1d,
                     ms_torch.nn.functional.conv_transpose1d, (32, 2), (192, 16, 50), (16, 32, 2), (32,))
    _check_lazy_conv(ms_torch.nn.ConvTranspose2d, ms_torch.nn.LazyConvTranspose2d,
                     ms_torch.nn.functional.conv_transpose2d, (32, 2), (192, 16, 8, 6), (16, 32, 2, 2), (32,))
    _check_lazy_conv(ms_torch.nn.ConvTranspose3d, ms_torch.nn.LazyConvTranspose3d,
                     ms_torch.nn.functional.conv_transpose3d, (32, 2), (192, 16, 8, 7, 6), (16, 32, 2, 2, 2), (32,))


@SKIP_ENV_GRAPH_MODE(reason="UninitializedBuffer is not supported in GRAPH_MODE")
def test_uninitialized_buffer():
    buffer = UninitializedBuffer()
    assert isinstance(buffer, UninitializedBuffer)
    buffer.materialize((3,))
    assert not isinstance(buffer, UninitializedBuffer)
    assert isinstance(buffer, ms_torch.Tensor)
    assert buffer.shape == (3,)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_lazylinear()
    test_lazy_batchnorm()
    test_lazy_instance_norm()
    test_lazy_conv()
    test_lazy_conv_transpose()
    test_uninitialized_buffer()
