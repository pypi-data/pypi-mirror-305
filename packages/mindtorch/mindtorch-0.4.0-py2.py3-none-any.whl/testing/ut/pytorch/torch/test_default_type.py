#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config, TestNet, SKIP_ENV_GPU, graph_lax_level, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()

def _test_base_fn(set_type, fn):
    ms_torch.set_default_dtype(set_type)

    net = TestNet(fn)
    out = net()
    ms_torch.set_default_dtype(ms_torch.float32)
    return out

def _test_base_tensor_fn(set_type, fn):
    ms_torch.set_default_tensor_type(set_type)

    net = TestNet(fn)
    out = net()
    ms_torch.set_default_tensor_type(ms_torch.float32)
    return out

def test_set_default_dtype():
    def fn():
        x = ms_torch.tensor([3., 4.])
        y = ms_torch.Tensor([1, 2])
        return x, y

    x, y = _test_base_fn(ms_torch.half, fn)

    assert x.dtype == ms_torch.half
    assert y.dtype == ms_torch.half


def test_set_default_tensor_type():
    def fn():
        x = ms_torch.tensor(3.0)
        return x

    x = _test_base_tensor_fn('torch.DoubleTensor', fn)
    assert x.dtype == ms_torch.float64


def test_set_default_tensor_type_2():
    tmp_tensor = ms_torch.tensor([1.0], dtype=ms_torch.float16)
    type2 = tmp_tensor.type()

    def fn():
        y = ms_torch.Tensor([3.2, 4.1])
        return y

    y = _test_base_tensor_fn(type2, fn)
    assert y.dtype == ms_torch.float16


def test_op_arange():
    def fn():
        x = ms_torch.arange(1, 4)
        y = ms_torch.arange(1, 2.5, 0.5)
        return x, y

    x, y = _test_base_tensor_fn(ms_torch.float64, fn)

    assert x.dtype == ms_torch.int64
    assert y.dtype == ms_torch.float64


def test_op_bartlett_window():
    def fn():
        x = ms_torch.bartlett_window(5, periodic=True)
        return x

    x = _test_base_tensor_fn(ms_torch.float64, fn)
    assert x.dtype == ms_torch.float64


def test_op_blackman_window():
    def fn():
        x = ms_torch.blackman_window(4, periodic=True)
        return x
    x = _test_base_tensor_fn(ms_torch.float64, fn)
    assert x.dtype == ms_torch.float64


def test_op_empty():
    def fn():
        x = ms_torch.empty((2, 3))
        return x

    x = _test_base_tensor_fn(ms_torch.half, fn)
    assert x.dtype == ms_torch.half


def test_op_empty_strided():
    def fn():
        x = ms_torch.empty_strided((2, 3), (1, 2))
        return x

    x = _test_base_tensor_fn(ms_torch.half, fn)
    assert x.dtype == ms_torch.half


def test_op_eye():
    def fn():
        x = ms_torch.eye(3)
        return x

    x = _test_base_tensor_fn(ms_torch.half, fn)
    assert x.dtype == ms_torch.half

def test_op_full():
    def fn():
        x = ms_torch.full((2, 3), 3.141592)
        y = ms_torch.full((2, 2), 3)
        return x, y

    x, y = _test_base_tensor_fn(ms_torch.float64, fn)
    assert x.dtype == ms_torch.float64
    assert y.dtype == ms_torch.int64


def test_op_hamming_window():
    def fn():
        x = ms_torch.hamming_window(4, False)
        return x

    x = _test_base_tensor_fn(ms_torch.float64, fn)
    assert x.dtype == ms_torch.float64


def test_op_hann_window():
    def fn():
        x = ms_torch.hann_window(2, False)
        return x

    x = _test_base_tensor_fn(ms_torch.float16, fn)
    assert x.dtype == ms_torch.float16


def test_op_kaiser_window():
    def fn():
        x = ms_torch.kaiser_window(4, True)
        return x

    x = _test_base_tensor_fn(ms_torch.float64, fn)
    assert x.dtype == ms_torch.float64


def test_op_linspace():
    def fn():
        x = ms_torch.linspace(start=-10, end=10, steps=1)
        return x

    x = _test_base_tensor_fn(ms_torch.float64, fn)
    assert x.dtype == ms_torch.float64


@SKIP_ENV_GPU(reason="ms.ops.logspace has bug when dtype difference")
def test_op_logspace():
    def fn():
        x = ms_torch.logspace(start=0.1, end=1.0, steps=1)
        return x

    x = _test_base_tensor_fn(ms_torch.float16, fn)  # Ascend unsupport float64
    assert x.dtype == ms_torch.float16


def test_op_ones():
    def fn():
        x = ms_torch.ones(3)
        return x

    x = _test_base_tensor_fn(ms_torch.float16, fn)
    assert x.dtype == ms_torch.float16


def test_op_rand():
    def fn():
        x = ms_torch.rand(4)
        return x

    x = _test_base_tensor_fn(ms_torch.float64, fn)
    assert x.dtype == ms_torch.float64


def test_op_randn():
    def fn():
        x = ms_torch.randn(2, 3)
        return x

    x = _test_base_tensor_fn(ms_torch.float16, fn)
    assert x.dtype == ms_torch.float16


def test_op_range():
    def fn():
        x = ms_torch.range(1, 4)
        return x

    x = _test_base_tensor_fn(ms_torch.float64, fn)
    assert x.dtype == ms_torch.float32


def test_op_zeros():
    def fn():
        x = ms_torch.zeros(3)
        return x

    x = _test_base_tensor_fn(ms_torch.float16, fn)
    assert x.dtype == ms_torch.float16


if __name__ == '__main__':
    set_mode_by_env_config()
    test_set_default_dtype()
    test_set_default_tensor_type()
    test_set_default_tensor_type_2()
    test_op_arange()
    test_op_bartlett_window()
    test_op_blackman_window()
    test_op_empty()
    test_op_empty_strided()
    test_op_eye()
    test_op_full()
    test_op_hamming_window()
    test_op_hann_window()
    test_op_kaiser_window()
    test_op_linspace()
    test_op_logspace()
    test_op_ones()
    test_op_rand()
    test_op_randn()
    test_op_range()
    test_op_zeros()
