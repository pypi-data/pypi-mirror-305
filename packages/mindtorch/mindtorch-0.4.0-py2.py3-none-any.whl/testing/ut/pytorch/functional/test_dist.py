#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import mindspore as ms
from mindspore import context
import torch
import mindtorch.torch as ms_torch
from ...utils import SKIP_ENV_ASCEND

from ...utils import set_mode_by_env_config
set_mode_by_env_config()


def test_cdist_1():
    x1 = np.array([[0.9041,  0.0196], [-0.3108, -2.4423], [-0.4821,  1.059]])
    x2 = np.array([[-2.1763, -0.4713], [-0.6986,  1.3702]])

    x1_pt = torch.tensor(x1, dtype=torch.float32)
    x2_pt = torch.tensor(x2, dtype=torch.float32)
    output_pt = torch.cdist(x1_pt, x2_pt, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')

    x1_ms = ms_torch.tensor(x1, dtype=ms_torch.float32)
    x2_ms = ms_torch.tensor(x2, dtype=ms_torch.float32)
    output_ms = ms_torch.cdist(x1_ms, x2_ms, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')
    assert np.allclose(output_pt.numpy(), output_ms.numpy())

@SKIP_ENV_ASCEND(reason='cdist not support float64 input')
def test_cdist_2():
    x1 = np.array([[0.9041,  0.0196], [-0.3108, -2.4423], [-0.4821,  1.059]])
    x2 = np.array([[-2.1763, -0.4713], [-0.6986,  1.3702]])

    x1_pt = torch.tensor(x1, dtype=torch.float64)
    x2_pt = torch.tensor(x2, dtype=torch.float64)
    output_pt = torch.cdist(x1_pt, x2_pt, p=0., compute_mode='use_mm_for_euclid_dist')

    x1_ms = ms_torch.tensor(x1, dtype=torch.float64)
    x2_ms = ms_torch.tensor(x2, dtype=torch.float64)
    output_ms = ms_torch.cdist(x1_ms, x2_ms, p=0., compute_mode='use_mm_for_euclid_dist')
    assert np.allclose(output_pt.numpy(), output_ms.numpy())

def test_atleast_1d():
    x_pt = torch.tensor(1.)
    output1_pt = torch.atleast_1d(x_pt)
    x_ms = ms_torch.tensor(1.)
    output1_ms = ms_torch.atleast_1d(x_ms)
    assert np.allclose(output1_pt.numpy(), output1_ms.numpy())

    y_pt = torch.tensor([2.0, 3.0])
    z_pt = torch.tensor([[4.0, 5.0]])
    output2_pt = torch.atleast_1d((x_pt, y_pt, z_pt))
    y_ms = ms_torch.tensor([2.0, 3.0])
    z_ms = ms_torch.tensor([[4.0, 5.0]])
    output2_ms = ms_torch.atleast_1d((x_ms, y_ms, z_ms))
    assert type(output2_pt) == type(output2_ms)
    for i in range(len(output2_pt)):
        assert np.allclose(output2_pt[i].numpy(), output2_ms[i].numpy())

def test_atleast_2d():
    x_pt = torch.tensor(1.)
    output1_pt = torch.atleast_2d(x_pt)
    x_ms = ms_torch.tensor(1.)
    output1_ms = ms_torch.atleast_2d(x_ms)
    assert output1_ms.dim() == 2
    assert np.allclose(output1_pt.numpy(), output1_ms.numpy())

    y_pt = torch.tensor([2.0, 3.0])
    z_pt = torch.tensor([[4.0, 5.0], [6.0, 7.0]])
    output2_pt = torch.atleast_2d((x_pt, y_pt, z_pt))
    y_ms = ms_torch.tensor([2.0, 3.0])
    z_ms = ms_torch.tensor([[4.0, 5.0], [6.0, 7.0]])
    output2_ms = ms_torch.atleast_2d((x_ms, y_ms, z_ms))
    assert type(output2_pt) == type(output2_ms)
    for i in range(len(output2_pt)):
        assert np.allclose(output2_pt[i].numpy(), output2_ms[i].numpy())

def test_atleast_3d():
    x_pt = torch.tensor(1.)
    output1_pt = torch.atleast_3d(x_pt)
    x_ms = ms_torch.tensor(1.)
    output1_ms = ms_torch.atleast_3d(x_ms)
    assert output1_ms.dim() == 3
    assert np.allclose(output1_pt.numpy(), output1_ms.numpy())

    y_pt = torch.tensor([[2.0, 3.0]])
    z_pt = torch.tensor([[[4.0, 5.0], [6.0, 7.0]]])
    output2_pt = torch.atleast_3d((x_pt, y_pt, z_pt))
    y_ms = ms_torch.tensor([2.0, 3.0])
    z_ms = ms_torch.tensor([[[4.0, 5.0], [6.0, 7.0]]])
    output2_ms = ms_torch.atleast_3d((x_ms, y_ms, z_ms))
    assert type(output2_pt) == type(output2_ms)
    for i in range(len(output2_pt)):
        assert output2_pt[i].dim() == output2_ms[i].dim()
        assert np.allclose(output2_pt[i].numpy(), output2_ms[i].numpy())



if __name__ == '__main__':
    set_mode_by_env_config()
    test_cdist_1()
    test_cdist_2()
    test_atleast_1d()
    test_atleast_2d()
    test_atleast_3d()
