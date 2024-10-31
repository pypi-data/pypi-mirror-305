#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_view_as_real1():
    np_array = np.array([[[[1+2j, 3+4j, 5+6j]],[[10+20j, 30+40j, 50+60j]]]])

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.view_as_real(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.view_as_real(ms_tensor)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_view_as_real2():
    np_array = np.array([-2.1, 0, 1.0j])

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.view_as_real(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.view_as_real(ms_tensor)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_bincount1():
    np_array = np.random.randint(0, 8, (7,)).astype(np.uint8)
    weight_array = np.linspace(0, 2, len(np_array))

    torch_tensor = torch.tensor(np_array)
    torch_weight = torch.tensor(weight_array)
    torch_out = torch.bincount(torch_tensor, torch_weight)

    ms_tensor = ms_torch.tensor(np_array)
    ms_weight = ms_torch.tensor(weight_array)
    ms_out = ms_torch.bincount(ms_tensor, ms_weight)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_bincount2():
    np_array = np.random.randint(0, 4, (8,)).astype(np.int64)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch.bincount(torch_tensor, minlength=5)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.bincount(ms_tensor, minlength=5)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_nonzero1():
    np_array = np.random.random((2,3,4)).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.nonzero(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.nonzero(ms_tensor)

    param_compare(torch_out, ms_out)


def test_nonzero2():
    np_array = np.random.random((2,3,4)).astype(np.int32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.nonzero(torch_tensor, as_tuple=True)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.nonzero(ms_tensor, as_tuple=True)

    param_compare(torch_out, ms_out)

def test_nonzero3():
    np_array = np.array([1, 1, 1, 0, 1]).astype(np.float64)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.nonzero(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.nonzero(ms_tensor)

    param_compare(torch_out, ms_out)

def test_nonzero4():
    np_array = np.array([1, 1, 1, 0, 1]).astype(np.float16)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.nonzero(torch_tensor, as_tuple=True)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.nonzero(ms_tensor, as_tuple=True)

    param_compare(torch_out, ms_out)

def test_nonzero5():
    np_array = np.array([[-4, -3, -5],[-6, -7, -8]]).astype(np.bool_)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.nonzero(torch_tensor, as_tuple=True)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.nonzero(ms_tensor, as_tuple=True)

    param_compare(torch_out, ms_out)

def test_nonzero6():
    torch_tensor = torch.zeros(2,3, dtype=torch.bool)
    torch_out = torch.nonzero(torch_tensor, as_tuple=True)

    ms_tensor = ms_torch.zeros(2,3, dtype=ms_torch.bool)
    ms_out = ms_torch.nonzero(ms_tensor, as_tuple=True)

    param_compare(torch_out, ms_out)

def test_nonzero7():
    torch_tensor = torch.full((2,3,4), False)
    torch_out = torch.nonzero(torch_tensor, as_tuple=True)

    ms_tensor = ms_torch.full((2,3,4), False)
    ms_out = ms_torch.nonzero(ms_tensor, as_tuple=True)

    param_compare(torch_out, ms_out)

    torch_tensor2 = torch.full((2,3,4), False)
    torch_out2 = torch.nonzero(torch_tensor2)

    ms_tensor2 = ms_torch.full((2,3,4), False)
    ms_out2 = ms_torch.nonzero(ms_tensor2)

    param_compare(torch_out2, ms_out2)

def test_frombuffer():
    import array
    a = array.array('i', [1, 2, 3])
    torch_tensor = torch.frombuffer(a, dtype=torch.int32)
    ms_tensor = ms_torch.frombuffer(a, dtype=ms_torch.int32)

    assert np.allclose(torch_tensor.numpy(), ms_tensor.numpy())
    assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype


def test_as_strided1():
    np_array = np.random.random((3,3)).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.as_strided(torch_tensor, (2, 2), (1, 2))

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.as_strided(ms_tensor, (2, 2), (1, 2))

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype


def test_unique1():
    np_array = np.array([1, 3, 2, 3])
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.unique(torch_tensor)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.unique(ms_tensor)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

# def test_unique2():
#     np_array = np.array([1, 3, 2, 3])
#     torch_tensor = torch.tensor(np_array)
#     torch_out = torch.unique(torch_tensor, sorted=False)
#
#     ms_tensor = ms_torch.tensor(np_array)
#     ms_out = ms_torch.unique(ms_tensor, sorted=False)
#
#     assert np.allclose(ms_out.numpy(), torch_out.numpy())
#     assert ms_out.numpy().dtype == torch_out.numpy().dtype

def test_unique3():
    np_array = np.array([[1, 3], [2, 3]])
    torch_tensor = torch.tensor(np_array)
    torch_out = torch.unique(torch_tensor, sorted=True)

    ms_tensor = ms_torch.tensor(np_array)
    ms_out = ms_torch.unique(ms_tensor, sorted=True)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

# def test_unique4():
#     np_array = np.array([[1, 3], [2, 3]])
#     torch_tensor = torch.tensor(np_array)
#     torch_out = torch.unique(torch_tensor, sorted=False, return_inverse=True)
#
#     ms_tensor = ms_torch.tensor(np_array)
#     ms_out = ms_torch.unique(ms_tensor, sorted=False, return_inverse=True)
#
#     for i in range(len(torch_out)):
#         assert np.allclose(ms_out[i].numpy(), torch_out[i].numpy())

def test_scalar_tensor():
    torch_out1 = torch.scalar_tensor(1)
    ms_out1 = ms_torch.scalar_tensor(1)
    param_compare(torch_out1, ms_out1)

    torch_out2 = torch.scalar_tensor(1., dtype=torch.int64)
    ms_out2 = ms_torch.scalar_tensor(1., dtype=ms_torch.int64)
    param_compare(torch_out2, ms_out2)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_view_as_real1()
    test_view_as_real2()
    test_bincount1()
    test_bincount2()
    test_nonzero1()
    test_nonzero2()
    test_nonzero3()
    test_nonzero4()
    test_nonzero5()
    test_nonzero6()
    test_nonzero7()
    test_frombuffer()
    test_as_strided1()
    test_unique1()
    # test_unique2()
    test_unique3()
    # test_unique4()
    test_scalar_tensor()

