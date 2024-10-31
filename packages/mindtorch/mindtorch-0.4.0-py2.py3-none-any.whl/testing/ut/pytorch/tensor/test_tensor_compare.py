#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_ge():
    x = [[1, 2], [3, 4]]
    y = [[1, 1], [4, 4]]

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch_x.ge(torch_y)

    ms_x = ms_torch.tensor(x)
    ms_y = ms_torch.tensor(y)
    ms_out = ms_x.ge(ms_y)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

def test_gt():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.int64)
    np_2 = np.array([[4, 2]]).astype(np.int64)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_out = ms_tensor_1.gt(ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch_tensor_1.gt(torch_tensor_2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_le():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.int64)
    np_2 = np.array([[4, 2]]).astype(np.int64)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_out = ms_tensor_1.le(ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch_tensor_1.le(torch_tensor_2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_lt():
    np_1 = np.array([[1, 2],[3, 4]]).astype(np.int64)
    np_2 = np.array([[4, 2]]).astype(np.int64)

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_out = ms_tensor_1.lt(ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_out = torch_tensor_1.lt(torch_tensor_2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_eq():
    x = np.random.randint(4, size=(2, 3, 4))
    other = np.random.randint(4, size=(2, 3, 4))

    torch_x = torch.tensor(x)
    torch_other = torch.tensor(other)

    ms_x = ms_torch.tensor(x)
    ms_other = ms_torch.tensor(other)

    torch_out1 = torch_x.eq(torch_other)
    ms_out1 = ms_x.eq(ms_other)
    torch_out2 = torch_x.eq(3)
    ms_out2 = ms_x.eq(3)

    assert np.allclose(ms_out1.numpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.numpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype

def test_ne():
    x = np.random.randn(2, 3, 4)
    y = np.random.randn(3, 4)

    ms_x = ms_torch.tensor(x)
    ms_y = ms_torch.tensor(y)
    ms_out = ms_x.ne(ms_y)

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch_x.ne(torch_y)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_equal():
    torch_x = torch.tensor([1, 2])
    torch_out = torch_x.equal(torch.tensor([1, 2]))

    ms_x = ms_torch.tensor([1, 2])
    ms_out = ms_x.equal(ms_torch.tensor([1, 2]))
    assert ms_out == torch_out
    assert type(ms_out) == type(torch_out)

    torch_x = torch.tensor([1., 1.])
    torch_out = torch_x.equal(torch.tensor([1.]))
    ms_x = ms_torch.tensor([1., 1.])
    ms_out = ms_x.equal(ms_torch.tensor([1.]))
    assert ms_out == torch_out
    assert type(ms_out) == type(torch_out)

def test_greater_equal():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([1, 1, 4])

    ms_tensor_1 = ms_torch.tensor(np_1, dtype=ms_torch.float16)
    ms_tensor_2 = ms_torch.tensor(np_2, dtype=ms_torch.float16)
    ms_out = ms_tensor_1.ge(ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1, dtype=torch.float16)
    torch_tensor_2 = torch.tensor(np_2, dtype=torch.float16)
    torch_out = torch_tensor_1.ge(torch_tensor_2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_greater():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([1, 1, 4])

    ms_tensor_1 = ms_torch.tensor(np_1, dtype=ms_torch.float64)
    ms_tensor_2 = ms_torch.tensor(np_2, dtype=ms_torch.float64)
    ms_out = ms_tensor_1.ge(ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1, dtype=torch.float64)
    torch_tensor_2 = torch.tensor(np_2, dtype=torch.float64)
    torch_out = torch_tensor_1.ge(torch_tensor_2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_less_equal():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([1, 1, 4])

    ms_tensor_1 = ms_torch.tensor(np_1, dtype=ms_torch.double)
    ms_tensor_2 = ms_torch.tensor(np_2, dtype=ms_torch.double)
    ms_out = ms_tensor_1.less_equal(ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1, dtype=torch.double)
    torch_tensor_2 = torch.tensor(np_2, dtype=torch.double)
    torch_out = torch_tensor_1.less_equal(torch_tensor_2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_less():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([1, 1, 4])

    ms_tensor_1 = ms_torch.tensor(np_1, dtype=ms_torch.long)
    ms_tensor_2 = ms_torch.tensor(np_2, dtype=ms_torch.long)
    ms_out = ms_tensor_1.ge(ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1, dtype=torch.long)
    torch_tensor_2 = torch.tensor(np_2, dtype=torch.long)
    torch_out = torch_tensor_1.ge(torch_tensor_2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_not_equal():
    np_1 = np.array([1, 2, 3])
    np_2 = np.array([1, 1, 4])

    ms_tensor_1 = ms_torch.tensor(np_1, dtype=ms_torch.int32)
    ms_tensor_2 = ms_torch.tensor(np_2, dtype=ms_torch.int32)
    ms_out = ms_tensor_1.ge(ms_tensor_2)

    torch_tensor_1 = torch.tensor(np_1, dtype=torch.int32)
    torch_tensor_2 = torch.tensor(np_2, dtype=torch.int32)
    torch_out = torch_tensor_1.ge(torch_tensor_2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

if __name__ == '__main__':
    set_mode_by_env_config()
    test_ge()
    test_gt()
    test_le()
    test_lt()
    test_eq()
    test_equal()
    test_greater_equal()
    test_greater()
    test_less_equal()
    test_not_equal()
    test_less()
    test_ne()
