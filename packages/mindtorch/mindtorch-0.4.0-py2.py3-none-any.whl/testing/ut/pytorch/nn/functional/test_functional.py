#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindtorch.torch as ms_torch
import numpy as np
import mindspore as ms
import torch
from mindtorch.torch.nn.functional import interpolate, adaptive_avg_pool2d
from mindtorch.utils import is_under_ascend_context
from ....utils import SKIP_ENV_GPU, set_mode_by_env_config, param_compare, SKIP_ENV_ASCEND, SKIP_ENV_ASCEND, \
    SKIP_ENV_CPU, TestNet
set_mode_by_env_config()



def test_interpolate1():
    tensor = np.arange(1, 5).reshape((1, 1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.interpolate(torch_tensor, size=[3, torch.tensor(3)],
                                                   mode="bilinear", align_corners=True)

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = interpolate(ms_tensor, size=[3, ms_torch.tensor(3)], mode="bilinear", align_corners=True)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())


def test_interpolate2():
    tensor = np.arange(1, 5).reshape((1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.interpolate(torch_tensor, scale_factor=4, mode='linear', align_corners=True)

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = interpolate(ms_tensor, scale_factor=4, mode='linear', align_corners=True)

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

def test_interpolate3():
    tensor = np.arange(1, 5).reshape((1, 1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.interpolate(torch_tensor, size=3, mode="bilinear", align_corners=False)

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = interpolate(ms_tensor, size=3, mode="bilinear", align_corners=False)

    param_compare(torch_output, ms_output)

def test_interpolate4():
    tensor = np.arange(1, 5).reshape((1, 1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.interpolate(torch_tensor, size=3, mode="nearest")

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = interpolate(ms_tensor, size=3, mode="nearest")

    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

def test_interpolate5():
    tensor = np.arange(1, 5).reshape((1, 1, 1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.interpolate(torch_tensor, mode="nearest", scale_factor=[1, 1, 1])

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = interpolate(ms_tensor, mode="nearest", scale_factor=[1, 1, 1])

    param_compare(torch_output, ms_output)

def test_interpolate6():
    tensor = np.random.randn(2, 2).reshape((1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.interpolate(torch_tensor, size=3, mode="nearest")

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = interpolate(ms_tensor, size=3, mode="nearest")

    param_compare(torch_output, ms_output)

def test_interpolate7():
    tensor = np.arange(1, 5).reshape((1, 1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    # TODO: when align_corners=False, mindspore result is the same as TensorFlow result,
    # but different from the result of PyTorch   
    torch_output = torch.nn.functional.interpolate(torch_tensor, size=3, mode="bicubic", align_corners=True)

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = interpolate(ms_tensor, size=3, mode="bicubic", align_corners=True)

    param_compare(torch_output, ms_output)

def test_interpolate8():
    tensor = np.arange(1, 5).reshape((1, 1, 1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.interpolate(torch_tensor, size=3, mode="trilinear")

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = interpolate(ms_tensor, size=3, mode="trilinear")

    param_compare(torch_output, ms_output)

def test_interpolate9():
    tensor = np.arange(1, 5).reshape((1, 1, 1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.interpolate(torch_tensor, size=3, mode="area")

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = interpolate(ms_tensor, size=3, mode="area")

    param_compare(torch_output, ms_output)

@SKIP_ENV_GPU(reason="currently nearest-exact mode not support on GPU")
def test_interpolate10():
    tensor = np.arange(1, 5).reshape((1, 1, 2, 2)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.interpolate(torch_tensor, size=3, mode="nearest-exact")

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = interpolate(ms_tensor, size=3, mode="nearest-exact")

    param_compare(torch_output, ms_output)

def test_interpolate_scale_factor():
    data = np.random.randn(1, 2, 3, 4, 5)
    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.interpolate(torch_tensor, scale_factor=(2, 2, 2), mode="trilinear")

    ms_tensor = ms_torch.tensor(data)
    ms_output = interpolate(ms_tensor, scale_factor=(2, 2, 2), mode="trilinear")

    param_compare(torch_output, ms_output)

def test_adaptive_avg_pool2d():
    tensor = np.random.randn(1, 32, 9, 9).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.adaptive_avg_pool2d(torch_tensor, (3, 5))

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = adaptive_avg_pool2d(ms_tensor, (3, 5))

    assert (torch_output.shape == ms_output.shape)
    #TODO assert np.allclose(ms_output.asnumpy(), torch_output.numpy())


def test_upsample_nearest1():
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.upsample_nearest(torch_tensor, (3, 5))

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.upsample_nearest(ms_tensor, (3, 5))

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-4)

def test_upsample_nearest2():
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.upsample_nearest(torch_tensor, 3)

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.upsample_nearest(ms_tensor, 3)

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-4)

def test_upsample_nearest3():
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.upsample_nearest(torch_tensor, scale_factor=2)

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.upsample_nearest(ms_tensor, scale_factor=2)

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-4)

#TODO: Unsupported op [UpsampleNearest3D] on CPU
'''
def test_upsample_nearest4():
    data = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.upsample_nearest(torch_tensor, (3, 4, 5))

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.upsample_nearest(ms_tensor, (3, 4, 5))

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-4)

def test_upsample_nearest5():
    data = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.upsample_nearest(torch_tensor, scale_factor=2)

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.upsample_nearest(ms_tensor, scale_factor=2)

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-4)

def test_upsample_nearest6():
    data = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.upsample_nearest(torch_tensor, 3)

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.upsample_nearest(ms_tensor, 3)

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-4)
'''

def test_upsample_bilinear1():
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.upsample_bilinear(torch_tensor, (3, 5))

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.upsample_bilinear(ms_tensor, (3, 5))

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-4)

def test_upsample_bilinear2():
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.upsample_bilinear(torch_tensor, 3)

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.upsample_bilinear(ms_tensor, 3)

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-4)

def test_upsample_bilinear3():
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.upsample_bilinear(torch_tensor, scale_factor=2)

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.upsample_bilinear(ms_tensor, scale_factor=2)

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-4)

def test_upsample_bilinear_list_scale_factor():
    data = np.random.randn(2, 3, 4, 5).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.upsample_bilinear(torch_tensor, scale_factor=[2, 3])

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.upsample_bilinear(ms_tensor, scale_factor=[2, 3])

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-4)

def test_adaptive_avg_pool1d():
    data = np.random.randint(0, 10, [1, 3, 6]).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.adaptive_avg_pool1d(torch_tensor, output_size=2)

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.adaptive_avg_pool1d(ms_tensor, output_size=2)

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-5)

def test_adaptive_max_pool1d():
    data = np.random.randint(0, 10, [1, 3, 6]).astype(np.float32)

    torch_tensor = torch.tensor(data)
    torch_output = torch.nn.functional.adaptive_max_pool1d(torch_tensor, output_size=2)

    ms_tensor = ms_torch.tensor(data)
    ms_output = ms_torch.nn.functional.adaptive_max_pool1d(ms_tensor, output_size=2)

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy(), atol=1e-5)


def test_adaptive_max_pool2d():
    tensor = np.random.randn(1, 32, 9, 9).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.adaptive_max_pool2d(torch_tensor, [3, 5])

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = ms_torch.nn.functional.adaptive_max_pool2d(ms_tensor, [3, 5])

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-2)
    else:
        param_compare(ms_output, torch_output)

def test_adaptive_max_pool2d_3d_input():
    tensor = np.random.randn(32, 9, 9).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.adaptive_max_pool2d(torch_tensor, (3, 5))

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = ms_torch.nn.functional.adaptive_max_pool2d(ms_tensor, (3, 5))

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-2)
    else:
        param_compare(ms_output, torch_output)


def test_adaptive_max_pool2d_3d_input_return_indice_true():
    tensor = np.random.randn(32, 9, 9).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.adaptive_max_pool2d(torch_tensor, (3, 5), True)

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = ms_torch.nn.functional.adaptive_max_pool2d(ms_tensor, (3, 5), True)

    if is_under_ascend_context():
        param_compare(ms_output, torch_output, atol=1e-2)
    else:
        param_compare(ms_output, torch_output)

def test_adaptive_avg_pool3d():
    tensor = np.random.randn(1, 32, 9, 9, 9).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.adaptive_avg_pool3d(torch_tensor, [3, 5, 3])

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = ms_torch.nn.functional.adaptive_avg_pool3d(ms_tensor, [3, 5, 3])

    assert (torch_output.shape == ms_output.shape)
    assert np.allclose(ms_output.numpy(), torch_output.numpy(), atol=1e-6)


def test_adaptive_max_pool3d():
    tensor = np.random.randn(1, 32, 9, 9, 9).astype(np.float32)

    torch_tensor = torch.tensor(tensor)
    torch_output = torch.nn.functional.adaptive_max_pool3d(torch_tensor, (3, 5, 3))

    ms_tensor = ms_torch.tensor(tensor)
    ms_output = ms_torch.nn.functional.adaptive_max_pool3d(ms_tensor, (3, 5, 3))

    if is_under_ascend_context():
        # Custom implementation only ensures shape consistency
        assert ms_output.shape == torch_output.size()
        # param_compare(ms_output, torch_output, atol=1e-3)
    else:
        param_compare(ms_output, torch_output)


def test_affine_grid1():
    size = (1, 1, 3, 2)
    theta_np = np.array([[0.5, 0, 0.75], [0, 0.75, 0]]).reshape(1, 2, 3)

    torch_size = torch.Size(size)
    torch_theta = torch.from_numpy(theta_np)
    torch_out = torch.nn.functional.affine_grid(torch_theta, torch_size)

    ms_torch_size = ms_torch.Size(size)
    ms_torch_theta = ms_torch.from_numpy(theta_np)
    ms_torch_out = ms_torch.nn.functional.affine_grid(ms_torch_theta, ms_torch_size)
    assert (torch_out.shape == ms_torch_out.shape)
    assert np.allclose(torch_out.numpy(), ms_torch_out.numpy())

def test_affine_grid2():
    theta = [[[0.8, 0.5, 0],[-0.5, 0.8, 0]]]
    size_ones = np.ones((1, 3, 2, 3))

    torch_ones = torch.tensor(size_ones)
    torch_size = torch_ones.size()
    torch_theta = torch.tensor(theta, dtype=torch.float32)
    torch_out = torch.nn.functional.affine_grid(torch_theta, torch_size, align_corners=True)

    ms_torch_ones = ms_torch.tensor(size_ones)
    ms_torch_size = ms_torch_ones.size()
    ms_torch_theta = ms_torch.tensor(theta, dtype=ms_torch.float32)
    ms_torch_out = ms_torch.nn.functional.affine_grid(ms_torch_theta, ms_torch_size, align_corners=True)
    assert (torch_out.shape == ms_torch_out.shape)
    assert np.allclose(torch_out.numpy(), ms_torch_out.numpy())

def test_tanh():
    input_np = np.random.randn(2, 3)

    torch_in = torch.tensor(input_np)
    torch_out = torch.nn.functional.tanh(torch_in)

    ms_in = ms_torch.tensor(input_np)
    ms_out = ms_torch.nn.functional.tanh(ms_in)

    param_compare(torch_out, ms_out)

def test_tanh_complex():
    np_1 = np.random.randn(2, 3).astype(np.complex64)
    np_2 = (np.random.randn(2, 3) * 1j).astype(np.complex64)

    ms_in = ms_torch.tensor(np_1 + np_2)
    torch_in = torch.tensor(np_1 + np_2)
    torch_out = torch.nn.functional.tanh(torch_in)
    ms_out = ms_torch.nn.functional.tanh(ms_in)

    param_compare(torch_out, ms_out)

def test_tanhshrink():
    input_np = np.random.randn(2, 3, 3)

    torch_in = torch.tensor(input_np)
    torch_out = torch.nn.functional.tanhshrink(torch_in)

    ms_in = ms_torch.tensor(input_np)
    ms_out = ms_torch.nn.functional.tanhshrink(ms_in)

    param_compare(torch_out, ms_out)

def test_tanhshrink_complex():
    np_1 = np.random.randn(2, 3).astype(np.complex64)
    np_2 = (np.random.randn(2, 3) * 1j).astype(np.complex64)

    ms_in = ms_torch.tensor(np_1 + np_2)
    torch_in = torch.tensor(np_1 + np_2)
    torch_out = torch.nn.functional.tanhshrink(torch_in)
    ms_out = ms_torch.nn.functional.tanhshrink(ms_in)

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason='softsign not support float64 input on Ascend')
def test_softsign_fp64():
    input_np = np.random.randn(2, 3)

    torch_in = torch.tensor(input_np)
    torch_out = torch.nn.functional.softsign(torch_in)

    ms_in = ms_torch.tensor(input_np)
    ms_out = ms_torch.nn.functional.softsign(ms_in)

    param_compare(torch_out, ms_out)

def test_softsign():
    input_np = np.random.randn(2, 3) * 50

    torch_in = torch.tensor(input_np)
    torch_out = torch.nn.functional.softsign(torch_in.int())

    ms_in = ms_torch.tensor(input_np)
    ms_out = ms_torch.nn.functional.softsign(ms_in.int())

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason='softmin not support float64 input on Ascend')
def test_softmin_fp64():
    input_np = np.random.randn(2, 3, 3) * 50

    torch_in = torch.tensor(input_np)
    torch_out1 = torch.nn.functional.softmin(torch_in, dim=2, dtype=torch.float64)
    torch_out2 = torch.nn.functional.softmin(torch_in, dim=1, dtype=torch.float32)
    torch_out3 = torch.nn.functional.softmin(torch_in)

    ms_in = ms_torch.tensor(input_np)
    ms_out1 = ms_torch.nn.functional.softmin(ms_in, dim=2, dtype=ms.float64)
    ms_out2 = ms_torch.nn.functional.softmin(ms_in, dim=1, dtype=ms.float32)
    ms_out3 = ms_torch.nn.functional.softmin(ms_in)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

def test_softmin_fp32():
    input_np = np.random.randn(2, 3) * 50

    torch_in = torch.tensor(input_np).float()
    torch_out2 = torch.nn.functional.softmin(torch_in, dim=1, dtype=torch.float32)
    torch_out3 = torch.nn.functional.softmin(torch_in)

    ms_in = ms_torch.tensor(input_np).float()
    ms_out2 = ms_torch.nn.functional.softmin(ms_in, dim=1, dtype=ms.float32)
    ms_out3 = ms_torch.nn.functional.softmin(ms_in)

    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

@SKIP_ENV_ASCEND(reason='softmax not support float64 input on Ascend')
def test_softmax_fp64():
    input_np = np.random.randn(2, 3, 3) * 50

    torch_in = torch.tensor(input_np)
    torch_out1 = torch.nn.functional.softmax(torch_in, dim=2, dtype=torch.float64)
    torch_out2 = torch.nn.functional.softmax(torch_in, dim=1, dtype=torch.float32)
    torch_out3 = torch.nn.functional.softmax(torch_in)

    ms_in = ms_torch.tensor(input_np)
    ms_out1 = ms_torch.nn.functional.softmax(ms_in, dim=2, dtype=ms.float64)
    ms_out2 = ms_torch.nn.functional.softmax(ms_in, dim=1, dtype=ms.float32)
    ms_out3 = ms_torch.nn.functional.softmax(ms_in)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

def test_softmax_fp32():
    input_np = np.random.randn(2, 3) * 50

    torch_in = torch.tensor(input_np).float()
    torch_out2 = torch.nn.functional.softmax(torch_in, dim=0, dtype=torch.float32)
    torch_out3 = torch.nn.functional.softmax(torch_in, dtype=torch.float32)

    ms_in = ms_torch.tensor(input_np).float()
    ms_out2 = ms_torch.nn.functional.softmax(ms_in, dim=0, dtype=ms.float32)
    ms_out3 = ms_torch.nn.functional.softmax(ms_in, dtype=ms.float32)

    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

def test_softshrink():
    input_np = np.random.randn(2, 3).astype(np.float32)

    torch_in = torch.tensor(input_np)
    torch_out1 = torch.nn.functional.softshrink(torch_in)
    torch_out2 = torch.nn.functional.softshrink(torch_in, lambd=2)

    ms_in = ms_torch.tensor(input_np)
    ms_out1 = ms_torch.nn.functional.softshrink(ms_in)
    ms_out2 = ms_torch.nn.functional.softshrink(ms_in, lambd=2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_channel_shuffle():
    np_data1 = np.random.randn(2, 9, 3, 4)

    ms_tensor = ms_torch.tensor(np_data1)
    ms_out = ms_torch.channel_shuffle(ms_tensor, 3)

    pt_tensor = torch.tensor(np_data1)
    pt_out = torch.channel_shuffle(pt_tensor, 3)

    param_compare(ms_out, pt_out)

def test_constant_pad_nd():
    padding = (3, 3)
    value = 3.5
    pt_input_2d = torch.ones(2, 3)
    pt_out = torch.constant_pad_nd(pt_input_2d, padding, value)

    ms_input_2d = ms_torch.ones(2, 3)
    ms_out = ms_torch.constant_pad_nd(ms_input_2d, padding, value)

    param_compare(pt_out, ms_out)

def test_mul1():
    torch_out = torch.mul(torch.tensor(0.5), 0.5)
    msa_net = TestNet(ms_torch.mul)
    ms_out = msa_net(ms_torch.tensor(0.5), 0.5)
    param_compare(torch_out, ms_out)

# TODO:test both input are bool type
# def test_mul2():
#     torch_out = torch.mul(torch.tensor([True, False, True]), torch.tensor([True, False, False]))
#     msa_net = TestNet(ms_torch.mul)
#     ms_out = msa_net(ms_torch.tensor([True, False, True]), ms_torch.tensor([True, False, False]))
#     param_compare(torch_out, ms_out)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_interpolate1()
    test_interpolate2()
    test_interpolate3()
    test_interpolate4()
    test_interpolate5()
    test_interpolate6()
    test_interpolate7()
    test_interpolate8()
    test_interpolate9()


    test_upsample_nearest1()
    test_upsample_nearest2()
    test_upsample_nearest3()
    # test_upsample_nearest4()
    # test_upsample_nearest5()
    # test_upsample_nearest6()

    test_upsample_bilinear1()
    test_upsample_bilinear2()
    test_upsample_bilinear3()

    test_adaptive_avg_pool1d()
    test_adaptive_max_pool1d()

    test_adaptive_avg_pool2d()
    test_adaptive_max_pool2d()

    test_adaptive_avg_pool3d()
    test_adaptive_max_pool3d()

    test_affine_grid1()
    test_affine_grid2()

    test_adaptive_max_pool2d_3d_input()
    test_adaptive_max_pool2d_3d_input_return_indice_true()

    test_tanh()
    test_tanhshrink()
    test_softsign()
    test_softsign_fp64()
    test_softmin_fp32()
    test_softmin_fp64()
    test_softmax_fp32()
    test_softmax_fp64()
    test_softshrink()
    test_tanh_complex()
    test_tanhshrink_complex()
    test_upsample_bilinear_list_scale_factor()
    test_channel_shuffle()
    test_constant_pad_nd()
    test_mul1()
    # test_mul2()
