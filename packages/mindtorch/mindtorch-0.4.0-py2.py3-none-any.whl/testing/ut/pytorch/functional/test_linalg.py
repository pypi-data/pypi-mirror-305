#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context
from mindtorch.utils import is_under_gpu_context
from ...utils import SKIP_ENV_ASCEND, SKIP_ENV_CPU, SKIP_ENV_GPU, SKIP_ENV_GRAPH_MODE, is_test_under_ascend_context, \
    is_test_under_pynative_context, param_compare, type_shape_compare, SKIP_ENV_ASCEND_GRAPH_MODE, \
    is_test_under_gpu_context, grad_test

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

@SKIP_ENV_GRAPH_MODE(reason='eigh not support on graph mode')
def test_eigh():
    a = np.array([[ 1.+0.j, -0.-2.j],
           [ 0.+2.j,  5.+0.j]])

    torch_tensor = torch.tensor(a)
    ms_tensor = ms_torch.tensor(a)

    torch_l, torch_q = torch.linalg.eigh(torch_tensor)
    ms_l, ms_q = ms_torch.linalg.eigh(ms_tensor)

    assert np.allclose(torch_l.numpy(), ms_l.numpy())
    assert np.allclose(torch_q.numpy(), ms_q.numpy())

@SKIP_ENV_GRAPH_MODE(reason='solve not support on graph mode')
def test_solve():
    a = np.random.randn(3, 3)
    b = np.random.randn(3,)

    torch_a = torch.tensor(a)
    ms_a = ms_torch.tensor(a)

    torch_b = torch.tensor(b)
    ms_b = ms_torch.tensor(b)

    torch_x = torch.linalg.solve(torch_a, torch_b)
    ms_x = ms_torch.linalg.solve(ms_a, ms_b)

    #TODO: mindspore has problem supporting numpy trans to ms.Tensor
    '''
    @ms.jit
    def func(a, b):
        x = ms_torch.linalg.solve(a, b)
        return x
    ms_x1 = func(ms_a, ms_b)
    '''

    param_compare(torch_x, ms_x)
    #param_compare(torch_x, ms_x1)

def test_slogdet():
    data1 = np.random.randn(3, 3)
    data2 = np.random.randn(2, 3, 4, 4)

    x = torch.tensor(data1)
    torch_out1 = torch.linalg.slogdet(x)
    x = torch.tensor(data2)
    torch_out2 = torch.linalg.slogdet(x)

    x = ms_torch.tensor(data1)
    ms_out1 = ms_torch.linalg.slogdet(x)
    x = ms_torch.tensor(data2)
    ms_out2 = ms_torch.linalg.slogdet(x)

    assert np.allclose(ms_out1[0].asnumpy(), torch_out1[0].numpy())
    assert ms_out1[0].asnumpy().dtype == torch_out1[0].numpy().dtype
    assert np.allclose(ms_out1[1].asnumpy(), torch_out1[1].numpy())
    assert ms_out1[1].asnumpy().dtype == torch_out1[1].numpy().dtype

    assert np.allclose(ms_out2[0].asnumpy(), torch_out2[0].numpy())
    assert ms_out2[0].asnumpy().dtype == torch_out2[0].numpy().dtype
    assert np.allclose(ms_out2[1].asnumpy(), torch_out2[1].numpy())
    assert ms_out2[1].asnumpy().dtype == torch_out2[1].numpy().dtype

def test_det():
    a1 = np.random.randn(3, 3)
    a2 = np.random.randn(3, 2, 2)
    torch_a1 = torch.tensor(a1)
    torch_a2 = torch.tensor(a2)
    torch_out1 = torch.linalg.det(torch_a1)
    torch_out2 = torch.linalg.det(torch_a2)
    ms_a1 = ms_torch.tensor(a1)
    ms_a2 = ms_torch.tensor(a2)
    ms_out1 = ms_torch.linalg.det(ms_a1)
    ms_out2 = ms_torch.linalg.det(ms_a2)
    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

def test_cholesky():
    A1 = np.random.randn(3, 2, 2).astype(np.float32)

    torch_A1 = torch.tensor(A1)
    torch_A1 = torch_A1 @ torch_A1.mT.conj() + torch.eye(2)
    torch_out1 = torch.linalg.cholesky(torch_A1)

    ms_A1 = ms_torch.tensor(A1)
    ms_A1 = ms_A1 @ ms_A1.mT.conj() + ms_torch.eye(2)
    ms_out1 = ms_torch.linalg.cholesky(ms_A1)

    param_compare(torch_out1, ms_out1)

@SKIP_ENV_ASCEND(reason="cholesky currently not support float64 on Ascend")
def test_cholesky_fp64():
    A1 = np.random.randn(2, 2).astype(np.float64)
    A1 = A1 @ A1.T.conj() + np.eye(2).astype(np.float64)

    torch_A1 = torch.tensor(A1)
    torch_A1 = torch_A1 @ torch_A1.T.conj() + torch.eye(2)
    torch_out1 = torch.linalg.cholesky(torch_A1)

    ms_A1 = ms_torch.tensor(A1)
    ms_A1 = ms_A1 @ ms_A1.T.conj() + ms_torch.eye(2)
    ms_out1 = ms_torch.linalg.cholesky(ms_A1)

    param_compare(torch_out1, ms_out1)

def test_cholesky_ex():
    A1 = np.random.randn(3, 2, 2).astype(np.float32)

    torch_A1 = torch.tensor(A1)
    torch_A1 = torch_A1 @ torch_A1.mT.conj() + torch.eye(2)
    torch_out1 = torch.linalg.cholesky_ex(torch_A1)
    torch_out2 = torch.linalg.cholesky_ex(torch_A1, upper=True)

    ms_A1 = ms_torch.tensor(A1)
    ms_A1 = ms_A1 @ ms_A1.mT.conj() + ms_torch.eye(2)
    ms_out1 = ms_torch.linalg.cholesky_ex(ms_A1)
    ms_out2 = ms_torch.linalg.cholesky_ex(ms_A1, upper=True)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

@SKIP_ENV_GPU(reason="cholesky_ex currently not support int32 input on GPU")
def test_cholesky_ex_int():
    A1 = np.random.randn(2, 2).astype(np.int32)

    torch_A1 = torch.tensor(A1)
    torch_A1 = torch_A1 @ torch_A1.mT.conj() + torch.eye(2)
    torch_out1, torch_info = torch.linalg.cholesky_ex(torch_A1)

    ms_A1 = ms_torch.tensor(A1)
    ms_A1 = ms_A1 @ ms_A1.mT.conj() + ms_torch.eye(2)
    ms_out1, ms_info = ms_torch.linalg.cholesky_ex(ms_A1)

    param_compare(torch_out1, ms_out1)
    assert torch_info == ms_info

@SKIP_ENV_ASCEND(reason="cholesky_ex currently not support float64 on Ascend")
def test_cholesky_ex_fp64():
    A1 = np.random.randn(2, 2)

    torch_A1 = torch.tensor(A1)
    torch_A1 = torch_A1 @ torch_A1.mT.conj() + torch.eye(2)
    torch_out1, torch_info1 = torch.linalg.cholesky_ex(torch_A1)
    ms_A1 = ms_torch.tensor(A1)
    ms_A1 = ms_A1 @ ms_A1.mT.conj() + ms_torch.eye(2)
    ms_out1, ms_info1 = ms_torch.linalg.cholesky_ex(ms_A1)

    param_compare(torch_out1, ms_out1)
    assert torch_info1 == ms_info1

def test_inv():
    A = np.random.randn(4, 4)
    torch_A = torch.tensor(A)
    ms_A = ms_torch.tensor(A)
    torch_out = torch.linalg.inv(torch_A)
    ms_out = ms_torch.linalg.inv(ms_A)
    param_compare(torch_out, ms_out)

    A = np.random.randn(2, 3, 4, 4)
    torch_A = torch.tensor(A)
    ms_A = ms_torch.tensor(A)
    torch_out = torch.linalg.inv(torch_A)
    ms_out = ms_torch.linalg.inv(ms_A)
    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="inv currently not support complex128 on Ascend")
def test_inv_complex():
    A = np.random.randn(4, 4).astype(np.complex128)
    torch_A = torch.tensor(A)
    ms_A = ms_torch.tensor(A)
    torch_out = torch.linalg.inv(torch_A)
    ms_out = ms_torch.linalg.inv(ms_A)
    param_compare(torch_out, ms_out)

def test_inv_ex():
    A = np.random.randn(2, 3, 4, 4)
    torch_A = torch.tensor(A)
    ms_A = ms_torch.tensor(A)
    torch_out = torch.linalg.inv_ex(torch_A)
    ms_out = ms_torch.linalg.inv_ex(ms_A)
    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="inv_ex currently not support complex128 on Ascend")
def test_inv_ex_complex():
    A = np.random.randn(4, 4).astype(np.complex128)
    torch_A = torch.tensor(A)
    ms_A = ms_torch.tensor(A)
    torch_out, torch_info = torch.linalg.inv_ex(torch_A)
    ms_out, ms_info = ms_torch.linalg.inv_ex(ms_A)
    param_compare(torch_out, ms_out)
    assert torch_info == ms_info

@SKIP_ENV_ASCEND(reason='matmul not support input dtype as float64 on Ascend')
def test_matmul_float64():
    a = np.random.randn(3).astype(np.float64)
    b = np.random.randn(3).astype(np.float64)
    torch_tensor1 = torch.tensor(a)
    torch_tensor2 = torch.tensor(b)
    torch_out1 = torch.linalg.matmul(torch_tensor1, torch_tensor2)
    ms_tensor1 = ms_torch.tensor(a)
    ms_tensor2 = ms_torch.tensor(b)
    ms_out1 = ms_torch.linalg.matmul(ms_tensor1, ms_tensor2)
    param_compare(torch_out1, ms_out1)

@SKIP_ENV_GPU(reason='matmul not support input dtype as complex128 on GPU')
@SKIP_ENV_ASCEND(reason='matmul not support input dtype as complex128 on Ascend')
def test_matmul_complex128():
    a = np.random.randn(3, 4).astype(np.complex128)
    b = np.random.randn(4).astype(np.complex128)
    torch_tensor1 = torch.tensor(a)
    torch_tensor2 = torch.tensor(b)
    torch_out2 = torch.linalg.matmul(torch_tensor1, torch_tensor2)
    ms_tensor1 = ms_torch.tensor(a)
    ms_tensor2 = ms_torch.tensor(b)
    ms_out2 = ms_torch.linalg.matmul(ms_tensor1, ms_tensor2)
    param_compare(torch_out2, ms_out2)

def test_matmul_int32():
    a = np.random.randn(10, 3, 4).astype(np.int32)
    b = np.random.randn(4, 5).astype(np.int32)
    torch_tensor1 = torch.tensor(a)
    torch_tensor2 = torch.tensor(b)
    torch_out3 = torch.linalg.matmul(torch_tensor1, torch_tensor2)
    ms_tensor1 = ms_torch.tensor(a)
    ms_tensor2 = ms_torch.tensor(b)
    ms_out3 = ms_torch.linalg.matmul(ms_tensor1, ms_tensor2)

    param_compare(torch_out3, ms_out3)

def test_diagonal():
    a = np.random.randn(3, 3).astype(np.float64)
    b = np.random.randint(0, 10, size=(3, 3)).astype(np.int64)
    x = np.random.randn(2, 5, 4, 2).astype(np.float16)

    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_x = torch.tensor(x)
    torch_out1 = torch.linalg.diagonal(torch_a, offset=0)
    torch_out2 = torch.linalg.diagonal(torch_b, offset=1)
    torch_out3 = torch.linalg.diagonal(torch_x, offset=-1, dim1=1, dim2=2)

    ms_a = ms_torch.tensor(a)
    ms_b = ms_torch.tensor(b)
    ms_x = ms_torch.tensor(x)
    ms_out1 = ms_torch.linalg.diagonal(ms_a, offset=0)
    ms_out2 = ms_torch.linalg.diagonal(ms_b, offset=1)
    ms_out3 = ms_torch.linalg.diagonal(ms_x, offset=-1, dim1=1, dim2=2)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype

@SKIP_ENV_GPU(reason='multi_dot not support input dtype as int64')
@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: ms.ops.Matmul not support int64 input on Ascend.")
def test_multi_dot_int64():
    torch_out1 = torch.linalg.multi_dot([torch.tensor([1, 2]), torch.tensor([2, 3])])
    ms_out1 = ms_torch.linalg.multi_dot([ms.Tensor([1, 2]), ms.Tensor([2, 3])])
    param_compare(torch_out1, ms_out1)

    A = np.arange(2 * 3).reshape(2, 3)
    B = np.arange(3 * 2).reshape(3, 2)
    C = np.arange(2 * 2).reshape(2, 2)

    torch_A = torch.tensor(A)
    torch_B = torch.tensor(B)
    torch_C = torch.tensor(C)
    torch_out4 = torch.linalg.multi_dot((torch_A, torch_B, torch_C))

    ms_A = torch.tensor(A)
    ms_B = torch.tensor(B)
    ms_C = torch.tensor(C)
    ms_out4 = torch.linalg.multi_dot((ms_A, ms_B, ms_C))

    param_compare(torch_out4, ms_out4)


def test_multi_dot():
    torch_out2 = torch.linalg.multi_dot([torch.tensor([[1, 2]], dtype=torch.float32),
                                         torch.tensor([2, 3], dtype=torch.float32)])
    ms_out2 = ms_torch.linalg.multi_dot([ms.Tensor([[1, 2]], dtype=ms.float32),
                                         ms.Tensor([2, 3], dtype=ms.float32)])
    param_compare(torch_out2, ms_out2)

@SKIP_ENV_ASCEND(reason="multi_dot currently not support float64 on Ascend")
def test_multi_dot_fp64():
    torch_out3 = torch.linalg.multi_dot([torch.tensor([[1, 2]], dtype=torch.float64),
                                        torch.tensor([[2], [3]], dtype=torch.float64)])
    ms_out3 = ms_torch.linalg.multi_dot([ms.Tensor([[1, 2]], dtype=ms.float64),
                                        ms.Tensor([[2], [3]], dtype=ms.float64)])
    param_compare(torch_out3, ms_out3)

def test_householder_product():
    h = np.random.randn(3, 3, 3, 2, 2).astype(np.complex128)
    tau = np.random.randn(3, 3, 3, 2).astype(np.complex128)

    torch_h = torch.tensor(h)
    torch_tau = torch.tensor(tau)
    torch_out1 = torch.linalg.householder_product(torch_h, torch_tau)

    ms_h = ms_torch.tensor(h)
    ms_tau = ms_torch.tensor(tau)
    ms_out1 = ms_torch.linalg.householder_product(ms_h, ms_tau)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason='lu not support on graph mode')
def test_lu():
    #TODO: Currently not support 3-D (*, M, N) input
    for type1 in (np.float32, np.float64):
        np_array1 = np.random.randn(4, 4).astype(type1)
        np_array2 = np.random.randn(6, 6).astype(type1)
        torch_tensor1 = torch.tensor(np_array1)
        ms_tensor1 = ms_torch.tensor(np_array1)
        torch_tensor2 = torch.tensor(np_array2)
        ms_tensor2 = ms_torch.tensor(np_array2)

        torch_p1, torch_l1, torch_u1 = torch.linalg.lu(torch_tensor1)
        torch_p2, torch_l2, torch_u2 = torch.linalg.lu(torch_tensor2)
        ms_p1, ms_l1, ms_u1 = ms_torch.linalg.lu(ms_tensor1)
        ms_p2, ms_l2, ms_u2 = ms_torch.linalg.lu(ms_tensor2)

        param_compare(torch_p1, ms_p1)
        param_compare(torch_p2, ms_p2)
        param_compare(torch_l1, ms_l1)
        param_compare(torch_l2, ms_l2)
        param_compare(torch_u1, ms_u1)
        param_compare(torch_u2, ms_u2)

        grad_test('lu', ms_torch.linalg.lu, ms_tensor1)


@SKIP_ENV_GRAPH_MODE(reason='lu_factor not support on graph mode')
def test_lu_factor():
    #TODO: Currently not support 3-D (*, M, N) input
    for type1 in (np.float32, np.float64):
        np_array1 = np.random.randn(3, 3).astype(type1)
        np_array2 = np.random.randn(6, 6).astype(type1)
        torch_tensor1 = torch.tensor(np_array1)
        ms_tensor1 = ms_torch.tensor(np_array1)
        torch_tensor2 = torch.tensor(np_array2)
        ms_tensor2 = ms_torch.tensor(np_array2)

        torch_lu1, torch_pivot1 = torch.linalg.lu_factor(torch_tensor1)
        torch_lu2, torch_pivot2 = torch.linalg.lu_factor(torch_tensor2)
        ms_lu1, ms_pivot1 = ms_torch.linalg.lu_factor(ms_tensor1)
        ms_lu2, ms_pivot2 = ms_torch.linalg.lu_factor(ms_tensor2)

        param_compare(torch_lu1, ms_lu1)
        param_compare(torch_lu2, ms_lu2)
        param_compare(torch_pivot1, ms_pivot1)
        param_compare(torch_pivot2, ms_pivot2)

        grad_test('lu_factor', ms_torch.linalg.lu_factor, ms_tensor1)
    

@SKIP_ENV_GRAPH_MODE(reason='lu_factor_ex not support on graph mode')
def test_lu_factor_ex():
    for type1 in (np.float32, np.float64):
        #TODO: Currently not support 3-D (*, M, N) input
        np_array1 = np.random.randn(3, 3).astype(type1)
        np_array2 = np.random.randn(6, 6).astype(type1)
        torch_tensor1 = torch.tensor(np_array1)
        ms_tensor1 = ms_torch.tensor(np_array1)
        torch_tensor2 = torch.tensor(np_array2)
        ms_tensor2 = ms_torch.tensor(np_array2)

        torch_lu1, torch_pivot1, torch_info1 = torch.linalg.lu_factor_ex(torch_tensor1)
        torch_lu2, torch_pivot2, torch_info2 = torch.linalg.lu_factor_ex(torch_tensor2)
        ms_lu1, ms_pivot1, ms_info1 = ms_torch.linalg.lu_factor_ex(ms_tensor1)
        ms_lu2, ms_pivot2, ms_info2 = ms_torch.linalg.lu_factor_ex(ms_tensor2)

        param_compare(torch_lu1, ms_lu1)
        param_compare(torch_lu2, ms_lu2)
        param_compare(torch_pivot1, ms_pivot1)
        param_compare(torch_pivot2, ms_pivot2)
        assert ms_info1 == torch_info1
        assert ms_info2 == torch_info2

@SKIP_ENV_GRAPH_MODE(reason="nn.cell currently has memcpy problem in graph mode")
def test_lstsq():
    if is_test_under_ascend_context():
        # lstsq Prim not support float64 on Ascend.
        _type = (np.float32,)
    else:
        _type = (np.float32, np.float64)

    for type1 in _type:
        x1 = np.random.randn(5,5).astype(type1)
        A1 = np.random.randn(5,5).astype(type1)
        x2 = np.random.randn(6,7).astype(type1)
        A2 = np.random.randn(6,7).astype(type1)
        torch_a1 = torch.tensor(A1)
        torch_x1 = torch.tensor(x1)
        ms_a1 = ms_torch.tensor(A1)
        ms_x1 = ms_torch.tensor(x1)
        torch_a2 = torch.tensor(A2)
        torch_x2 = torch.tensor(x2)
        ms_a2 = ms_torch.tensor(A2)
        ms_x2 = ms_torch.tensor(x2)

        torch_x1, torch_res1, torch_rank1, _ = torch.linalg.lstsq(torch_a1,torch_x1)
        ms_x1, ms_res1, ms_rank1, _ = ms_torch.linalg.lstsq(ms_a1, ms_x1)
        torch_x2, torch_res2, torch_rank2, _ = torch.linalg.lstsq(torch_a2, torch_x2)
        ms_x2, ms_res2, ms_rank2, _ = ms_torch.linalg.lstsq(ms_a2, ms_x2)
        param_compare(torch_x1, ms_x1, atol=1e-4)
        param_compare(torch_x2, ms_x2, atol=1e-4)
        param_compare(torch_res1, ms_res1, atol=1e-4)
        param_compare(torch_res2, ms_res2, atol=1e-4)
        assert torch_rank1 == ms_rank1
        assert torch_rank2 == ms_rank2
        #TODO: pytorch return s=[], while numpy returns narray
        grad_test('lstsq', ms_torch.linalg.lstsq, ms_x1, ms_a1)

def test_qr():
    np_array = np.random.randn(2,3).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = ms_torch.tensor(np_array)
    torch_q1, torch_r1 = torch.linalg.qr(torch_tensor)
    ms_q1, ms_r1 = ms_torch.linalg.qr(ms_tensor)
    torch_q2, torch_r2 = torch.linalg.qr(torch_tensor, mode="complete")
    ms_q2, ms_r2 = ms_torch.linalg.qr(ms_tensor, mode="complete")

    param_compare(torch_q1, ms_q1, atol=1e-6)
    param_compare(torch_q2, ms_q2, atol=1e-6)
    param_compare(torch_r1, ms_r1, atol=1e-6)
    param_compare(torch_r2, ms_r2, atol=1e-6)

def test_vander():
    np_array = [1, 2, 3, 4, 5]
    torch_tensor = torch.tensor(np_array)
    ms_tensor = ms_torch.tensor(np_array)

    torch_out1 = torch.linalg.vander(torch_tensor)
    torch_out2 = torch.linalg.vander(torch_tensor, N=3)
    torch_out3 = torch.linalg.vander(torch_tensor, N=4)
    ms_out1 = ms_torch.linalg.vander(ms_tensor)
    ms_out2 = ms_torch.linalg.vander(ms_tensor, N=3)
    ms_out3 = ms_torch.linalg.vander(ms_tensor, N=4)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

@SKIP_ENV_GPU("test_eigvals only test on CPU and Ascend, which encapsulates the ms.ops.eig")
def test_eigvals():
    np_array = np.random.randn(3, 3).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = ms_torch.tensor(np_array)
    torch_out = torch.linalg.eigvals(torch_tensor)
    ms_out = ms_torch.linalg.eigvals(ms_tensor)
    assert np.allclose(np.sort(np.abs(torch_out.numpy())), np.sort(np.abs(ms_out.numpy())), atol=1e-5)
    type_shape_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND("test_eigvals_grad only test on GPU because it encapsulates the numpy.linalg.eig")
@SKIP_ENV_CPU("test_eigvals_gpu only test on GPU because it encapsulates the numpy.linalg.eig")
@SKIP_ENV_GRAPH_MODE("eigvals have prolem on GPU when using graph mode")
def test_eigvals_grad():
    np_array = np.random.randn(2, 2).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = ms_torch.tensor(np_array)
    torch_out = torch.linalg.eigvals(torch_tensor)
    ms_out = ms_torch.linalg.eigvals(ms_tensor)
    assert np.allclose(np.sort(np.abs(torch_out.numpy())), np.sort(np.abs(ms_out.numpy())), atol=1e-5)
    type_shape_compare(torch_out, ms_out)
    #grad_test('eigvals', ms_torch.linalg.eigvals, ms_tensor)

@SKIP_ENV_ASCEND_GRAPH_MODE("Ascend encapsulate numpy func, which has PyInterpret problem on Graph mode")
def test_svd():
    data = np.random.randn(5, 3).astype(np.float32)
    torch_tensor = torch.tensor(data)
    ms_tensor = ms_torch.tensor(data)
    torch_u1 = torch.linalg.svd(torch_tensor).U
    torch_s1 = torch.linalg.svd(torch_tensor).S
    torch_v1 = torch.linalg.svd(torch_tensor).Vh
    torch_u2 = torch.linalg.svd(torch_tensor, full_matrices=False).U
    torch_s2 = torch.linalg.svd(torch_tensor, full_matrices=False).S
    torch_v2 = torch.linalg.svd(torch_tensor, full_matrices=False).Vh
    if is_test_under_pynative_context():
        ms_u1 = ms_torch.linalg.svd(ms_tensor).U
        ms_s1 = ms_torch.linalg.svd(ms_tensor).S
        ms_v1 = ms_torch.linalg.svd(ms_tensor).Vh
        ms_u2 = ms_torch.linalg.svd(ms_tensor, full_matrices=False).U
        ms_s2 = ms_torch.linalg.svd(ms_tensor, full_matrices=False).S
        ms_v2 = ms_torch.linalg.svd(ms_tensor, full_matrices=False).Vh
    else:
        ms_u1, ms_s1, ms_v1 = ms_torch.linalg.svd(ms_tensor)
        ms_u2, ms_s2, ms_v2 = ms_torch.linalg.svd(ms_tensor, full_matrices=False)

    type_shape_compare(torch_u1, ms_u1)
    param_compare(torch_s1, ms_s1)
    type_shape_compare(torch_v1, ms_v1)
    type_shape_compare(torch_u2, ms_u2)
    param_compare(torch_s2, ms_s2)
    type_shape_compare(torch_v2, ms_v2)
    torch_dist1 = torch.dist(torch_tensor, torch.mm(torch.mm(torch_u1[:, :3], torch.diag(torch_s1)), torch_v1))
    ms_dist1 = ms_torch.dist(ms_tensor, ms_torch.mm(ms_torch.mm(ms_u1[:, :3], ms_torch.diag(ms_s1)), ms_v1))
    torch_dist2 = torch.dist(torch_tensor, torch.mm(torch.mm(torch_u2, torch.diag(torch_s2)), torch_v2))
    ms_dist2 = ms_torch.dist(ms_tensor, ms_torch.mm(ms_torch.mm(ms_u2, ms_torch.diag(ms_s2)), ms_v2))
    param_compare(torch_dist1, ms_dist1, atol=1e-5)
    param_compare(torch_dist2, ms_dist2, atol=1e-5)

@SKIP_ENV_ASCEND_GRAPH_MODE("Ascend encapsulate numpy func, which has PyInterpret problem on Graph mode")
def test_svdvals():
    for type1 in (np.float32, np.float64):
        data = np.random.randn(5, 3).astype(type1)
        torch_tensor = torch.tensor(data)
        ms_tensor = ms_torch.tensor(data)
        torch_out1 = torch.linalg.svdvals(torch_tensor)
        ms_out1 = ms_torch.linalg.svdvals(ms_tensor)

        param_compare(torch_out1, ms_out1)

def test_matrix_power():
    np_array = np.random.rand(4, 4, 4)
    for type1 in (np.float64, np.float32):
        np_array1 = np_array.astype(type1)
        torch_tensor1 = torch.tensor(np_array1)
        ms_tensor1 = ms_torch.tensor(np_array1)
        torch_out1 = torch.linalg.matrix_power(torch_tensor1, 0)
        torch_out2 = torch.linalg.matrix_power(torch_tensor1, 3)
        ms_out1 = ms_torch.linalg.matrix_power(ms_tensor1, 0)
        ms_out2 = ms_torch.linalg.matrix_power(ms_tensor1, 3)
        #TODO: GPU currently not support n < 0
        if not is_test_under_gpu_context():
            torch_out3 = torch.matrix_power(torch_tensor1, -3)
            ms_out3 = ms_torch.matrix_power(ms_tensor1, -3)
            param_compare(ms_out3, torch_out3, rtol=1e-3, atol=1e-4)
        param_compare(ms_out1, torch_out1)
        param_compare(ms_out2, torch_out2)

@SKIP_ENV_ASCEND(reason="pinv currently not support on Ascend")
def test_pinv():
    np_array1 = np.random.rand(3, 5)
    np_array2 = np.random.rand(2, 6, 3)
    np_array3 = np.random.rand(6, 6)
    for type1 in (np.float64, np.float32):
        np_array1 = np_array1.astype(type1)
        np_array2 = np_array2.astype(type1)
        torch_tensor1 = torch.tensor(np_array1)
        torch_tensor2 = torch.tensor(np_array2)
        torch_tensor3 = torch.tensor(np_array3)
        ms_tensor1 = ms_torch.tensor(np_array1)
        ms_tensor2 = ms_torch.tensor(np_array2)
        ms_tensor3 = ms_torch.tensor(np_array3)
        torch_out1 = torch.linalg.pinv(torch_tensor1)
        torch_out2 = torch.linalg.pinv(torch_tensor2)
        torch_out3 = torch.linalg.pinv(torch_tensor3, hermitian=True)
        ms_out1 = ms_torch.linalg.pinv(ms_tensor1)
        ms_out2 = ms_torch.linalg.pinv(ms_tensor2)
        ms_out3 = ms_torch.linalg.pinv(ms_tensor3, hermitian=True)

        param_compare(ms_out1, torch_out1, atol=1e-5)
        param_compare(ms_out2, torch_out2, atol=1e-5)
        param_compare(ms_out3, torch_out3, atol=1e-5)

@SKIP_ENV_GRAPH_MODE(reason='eigvalsh not support on graph mode')
def test_eigvalsh():
    a = np.random.randn(3, 3).astype(np.float32)
    b = np.array([[ 1.+0.j, -0.-2.j], [ 0.+2.j,  5.+0.j]])
    c = np.array([[ 1.+1.j, -0.-2.j], [ 0.+2.j,  5.+1.j]])

    torch_tensor1 = torch.tensor(a)
    ms_tensor1 = ms_torch.tensor(a)
    torch_tensor2 = torch.tensor(b)
    ms_tensor2 = ms_torch.tensor(b)
    torch_tensor3 = torch.tensor(c)
    ms_tensor3 = ms_torch.tensor(c)

    torch_output1 = torch.linalg.eigvalsh(torch_tensor1)
    ms_output1 = ms_torch.linalg.eigvalsh(ms_tensor1)
    torch_output2 = torch.linalg.eigvalsh(torch_tensor2)
    ms_output2 = ms_torch.linalg.eigvalsh(ms_tensor2)
    torch_output3 = torch.linalg.eigvalsh(torch_tensor3)
    ms_output3 = ms_torch.linalg.eigvalsh(ms_tensor3)
    torch_output4 = torch.linalg.eigvalsh(torch_tensor3, UPLO='U')
    ms_output4 = ms_torch.linalg.eigvalsh(ms_tensor3, UPLO='U')

    param_compare(torch_output1, ms_output1)
    param_compare(torch_output2, ms_output2)
    param_compare(torch_output3, ms_output3)
    param_compare(torch_output4, ms_output4)
    #TODO: mindspore has problem supporting numpy trans to ms.Tensor
    '''
    grad_test('eigvalsh', ms_torch.linalg.eigvalsh, ms_tensor1)
    @ms.jit
    def fun(tensor1):
        ms_output1 = ms_torch.linalg.eigvalsh(tensor1)
        return ms_output1
    ms_output5 = fun(ms_tensor1)
    param_compare(torch_output1, ms_output5)
    '''

def test_norm():
    x = np.random.randn(2, 2)
    y = np.random.randn(2, 4)
    torch_tensor1 = torch.tensor(x)
    torch_tensor2 = torch.tensor(y)
    ms_tensor1 = ms_torch.tensor(x)
    ms_tensor2 = ms_torch.tensor(y)
    t_r1 = torch.linalg.norm(torch_tensor1)
    t_r2 = torch.linalg.norm(torch_tensor2)
    t_r3 = torch.linalg.norm(torch_tensor2, 'fro')
    ms_r1 = ms_torch.linalg.norm(ms_tensor1)
    ms_r2 = ms_torch.linalg.norm(ms_tensor2)
    ms_r3 = ms_torch.linalg.norm(ms_tensor2, 'fro')

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r3, ms_r3)

@SKIP_ENV_ASCEND(reason="Ascend not support nuclear norm, float('inf') and ord=int")
def test_norm_advanced():
    y = np.random.randn(2, 4)
    torch_tensor = torch.tensor(y)
    ms_tensor = ms_torch.tensor(y)
    t_r1 = torch.linalg.norm(torch_tensor, 2)
    t_r2 = torch.linalg.norm(torch_tensor, -2)
    t_r3 = torch.linalg.norm(torch_tensor, 'nuc')
    t_r4 = torch.linalg.norm(torch_tensor, float('inf'))
    ms_r1 = ms_torch.linalg.norm(ms_tensor, 2)
    ms_r2 = ms_torch.linalg.norm(ms_tensor, -2)
    ms_r3 = ms_torch.linalg.norm(ms_tensor, 'nuc')
    ms_r4 = ms_torch.linalg.norm(ms_tensor, float('inf'))

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r3, ms_r3)
    param_compare(t_r4, ms_r4)

def test_vector_norm():
    x = np.arange(9, dtype=np.float32) - 4.0
    y = x.reshape((3, 3))
    torch_tensor1 = torch.tensor(x)
    torch_tensor2 = torch.tensor(y)
    ms_tensor1 = ms_torch.tensor(x)
    ms_tensor2 = ms_torch.tensor(y)

    t_r1 = torch.linalg.vector_norm(torch_tensor1)
    t_r2 = torch.linalg.vector_norm(torch_tensor2)
    t_r3 = torch.linalg.vector_norm(torch_tensor2, float('-inf'))
    t_r4 = torch.linalg.vector_norm(torch_tensor2, float('inf'))
    ms_r1 = ms_torch.linalg.vector_norm(ms_tensor1)
    ms_r2 = ms_torch.linalg.vector_norm(ms_tensor2)
    ms_r3 = ms_torch.linalg.vector_norm(ms_tensor2, float('-inf'))
    ms_r4 = ms_torch.linalg.vector_norm(ms_tensor2, float('inf'))

    #The result when ord < 0 on Ascend is not correct
    if not is_test_under_ascend_context():
        t_r = torch.linalg.vector_norm(torch_tensor2, -1)
        ms_r = ms_torch.linalg.vector_norm(ms_tensor2, -1)
        param_compare(t_r, ms_r)

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r4, ms_r4)

# TODO: vecdot is only supported in torch2.0, uncomment torch result after switching to latest torch
def test_vecdot():
    # v1 = np.random.randn(3, 2).astype(np.float32)
    # v2 = np.random.randn(3, 2)
    # torch_v1 = torch.tensor(v1)
    # torch_v2 = torch.tensor(v2)
    v1 = np.array([[ 0.20327474,  2.09068204], [-1.39672132, -0.70987052], [ 0.08028283,  1.01100276]])
    v2 = np.array([[ 0.41353498, -0.8191005 ], [ 0.31328247,  0.59503497], [ 0.92232394, -0.51092646]])
    ms_v1 = ms_torch.tensor(v1)
    ms_v2 = ms_torch.tensor(v2)

    # torch_out = torch.linalg.vecdot(torch_v1, torch_v2)
    ms_out = ms_torch.linalg.vecdot(ms_v1, ms_v2)

    # assert torch_out.numpy().dtype == ms_out.numpy().dtype
    # assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert ms_out.dtype == ms.float64
    assert np.allclose(ms_out.numpy(), np.array([-1.62841749, -0.85996609, -0.44250129]))

def test_matrix_norm():
    x = np.random.randn(2, 3, 4).astype(np.float32)
    torch_tensor1 = torch.tensor(x)
    ms_tensor1 = ms_torch.tensor(x)
    t_r1 = torch.linalg.matrix_norm(torch_tensor1)
    t_r2 = torch.linalg.matrix_norm(torch_tensor1, dim=(0, -1))
    t_r3 = torch.linalg.matrix_norm(torch_tensor1, dim=(0, -1), keepdim=True)
    ms_r1 = ms_torch.linalg.matrix_norm(ms_tensor1)
    ms_r2 = ms_torch.linalg.matrix_norm(ms_tensor1, dim=(0, -1))
    ms_r3 = ms_torch.linalg.matrix_norm(ms_tensor1, dim=(0, -1), keepdim=True)

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r3, ms_r3)

def test_matrix_norm_ord1():
    y = np.random.randn(2, 3).astype(np.float32)
    torch_tensor = torch.tensor(y)
    ms_tensor = ms_torch.tensor(y)
    t_r1 = torch.linalg.matrix_norm(torch_tensor, 1)
    t_r2 = torch.linalg.matrix_norm(torch_tensor, -1)
    t_r3 = torch.linalg.matrix_norm(torch_tensor, float('inf'))
    t_r4 = torch.linalg.matrix_norm(torch_tensor, float('-inf'))
    ms_r1 = ms_torch.linalg.matrix_norm(ms_tensor, 1)
    ms_r2 = ms_torch.linalg.matrix_norm(ms_tensor, -1)
    ms_r3 = ms_torch.linalg.matrix_norm(ms_tensor, float('inf'))
    ms_r4 = ms_torch.linalg.matrix_norm(ms_tensor, float('-inf'))

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r3, ms_r3)
    param_compare(t_r4, ms_r4)

@SKIP_ENV_ASCEND(reason="Ascend not support nuclear norm, and -2/2 norm")
def test_matrix_norm_ord2():
    y = np.random.randn(2, 3).astype(np.float32)
    torch_tensor = torch.tensor(y)
    ms_tensor = ms_torch.tensor(y)
    t_r1 = torch.linalg.matrix_norm(torch_tensor, 2)
    t_r2 = torch.linalg.matrix_norm(torch_tensor, -2)
    t_r3 = torch.linalg.matrix_norm(torch_tensor, 'nuc')
    ms_r1 = ms_torch.linalg.matrix_norm(ms_tensor, 2)
    ms_r2 = ms_torch.linalg.matrix_norm(ms_tensor, -2)
    ms_r3 = ms_torch.linalg.matrix_norm(ms_tensor, 'nuc')

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r3, ms_r3)

@SKIP_ENV_ASCEND(reason="matrix_norm currently not support float64 on Ascend")
def test_matrix_norm_fp64():
    x = np.random.randn(2, 3, 4)
    torch_tensor1 = torch.tensor(x)
    ms_tensor1 = ms_torch.tensor(x)
    t_r1 = torch.linalg.matrix_norm(torch_tensor1)
    ms_r1 = ms_torch.linalg.matrix_norm(ms_tensor1)

    param_compare(t_r1, ms_r1)

def test_matrix_rank():
    A_t = torch.eye(10)
    A_ms = ms_torch.eye(10)
    torch_out1 = torch.linalg.matrix_rank(A_t)
    torch_out2 = torch.linalg.matrix_rank(A_t, hermitian=True)
    torch_out3 = torch.linalg.matrix_rank(A_t, atol=1.0, rtol=0.0)

    ms_out1 = ms_torch.linalg.matrix_rank(A_ms)
    ms_out2 = ms_torch.linalg.matrix_rank(A_ms, hermitian=True)
    ms_out3 = ms_torch.linalg.matrix_rank(A_ms, atol=1.0, rtol=0.0)
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)
    '''
    @ms.jit
    def my_test(A):
        ms_out = ms_torch.linalg.matrix_rank(A)
        return ms_out
    ms_out4 = my_test(A_ms)
    param_compare(torch_out1, ms_out4)
    '''

def test_matrix_rank_4d():
    A = np.random.randn(2, 4, 3, 3).astype(np.float32)
    A_t = torch.tensor(A)
    A_ms = ms_torch.tensor(A)
    torch_out1 = torch.linalg.matrix_rank(A_t)
    ms_out1 = ms_torch.linalg.matrix_rank(A_ms)
    param_compare(torch_out1, ms_out1)

@SKIP_ENV_GPU(reason="cross currently not support on GPU")
def test_cross():
    np_1 = np.random.randn(2, 3, 3).astype(np.float32)
    np_2 = np.random.randn(2, 3, 3).astype(np.float32)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.cross(ms_tensor_1, ms_tensor_2)
    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.cross(torch_tensor_1, torch_tensor_2)
    param_compare(ms_result, torch_result)

@SKIP_ENV_ASCEND(reason="solve_triangular currently not support on Ascend")
def test_solve_triangular():
    np_array1 = np.random.randn(3, 3).astype(np.float32)
    np_array2 = np.random.randn(3, 4).astype(np.float32)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)

    A_t = torch_tensor1.triu()
    A_t1 = torch_tensor1.tril()
    X_t = torch.linalg.solve_triangular(A_t, torch_tensor2, upper=True)
    X_t1 = torch.linalg.solve_triangular(A_t1, torch_tensor2, upper=False, unitriangular=True)

    A_ms1 = ms_tensor1.tril()
    A_ms = ms_tensor1.triu()
    X_ms = ms_torch.linalg.solve_triangular(A_ms, ms_tensor2, upper=True)
    X_ms1 = ms_torch.linalg.solve_triangular(A_ms1, ms_tensor2, upper=False, unitriangular=True)

    param_compare(X_t, X_ms)
    param_compare(X_t1, X_ms1)

@SKIP_ENV_ASCEND(reason="solve_triangular currently not support on Ascend")
def test_solve_triangular_3d():
    np_array1 = np.random.randn(2, 3, 3).astype(np.float32)
    np_array2 = np.random.randn(2, 3, 4).astype(np.float32)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = ms_torch.tensor(np_array1)
    ms_tensor2 = ms_torch.tensor(np_array2)

    A_t = torch_tensor1.triu()
    X_t = torch.linalg.solve_triangular(A_t, torch_tensor2, upper=True, unitriangular=True)
    A_ms = ms_tensor1.triu()
    X_ms = ms_torch.linalg.solve_triangular(A_ms, ms_tensor2, upper=True, unitriangular=True)
    param_compare(X_t, X_ms)

@SKIP_ENV_ASCEND(reason="cond currently not support complex input on Ascend")
def test_cond_complex128():
    x = np.random.randn(3, 3).astype(np.complex128)
    torch_tensor1 = torch.tensor(x)
    ms_tensor1 = ms_torch.tensor(x)
    t_r1 = torch.linalg.cond(torch_tensor1)
    t_r2 = torch.linalg.cond(torch_tensor1, -2)
    ms_r1 = ms_torch.linalg.cond(ms_tensor1)
    ms_r2 = ms_torch.linalg.cond(ms_tensor1, -2)

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)

@SKIP_ENV_ASCEND(reason="cond currently not support complex input on Ascend")
def test_cond_complex64():
    y = np.random.randn(3, 3).astype(np.complex64)
    torch_tensor1 = torch.tensor(y)
    ms_tensor1 = ms_torch.tensor(y)
    t_r1 = torch.linalg.cond(torch_tensor1, 'fro')
    t_r2 = torch.linalg.cond(torch_tensor1, 'nuc')
    ms_r1 = ms_torch.linalg.cond(ms_tensor1, 'fro')
    ms_r2 = ms_torch.linalg.cond(ms_tensor1, 'nuc')

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)

@SKIP_ENV_ASCEND(reason="ms.ops.cond not support on Ascend")
def test_cond_float():
    y = np.random.randn(4, 4).astype(np.float32)
    torch_tensor1 = torch.tensor(y)
    ms_tensor1 = ms_torch.tensor(y)
    t_r1 = torch.linalg.cond(torch_tensor1)
    t_r2 = torch.linalg.cond(torch_tensor1, 1)
    t_r3 = torch.linalg.cond(torch_tensor1, float('inf'))
    ms_r1 = ms_torch.linalg.cond(ms_tensor1)
    ms_r2 = ms_torch.linalg.cond(ms_tensor1, 1)
    ms_r3 = ms_torch.linalg.cond(ms_tensor1, float('inf'))

    param_compare(t_r1, ms_r1)
    param_compare(t_r2, ms_r2)
    param_compare(t_r3, ms_r3)

@SKIP_ENV_GRAPH_MODE(reason='lu_solve not support on graph mode')
def test_lu_solve():
    # lu_solve Prim not support float64 on Ascend
    lu_array = np.random.randn(3, 3).astype(np.float32)
    b_array = np.random.randn(3, 1).astype(np.float32)
    p_array = np.random.randint(1, 3, size=3).astype(np.int32)

    torch_lu = torch.tensor(lu_array)
    torch_pivot = torch.tensor(p_array)
    torch_b = torch.tensor(b_array)

    ms_lu = ms_torch.tensor(lu_array)
    ms_pivot = ms_torch.tensor(p_array)
    ms_b = ms_torch.tensor(b_array)

    torch_out1 = torch.lu_solve(torch_b, torch_lu, torch_pivot)
    #TODO: torch 1.12.1 not support adjoint
    #torch_out2 = torch.lu_solve(torch_b1, torch_lu1, torch_pivot1, adjoint=True)
    ms_out1 = ms_torch.linalg.lu_solve(ms_b, ms_lu, ms_pivot)
    #ms_out2 = ms_torch.linalg.lu_solve(ms_b1, ms_lu1, ms_pivot1, adjoint=True)

    param_compare(torch_out1, ms_out1)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_eigh()
    test_solve()
    test_slogdet()
    test_det()
    test_cholesky()
    test_cholesky_int()
    test_inv()
    test_matmul_float64()
    test_matmul_complex128()
    test_matmul_int32()
    test_diagonal()
    test_multi_dot_int64()
    test_multi_dot()
    test_householder_product()
    test_lu()
    test_lu_factor()
    test_lu_factor_ex()
    test_lstsq()
    test_qr()
    test_vander()
    test_eigvals()
    test_eigvals_grad()
    test_svd()
    test_svdvals()
    test_matrix_power()
    test_pinv()
    test_eigvalsh()
    test_norm()
    test_norm_advanced()
    test_vector_norm()
    # test_vecdot()
    test_cholesky_fp64()
    test_multi_dot_fp64()
    test_inv_complex()
    test_cholesky_ex()
    test_cholesky_ex_fp64()
    test_inv_ex()
    test_inv_ex_complex()
    test_matrix_norm()
    test_matrix_norm_ord1()
    test_matrix_norm_ord2()
    test_matrix_norm_fp64()
    test_matrix_rank()
    test_matrix_rank_4d()
    test_cross()
    test_solve_triangular()
    test_solve_triangular_3d()
    test_cond_complex128()
    test_cond_complex64()
    test_cond_float()
    test_lu_solve()