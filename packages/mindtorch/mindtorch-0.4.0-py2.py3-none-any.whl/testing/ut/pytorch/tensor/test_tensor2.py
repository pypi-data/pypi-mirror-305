#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import numpy as np
import torch
import mindspore as ms
from mindspore import context
import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_GPU, SKIP_ENV_GRAPH_MODE, SKIP_ENV_ASCEND, \
    graph_lax_level, TestNet, type_shape_compare
set_mode_by_env_config()

def test_var():
    input = np.random.random((2,3)).astype(np.float32)
    py_tensor = torch.tensor(input)
    output1_py = py_tensor.var()
    ms_tensor = ms_torch.tensor(input)
    output1_ms = ms_tensor.var()
    assert np.allclose(output1_py.numpy(), output1_ms.numpy())

    py_tensor = torch.tensor(input)
    output2_py = py_tensor.var(dim=0, unbiased=False, keepdim=True)
    ms_tensor = ms_torch.tensor(input)
    output2_ms = ms_tensor.var(dim=0, unbiased=False, keepdim=True)
    assert np.allclose(output2_py.numpy(), output2_ms.numpy())

def test_narrow():
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    x1_pt = torch.tensor(x)
    out1_pt = x1_pt.narrow(0, 0, 2)
    x1_ms = ms_torch.tensor(x)
    out1_ms = x1_ms.narrow(0, 0, 2)
    assert np.allclose(out1_pt.numpy(), out1_ms.numpy())

    out2_pt = torch.narrow(x1_pt, 1, 1, 2)
    out2_ms = ms_torch.narrow(x1_ms, 1, 1, 2)
    assert np.allclose(out2_pt.numpy(), out2_ms.numpy())

def test_norm():
    a_pt = torch.arange(0, 9, dtype=torch.float) - 4
    a_ms = ms_torch.arange(0, 9, dtype=ms_torch.float) - 4

    # TODO: ms_torch.norm cannot support this function now
    # out1_pt = a_pt.norm()
    # out1_ms = a_ms.norm()
    # assert np.allclose(out1_pt.numpy(), out1_ms.numpy())

    out2_pt = a_pt.norm(float('inf'))
    out2_ms = a_ms.norm(float('inf'))
    assert np.allclose(out2_pt.numpy(), out2_ms.numpy())

    b_pt = torch.tensor([[ 1, 2, 3],[-1, 1, 4]] , dtype= torch.float)
    b_ms = ms_torch.tensor([[ 1, 2, 3],[-1, 1, 4]] , dtype= ms_torch.float)
    out3_pt = b_pt.norm(p=1, dim=1)
    out3_ms = b_ms.norm(p=1, dim=1)
    assert np.allclose(out3_pt.numpy(), out3_ms.numpy())

    out4_pt = b_pt.norm(p=1, dim=1, keepdim=True, dtype=torch.float16)
    out4_ms = b_ms.norm(p=1, dim=1, keepdim=True, dtype=ms_torch.float16)
    assert out4_pt.numpy().dtype == out4_ms.numpy().dtype
    assert np.allclose(out4_pt.numpy(), out4_ms.numpy())


def test_nanmean():
    x = np.array([[1, np.nan], [3, 4]]).astype(np.float32)
    x_pt = torch.tensor(x)
    out1_pt = x_pt.nanmean()
    x_ms = ms_torch.tensor(x)
    out1_ms = x_ms.nanmean()
    assert np.allclose(out1_pt.numpy(), out1_ms.numpy())

    out2_pt = x_pt.nanmean(0, True)
    out2_ms = x_ms.nanmean(0, True)
    assert np.allclose(out2_pt.numpy(), out2_ms.numpy())

    out3_pt = x_pt.nanmean(1, True, dtype=torch.float16)
    out3_ms = x_ms.nanmean(1, True, dtype=ms_torch.float16)
    assert np.allclose(out3_pt.numpy(), out3_ms.numpy())

@SKIP_ENV_ASCEND(reason="nanmean not support float64 input")
def test_nanmean_float64():
    x = np.array([[1, np.nan], [3, 4]])
    x_pt = torch.tensor(x)
    out1_pt = x_pt.nanmean()
    x_ms = ms_torch.tensor(x)
    out1_ms = x_ms.nanmean()
    assert np.allclose(out1_pt.numpy(), out1_ms.numpy())

def test_nansum():
    x = np.array([[float("nan"), 2, 3], [1, 2, float("nan")]]).astype(np.float32)
    x_pt = torch.tensor(x)
    out1_pt = x_pt.nansum()
    x_ms = ms_torch.tensor(x)
    out1_ms = x_ms.nansum()
    assert np.allclose(out1_pt.numpy(), out1_ms.numpy())

    out2_pt = x_pt.nansum(0, True)
    out2_ms = x_ms.nansum(0, True)
    assert np.allclose(out2_pt.numpy(), out2_ms.numpy())

    out3_pt = x_pt.nansum(1, True, dtype=torch.float16)
    out3_ms = x_ms.nansum(1, True, dtype=ms_torch.float16)
    assert np.allclose(out3_pt.numpy(), out3_ms.numpy())

@SKIP_ENV_ASCEND(reason="nansum not support float64 on ascend")
def test_nansum_float64():
    x = np.array([[float("nan"), 2, 3], [1, 2, float("nan")]])
    x_pt = torch.tensor(x)
    out1_pt = x_pt.nansum()
    x_ms = ms_torch.tensor(x)
    out1_ms = x_ms.nansum()
    assert np.allclose(out1_pt.numpy(), out1_ms.numpy())

def test_argwhere():
    data = np.array([[1, 0, 1], [2, 3, 4]])

    a = torch.tensor(data)
    torch_out = a.argwhere()

    a = ms_torch.tensor(data)
    ms_out = a.argwhere()

    assert np.allclose(torch_out.numpy(), ms_out.numpy())

@SKIP_ENV_GPU(reason="unsupported op Cauchy on GPU.")
@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_cauchy_():
    data = np.array([[1, 2, 3, 4, 5], [3, 4, 5, 6, 7]])
    ms_tensor = ms_torch.tensor(data)
    _origin_shape = ms_tensor.shape

    ms_tensor.cauchy_()
    assert ms_tensor.shape == _origin_shape
    assert not np.allclose(ms_tensor.numpy(), data)

def test_conj_physical():
    np_array1 = np.array([[1, 2, 3, 4]]).astype(np.int16)
    np_array2 = np.array([[1+5j, 2-1j, 3.0, -4j, -0j]])

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch_tensor1.conj_physical()
    torch_out2 = torch_tensor2.conj_physical()

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out1 = ms_tensor1.conj_physical()
    ms_out2 = ms_tensor2.conj_physical()

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_conj_physical_():
    np_array1 = np.array([[1, 2, 3, 4]]).astype(np.int16)
    np_array2 = np.array([[1+5j, 2-1j, 3.0, -4j, -0j]])

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor1.conj_physical_()
    torch_tensor2.conj_physical_()

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_tensor1.conj_physical_()
    ms_tensor2.conj_physical_()

    assert np.allclose(ms_tensor1.asnumpy(), torch_tensor1.numpy())
    assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype
    assert np.allclose(ms_tensor2.asnumpy(), torch_tensor2.numpy())
    assert ms_tensor2.asnumpy().dtype == torch_tensor2.numpy().dtype

def test_unfold():
    data1 = np.arange(1., 8).astype(np.float32)
    data2 = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)
    data3 = np.random.randn(1, 11, 14).astype(np.float32)

    x = torch.tensor(data1)
    torch_out1 = x.unfold(0, 2, 1)
    torch_out2 = x.unfold(0, 2, 2)
    x = torch.tensor(data2)
    torch_out3 = x.unfold(3, 2, 2)
    torch_out4 = x.unfold(2, 1, 1)
    x = torch.tensor(data3)
    torch_out5 = x.unfold(-1, 3, 2)
    torch_out6 = x.unfold(-2, 4, 5)

    x = ms_torch.arange(1., 8)
    ms_out1 = x.unfold(0, 2, 1)
    ms_out2 = x.unfold(0, 2, 2)
    x = ms_torch.tensor(data2)
    ms_out3 = x.unfold(3, 2, 2)
    ms_out4 = x.unfold(2, 1, 1)
    x = ms_torch.tensor(data3)
    ms_out5 = x.unfold(-1, 3, 2)
    ms_out6 = x.unfold(-2, 4, 5)

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)
    param_compare(ms_out3, torch_out3)
    param_compare(ms_out4, torch_out4)
    param_compare(ms_out5, torch_out5)
    param_compare(ms_out6, torch_out6)

def test_slogdet():
    data1 = np.random.randn(3, 3)
    data2 = np.random.randn(2, 3, 4, 4)

    x = torch.tensor(data1)
    torch_out1 = x.slogdet()
    x = torch.tensor(data2)
    torch_out2 = x.slogdet()

    x = ms_torch.tensor(data1)
    ms_out1 = x.slogdet()
    x = ms_torch.tensor(data2)
    ms_out2 = x.slogdet()

    assert np.allclose(ms_out1[0].asnumpy(), torch_out1[0].numpy())
    assert ms_out1[0].asnumpy().dtype == torch_out1[0].numpy().dtype
    assert np.allclose(ms_out1[1].asnumpy(), torch_out1[1].numpy())
    assert ms_out1[1].asnumpy().dtype == torch_out1[1].numpy().dtype

    assert np.allclose(ms_out2[0].asnumpy(), torch_out2[0].numpy())
    assert ms_out2[0].asnumpy().dtype == torch_out2[0].numpy().dtype
    assert np.allclose(ms_out2[1].asnumpy(), torch_out2[1].numpy())
    assert ms_out2[1].asnumpy().dtype == torch_out2[1].numpy().dtype

def test_slice_scatter():
    a = torch.zeros(8, 8)
    # TODO: to use b = torch.ones(8) as testcase on pytorch documents after pytorch fix slice_scatter.
    b = torch.ones(2, 8)
    torch_out1 = a.slice_scatter(b, start=6)

    b = torch.ones(8, 2)
    torch_out2 = a.slice_scatter(b, dim=1, start=2, end=6, step=2)

    a = torch.zeros(2, 3, 4, 5)
    b = torch.ones(2, 1, 4, 5)
    torch_out3 = a.slice_scatter(b, start=2, dim=1)

    a = ms_torch.zeros(8, 8)
    b = ms_torch.ones(8)
    ms_out1 = a.slice_scatter(b, start=6)

    b = ms_torch.ones(2)
    ms_out2 = a.slice_scatter(b, dim=1, start=2, end=6, step=2)

    a = ms_torch.zeros(2, 3, 4, 5)
    b = ms_torch.ones(4, 5)
    ms_out3 = a.slice_scatter(b, start=2, dim=1)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy())
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

def test_select_scatter():
    a = torch.zeros(2, 2)
    b = torch.ones(2)
    torch_out1 = a.select_scatter(b, 0, 0)

    a = ms_torch.zeros(2, 2)
    b = ms_torch.ones(2)
    ms_out1 = a.select_scatter(b, 0, 0)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype

def test_cross1():
    np_1 = np.random.randn(4, 3).astype(np.float32)
    np_2 = np.random.randn(4, 3).astype(np.float32)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_tensor_1.cross(ms_tensor_2)
    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch_tensor_1.cross(torch_tensor_2)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_cross2():
    np_1 = np.random.randn(4, 3).astype(np.int32)
    np_2 = np.random.randn(4, 3).astype(np.int32)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_tensor_1.cross(ms_tensor_2)
    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch_tensor_1.cross(torch_tensor_2)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_fill_diagonal_():
    a1 = torch.zeros(3, 3)
    a1.fill_diagonal_(5)
    b1 = torch.zeros(7, 3)
    b1.fill_diagonal_(5)
    c1 = torch.zeros(7, 3)
    c1.fill_diagonal_(5, wrap=True)

    a2 = ms_torch.zeros(3, 3)
    a2.fill_diagonal_(5)
    b2 = ms_torch.zeros(7, 3)
    b2.fill_diagonal_(5)
    c2 = ms_torch.zeros(7, 3)
    c2.fill_diagonal_(5, wrap=True)

    assert np.allclose(a1.numpy(), a2.numpy())
    assert np.allclose(b1.numpy(), b2.numpy())
    assert np.allclose(c1.numpy(), c2.numpy())

def test_fmax():
    a = torch.tensor([1., float('nan'), 3, float('nan')])
    b = torch.tensor([float('nan'), 2., 1., float('nan')])
    torch_output = a.fmax(b)

    a = ms_torch.tensor([1., float('nan'), 3, float('nan')])
    b = ms_torch.tensor([float('nan'), 2., 1., float('nan')])
    with graph_lax_level():
        ms_out = a.fmax(b)

    assert np.allclose(torch_output.numpy(), ms_out.numpy(), equal_nan=True)

def test_fmin():
    a = torch.tensor([1., float('nan'), 3, float('nan')])
    b = torch.tensor([float('nan'), 2., 1., float('nan')])
    torch_output = a.fmin(b)

    a = ms_torch.tensor([1., float('nan'), 3, float('nan')])
    b = ms_torch.tensor([float('nan'), 2., 1., float('nan')])
    with graph_lax_level():
        ms_out = a.fmin(b)

    assert np.allclose(torch_output.numpy(), ms_out.numpy(), equal_nan=True)

def test_H():
    a = torch.tensor([[1+1j, 2], [1-1j, 1]])
    torch_out = a.H

    a = ms_torch.tensor([[1+1j, 2], [1-1j, 1]])
    ms_out = a.H

    assert np.allclose(torch_out.resolve_conj().numpy(), ms_out.numpy(), equal_nan=True)
    # TODO: torch_out is complex64 ms_out is complex128
    # assert torch_out.resolve_conj().numpy().dtype == ms_out.numpy().dtype


def test_histc():
    data1 = np.array([1, 2, 1, 0, -1, -2, 2, 2, 3, 3, 4, 5, 6]).astype(np.float32)
    t_r1 = torch.tensor(data1).histc(bins=4, min=3, max=3)
    ms_r1 = ms_torch.tensor(data1).histc(bins=4, min=3, max=3)
    t_r2 = torch.tensor([[1., 2, 1, 0, -1, -2, 2.1, 2.9, 3, 3.1, 4, 5, 6]]).histc(bins=4, min=0, max=3)
    ms_r2 = ms_torch.tensor([[1., 2, 1, 0, -1, -2, 2.1, 2.9, 3, 3.1, 4, 5, 6]]).histc(bins=4, min=0, max=3)
    t_r3 = torch.tensor([1., 1, 1]).histc(bins=4, min=3, max=3)
    ms_r3 = ms_torch.tensor([1., 1, 1]).histc(bins=4, min=3, max=3)
    t_r4 = torch.tensor(data1).histc(bins=4, min=3., max=4)
    ms_r4 = ms_torch.tensor(data1).histc(bins=4, min=3., max=4)

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r3, ms_r3)
    param_compare(t_r4, ms_r4)


def test_histogram():
    n1 = random.randint(1, 50)
    data1 = np.random.randn(n1).astype(np.float32)
    bins1 = random.randint(1, 50)
    range1_0 = random.randint(1, 50)
    range1_1 = random.randint(1, 50)
    if range1_0 >= range1_1:
        range1 = (range1_1, range1_0)
    else:
        range1 = (range1_0, range1_1)
    weight1 = np.random.randint(low=20, size=n1).astype(np.float32)

    torch_out1 = torch.tensor(data1).histogram(bins=bins1, range=range1, weight=torch.tensor(weight1))
    torch_out2 = torch.tensor(data1).histogram(bins=bins1, range=range1, weight=torch.tensor(weight1), density=True)

    ms_out1 = ms_torch.tensor(data1).histogram(bins=bins1, range=range1, weight=ms_torch.tensor(weight1))
    ms_out2 = ms_torch.tensor(data1).histogram(bins=bins1, range=range1, weight=ms_torch.tensor(weight1), density=True)

    assert np.allclose(torch_out1[0].numpy(), ms_out1[0].numpy(), equal_nan=True)
    assert np.allclose(torch_out1[1].numpy(), ms_out1[1].numpy(), equal_nan=True)
    assert np.allclose(torch_out2[0].numpy(), ms_out2[0].numpy(), equal_nan=True)
    assert np.allclose(torch_out2[1].numpy(), ms_out2[1].numpy(), equal_nan=True)

def test_tensor_shape_with_zero():
    a = ms_torch.Tensor(0, 2, 3, 0)
    assert a.shape == (0, 2, 3, 0)

def test_tensor_device():
    a = ms_torch.Tensor(1)
    b = ms_torch.Tensor(2)
    assert np.allclose(b.to(a.device).numpy(), b.numpy())

def test_format():
    x = ms_torch.tensor(1.02344)
    print("x = {:.4f}".format(x))

def test_create_adapter_tensor_in_forward():
    class Net(ms_torch.nn.Module):
        def forward(self, input):
            # output = ms_torch.Tensor(input.numpy())
            #TODO: mindspore has problem supporting numpy trans to ms.Tensor
            # ms_tensor = ms.Tensor(input.numpy())
            ms_tensor = ms.Tensor(1)
            output = ms_torch.cast_to_adapter_tensor(ms_tensor)
            return output

    net = Net()
    #TODO: mindspore has problem supporting numpy trans to ms.Tensor
    #input = ms_torch.tensor([1.0, 2.0])
    input = ms_torch.tensor(1)
    with graph_lax_level():
        output = net(input)
    assert np.allclose(input.numpy(), output.numpy())

def test_polygamma():
    a = ms_torch.Tensor([1, 0.5])
    b = torch.Tensor([1, 0.5])

    param_compare(a.polygamma(1), b.polygamma(1))
    param_compare(a.polygamma(2), b.polygamma(2))
    param_compare(a.polygamma(3), b.polygamma(3))
    param_compare(a.polygamma(4), b.polygamma(4))

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_polygamma_():
    a = ms_torch.Tensor([1, 0.5])
    b = torch.Tensor([1, 0.5])
    a.polygamma_(1)
    b.polygamma_(1)
    param_compare(a, b)

    a = ms_torch.Tensor([1, 0.5])
    b = torch.Tensor([1, 0.5])
    a.polygamma_(2)
    b.polygamma_(2)
    param_compare(a, b)

def test_tensor_with_tensor_shape():
    a = ms_torch.Tensor(1, 2, 3)
    b = torch.Tensor(1, 2, 3)
    assert a.numpy().shape == b.numpy().shape

    a = ms_torch.Tensor(1, 2, ms_torch.tensor(3), ms_torch.tensor(4))
    b = torch.Tensor(1, 2, torch.tensor(3), torch.tensor(4))
    assert a.numpy().shape == b.numpy().shape

    a = ms_torch.Tensor(1, 2, True, ms_torch.tensor(4))
    b = torch.Tensor(1, 2, True, torch.tensor(4))
    assert a.numpy().shape == b.numpy().shape

    a = ms_torch.Tensor(1, 2, False, ms_torch.tensor(4))
    b = torch.Tensor(1, 2, False, torch.tensor(4))
    assert a.numpy().shape == b.numpy().shape

    a = ms_torch.Tensor(1, 2, ms_torch.tensor(True), ms_torch.tensor(4))
    b = torch.Tensor(1, 2, ms_torch.tensor(True), torch.tensor(4))
    assert a.numpy().shape == b.numpy().shape

@SKIP_ENV_GRAPH_MODE(reason='tensor.apply_(fn), fn is a function, but graph mode not support func-type as input yet')
def test_apply_():
    data = np.random.randn(1, 2, 3).astype(np.float32)
    a = ms_torch.tensor(data)
    a.apply_(lambda x: x + 1)

    b = torch.tensor(data)
    b.apply_(lambda x: x + 1)

    param_compare(a, b)

    a_1 = ms_torch.tensor(data + 1)
    param_compare(a, a_1)

@SKIP_ENV_GRAPH_MODE(reason='tensor.apply_(fn), fn is a function, but graph mode not support func-type as input yet')
@SKIP_ENV_ASCEND(reason="apply_ currently not support float64 on Ascend")
def test_apply_fp64():
    data = np.random.randn(2, 3)
    a = ms_torch.tensor(data)
    a.apply_(lambda x: x + 1)

    b = torch.tensor(data)
    b.apply_(lambda x: x + 1)

    param_compare(a, b)

    a_1 = ms_torch.tensor(data + 1)
    param_compare(a, a_1)

def test_diagonal_scatter():
    a = ms_torch.zeros(3, 3)
    ms_out1 = a.diagonal_scatter(ms_torch.ones(3), 0)
    ms_out2 = a.diagonal_scatter(ms_torch.ones(2), 1)

    a = torch.zeros(3, 3)
    torch_out1 = a.diagonal_scatter(torch.ones(3), 0)
    torch_out2 = a.diagonal_scatter(torch.ones(2), 1)

    a = torch.zeros(1, 4, 5, 2)
    torch_out3 = a.diagonal_scatter(torch.ones(1, 2, 4), 1, dim1=1, dim2=2)
    a = ms_torch.zeros(1, 4, 5, 2)
    ms_out3 = a.diagonal_scatter(ms_torch.ones(1, 2, 4), 1, dim1=1, dim2=2)

    a = torch.zeros(1, 4, 4, 2)
    torch_out4 = a.diagonal_scatter(torch.ones(1, 2, 4), 0, dim1=1, dim2=2)
    a = ms_torch.zeros(1, 4, 4, 2)
    ms_out4 = a.diagonal_scatter(ms_torch.ones(1, 2, 4), 0, dim1=1, dim2=2)

    a = torch.zeros(1, 4, 3, 2)
    torch_out5 = a.diagonal_scatter(torch.ones(1, 2, 3), 0, dim1=1, dim2=2)
    a = ms_torch.zeros(1, 4, 3, 2)
    ms_out5 = a.diagonal_scatter(ms_torch.ones(1, 2, 3), 0, dim1=1, dim2=2)

    a = ms_torch.zeros(1, 4, 4, 2)
    ms_out6 = a.diagonal_scatter(ms_torch.ones(1, 2, 3), 1, dim1=1, dim2=2)
    a = torch.zeros(1, 4, 4, 2)
    torch_out6 = a.diagonal_scatter(torch.ones(1, 2, 3), 1, dim1=1, dim2=2)

    a = ms_torch.zeros(1, 4, 4, 2)
    ms_out7 = a.diagonal_scatter(ms_torch.ones(1, 2, 3), -1, dim1=1, dim2=2)
    a = torch.zeros(1, 4, 4, 2)
    torch_out7 = a.diagonal_scatter(torch.ones(1, 2, 3), -1, dim1=1, dim2=2)

    a = ms_torch.zeros(1, 4, 6, 2)
    ms_out8 = a.diagonal_scatter(ms_torch.ones(1, 2, 4), 1, dim1=1, dim2=2)
    a = torch.zeros(1, 4, 6, 2)
    torch_out8 = a.diagonal_scatter(torch.ones(1, 2, 4), 1, dim1=1, dim2=2)

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)
    param_compare(ms_out3, torch_out3)
    param_compare(ms_out4, torch_out4)
    param_compare(ms_out5, torch_out5)
    param_compare(ms_out6, torch_out6)
    param_compare(ms_out7, torch_out7)
    param_compare(ms_out8, torch_out8)

def test_diagonal_scatter_graph():
    a = ms_torch.zeros(3, 3)
    src = ms_torch.ones(3)
    @ms.jit
    def func(input, src):
        return input.diagonal_scatter(src, 0)
    with graph_lax_level():
        ms_out1 = func(a, src)

    a = torch.zeros(3, 3)
    torch_out1 = a.diagonal_scatter(torch.ones(3), 0)

    param_compare(ms_out1, torch_out1)


def test_narrow_copy():
    x = (np.random.randn(3, 5) * 5).astype(np.uint8)
    x1_pt = torch.tensor(x)
    x1_ms = ms_torch.tensor(x)
    out1_pt = x1_pt.narrow_copy(0, 0, 2)
    out1_ms = x1_ms.narrow_copy(0, 0, 2)
    out2_pt = x1_pt.narrow_copy(1, 2, 3)
    out2_ms = x1_ms.narrow_copy(1, 2, 3)
    param_compare(out1_pt, out1_ms)
    param_compare(out2_pt, out2_ms)


def test_data():
    zeros_tensor = ms_torch.zeros(3, 3)
    ones_tenor = ms_torch.ones(3, 3)
    ones_tenor.data = zeros_tensor.data.clone().detach()
    param_compare(ones_tenor, zeros_tensor)


def test_new_full():
    torch_size = [2, 3, torch.tensor(2), torch.tensor(3)]
    torch＿tensor = torch.zeros(2, 3)
    torch_out = torch＿tensor.new_full(torch_size, 2)

    msa_size = [2, 3, ms_torch.tensor(2), ms_torch.tensor(3)]
    msa＿tensor = ms_torch.zeros(2, 3)
    msa_out = msa＿tensor.new_full(msa_size, 2)
    param_compare(torch_out, msa_out)

def test_cast_tensor_in_dict():
    dict_ms = {'x': ms.Tensor([1, 2, 3]), 'y': ms.Tensor([2, 3, 4])}
    dict_msa = ms_torch.cast_to_adapter_tensor(dict_ms)
    for key, value in dict_msa.items():
        assert type(value) is ms_torch.Tensor

    dict_msa2ms = ms_torch.cast_to_ms_tensor(dict_msa)
    for key, value in dict_msa2ms.items():
        assert type(value) is not ms_torch.Tensor

def test_device_equal():
    a = ms_torch.tensor(1)
    b = ms_torch.tensor(2)
    assert a.device == b.device

def test_view_dynamic():
    @ms.jit(input_signature=ms_torch.cast_to_adapter_tensor(ms.tensor(shape=[None, 2], dtype=ms.float32)))
    def view_func(x):
        return x.view(-1, 2)

    a = ms_torch.Tensor(0, 2)
    out = view_func(a)
    assert out.shape == (0, 2)

def test_bfloat16_tensor():
    tensor_1 = ms_torch.BFloat16Tensor()
    assert tensor_1.dtype == ms_torch.bfloat16

    def fn():
        return ms_torch.BFloat16Tensor([1, 2, 3])

    with graph_lax_level():
        net = TestNet(fn)
        tensor_2 = net()
    assert tensor_2.shape == (3,)
    assert tensor_2.dtype == ms_torch.bfloat16

@SKIP_ENV_ASCEND(reason="ms.ops.Cast unspport bfloat16 on Ascend.")
@SKIP_ENV_GPU(reason="ms.ops.Cast unspport bfloat16 on GPU.")
def test_bfloat16():
    def fn():
        a = ms_torch.Tensor(1, 2)
        a = a.bfloat16()
        return a

    net = TestNet(fn)
    a = net()
    assert a.dtype == ms_torch.bfloat16

def test_cfloat():
    def fn():
        a = ms_torch.Tensor(1, 2)
        a = a.cfloat()
        return a

    net = TestNet(fn)
    a = net()
    assert a.dtype == ms_torch.complex64

def test_cdouble():
    def fn():
        a = ms_torch.Tensor(1, 2)
        a = a.cdouble()
        return a

    net = TestNet(fn)
    a = net()
    assert a.dtype == ms_torch.complex128


def test_is_set_to():
    a = ms_torch.Tensor(2, 3)
    a_ms = ms_torch.cast_to_ms_tensor(a)
    a_msa = ms_torch.cast_to_adapter_tensor(a_ms)
    assert a.is_set_to(a_msa)

def test_logcumsumexp():
    data = np.ones(shape=[1,2,3,4])
    torch_out1 = torch.tensor(data).logcumsumexp(0)
    ms_out1 = ms_torch.tensor(data).logcumsumexp(0)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy(), equal_nan=True)

def test_new_tensor():
    x1 = [[[-4.5, -1.5], [7.0, 6.0]], [[2.5, 0.5], [3.0, 9.0]]]
    x2 = [3, 2]
    torch_tensor = torch.tensor(x1)
    ms_tensor = ms_torch.tensor(x1)

    torch_out1 = torch_tensor.new_tensor(x2)
    ms_out1 = ms_tensor.new_tensor(x2)
    param_compare(torch_out1, ms_out1)

    torch_out2 = torch_tensor.new_tensor(x2, dtype=torch.int64)
    ms_out2 = ms_tensor.new_tensor(x2, dtype=ms_torch.int64)
    param_compare(torch_out2, ms_out2)

def test_tensor_np_shape():
    shape = np.ones((2,), dtype=np.int64)
    ms_tensor = ms_torch.Tensor(shape[0], shape[1])
    torch_tensor = torch.Tensor(shape[0], shape[1])
    assert ms_tensor.size() == torch_tensor.size()

    ms_tensor = ms_torch.Tensor((shape[0], shape[1]))
    torch_tensor = torch.Tensor((shape[0], shape[1]))
    param_compare(ms_tensor, torch_tensor)

@SKIP_ENV_GRAPH_MODE(reason="Tensor[Float32] object has no attribute: contiguous' in graph mode.")
def test_contiguous():
    ms_tensor = ms_torch.Tensor(2, 3)
    def contiguous_fun(x):
        return x.contiguous()

    msa_net = TestNet(contiguous_fun)
    output = msa_net(ms_tensor)
    assert output.is_contiguous() == True

def test_reshape():
    ms_tensor = ms_torch.Tensor(2, 3)
    assert ms_tensor.reshape(shape=(-1, 1)).size() == ms_tensor.reshape(-1, 1).size()
    assert ms_tensor.reshape(shape=(-1,)).size() == ms_tensor.reshape(-1).size()
    assert ms_tensor.reshape(shape=(-1,)).size() == ms_tensor.reshape((-1,)).size()

def test_zero_dimention():
    ms_tensor1 = ms_torch.Tensor()
    torch_tensor1 = torch.Tensor()
    param_compare(ms_tensor1, torch_tensor1)

    ms_tensor2 = ms_torch.Tensor([])
    torch_tensor2 = torch.Tensor([])
    param_compare(ms_tensor2, torch_tensor2)

    ms_tensor3 = ms_torch.Tensor(())
    torch_tensor3 = torch.Tensor(())
    param_compare(ms_tensor3, torch_tensor3)

    ms_tensor4 = ms_torch.tensor(())
    torch_tensor4 = torch.tensor(())
    param_compare(ms_tensor4, torch_tensor4)

    ms_tensor5 = ms_torch.tensor([], dtype=ms_torch.int32)
    torch_tensor5 = torch.tensor([], dtype=torch.int32)
    param_compare(ms_tensor5, torch_tensor5)

    ms_tensor6 = ms_torch.empty((), dtype=ms_torch.int8)
    torch_tensor6 = torch.empty((), dtype=torch.int8)
    type_shape_compare(ms_tensor6, torch_tensor6)

    ms_tensor7 = ms_torch.empty_like(ms_tensor6)
    torch_tensor7 = torch.empty_like(torch_tensor6)
    type_shape_compare(ms_tensor7, torch_tensor7)

    ms_tensor8 = ms_torch.empty_like(ms_tensor5, dtype=ms_torch.int8)
    torch_tensor8 = torch.empty_like(torch_tensor5, dtype=torch.int8)
    param_compare(ms_tensor8, torch_tensor8)

    ms_tensor9 = ms_torch.Tensor((1,))
    torch_tensor9 = torch.Tensor((1,))
    param_compare(ms_tensor9, torch_tensor9)

    ms_tensor10 = ms_torch.tensor((1,))
    torch_tensor10 = torch.tensor((1,))
    param_compare(ms_tensor10, torch_tensor10)

    ms_tensor11 = ms_torch.empty((3,))
    torch_tensor11 = torch.empty((3,))
    type_shape_compare(ms_tensor11, torch_tensor11)

    ms_tensor12 = ms_torch.empty(0)
    torch_tensor12 = torch.empty(0)
    param_compare(ms_tensor12, torch_tensor12)

    ms_tensor13 = ms_torch.empty(0, 1)
    torch_tensor13 = torch.empty(0, 1)
    param_compare(ms_tensor13, torch_tensor13)

    ms_tensor14 = ms_torch.Tensor(0)
    torch_tensor14 = torch.Tensor(0)
    param_compare(ms_tensor14, torch_tensor14)

    ms_tensor15 = ms_torch.Tensor(0, 2)
    torch_tensor15 = torch.Tensor(0, 2)
    param_compare(ms_tensor15, torch_tensor15)

# TODO: Currently, The return value type of add_one will be cast as mindtorch tensor.
# def test_make_subclass():
#     class MyTorchTensor(torch.Tensor):
#         def add_one(self):
#             return self + 1
#
#     class MyMSTensor(ms_torch.Tensor):
#         def add_one(self):
#             return self + 1
#
#     data_np = np.random.random((2,3))
#     torch_tensor = torch.Tensor(data_np)
#     torch_tensor1 = MyTorchTensor._make_subclass(MyTorchTensor, torch_tensor)
#     torch_tensor2 = torch_tensor1.add_one()
#
#     ms_tensor = ms_torch.Tensor(data_np)
#     ms_tensor1 = MyMSTensor._make_subclass(MyMSTensor, ms_tensor)
#     ms_tensor2 = ms_tensor1.add_one()
#
#     param_compare(torch_tensor1, ms_tensor1)
#     param_compare(torch_tensor2, ms_tensor2)
#
#     torch_tensor3 = torch_tensor2.add_one()
#     ms_tensor3 = ms_tensor2.add_one()
#     param_compare(torch_tensor3, ms_tensor3)


def test_mH():
    data_np = np.random.random((2, 3))
    ms_tensor = ms_torch.Tensor(data_np)
    def mH_fun(x):
        return x.mH

    msa_net = TestNet(mH_fun)
    msa_output = msa_net(ms_tensor)

    torch_tensor = torch.Tensor(data_np)
    torch_out = mH_fun(torch_tensor)
    param_compare(torch_out, msa_output)


def test_mT():
    data_np = np.random.random((2, 3))
    ms_tensor = ms_torch.Tensor(data_np)
    def mT_fun(x):
        return x.mT

    msa_net = TestNet(mT_fun)
    msa_output = msa_net(ms_tensor)

    torch_tensor = torch.Tensor(data_np)
    torch_out = mT_fun(torch_tensor)
    param_compare(torch_out, msa_output)

@SKIP_ENV_GRAPH_MODE(reason="storage_offset is not supported in graph mode.")
def test_storage_offset():
    ms_tensor = ms_torch.Tensor(2, 3)
    def storage_offset_fun(x):
        y = x[1:, 1:]
        out = y.storage_offset()
        return out

    msa_net = TestNet(storage_offset_fun)
    msa_output = msa_net(ms_tensor)

    torch_tensor = torch.Tensor(2, 3)
    torch_out = storage_offset_fun(torch_tensor)
    assert torch_out == msa_output

@SKIP_ENV_GRAPH_MODE(reason="The graph mode is not supported when the input of view is dtype.")
def test_view_dtype():
    data_np = np.random.random((2, 3, 4))
    ms_tensor = ms_torch.Tensor(data_np)
    def view_dtype_fun(x):
        out = x.view(dtype=ms_torch.float16)
        return out

    msa_net = TestNet(view_dtype_fun)
    msa_output = msa_net(ms_tensor)

    torch_tensor = torch.Tensor(data_np)
    torch_out = torch_tensor.view(torch.float16)
    param_compare(torch_out, msa_output, equal_nan=True)

def test_view_shape_has_tensor():
    data_np = np.random.random((2, 3, 4))
    ms_tensor = ms_torch.Tensor(data_np)
    def view_shape_fun(x):
        out = x.view((2, ms_torch.tensor(12)))
        return out

    msa_net = TestNet(view_shape_fun)
    msa_output = msa_net(ms_tensor)

    torch_tensor = torch.Tensor(data_np)
    torch_out = torch_tensor.view((2, torch.tensor(12)))
    param_compare(torch_out, msa_output, equal_nan=True)

def test_tensor_type_str():
    a = torch.FloatTensor(2)
    assert a.type() == 'torch.FloatTensor'

    b = torch.HalfTensor(3)
    assert b.type() == 'torch.HalfTensor'

def test_bool_add_mul():
    def add_func(x, y, z):
        out = x * y
        out = out.mul(y)
        out = out + z
        out = out.add(z)
        return out

    msa_net = TestNet(add_func)
    ms_x = ms_torch.tensor([True, True, False])
    ms_y = ms_torch.tensor([True, False, False])
    ms_z = ms_torch.tensor([False, True, True])
    msa_output = msa_net(ms_x, ms_y, ms_z)

    torch_x = torch.tensor([True, True, False])
    torch_y = torch.tensor([True, False, False])
    torch_z = torch.tensor([False, True, True])
    torch_out = add_func(torch_x, torch_y, torch_z)
    param_compare(torch_out, msa_output)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_var()
    test_narrow()
    test_norm()
    test_nanmean()
    test_nansum()
    test_argwhere()
    test_cross1()
    test_cross2()
    test_fill_diagonal_()
    test_fmax()
    test_fmin()
    test_H()
    test_histc()
    test_tensor_shape_with_zero()
    test_tensor_device()
    test_format()
    test_create_adapter_tensor_in_forward()
    test_tensor_with_tensor_shape()
    test_polygamma()
    test_polygamma_()
    test_apply_()
    test_diagonal_scatter()
    test_diagonal_scatter_graph()
    test_nanmean_float64()
    test_nansum_float64()
    test_narrow_copy()
    test_apply_fp64()
    test_data()
    test_new_full()
    test_cast_tensor_in_dict()
    test_device_equal()
    test_view_dynamic()
    test_bfloat16_tensor()
    test_bfloat16()
    test_cfloat()
    test_cdouble()
    test_is_set_to()
    test_logcumsumexp()
    test_new_tensor()
    test_tensor_np_shape()
    test_contiguous()
    test_reshape()
    test_zero_dimention()
    # test_make_subclass()
    test_mH()
    test_mT()
    test_storage_offset()
    test_view_dtype()
    test_view_shape_has_tensor()
    test_tensor_type_str()
    test_bool_add_mul()
