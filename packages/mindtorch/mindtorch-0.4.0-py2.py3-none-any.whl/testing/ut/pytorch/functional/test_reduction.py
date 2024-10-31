#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context
from mindtorch.torch.nn import Module
from ...utils import SKIP_ENV_GRAPH_MODE, set_mode_by_env_config, param_compare, SKIP_ENV_ASCEND, \
                     SKIP_ENV_GPU
set_mode_by_env_config()

def test_max():
    np_array = np.array([[1, 2],[3, 4]]).astype(np.int32)

    pt_tensor = torch.tensor(np_array)
    class MaxPt(torch.nn.Module):
        def __init__(self, dim=None, keepdim=False, out=None):
            super(MaxPt, self).__init__()
            self.dim = dim
            self.keepdim = keepdim
            self.out =out

        def forward(self, input):
            x = torch.max(input, dim=self.dim, keepdim=self.keepdim, out=self.out)
            return x

    pt_max1 = MaxPt(dim=0)
    pt_max2 = MaxPt(dim=1, keepdim=True)

    pt_out1 = pt_max1(pt_tensor)
    pt_out2 = pt_max2(pt_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    class MaxMs(Module):
        def __init__(self, dim=None, keepdim=False, out=None):
            super(MaxMs, self).__init__()
            self.dim = dim
            self.keepdim = keepdim
            self.out =out

        def forward(self, input):
            x = ms_torch.max(input, dim=self.dim, keepdim=self.keepdim, out=self.out)
            return x

    ms_max1 = MaxMs(dim=0)
    ms_max2 = MaxMs(dim=1, keepdim=True)

    ms_out1 = ms_max1(ms_tensor)
    ms_out2 = ms_max2(ms_tensor)

    param_compare(ms_out1, pt_out1)
    param_compare(ms_out2, pt_out2)

def test_max1():
    np_array = np.array([[1, 2],[3, 4]]).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.max(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.max(ms_tensor)

    param_compare(torch_out, ms_out)


@SKIP_ENV_GRAPH_MODE(reason="graph cannot support collections.namedtuple.")
def test_max2():
    np_array = np.array([[1, 2],[3, 4]]).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.max(torch_tensor, dim=1, keepdim=True)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.max(ms_tensor, dim=1, keepdim=True)

    param_compare(torch_out, ms_out)



@SKIP_ENV_GRAPH_MODE(reason="graph cannot support collections.namedtuple.")
def test_max3():
    np_array = np.array([1, 2, 3, 4]).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.max(torch_tensor, dim=0)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.max(ms_tensor, dim=0)

    param_compare(torch_out, ms_out)


def test_max4():
    np_array1 = (np.random.randn(2, 3) * 5).astype(np.int32)
    np_array2 = (np.random.randn(2, 3) * 5).astype(np.int32)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out = torch.max(input=torch_tensor1, other=torch_tensor2)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out = ms_torch.max(input=ms_tensor1, other=ms_tensor2)

    param_compare(torch_out, ms_out)


def test_mean_sum1():
    np_array = np.array([[1, 2],[9, 8]]).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.mean(torch_tensor, dim=0, keepdim=True, dtype=torch.float16)
    torch_out2 = torch.sum(torch_tensor, dim=0, keepdim=True, dtype=torch.float16)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out1 = ms_torch.mean(ms_tensor, dim=0, keepdim=True, dtype=ms_torch.float16)
    ms_out2 = ms_torch.sum(ms_tensor, dim=0, keepdim=True, dtype=ms_torch.float16)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)


def test_mean_sum2():
    np_array = np.array([[1, 2],[9, 8]]).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.mean(torch_tensor, dim=0, keepdim=True, dtype=torch.float)
    torch_out2 = torch.sum(torch_tensor, dim=0, keepdim=True, dtype=torch.float)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out1 = ms_torch.mean(ms_tensor, dim=0, keepdim=True, dtype=ms_torch.float)
    ms_out2 = ms_torch.sum(ms_tensor, dim=0, keepdim=True, dtype=ms_torch.float)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)


def test_mean_sum3():
    np_array = np.array([1, 2, 9, 8]).astype(np.double)

    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.mean(torch_tensor, dim=0)
    torch_out2 = torch.sum(torch_tensor, dim=0)
    torch_out3 = torch.mean(torch_tensor)
    torch_out4 = torch.sum(torch_tensor)
    ms_tensor = ms_torch.tensor(np_array)

    @ms.jit
    def test_ms_fn(ms_tensor):
        ms_out1 = ms_torch.mean(ms_tensor, dim=0)
        ms_out2 = ms_torch.sum(ms_tensor, dim=0)
        ms_out3 = ms_torch.mean(ms_tensor)
        ms_out4 = ms_torch.sum(ms_tensor)
        return ms_out1, ms_out2, ms_out3, ms_out4

    ms_out1, ms_out2, ms_out3, ms_out4 = test_ms_fn(ms_tensor)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)
    param_compare(torch_out4, ms_out4)


def test_mean_sum4():
    np_array = np.arange(0, 144).reshape(3, 3, 4, 4).astype(np.float32).astype(np.half)
    dim = (0, 2, 3)

    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.mean(torch_tensor, dim)
    torch_out2 = torch.sum(torch_tensor, dim)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out1 = ms_torch.mean(ms_tensor, dim)
    ms_out2 = ms_torch.sum(ms_tensor, dim)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)


def test_mean_sum5():
    np_array = np.array([2.0045, 2.0045, 2.0045]).astype(np.double)

    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.mean(torch_tensor, dtype=torch.float16)
    torch_out2 = torch.sum(torch_tensor, dtype=torch.float16)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out1 = ms_torch.mean(ms_tensor, dtype=ms_torch.float16)
    ms_out2 = ms_torch.sum(ms_tensor, dtype=ms_torch.float16)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_median1():
    np_array = np.arange(0, 36).astype(np.double)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.median(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.median(ms_tensor)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="graph cannot support collections.namedtuple.")
def test_median2():
    np_array = np.arange(0, 36).astype(np.double)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.median(torch_tensor, dim=0)
    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.median(ms_tensor, dim=0)
    assert np.allclose(ms_out.values.numpy(), torch_out.values.numpy())
    assert np.allclose(ms_out.indices.numpy(), torch_out.indices.numpy())
    assert ms_out.values.numpy().dtype == torch_out.values.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="graph cannot support collections.namedtuple.")
def test_median3():
    np_array = np.arange(0, 36).reshape(2, 3, 6).astype(np.double)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.median(torch_tensor, dim=1, keepdim=True)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.median(ms_tensor, dim=1, keepdim=True)

    assert np.allclose(ms_out.values.numpy(), torch_out.values.numpy())
    assert np.allclose(ms_out.indices.numpy(), torch_out.indices.numpy())
    assert ms_out.values.numpy().dtype == torch_out.values.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="graph cannot support collections.namedtuple.")
def test_median4():
    np_array = np.arange(0, 36).reshape(2, 3, 6).astype(np.int16)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.median(torch_tensor, dim=-1)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.median(ms_tensor, dim=-1)

    assert np.allclose(ms_out.values.numpy(), torch_out.values.numpy())
    assert np.allclose(ms_out.indices.numpy(), torch_out.indices.numpy())
    assert ms_out.values.numpy().dtype == torch_out.values.numpy().dtype


def test_min1():
    np_array = np.array([[1, 2],[3, 4]]).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.min(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.min(ms_tensor)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_min2():
    np_array = np.array([[1, 2],[3, 4]]).astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_out, torch_indices = torch.min(torch_tensor, dim=1)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out, ms_indices = ms_torch.min(ms_tensor,dim=1)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert np.allclose(ms_indices.asnumpy(), torch_indices.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_min3():
    np_array = np.array([[1, 2],[3, 4]]).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out, torch_indices = torch.min(torch_tensor, dim=1, keepdim=True)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out, ms_indices = ms_torch.min(ms_tensor, dim=1, keepdim=True)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert np.allclose(ms_indices.asnumpy(), torch_indices.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="graph cannot support out inplace.")
def test_min4():
    np_array = np.array([[1, 2],[4, 3]]).astype(np.float32)

    torch_out1 = torch.Tensor()
    torch_out2 = torch.LongTensor()
    torch_tensor = torch.tensor(np_array)
    torch_out, torch_indices = torch.min(torch_tensor, dim=1, keepdim=True, out=(torch_out1, torch_out2))

    ms_out1 = ms_torch.FloatTensor(2, 1)
    ms_out2 = ms_torch.IntTensor(2, 1)
    ms_tensor = ms_torch.tensor(np_array)
    ms_torch.min(ms_tensor, dim=1, keepdim=True, out=(ms_out1, ms_out2))

    assert np.allclose(ms_out1.asnumpy(), torch_out.numpy())
    assert np.allclose(ms_out2.asnumpy(), torch_indices.numpy())
    assert ms_out1.asnumpy().dtype == torch_out.numpy().dtype

def test_min5():
    np_array1 = (np.random.randn(2, 3) * 5).astype(np.int32)
    np_array2 = (np.random.randn(2, 3) * 5).astype(np.int32)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out = torch.min(input=torch_tensor1, other=torch_tensor2)

    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)
    ms_out = ms_torch.min(input=ms_tensor1, other=ms_tensor2)

    param_compare(torch_out, ms_out)

def test_prod():
    np_array = np.random.randn(2, 3, 4) * 2

    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch.prod(torch_tensor)
    torch_out2 = torch.prod(torch_tensor, dtype=int)
    torch_out3 = torch.prod(torch_tensor, dtype=torch.float32, dim=1, keepdim=False)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out1 = ms_torch.prod(ms_tensor)
    ms_out2 = ms_torch.prod(ms_tensor, dtype=int)
    ms_out3 = ms_torch.prod(ms_tensor, dtype=ms_torch.float32, dim=1, keepdim=False)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy())
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

def test_sum():
    int64_max = np.iinfo(np.int64).max
    torch_output = torch.sum(torch.tensor([int64_max, int64_max]), dtype=torch.int8)
    ms_output = ms_torch.sum(ms_torch.tensor([int64_max, int64_max]), dtype=ms_torch.int8)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

    torch_output = torch.sum(torch.tensor([int64_max, int64_max]), dtype=torch.float64)
    ms_output = ms_torch.sum(ms_torch.tensor([int64_max, int64_max]), dtype=ms_torch.float64)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

@SKIP_ENV_GPU(reason="ms.Tensor(float64_max).astype(ms.int16), gpu result is not the same as CPU, will have wrong result")
@SKIP_ENV_ASCEND(reason='ms.Tensor(float64_max).astype(ms.int16), ascend result is not the same as CPU, will have wrong result')
def test_sum_float64_max_to_int16():
    float64_max = np.finfo(np.float64).max
    torch_output = torch.sum(torch.tensor([float64_max, float64_max]), dtype=torch.int16)
    ms_output = ms_torch.sum(ms_torch.tensor([float64_max, float64_max]), dtype=ms_torch.int16)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

def test_sum_dim_list():
    a = np.random.randn(2, 3, 3)
    torch_output1 = torch.sum(torch.tensor(a), dim=[1])
    torch_output2 = torch.sum(torch.tensor(a), dim=[1, 0])
    ms_output1 = ms_torch.sum(ms_torch.tensor(a), dim=[1])
    ms_output2 = ms_torch.sum(ms_torch.tensor(a), dim=[1, 0])
    param_compare(torch_output1, ms_output1)
    param_compare(torch_output2, ms_output2)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_max()
    test_max1()
    test_max2()
    test_max3()
    test_max4()
    test_mean_sum1()
    test_mean_sum2()
    test_mean_sum3()
    test_mean_sum4()
    test_mean_sum5()
    test_median1()
    test_median2()
    test_median3()
    test_median4()
    test_min1()
    test_min2()
    test_min3()
    test_min4()
    test_min5()
    test_prod()
    test_sum()
    test_sum_dim_list()
