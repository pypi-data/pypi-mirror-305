#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindtorch.torch as ms_torch
import torch
import numpy as np
from ...utils import SKIP_ENV_ASCEND, set_mode_by_env_config, param_compare, TestNet

set_mode_by_env_config()

def test_ge1():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.int64)
    np_2 = np.array([[4, 2]]).astype(np.int64)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    msa_net = TestNet(ms_torch.ge)
    ms_out = msa_net(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch.ge(torch_tensor_1, torch_tensor_2)

    param_compare(torch_out, ms_out)


def test_ge2():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.half)

    ms_tensor_1 = ms_torch.tensor(np_1)
    msa_net = TestNet(ms_torch.ge)
    ms_out = msa_net(ms_tensor_1, 3.0)

    torch_tensor_1 = torch.tensor(np_1)
    torch_out = torch.ge(torch_tensor_1, 3.0)

    param_compare(torch_out, ms_out)


def test_gt1():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.int64)
    np_2 = np.array([[4, 2]]).astype(np.int64)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    msa_net = TestNet(ms_torch.gt)
    ms_out = msa_net(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch.gt(torch_tensor_1, torch_tensor_2)

    param_compare(torch_out, ms_out)


def test_gt2():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.half)

    ms_tensor_1 = ms_torch.tensor(np_1)
    msa_net = TestNet(ms_torch.gt)
    ms_out = msa_net(ms_tensor_1, 3.0)

    torch_tensor_1 = torch.tensor(np_1)
    torch_out = torch.gt(torch_tensor_1, 3.0)

    param_compare(torch_out, ms_out)


def test_le1():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.int64)
    np_2 = np.array([[4, 2]]).astype(np.int64)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    msa_net = TestNet(ms_torch.le)
    ms_out = msa_net(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch.le(torch_tensor_1, torch_tensor_2)

    param_compare(torch_out, ms_out)



def test_le2():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.half)

    ms_tensor_1 = ms_torch.tensor(np_1)
    msa_net = TestNet(ms_torch.le)
    ms_out = msa_net(ms_tensor_1, 3.0)

    torch_tensor_1 = torch.tensor(np_1)
    torch_out = torch.le(torch_tensor_1, 3.0)

    param_compare(torch_out, ms_out)



def test_lt1():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.int64)
    np_2 = np.array([[4, 2]]).astype(np.int64)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    msa_net = TestNet(ms_torch.lt)
    ms_out = msa_net(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch.lt(torch_tensor_1, torch_tensor_2)

    param_compare(torch_out, ms_out)



def test_lt2():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.half)

    ms_tensor_1 = ms_torch.tensor(np_1)
    msa_net = TestNet(ms_torch.lt)
    ms_out = msa_net(ms_tensor_1, 3.0)

    torch_tensor_1 = torch.tensor(np_1)
    torch_out = torch.lt(torch_tensor_1, 3.0)

    param_compare(torch_out, ms_out)


@SKIP_ENV_ASCEND(reason='maximum, minimum not support float64 input on Ascend')
def test_maximum_minimum_float64():
    np_array = np.random.randn(1, 2, 3, 4).astype(np.half)
    np_other = np.random.randn(1, 2, 3, 4).astype(np.double)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out1 = torch.maximum(torch_tensor, torch_other)
    torch_out2 = torch.minimum(torch_tensor, torch_other)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    msa_net1 = TestNet(ms_torch.maximum)
    ms_out1 = msa_net1(ms_tensor, ms_other)
    msa_net2 = TestNet(ms_torch.minimum)
    ms_out2 = msa_net2(ms_tensor, ms_other)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype

def test_maximum_minimum_float32():
    np_array = np.random.randn(1, 2, 3, 4).astype(np.half)
    np_other = np.random.randn(1, 2, 3, 4).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out1 = torch.maximum(torch_tensor, torch_other)
    torch_out2 = torch.minimum(torch_tensor, torch_other)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    msa_net1 = TestNet(ms_torch.maximum)
    ms_out1 = msa_net1(ms_tensor, ms_other)
    msa_net2 = TestNet(ms_torch.minimum)
    ms_out2 = msa_net2(ms_tensor, ms_other)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype


def test_eq():
    np_array = (np.random.rand(1, 2, 3, 4) * 5).astype(np.int32)
    np_other = np.random.rand(1, 2, 3, 4) * 5
    np_array = np_array.astype(np.int32)
    np_other = np_other.astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out = torch.eq(torch_tensor, torch_other)

    ms_tensor = ms_torch.tensor(np_array)
    ms_other = ms_torch.tensor(np_other)
    msa_net = TestNet(ms_torch.eq)
    ms_out = msa_net(ms_tensor, ms_other)

    param_compare(torch_out, ms_out)


def test_ne():
    x = np.random.randn(2, 3, 4)
    y = np.random.randn(3, 4)

    ms_x = ms_torch.tensor(x)
    ms_y = ms_torch.tensor(y)
    msa_net = TestNet(ms_torch.ne)
    ms_out = msa_net(ms_x, ms_y)

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch.ne(torch_x, torch_y)

    param_compare(torch_out, ms_out)


def test_equal():
    msa_net = TestNet(ms_torch.equal)
    torch_out = torch.equal(torch.tensor([1, 2]), torch.tensor([1, 2]))
    ms_out = msa_net(ms_torch.tensor([1, 2]), ms_torch.tensor([1, 2]))
    assert ms_out == torch_out
    assert type(ms_out) == type(torch_out)

    torch_out = torch.equal(torch.tensor([1., 1.]), torch.tensor([1.]))
    ms_out = msa_net(ms_torch.tensor([1., 1.]), ms_torch.tensor([1.]))
    assert ms_out == torch_out
    assert type(ms_out) == type(torch_out)

def test_greater_equal():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([1, 1, 4])

    ms_tensor_1 = ms_torch.tensor(np_1, dtype=ms_torch.float16)
    ms_tensor_2 = ms_torch.tensor(np_2, dtype=ms_torch.float16)
    msa_net = TestNet(ms_torch.ge)
    ms_out = msa_net(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1, dtype=torch.float16)
    torch_tensor_2 = torch.tensor(np_2, dtype=torch.float16)
    torch_out = torch.ge(torch_tensor_1, torch_tensor_2)

    param_compare(torch_out, ms_out)


def test_greater():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([1, 1, 4])

    ms_tensor_1 = ms_torch.tensor(np_1, dtype=ms_torch.float64)
    ms_tensor_2 = ms_torch.tensor(np_2, dtype=ms_torch.float64)
    msa_net = TestNet(ms_torch.ge)
    ms_out = msa_net(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1, dtype=torch.float64)
    torch_tensor_2 = torch.tensor(np_2, dtype=torch.float64)
    torch_out = torch.ge(torch_tensor_1, torch_tensor_2)

    param_compare(torch_out, ms_out)


def test_less_equal():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([1, 1, 4])

    ms_tensor_1 = ms_torch.tensor(np_1, dtype=ms_torch.double)
    ms_tensor_2 = ms_torch.tensor(np_2, dtype=ms_torch.double)
    msa_net = TestNet(ms_torch.less_equal)
    ms_out = msa_net(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1, dtype=torch.double)
    torch_tensor_2 = torch.tensor(np_2, dtype=torch.double)
    torch_out = torch.less_equal(torch_tensor_1, torch_tensor_2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_less():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([1, 1, 4])

    ms_tensor_1 = ms_torch.tensor(np_1, dtype=ms_torch.long)
    ms_tensor_2 = ms_torch.tensor(np_2, dtype=ms_torch.long)
    msa_net = TestNet(ms_torch.ge)
    ms_out = msa_net(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1, dtype=torch.long)
    torch_tensor_2 = torch.tensor(np_2, dtype=torch.long)
    torch_out = torch.ge(torch_tensor_1, torch_tensor_2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_not_equal():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([1, 1, 4])

    ms_tensor_1 = ms_torch.tensor(np_1, dtype=ms_torch.int32)
    ms_tensor_2 = ms_torch.tensor(np_2, dtype=ms_torch.int32)
    msa_net = TestNet(ms_torch.ge)
    ms_out = msa_net(ms_tensor_1, ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1, dtype=torch.int32)
    torch_tensor_2 = torch.tensor(np_2, dtype=torch.int32)
    torch_out = torch.ge(torch_tensor_1, torch_tensor_2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

if __name__ == '__main__':
    set_mode_by_env_config()()
    test_ge1()
    test_ge2()
    test_gt1()
    test_gt2()
    test_le1()
    test_le2()
    test_lt1()
    test_lt2()
    test_maximum_minimum_float64()
    test_maximum_minimum_float32()
    test_eq()
    test_ne()
    test_equal()
    test_greater_equal()
    test_greater()
    test_less_equal()
    test_less()
    test_not_equal()

