#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import torch
import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config, param_compare, type_shape_compare
set_mode_by_env_config()

def test_dirac_():
    t_w1 = torch.empty(3, 16, 5, 5, dtype=torch.float64)
    torch.nn.init.dirac_(t_w1)
    t_w2 = torch.empty(3, 24, 5, 5)
    torch.nn.init.dirac_(t_w2, 3)

    m_w1 = ms_torch.empty(3, 16, 5, 5, dtype=ms_torch.float64)
    ms_torch.nn.init.dirac_(m_w1)
    m_w2 = ms_torch.empty(3, 24, 5, 5)
    ms_torch.nn.init.dirac_(m_w2, 3)

    type_shape_compare(t_w1, m_w1)
    type_shape_compare(t_w2, m_w2)

def test_orthogonal_():
    t_w = torch.empty(3, 5)
    torch.nn.init.orthogonal_(t_w)
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.orthogonal_(m_w)
    type_shape_compare(t_w, m_w)

    mul = ms_torch.matmul(m_w, m_w.T)
    id_mat = ms_torch.eye(m_w.shape[0])
    param_compare(mul, id_mat, rtol=1e-4, atol=1e-6)

def test_eye_():
    t_w = torch.empty(3, 5)
    torch.nn.init.eye_(t_w)
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.eye_(m_w)

    param_compare(t_w, m_w)

def test_calculate_gain():
    torch_gain = torch.nn.init.calculate_gain('leaky_relu', 0.2)
    pytorch_gain = ms_torch.nn.init.calculate_gain('leaky_relu', 0.2)
    assert torch_gain == pytorch_gain

def test_uniform_():
    t_w = torch.empty(3, 5)
    torch.nn.init.uniform_(t_w)
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.uniform_(m_w)
    assert t_w.numpy().dtype == m_w.numpy().dtype
    assert t_w.numpy().shape == m_w.numpy().shape

def test_normal_():
    t_w = torch.empty(3, 5)
    torch.nn.init.normal_(t_w)
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.normal_(m_w)
    assert t_w.numpy().dtype == m_w.numpy().dtype
    assert t_w.numpy().shape == m_w.numpy().shape

def test_constant_():
    t_w = torch.empty(3, 5)
    torch.nn.init.constant_(t_w, 0.3)
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.constant_(m_w, 0.3)
    param_compare(t_w, m_w)

def test_ones_():
    t_w = torch.empty(3, 5)
    torch.nn.init.ones_(t_w)
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.ones_(m_w)
    param_compare(t_w, m_w)

def test_zeros_():
    t_w = torch.empty(3, 5)
    torch.nn.init.zeros_(t_w)
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.zeros_(m_w)
    param_compare(t_w, m_w)

def test_xavier_uniform_():
    t_w = torch.empty(3, 5)
    torch.nn.init.xavier_uniform_(t_w, gain=torch.nn.init.calculate_gain('relu'))
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.xavier_uniform_(m_w, gain=ms_torch.nn.init.calculate_gain('relu'))
    assert t_w.numpy().dtype == m_w.numpy().dtype
    assert t_w.numpy().shape == m_w.numpy().shape

def test_xavier_normal_():
    t_w = torch.empty(3, 5)
    torch.nn.init.xavier_normal_(t_w)
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.xavier_normal_(m_w)
    assert t_w.numpy().dtype == m_w.numpy().dtype
    assert t_w.numpy().shape == m_w.numpy().shape

def test_kaiming_uniform_():
    t_w = torch.empty(3, 5)
    torch.nn.init.kaiming_uniform_(t_w, mode='fan_in', nonlinearity='relu')
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.kaiming_uniform_(m_w, mode='fan_in', nonlinearity='relu')
    assert t_w.numpy().dtype == m_w.numpy().dtype
    assert t_w.numpy().shape == m_w.numpy().shape

def test_kaiming_normal_():
    t_w = torch.empty(3, 5)
    torch.nn.init.kaiming_normal_(t_w, mode='fan_out', nonlinearity='relu')
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.kaiming_normal_(m_w, mode='fan_out', nonlinearity='relu')
    assert t_w.numpy().dtype == m_w.numpy().dtype
    assert t_w.numpy().shape == m_w.numpy().shape

def test_trunc_normal_():
    t_w = torch.empty(3, 5)
    torch.nn.init.trunc_normal_(t_w)
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.trunc_normal_(m_w)
    assert t_w.numpy().dtype == m_w.numpy().dtype
    assert t_w.numpy().shape == m_w.numpy().shape

def test_sparse_():
    t_w = torch.empty(3, 5)
    torch.nn.init.sparse_(t_w, sparsity=0.1)
    m_w = ms_torch.empty(3, 5)
    ms_torch.nn.init.sparse_(m_w, sparsity=0.1)
    type_shape_compare(t_w, m_w)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_dirac_()
    test_orthogonal_()
    test_eye_()
    test_calculate_gain()
    test_uniform_()
    test_normal_()
    test_constant_()
    test_ones_()
    test_zeros_()
    test_xavier_uniform_()
    test_xavier_normal_()
    test_kaiming_uniform_()
    test_kaiming_normal_()
    test_trunc_normal_()
    test_sparse_()
