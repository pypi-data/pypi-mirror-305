import numpy as np
import mindspore as ms
import torch
from mindspore import context
import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()


def test_tensor_type_1():
    x = [[1, 2], [3, 4]]

    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch_x.type()

    ms_x = ms_torch.tensor(x, dtype=ms_torch.float32)
    ms_out = ms_x.type()
    assert (ms_out in torch_out)

def test_tensor_type_2():
    x = [[1, 2], [3, 4]]

    torch_x = torch.tensor(x, dtype=torch.double)
    torch_out = torch_x.type(torch.int)

    ms_x = ms_torch.tensor(x, dtype=ms_torch.double)
    ms_out = ms_x.type(ms_torch.int)
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

def test_tensor_type_3():
    x = [[1, 2], [3, 4]]

    torch_x = torch.tensor(x, dtype=torch.int64)
    torch_out = torch_x.type(torch.int64)

    ms_x = ms_torch.tensor(x, dtype=ms_torch.int64)
    ms_out = ms_x.type(ms_torch.int64)
    assert ms_out.numpy().dtype == torch_out.numpy().dtype
    assert id(ms_x) == id(ms_out)

def test_tensor_type_4():
    x = [[1, 2], [3, 4]]
    y = [1., 2.]

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out1 = torch_y.type()
    torch_out2 = torch_x.type(torch_out1)

    ms_x = ms_torch.tensor(x)
    ms_y = ms_torch.tensor(y)
    ms_out1 = ms_y.type()
    ms_out2 = ms_x.type(ms_out1)
    assert (ms_out1 in torch_out1)
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

def test_tensor_type_as():
    x = [[1, 2], [3, 4]]
    y = [1., 2.]

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch_x.type_as(torch_y)

    ms_x = ms_torch.tensor(x)
    ms_y = ms_torch.tensor(y)
    ms_out = ms_x.type_as(ms_y)
    assert torch_out.numpy().dtype == ms_out.numpy().dtype


def test_tensor_type_jit():
    x = [[1, 2], [3, 4]]
    y = [1., 2.]

    ms_x = ms_torch.tensor(x)
    ms_y = ms_torch.tensor(y)

    @ms.jit
    def fun1(ms_x, ms_y):
        return  ms_x.type_as(ms_y)
    ms_out1 = fun1(ms_x, ms_y)

    @ms.jit
    def fun2(ms_x, ms_y):
        ms_out1 = ms_y.type()
        ms_out2 = ms_x.type(ms_out1)
        return ms_out2
    ms_out2 = fun2(ms_x, ms_y)
    assert ms_out1.dtype == ms_out2.dtype

def test_type_with_TypeTensor():
    a_ms = ms_torch.tensor([2, 0])
    b_ms = a_ms.type(ms_torch.BoolTensor)
    a_pt = torch.tensor([2, 0])
    b_pt = a_pt.type(torch.BoolTensor)
    param_compare(b_ms, b_pt)

    a_ms = ms_torch.tensor([2., 0])
    @ms.jit
    def ms_type(a_ms):
        return a_ms.type(ms_torch.FloatTensor)
    b_ms = ms_type(a_ms)
    a_pt = torch.tensor([2., 0])
    b_pt = a_pt.type(torch.FloatTensor)
    param_compare(b_ms, b_pt)

def test_type_with_TypeTensor_str():
    a_ms = ms_torch.tensor([2, 0])
    b_ms = a_ms.type('ms_torch.BoolTensor')
    a_pt = torch.tensor([2, 0])
    b_pt = a_pt.type('torch.BoolTensor')
    param_compare(b_ms, b_pt)

    a_ms = ms_torch.tensor([2., 0])
    @ms.jit
    def ms_type(a_ms):
        return a_ms.type('ms_torch.BoolTensor')
    b_ms = ms_type(a_ms)
    a_pt = torch.tensor([2., 0])
    b_pt = a_pt.type('torch.BoolTensor')
    param_compare(b_ms, b_pt)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_tensor_type_1()
    test_tensor_type_2()
    test_tensor_type_3()
    test_tensor_type_4()

    test_tensor_type_as()
    test_tensor_type_jit()
    test_type_with_TypeTensor()
    test_type_with_TypeTensor_str()
