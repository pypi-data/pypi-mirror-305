#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import torch
import mindspore as ms
from mindspore import context

import mindtorch.torch as ms_torch

from ....utils import set_mode_by_env_config, SKIP_ENV_ASCEND, SKIP_ENV_CPU, param_compare
set_mode_by_env_config()


def test_ctc_loss():
    np_log_probs = np.random.randn(12, 2, 10).astype(np.float32)
    np_targets = np.random.rand(2, 10).astype(np.float32) * 10
    np_input_length = np.array([8, 10]).astype(np.int32)
    np_target_length = np.array([5, 6]).astype(np.int32)

    torch_log_probs = torch.tensor(np_log_probs)
    torch_targets = torch.tensor(np_targets)
    torch_input_length = torch.tensor(np_input_length)
    torch_target_length = torch.tensor(np_target_length)
    result_torch = torch.nn.functional.ctc_loss(torch_log_probs, torch_targets, torch_input_length, torch_target_length,\
                                                blank=1, reduction='sum', zero_infinity=True)

    ms_log_probs = ms_torch.tensor(np_log_probs)
    ms_targets = ms_torch.tensor(np_targets)
    ms_input_length = ms_torch.tensor(np_input_length)
    ms_target_length = ms_torch.tensor(np_target_length)
    result_ms = ms_torch.nn.functional.ctc_loss(ms_log_probs, ms_targets, ms_input_length, ms_target_length,\
                                                blank=1, reduction='sum', zero_infinity=True)

    param_compare(result_ms, result_torch)

def test_gaussian_nll_loss():
    np_input = np.random.randn(2, 3, 4, 5).astype(np.float32)
    np_targets = np.random.rand(2, 3, 4, 5).astype(np.float32)
    np_var = np.ones([2, 3, 4, 5]).astype(np.float32)

    torch_log_probs = torch.tensor(np_input)
    torch_targets = torch.tensor(np_targets)
    torch_var = torch.tensor(np_var)
    result_torch = torch.nn.functional.gaussian_nll_loss(torch_log_probs, torch_targets, torch_var, reduction='none')

    ms_log_probs = ms_torch.tensor(np_input)
    ms_targets = ms_torch.tensor(np_targets)
    ms_var = ms_torch.tensor(np_var)
    result_ms = ms_torch.nn.functional.gaussian_nll_loss(ms_log_probs, ms_targets, ms_var, reduction='none')

    param_compare(result_ms, result_torch, atol=1e-6)


def test_gaussian_nll_loss_1d():
    np_input = np.array([0.1, 0.2, 0.4, 0.8]).astype(np.float32)
    np_targets = np.array([1, 2, 0, 3]).astype(np.float32)
    np_var = np.ones((4)).astype(np.float32)

    torch_log_probs = torch.tensor(np_input)
    torch_targets = torch.tensor(np_targets)
    torch_var = torch.tensor(np_var)
    result_torch = torch.nn.functional.gaussian_nll_loss(torch_log_probs, torch_targets, torch_var)

    ms_log_probs = ms_torch.tensor(np_input)
    ms_targets = ms_torch.tensor(np_targets)
    ms_var = ms_torch.tensor(np_var)
    result_ms = ms_torch.nn.functional.gaussian_nll_loss(ms_log_probs, ms_targets, ms_var)

    param_compare(result_ms, result_torch, atol=1e-6)


def test_hinge_embedding_loss():
    np_input = np.random.randn(2, 3, 4, 5).astype(np.int32)
    np_targets = np.sign(np.random.rand(2, 3, 4, 5)).astype(np.int32)

    torch_log_probs = torch.tensor(np_input)
    torch_targets = torch.tensor(np_targets)
    result_torch = torch.nn.functional.hinge_embedding_loss(torch_log_probs, torch_targets, reduction='sum')

    ms_log_probs = ms_torch.tensor(np_input)
    ms_targets = ms_torch.tensor(np_targets)
    result_ms = ms_torch.nn.functional.hinge_embedding_loss(ms_log_probs, ms_targets, reduction='sum')
    print(result_ms.dtype, result_torch.dtype)
    param_compare(result_ms, result_torch)


def test_margin_ranking_loss_mean():
    np_input1 = np.random.randn(1, 2, 3, 4).astype(np.int32)
    np_input2 = np.random.randn(1, 2, 3, 4).astype(np.int32)
    np_targets = np.sign(np.random.rand(1, 2, 3, 4)).astype(np.int32)

    torch_input1 = torch.tensor(np_input1)
    torch_input2 = torch.tensor(np_input2)
    torch_targets = torch.tensor(np_targets)
    result_torch = torch.nn.functional.margin_ranking_loss(torch_input1, torch_input2, torch_targets)

    ms_input1 = ms_torch.tensor(np_input1)
    ms_input2 = ms_torch.tensor(np_input2)
    ms_targets = ms_torch.tensor(np_targets)
    result_ms = ms_torch.nn.functional.margin_ranking_loss(ms_input1, ms_input2, ms_targets)
    param_compare(result_ms, result_torch)


@SKIP_ENV_ASCEND(reason="float64 is unsupport on Ascend.")
def test_margin_ranking_loss_float64():
    np_input1 = np.random.randn(3)
    np_input2 = np.random.randn(3)
    np_targets = np.sign(np.random.rand(3))

    torch_input1 = torch.tensor(np_input1)
    torch_input2 = torch.tensor(np_input2)
    torch_targets = torch.tensor(np_targets)
    result_torch = torch.nn.functional.margin_ranking_loss(torch_input1, torch_input2, torch_targets,reduction='sum')

    ms_input1 = ms_torch.tensor(np_input1)
    ms_input2 = ms_torch.tensor(np_input2)
    ms_targets = ms_torch.tensor(np_targets)
    result_ms = ms_torch.nn.functional.margin_ranking_loss(ms_input1, ms_input2, ms_targets, reduction='sum')
    param_compare(result_ms, result_torch)


@SKIP_ENV_CPU(reason="ms.ops.multilabel_margin_loss unsupport on CPU.")
def test_multilabel_margin_loss():
    np_input = np.random.randn(5, 10)
    np_targets = np.random.rand(5, 10)*10-1

    torch_input = torch.tensor(np_input, dtype=torch.float32)
    torch_targets = torch.tensor(np_targets, dtype=torch.int64)
    result_torch = torch.nn.functional.multilabel_margin_loss(torch_input, torch_targets)

    ms_input = ms_torch.tensor(np_input, dtype=ms_torch.float32)
    ms_targets = ms_torch.tensor(np_targets, dtype=ms_torch.int64)
    result_ms = ms_torch.nn.functional.multilabel_margin_loss(ms_input, ms_targets)

    param_compare(result_ms, result_torch)


def test_multilabel_soft_margin_loss():
    np_input = np.array([[0.3, 0.6, 0.6], [0.9, 0.4, 0.2]])
    np_targets = np.array([[0.0, 0.0, 1.0], [0.0, 0.0, 1.0]])

    torch_input = torch.tensor(np_input)
    torch_targets = torch.tensor(np_targets)
    result_torch = torch.nn.functional.multilabel_soft_margin_loss(torch_input, torch_targets)

    ms_input = ms_torch.tensor(np_input)
    ms_targets = ms_torch.tensor(np_targets)
    result_ms = ms_torch.nn.functional.multilabel_soft_margin_loss(ms_input, ms_targets)

    param_compare(result_ms, result_torch)

def test_multi_margin_loss_N_C():
    np_input = np.array([[0.1, 0.2, 0.4, 0.8]])
    np_targets = np.array([3])

    torch_input = torch.tensor(np_input)
    torch_targets = torch.tensor(np_targets, dtype=torch.int64)
    result_torch = torch.nn.functional.multi_margin_loss(torch_input, torch_targets)

    ms_input = ms_torch.tensor(np_input)
    ms_targets = ms_torch.tensor(np_targets, dtype=ms.int64)
    result_ms = ms_torch.nn.functional.multi_margin_loss(ms_input, ms_targets)

    param_compare(result_ms, result_torch)

def test_multi_margin_loss_C():
    np_input = np.array([0.1, 0.2, 0.4, 0.8])
    np_targets = np.array(3)

    torch_input = torch.tensor(np_input)
    torch_targets = torch.tensor(np_targets, dtype=torch.int64)
    result_torch = torch.nn.functional.multi_margin_loss(torch_input, torch_targets, reduction="none")

    ms_input = ms_torch.tensor(np_input)
    ms_targets = ms_torch.tensor(np_targets, dtype=ms.int64)
    result_ms = ms_torch.nn.functional.multi_margin_loss(ms_input, ms_targets, reduction="none")
    param_compare(result_ms, result_torch)

def test_huber_loss():
    np_input = np.array([1.0, 2, 10, 2]).astype(np.float32)
    np_targets = np.array([1.0, 5, 1, 20]).astype(np.float32)

    torch_input = torch.tensor(np_input)
    torch_targets = torch.tensor(np_targets)
    result_torch = torch.nn.functional.huber_loss(torch_input, torch_targets)

    ms_input = ms_torch.tensor(np_input)
    ms_targets = ms_torch.tensor(np_targets)
    result_ms = ms_torch.nn.functional.huber_loss(ms_input, ms_targets)

    param_compare(result_ms, result_torch)


@SKIP_ENV_ASCEND(reason="triplet_margin_loss use abs, ms.ops.abs unsupport float64 on Ascend.")
def test_triplet_margin_loss():
    np_anc = np.random.randn(2, 4)
    np_pos = np.random.randn(2, 4)
    np_neg = np.random.randn(2, 4)

    torch_anc = torch.tensor(np_anc, requires_grad=True)
    torch_pos = torch.tensor(np_pos, requires_grad=True)
    torch_neg = torch.tensor(np_neg, requires_grad=True)
    result_torch = torch.nn.functional.triplet_margin_loss(torch_anc, torch_pos, torch_neg)

    ms_anc = ms_torch.tensor(np_anc, requires_grad=True)
    ms_pos = ms_torch.tensor(np_pos, requires_grad=True)
    ms_neg = ms_torch.tensor(np_neg, requires_grad=True)
    result_ms = ms_torch.nn.functional.triplet_margin_loss(ms_anc, ms_pos, ms_neg)
    param_compare(result_ms.detach(), result_torch.detach())

def test_binary_cross_entropy():
    np_input = np.random.randn(3, 2).astype(np.float32)
    np_target = np.random.randn(3, 2).astype(np.float32)

    pt_input = torch.tensor(np_input)
    pt_target = torch.tensor(np_target)
    pt_loss = torch.nn.functional.binary_cross_entropy(torch.sigmoid(pt_input), pt_target)

    ms_input = ms_torch.tensor(np_input)
    ms_target = ms_torch.tensor(np_target)
    ms_loss = ms_torch.nn.functional.binary_cross_entropy(ms_torch.sigmoid(ms_input), ms_target)
    param_compare(ms_loss, pt_loss, atol=1e-5)


def test_binary_cross_entropy_with_logits():
    np_input = np.random.randn(3).astype(np.float32)
    np_target = np.random.randn(3).astype(np.float32)

    pt_input = torch.tensor(np_input)
    pt_target = torch.tensor(np_target)
    pt_loss = torch.nn.functional.binary_cross_entropy_with_logits(pt_input, pt_target)

    ms_input = ms_torch.tensor(np_input)
    ms_target = ms_torch.tensor(np_target)
    ms_loss = ms_torch.nn.functional.binary_cross_entropy_with_logits(ms_input, ms_target)
    param_compare(ms_loss, pt_loss, atol=1e-6)


def test_cross_entropy():
    np_input = np.random.randn(3, 5).astype(np.float32)
    np_target = np.random.randn(3, 5).astype(np.float32)

    pt_input = torch.tensor(np_input)
    pt_target = torch.tensor(np_target).softmax(dim=1)
    pt_loss = torch.nn.functional.cross_entropy(pt_input, pt_target)

    ms_input = ms_torch.tensor(np_input)
    ms_target = ms_torch.tensor(np_target).softmax(dim=1)
    ms_loss = ms_torch.nn.functional.cross_entropy(ms_input, ms_target)
    param_compare(ms_loss, pt_loss)


def test_kl_div():
    np_input = np.random.randn(3, 5).astype(np.float32)
    np_target = np.random.randn(3, 5).astype(np.float32)

    pt_input = torch.tensor(np_input)
    pt_target = torch.tensor(np_target).log_softmax(dim=-1)
    pt_loss = torch.nn.functional.kl_div(pt_input, pt_target, reduction="mean", log_target=True)

    ms_input = ms_torch.tensor(np_input)
    ms_target = ms_torch.tensor(np_target).log_softmax(dim=-1)
    ms_loss = ms_torch.nn.functional.kl_div(ms_input, ms_target, reduction="mean", log_target=True)
    param_compare(ms_loss, pt_loss, atol=1e-05)

    pt_loss = torch.nn.functional.kl_div(pt_input, pt_target, reduction="none", log_target=True)
    ms_loss = ms_torch.nn.functional.kl_div(ms_input, ms_target, reduction="none", log_target=True)
    param_compare(ms_loss, pt_loss, atol=1e-05)

    pt_loss = torch.nn.functional.kl_div(pt_input, pt_target, reduction="batchmean", log_target=True)
    ms_loss = ms_torch.nn.functional.kl_div(ms_input, ms_target, reduction="batchmean", log_target=True)
    param_compare(ms_loss, pt_loss, atol=1e-05)

    pt_loss = torch.nn.functional.kl_div(pt_input, pt_target, reduction="sum", log_target=True)
    ms_loss = ms_torch.nn.functional.kl_div(ms_input, ms_target, reduction="sum", log_target=True)
    param_compare(ms_loss, pt_loss, atol=1e-05)


@SKIP_ENV_ASCEND(reason="ms.ops.l1_loss unsupport float64 on Ascend.")
def test_l1_loss():
    np_input = np.random.randn(3, 5).astype(np.float64)
    np_target = np.random.randn(3, 5).astype(np.float64)

    pt_input = torch.tensor(np_input)
    pt_target = torch.tensor(np_target)
    pt_loss = torch.nn.functional.l1_loss(pt_input, pt_target)

    ms_input = ms_torch.tensor(np_input)
    ms_target = ms_torch.tensor(np_target)
    ms_loss = ms_torch.nn.functional.l1_loss(ms_input, ms_target)
    param_compare(ms_loss, pt_loss)

def test_mse_loss():
    np_input = np.random.randn(3, 5).astype(np.float64)
    np_target = np.random.randn(3, 5).astype(np.float64)

    pt_input = torch.tensor(np_input)
    pt_target = torch.tensor(np_target)
    pt_loss = torch.nn.functional.mse_loss(pt_input, pt_target)

    ms_input = ms_torch.tensor(np_input)
    ms_target = ms_torch.tensor(np_target)
    ms_loss = ms_torch.nn.functional.mse_loss(ms_input, ms_target)
    param_compare(ms_loss, pt_loss)

def test_smooth_l1_loss():
    np_input = np.random.randn(2, 2, 2, 2).astype(np.float64)
    np_target = np.random.randn(2, 2, 2, 2).astype(np.float64)

    pt_input = torch.tensor(np_input)
    pt_target = torch.tensor(np_target)
    pt_loss = torch.nn.functional.smooth_l1_loss(pt_input, pt_target, reduction='elementwise_mean')

    ms_input = ms_torch.tensor(np_input)
    ms_target = ms_torch.tensor(np_target)
    ms_loss = ms_torch.nn.functional.smooth_l1_loss(ms_input, ms_target, reduction='elementwise_mean')
    param_compare(ms_loss, pt_loss)


def test_poisson_nll_loss_mean():
    np_input = np.random.randn(2, 5).astype(np.float32)
    np_target = np.random.randn(2, 5).astype(np.float32)

    pt_input = torch.tensor(np_input)
    pt_target = torch.tensor(np_target)
    pt_loss = torch.nn.functional.poisson_nll_loss(pt_input, pt_target, log_input=True, full=True)

    ms_input = ms_torch.tensor(np_input)
    ms_target = ms_torch.tensor(np_target)
    ms_loss = ms_torch.nn.functional.poisson_nll_loss(ms_input, ms_target, log_input=True, full=True)
    param_compare(ms_loss, pt_loss, equal_nan=True)

def test_poisson_nll_loss_none():
    np_input = np.random.randn(2, 5).astype(np.float64)
    np_target = np.random.randn(2, 5).astype(np.float64)

    pt_input = torch.tensor(np_input)
    pt_target = torch.tensor(np_target)
    pt_loss = torch.nn.functional.poisson_nll_loss(pt_input, pt_target, reduction='none')

    ms_input = ms_torch.tensor(np_input)
    ms_target = ms_torch.tensor(np_target)
    ms_loss = ms_torch.nn.functional.poisson_nll_loss(ms_input, ms_target, reduction='none')
    param_compare(ms_loss, pt_loss)


def test_triplet_margin_with_distance_loss_sum():
    np_anc = np.random.randn(2, 3, 4).astype(np.float32)
    np_pos = np.random.randn(2, 3, 4).astype(np.float32)
    np_neg = np.random.randn(2, 3, 4).astype(np.float32)

    t_anc = torch.tensor(np_anc)
    t_pos = torch.tensor(np_pos)
    t_neg = torch.tensor(np_neg)
    ms_anc = ms_torch.tensor(np_anc)
    ms_pos = ms_torch.tensor(np_pos)
    ms_neg = ms_torch.tensor(np_neg)

    def pt_l_infinity(x1, x2):
        return torch.max(torch.abs(x1 - x2), dim=1)[0]

    def ms_l_infinity(x1, x2):
        return ms_torch.max(ms_torch.abs(x1 - x2), dim=1)[0]

    pt_loss = torch.nn.functional.triplet_margin_with_distance_loss(t_anc, t_pos, t_neg, distance_function=pt_l_infinity,
                                                                    reduction='sum')
    ms_loss = ms_torch.nn.functional.triplet_margin_with_distance_loss(ms_anc, ms_pos, ms_neg, distance_function=ms_l_infinity,
                                                                       reduction='sum')
    param_compare(ms_loss, pt_loss)


def test_triplet_margin_with_distance_loss_none():
    np_anc = np.random.randn(2, 3, 4).astype(np.float32)
    np_pos = np.random.randn(2, 3, 4).astype(np.float32)
    np_neg = np.random.randn(2, 3, 4).astype(np.float32)

    t_anc = torch.tensor(np_anc)
    t_pos = torch.tensor(np_pos)
    t_neg = torch.tensor(np_neg)
    ms_anc = ms_torch.tensor(np_anc)
    ms_pos = ms_torch.tensor(np_pos)
    ms_neg = ms_torch.tensor(np_neg)

    pt_func = lambda x, y: 1.0 - torch.nn.functional.cosine_similarity(x, y)
    pt_loss = torch.nn.functional.triplet_margin_with_distance_loss(t_anc, t_pos, t_neg, 
                                                                    distance_function=pt_func,
                                                                    reduction='none')
    ms_func = lambda x, y: 1.0 - ms_torch.nn.functional.cosine_similarity(x, y)
    ms_loss = ms_torch.nn.functional.triplet_margin_with_distance_loss(ms_anc, ms_pos, ms_neg,
                                                                       distance_function=ms_func,
                                                                       reduction='none')
    param_compare(ms_loss, pt_loss, atol=1e-7)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_ctc_loss()
    test_gaussian_nll_loss()
    test_gaussian_nll_loss_1d()
    test_hinge_embedding_loss()
    test_margin_ranking_loss_mean()
    test_margin_ranking_loss_float64()
    test_multilabel_margin_loss()
    test_multilabel_soft_margin_loss()
    test_multi_margin_loss_N_C()
    test_multi_margin_loss_C()
    test_huber_loss()
    test_triplet_margin_loss()
    test_binary_cross_entropy()
    test_binary_cross_entropy_with_logits()
    test_cross_entropy()
    test_kl_div()
    test_l1_loss()
    test_mse_loss()
    test_smooth_l1_loss()
    test_poisson_nll_loss_mean()
    test_poisson_nll_loss_none()
    test_triplet_margin_with_distance_loss_sum()
    test_triplet_margin_with_distance_loss_none()

