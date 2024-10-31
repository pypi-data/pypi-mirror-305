#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import torch
import mindspore as ms

import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, SKIP_ENV_CPU, SKIP_ENV_ASCEND, param_compare, SKIP_ENV_PYNATIVE_MODE
set_mode_by_env_config()


def test_smoothl1loss1():
    a = np.array([1, 2, 3]).astype(np.float32)
    b = np.array([1, 2, 2]).astype(np.float32)

    ms_logits = ms_torch.tensor(a)
    ms_labels = ms_torch.tensor(b)
    result_ms = ms_torch.nn.SmoothL1Loss()(ms_logits, ms_labels)

    torch_logits = torch.tensor(a)
    torch_labels = torch.tensor(b)
    result_torch = torch.nn.SmoothL1Loss()(torch_logits, torch_labels)
    param_compare(result_ms, result_torch)


def test_smoothl1loss2():
    a = np.array([1, 2, 3]).astype(np.float32)
    b = np.array([1, 2, 2]).astype(np.float32)

    ms_logits = ms_torch.tensor(a)
    ms_labels = ms_torch.tensor(b)
    result_ms = ms_torch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='sum', beta=0.5)(ms_logits, ms_labels)

    torch_logits = torch.tensor(a)
    torch_labels = torch.tensor(b)
    result_torch = torch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='sum', beta=0.5)(torch_logits, torch_labels)
    param_compare(result_ms, result_torch)

def test_smoothl1loss3():
    a = np.array([1, 2, 3]).astype(np.float32)
    b = np.array([1, 2, 2]).astype(np.float32)

    ms_logits = ms_torch.tensor(a)
    ms_labels = ms_torch.tensor(b)
    result_ms = ms_torch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='none', beta=0.5)(ms_logits, ms_labels)

    torch_logits = torch.tensor(a)
    torch_labels = torch.tensor(b)
    result_torch = torch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='none', beta=0.5)(torch_logits, torch_labels)
    param_compare(result_ms, result_torch)


def test_l1loss_reduction_none():
    a = np.random.randn(2).astype(np.float32)
    b = np.random.randn(2).astype(np.float32)

    ms_logits = ms_torch.tensor(a)
    ms_labels = ms_torch.tensor(b)
    result_ms = ms_torch.nn.L1Loss(size_average=None, reduce=None, reduction='none')(ms_logits, ms_labels)

    torch_input = torch.tensor(a)
    torch_target = torch.tensor(b)
    result_torch = torch.nn.L1Loss(size_average=None, reduce=None, reduction='none')(torch_input, torch_target)
    param_compare(result_ms, result_torch)


def test_l1loss_reduction_sum():
    a = np.random.randn(2, 3).astype(np.float32)
    b = np.random.randn(2, 3).astype(np.float32)

    torch_input = torch.tensor(a)
    torch_target = torch.tensor(b)
    result_torch = torch.nn.L1Loss(size_average=None, reduce=None, reduction='sum')(torch_input, torch_target)

    ms_logits = ms_torch.tensor(a)
    ms_labels = ms_torch.tensor(b)
    result_ms = ms_torch.nn.L1Loss(size_average=None, reduce=None, reduction='sum')(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)


def test_l1loss_reduction_mean():
    a = np.random.randn(2, 2, 3).astype(np.float32)
    b = np.random.randn(2, 2, 3).astype(np.float32)

    torch_input = torch.tensor(a)
    torch_target = torch.tensor(b)
    result_torch = torch.nn.L1Loss(size_average=None, reduce=None, reduction='mean')(torch_input, torch_target)
    
    ms_logits = ms_torch.tensor(a)
    ms_labels = ms_torch.tensor(b)
    result_ms = ms_torch.nn.L1Loss(size_average=None, reduce=None, reduction='mean')(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)


def test_mseloss_reduction_none():
    a = np.random.randn(2).astype(float)
    b = np.random.randn(2).astype(float)

    torch_input = torch.tensor(a)
    torch_target = torch.tensor(b)
    result_torch = torch.nn.MSELoss(size_average=None, reduce=None, reduction='none')(torch_input, torch_target)
    ms_logits = ms_torch.tensor(a)
    ms_labels = ms_torch.tensor(b)
    result_ms = ms_torch.nn.MSELoss(size_average=None, reduce=None, reduction='none')(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)


def test_mseloss_reduction_sum():
    a = np.random.randn(2, 3).astype(float)
    b = np.random.randn(2, 3).astype(float)

    torch_input = torch.tensor(a)
    torch_target = torch.tensor(b)
    result_torch = torch.nn.MSELoss(size_average=None, reduce=None, reduction='sum')(torch_input, torch_target)

    ms_logits = ms_torch.tensor(a)
    ms_labels = ms_torch.tensor(b)
    result_ms = ms_torch.nn.MSELoss(size_average=None, reduce=None, reduction='sum')(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)


def test_mseloss_reduction_sum():
    a = np.random.randn(2, 2, 3).astype(float)
    b = np.random.randn(2, 2, 3).astype(float)

    torch_input = torch.tensor(a)
    torch_target = torch.tensor(b)
    result_torch = torch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')(torch_input, torch_target)

    ms_logits = ms_torch.tensor(a)
    ms_labels = ms_torch.tensor(b)
    result_ms = ms_torch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

def test_cross_entropy_reduction_none():
    a = np.random.randn(3, 5).astype(float)
    b = np.array([1, 0, 4])
    c = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

    torch_input = torch.tensor(a, dtype=torch.float32)
    torch_target = torch.tensor(b, dtype=torch.int64)
    torch_weight = torch.tensor(c, dtype=torch.float32)
    torch_loss = torch.nn.CrossEntropyLoss(weight=torch_weight, reduction='none')
    result_torch = torch_loss(torch_input, torch_target)

    ms_logits = ms_torch.tensor(a, ms_torch.float32)
    ms_labels = ms_torch.tensor(b, ms_torch.int64)
    ms_weight = ms_torch.tensor(c, ms_torch.float32)
    ms_loss = ms_torch.nn.CrossEntropyLoss(weight=ms_weight, reduction='none')
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)


def test_cross_entropy_reduction_sum():
    a = np.random.randn(3, 5).astype(float)
    b = np.random.randn(3, 5).astype(float)

    torch_input = torch.tensor(a, dtype=torch.float32)
    torch_target = torch.tensor(b, dtype=torch.float32)
    torch_loss = torch.nn.CrossEntropyLoss(weight=None, reduction='sum', label_smoothing=1.0)
    result_torch = torch_loss(torch_input, torch_target)

    ms_logits = ms_torch.tensor(a, ms_torch.float32)
    ms_labels = ms_torch.tensor(b, ms_torch.float32)
    ms_loss = ms_torch.nn.CrossEntropyLoss(weight=None, reduction='sum', label_smoothing=1.0)
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

def test_cross_entropy_reduction_mean():
    a = np.random.randn(3, 5).astype(float)
    b = np.array([1, 0, 4])

    torch_input = torch.tensor(a, dtype=torch.float32)
    torch_target = torch.tensor(b, dtype=torch.int64)
    torch_loss = torch.nn.CrossEntropyLoss(weight=None, ignore_index=-1, reduction='mean', label_smoothing=0.1)
    result_torch = torch_loss(torch_input, torch_target)

    ms_logits = ms_torch.tensor(a, ms_torch.float32)
    ms_labels = ms_torch.tensor(b, ms_torch.int64)
    ms_loss = ms_torch.nn.CrossEntropyLoss(weight=None, ignore_index=-1, reduction='mean', label_smoothing=0.1)
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)


def test_nllloss_reduction():
    a = np.array([[0.1, 0.2, 0.3], [0.5, 0.7, 0.9], [0.5, 0.7, 0.9]])
    b = np.array([0, 1, 0])
    c = np.array([1.0, 2.0, 3.0])

    torch_input = torch.tensor(a, dtype=torch.float32)
    torch_target = torch.tensor(b, dtype=torch.int64)
    torch_weight = torch.tensor(c, dtype=torch.float32)

    ms_logits = ms_torch.tensor(a, ms_torch.float32)
    ms_labels = ms_torch.tensor(b, ms_torch.int64)
    ms_weight = ms_torch.tensor(c, ms_torch.float32)

    torch_loss = torch.nn.NLLLoss(weight=None, ignore_index=-1, reduction='mean')
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.NLLLoss(weight=None, ignore_index=-1, reduction='mean')
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

    torch_loss = torch.nn.NLLLoss(weight=torch_weight, reduction='sum')
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.NLLLoss(weight=ms_weight, reduction='sum')
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

    torch_loss = torch.nn.NLLLoss(weight=torch_weight, reduction='none')
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.NLLLoss(weight=ms_weight, reduction='none')
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

def test_kl_div_loss_reduction():
    a = np.array([0.2, 0.7, 0.1])
    b = np.array([0., 1., 0.])

    torch_input = torch.tensor(a)
    torch_target = torch.tensor(b)
    torch_loss = torch.nn.KLDivLoss(reduction='mean', log_target=False)
    result_torch = torch_loss(torch_input, torch_target)

    ms_logits = ms_torch.tensor(a)
    ms_labels = ms_torch.tensor(b)
    ms_loss = ms_torch.nn.KLDivLoss(reduction='mean', log_target=False)
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

    torch_loss = torch.nn.KLDivLoss(reduction='sum', log_target=False)
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.KLDivLoss(reduction='sum', log_target=False)
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

    torch_loss = torch.nn.KLDivLoss(reduction='none')
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.KLDivLoss(reduction='none')
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

    torch_loss = torch.nn.KLDivLoss(reduction='batchmean')
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.KLDivLoss(reduction='batchmean')
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

def test_bce_loss():
    a = np.array([[0.1, 0.2, 0.3], [0.5, 0.7, 0.9]])
    b = np.array([[0, 1, 0], [0, 0, 1]])
    c = np.array([[1.0, 2.0, 3.0], [4.0, 3.3, 2.2]])

    torch_input = torch.tensor(a, dtype=torch.float32)
    torch_target = torch.tensor(b, dtype=torch.float32)
    torch_weight = torch.tensor(c, dtype=torch.float32)

    ms_logits = ms_torch.tensor(a, ms_torch.float32)
    ms_labels = ms_torch.tensor(b, ms_torch.float32)
    ms_weight = ms_torch.tensor(c, ms_torch.float32)

    torch_loss = torch.nn.BCELoss(weight=None, reduction='none')
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.BCELoss(weight=None, reduction='none')
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

    torch_loss = torch.nn.BCELoss(weight=torch_weight, reduction='sum')
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.BCELoss(weight=ms_weight, reduction='sum')
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

    torch_loss = torch.nn.BCELoss(weight=torch_weight, reduction='mean')
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.BCELoss(weight=ms_weight, reduction='mean')
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)



def test_binary_cross_entropy_with_logits():
    a = np.array([[-0.8, 1.2, 0.7], [-0.1, -0.4, 0.7]])
    b = np.array([[0.3, 0.8, 1.2], [-0.6, 0.1, 2.2]])
    c = np.array([1.0, 1.0, 1.0])
    d = np.array([0.1, 0.1, 0.1])

    torch_input = torch.tensor(a, dtype=torch.float32)
    torch_target = torch.tensor(b, dtype=torch.float32)
    torch_weight = torch.tensor(c, dtype=torch.float32)
    torch_pos_weight = torch.tensor(d, dtype=torch.float32)

    ms_logits = ms_torch.tensor(a, ms_torch.float32)
    ms_labels = ms_torch.tensor(b, ms_torch.float32)
    ms_weight = ms_torch.tensor(c, ms_torch.float32)
    ms_pos_weight = ms_torch.tensor(d, ms_torch.float32)

    torch_loss = torch.nn.BCEWithLogitsLoss(weight=torch_weight, reduction='none', pos_weight=torch_pos_weight)
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.BCEWithLogitsLoss(weight=ms_weight, reduction='none', pos_weight=ms_pos_weight)
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

    torch_loss = torch.nn.BCEWithLogitsLoss(weight=torch_weight, reduction='sum', pos_weight=None)
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.BCEWithLogitsLoss(weight=ms_weight, reduction='sum', pos_weight=None)
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)

    torch_loss = torch.nn.BCEWithLogitsLoss(weight=None, reduction='mean', pos_weight=torch_pos_weight)
    result_torch = torch_loss(torch_input, torch_target)
    ms_loss = ms_torch.nn.BCEWithLogitsLoss(weight=None, reduction='mean', pos_weight=ms_pos_weight)
    result_ms = ms_loss(ms_logits, ms_labels)
    param_compare(result_ms, result_torch)


@SKIP_ENV_ASCEND(reason="float64 is unsupport on Ascend.")
def test_huber_loss_mean():
    input = np.random.randn(3, 5).astype(np.float64)
    target = np.random.randn(3, 5).astype(np.float64)

    torch_input = torch.tensor(input)
    torch_target = torch.tensor(target)
    torch_loss = torch.nn.HuberLoss(reduction='mean', delta=1.0)
    result_torch = torch_loss(torch_input, torch_target)

    ms_logits = ms_torch.tensor(input)
    ms_labels = ms_torch.tensor(target)
    ms_loss = ms_torch.nn.HuberLoss(reduction='mean', delta=1.0)
    result_ms = ms_loss(ms_logits, ms_labels)

    param_compare(result_ms, result_torch)


def test_huber_loss_sum():
    input = np.random.randn(3, 5).astype(np.float32)
    target = np.random.randn(3, 5).astype(np.float32)

    torch_input = torch.tensor(input)
    torch_target = torch.tensor(target)
    torch_loss = torch.nn.HuberLoss(reduction='sum', delta=1.0)
    result_torch = torch_loss(torch_input, torch_target)

    ms_logits = ms_torch.tensor(input)
    ms_labels = ms_torch.tensor(target)
    ms_loss = ms_torch.nn.HuberLoss(reduction='sum', delta=1.0)
    result_ms = ms_loss(ms_logits, ms_labels)

    param_compare(result_ms, result_torch)

def test_huber_loss_none():
    input = np.random.randn(3, 5).astype(np.float32)
    target = np.random.randn(3, 5).astype(np.float32)

    torch_input = torch.tensor(input)
    torch_target = torch.tensor(target)
    torch_loss = torch.nn.HuberLoss(reduction='none', delta=1.0)
    result_torch = torch_loss(torch_input, torch_target)

    ms_logits = ms_torch.tensor(input)
    ms_labels = ms_torch.tensor(target)
    ms_loss = ms_torch.nn.HuberLoss(reduction='none', delta=1.0)
    result_ms = ms_loss(ms_logits, ms_labels)

    param_compare(result_ms, result_torch)

@SKIP_ENV_CPU(reason="ms.ops.soft_margin_loss is unsupport on CPU.")
def test_soft_margin_loss_mean():
    input = np.random.randn(3, 5).astype(np.float32)
    target = np.random.randn(3, 5).astype(np.float32)

    torch_input = torch.tensor(input)
    torch_target = torch.tensor(target)
    torch_loss = torch.nn.SoftMarginLoss(reduction='mean')
    result_torch = torch_loss(torch_input, torch_target)

    ms_logits = ms_torch.tensor(input)
    ms_labels = ms_torch.tensor(target)
    ms_loss = ms_torch.nn.SoftMarginLoss(reduction='mean')
    result_ms = ms_loss(ms_logits, ms_labels)

    param_compare(result_ms, result_torch)

@SKIP_ENV_CPU(reason="ms.ops.soft_margin_loss is unsupport on CPU.")
def test_soft_margin_loss_sum():
    input = np.random.randn(3, 5).astype(np.float32)
    target = np.random.randn(3, 5).astype(np.float32)

    torch_input = torch.tensor(input)
    torch_target = torch.tensor(target)
    torch_loss = torch.nn.SoftMarginLoss(reduction='sum')
    result_torch = torch_loss(torch_input, torch_target)

    ms_logits = ms_torch.tensor(input)
    ms_labels = ms_torch.tensor(target)
    ms_loss = ms_torch.nn.SoftMarginLoss(reduction='sum')
    result_ms = ms_loss(ms_logits, ms_labels)

    param_compare(result_ms, result_torch)

@SKIP_ENV_CPU(reason="ms.ops.soft_margin_loss is unsupport on CPU.")
def test_soft_margin_loss_none():
    input = np.random.randn(3, 5).astype(np.float32)
    target = np.random.randn(3, 5).astype(np.float32)

    torch_input = torch.tensor(input)
    torch_target = torch.tensor(target)
    torch_loss = torch.nn.SoftMarginLoss(reduction='none')
    result_torch = torch_loss(torch_input, torch_target)

    ms_logits = ms_torch.tensor(input)
    ms_labels = ms_torch.tensor(target)
    ms_loss = ms_torch.nn.SoftMarginLoss(reduction='none')
    result_ms = ms_loss(ms_logits, ms_labels)

    param_compare(result_ms, result_torch)

def test_cosine_embedding_loss_none():
    input1 = np.random.randn(3, 5).astype(np.float32)
    input2 = np.random.randn(3, 5).astype(np.float32)
    target = np.array([1, -1, 1]).astype(np.float32)

    torch_input1 = torch.tensor(input1)
    torch_input2 = torch.tensor(input2)
    torch_target = torch.tensor(target)
    torch_loss = torch.nn.CosineEmbeddingLoss(reduction='none', margin=0.5)
    result_torch = torch_loss(torch_input1, torch_input2, torch_target)

    ms_logits1 = ms_torch.tensor(input1)
    ms_logits2 = ms_torch.tensor(input2)
    ms_labels = ms_torch.tensor(target)
    ms_loss = ms_torch.nn.CosineEmbeddingLoss(reduction='none', margin=0.5)
    result_ms = ms_loss(ms_logits1, ms_logits2, ms_labels)

    param_compare(result_ms, result_torch)

def test_cosine_embedding_loss_sum():
    input1 = np.random.randn(3, 5).astype(np.float32)
    input2 = np.random.randn(3, 5).astype(np.float32)
    target = np.array([1, -1, 1]).astype(np.float32)

    torch_input1 = torch.tensor(input1)
    torch_input2 = torch.tensor(input2)
    torch_target = torch.tensor(target)
    torch_loss = torch.nn.CosineEmbeddingLoss(reduction='sum', margin=0.5)
    result_torch = torch_loss(torch_input1, torch_input2, torch_target)

    ms_logits1 = ms_torch.tensor(input1)
    ms_logits2 = ms_torch.tensor(input2)
    ms_labels = ms_torch.tensor(target)
    ms_loss = ms_torch.nn.CosineEmbeddingLoss(reduction='sum', margin=0.5)
    result_ms = ms_loss(ms_logits1, ms_logits2, ms_labels)

    param_compare(result_ms, result_torch)

def test_cosine_embedding_loss_mean():
    input1 = np.random.randn(3, 5).astype(np.float32)
    input2 = np.random.randn(3, 5).astype(np.float32)
    target = np.array([1, -1, 1]).astype(np.float32)

    torch_input1 = torch.tensor(input1)
    torch_input2 = torch.tensor(input2)
    torch_target = torch.tensor(target)
    torch_loss = torch.nn.CosineEmbeddingLoss(reduction='mean', margin=0.5)
    result_torch = torch_loss(torch_input1, torch_input2, torch_target)

    ms_logits1 = ms_torch.tensor(input1)
    ms_logits2 = ms_torch.tensor(input2)
    ms_labels = ms_torch.tensor(target)
    ms_loss = ms_torch.nn.CosineEmbeddingLoss(reduction='mean', margin=0.5)
    result_ms = ms_loss(ms_logits1, ms_logits2, ms_labels)

    param_compare(result_ms, result_torch)


def test_triplet_margin_loss_none():
    anchor = np.random.randn(2, 5).astype(np.float32)
    positive = np.random.randn(2, 5).astype(np.float32)
    negative = np.random.randn(2, 5).astype(np.float32)

    torch_input1 = torch.tensor(anchor)
    torch_input2 = torch.tensor(positive)
    torch_target = torch.tensor(negative)
    torch_triplet_loss = torch.nn.TripletMarginLoss(margin=1.0, p=2., reduction='none')
    result_torch = torch_triplet_loss(torch_input1, torch_input2, torch_target)

    ms_logits1 = ms_torch.tensor(anchor)
    ms_logits2 = ms_torch.tensor(positive)
    ms_labels = ms_torch.tensor(negative)
    ms_loss = ms_torch.nn.TripletMarginLoss(margin=1.0, p=2., reduction='none')
    result_ms = ms_loss(ms_logits1, ms_logits2, ms_labels)

    param_compare(result_ms, result_torch)


def test_triplet_margin_loss_sum():
    anchor = np.random.randn(2, 5).astype(np.float32)
    positive = np.random.randn(2, 5).astype(np.float32)
    negative = np.random.randn(2, 5).astype(np.float32)

    torch_input1 = torch.tensor(anchor)
    torch_input2 = torch.tensor(positive)
    torch_target = torch.tensor(negative)
    torch_triplet_loss = torch.nn.TripletMarginLoss(margin=1.0, p=3, reduction='sum')
    result_torch = torch_triplet_loss(torch_input1, torch_input2, torch_target)

    ms_logits1 = ms_torch.tensor(anchor)
    ms_logits2 = ms_torch.tensor(positive)
    ms_labels = ms_torch.tensor(negative)
    ms_loss = ms_torch.nn.TripletMarginLoss(margin=1.0, p=3, reduction='sum')
    result_ms = ms_loss(ms_logits1, ms_logits2, ms_labels)

    param_compare(result_ms, result_torch)


def test_triplet_margin_loss_mean():
    anchor = np.random.randn(3).astype(np.float32)
    positive = np.random.randn(3).astype(np.float32)
    negative = np.random.randn(3).astype(np.float32)

    torch_input1 = torch.tensor(anchor)
    torch_input2 = torch.tensor(positive)
    torch_target = torch.tensor(negative)
    torch_triplet_loss = torch.nn.TripletMarginLoss(margin=1.0, p=2)
    result_torch = torch_triplet_loss(torch_input1, torch_input2, torch_target)

    ms_logits1 = ms_torch.tensor(anchor)
    ms_logits2 = ms_torch.tensor(positive)
    ms_labels = ms_torch.tensor(negative)
    ms_loss = ms_torch.nn.TripletMarginLoss(margin=1.0, p=2)
    result_ms = ms_loss(ms_logits1, ms_logits2, ms_labels)

    param_compare(result_ms, result_torch)


def test_multi_margin_loss_none():
    x = np.array([0.1, 0.2, 0.4, 0.8])
    y = np.array(3)

    torch_input1 = torch.tensor(x)
    torch_input2 = torch.tensor(y, dtype=torch.int64)
    torch_loss = torch.nn.MultiMarginLoss(p=2, reduction='none')
    result_torch = torch_loss(torch_input1, torch_input2)

    ms_logits1 = ms_torch.tensor(x)
    ms_logits2 = ms_torch.tensor(y, dtype=ms.int64)
    ms_loss = ms_torch.nn.MultiMarginLoss(p=2, reduction='none')
    result_ms = ms_loss(ms_logits1, ms_logits2)

    param_compare(result_ms, result_torch)

def test_multi_margin_loss_weight():
    x = np.array([[0.1, 0.2, 0.4, 0.8]])
    y = np.array([3])
    weight = np.array([0.2, 0.3, 0.4, 0.1])

    torch_input1 = torch.tensor(x)
    torch_input2 = torch.tensor(y, dtype=torch.int64)
    torch_weight = torch.tensor(weight)
    torch_loss = torch.nn.MultiMarginLoss(weight=torch_weight)
    result_torch = torch_loss(torch_input1, torch_input2)

    ms_logits1 = ms_torch.tensor(x)
    ms_logits2 = ms_torch.tensor(y, dtype=ms.int64)
    ms_weight = ms_torch.tensor(weight)
    ms_loss = ms_torch.nn.MultiMarginLoss(weight=ms_weight)
    result_ms = ms_loss(ms_logits1, ms_logits2)

    param_compare(result_ms, result_torch)

def test_poisson_nll_loss():
    np_data = np.random.randn(5, 2)
    np_target = np.random.randn(5, 2)

    torch_input = torch.tensor(np_data, requires_grad=True)
    torch_target = torch.tensor(np_target)
    ms_input = ms_torch.tensor(np_data, requires_grad=True)
    ms_target = ms_torch.tensor(np_target)

    torch_loss = torch.nn.PoissonNLLLoss(reduction="sum")
    ms_loss = ms_torch.nn.PoissonNLLLoss(reduction="sum")

    torch_out = torch_loss(torch_input, torch_target)
    ms_out = ms_loss(ms_input, ms_target)

    param_compare(torch_out.detach(), ms_out.detach())


@SKIP_ENV_ASCEND(reason="float64 is unsupport on Ascend.")
def test_gaussian_nll_loss():
    np_data = np.random.randn(5, 2)
    np_target = np.random.randn(5, 2)
    np_var = np.ones((5, 2))

    torch_input = torch.tensor(np_data, requires_grad=True)
    torch_target = torch.tensor(np_target)
    torch_var = torch.tensor(np_var, requires_grad=True)
    ms_input = ms_torch.tensor(np_data, requires_grad=True)
    ms_target = ms_torch.tensor(np_target)
    ms_var = ms_torch.tensor(np_var, requires_grad=True)

    torch_loss = torch.nn.GaussianNLLLoss()
    ms_loss = ms_torch.nn.GaussianNLLLoss()

    torch_out = torch_loss(torch_input, torch_target, torch_var)
    ms_out = ms_loss(ms_input, ms_target, ms_var)

    param_compare(torch_out.detach(), ms_out.detach())

def test_gaussian_nll_loss_sum():
    np_data = np.random.randn(3, 2).astype(np.float32)
    np_target = np.random.randn(3, 2).astype(np.float32)
    np_var = np.ones((3, 2)).astype(np.float32)

    torch_input = torch.tensor(np_data, requires_grad=True)
    torch_target = torch.tensor(np_target)
    torch_var = torch.tensor(np_var, requires_grad=True)
    ms_input = ms_torch.tensor(np_data, requires_grad=True)
    ms_target = ms_torch.tensor(np_target)
    ms_var = ms_torch.tensor(np_var, requires_grad=True)

    torch_loss = torch.nn.GaussianNLLLoss(full=True, reduction='sum')
    ms_loss = ms_torch.nn.GaussianNLLLoss(full=True, reduction='sum')

    torch_out = torch_loss(torch_input, torch_target, torch_var)
    ms_out = ms_loss(ms_input, ms_target, ms_var)

    param_compare(torch_out.detach(), ms_out.detach())


@SKIP_ENV_ASCEND(reason="float64 is unsupport on Ascend.")
def test_hinge_embedding_loss_none():
    np_data = np.random.randn(5, 2)
    np_target = np.sign(np.random.randn(5, 2))

    torch_input = torch.tensor(np_data, requires_grad=True)
    torch_target = torch.tensor(np_target)
    ms_input = ms_torch.tensor(np_data, requires_grad=True)
    ms_target = ms_torch.tensor(np_target)

    torch_loss = torch.nn.HingeEmbeddingLoss(reduction="none")
    ms_loss = ms_torch.nn.HingeEmbeddingLoss(reduction="none")

    torch_out = torch_loss(torch_input, torch_target)
    ms_out = ms_loss(ms_input, ms_target)

    param_compare(torch_out.detach(), ms_out.detach())


def test_hinge_embedding_loss_mean():
    np_data = np.random.randn(3, 2).astype(np.float32)
    np_target = np.sign(np.random.randn(3, 2)).astype(np.float32)

    torch_input = torch.tensor(np_data, requires_grad=True)
    torch_target = torch.tensor(np_target)
    ms_input = ms_torch.tensor(np_data, requires_grad=True)
    ms_target = ms_torch.tensor(np_target)

    torch_loss = torch.nn.HingeEmbeddingLoss(margin=2.0, reduction='mean')
    ms_loss = ms_torch.nn.HingeEmbeddingLoss(margin=2.0, reduction='mean')

    torch_out = torch_loss(torch_input, torch_target)
    ms_out = ms_loss(ms_input, ms_target)

    param_compare(torch_out.detach(), ms_out.detach())


@SKIP_ENV_CPU(reason="ms.ops.multilabel_margin_loss is unsupport on CPU.")
def test_multilabel_margin_loss():
    np_data = np.array([[0.1, 0.2, 0.4, 0.8], [0.2, 0.3, 0.5, 0.7]]).astype(np.float32)
    np_target = np.array([[1, 2, 0, 3], [2, 3, -1, 1]])

    torch_input = torch.tensor(np_data, requires_grad=True)
    torch_target = torch.tensor(np_target, dtype=torch.int64)
    ms_input = ms_torch.tensor(np_data, requires_grad=True)
    ms_target = ms_torch.tensor(np_target, dtype=ms.int64)

    torch_loss = torch.nn.MultiLabelMarginLoss(reduction="none")
    ms_loss = ms_torch.nn.MultiLabelMarginLoss(reduction="none")

    torch_out = torch_loss(torch_input, torch_target)
    ms_out = ms_loss(ms_input, ms_target)

    param_compare(torch_out.detach(), ms_out.detach())


@SKIP_ENV_CPU(reason="ms.ops.multilabel_margin_loss is unsupport on CPU.")
def test_multilabel_margin_loss_1d():
    np_data = np.array([0.1, 0.2, 0.4, 0.8]).astype(np.float32)
    np_target = np.array([1, 2, 0, 3])

    torch_input = torch.tensor(np_data)
    torch_target = torch.tensor(np_target, dtype=torch.int64)
    ms_input = ms_torch.tensor(np_data)
    ms_target = ms_torch.tensor(np_target, dtype=ms.int64)

    torch_loss = torch.nn.MultiLabelMarginLoss(reduction="sum")
    ms_loss = ms_torch.nn.MultiLabelMarginLoss(reduction="sum")

    torch_out = torch_loss(torch_input, torch_target)
    ms_out = ms_loss(ms_input, ms_target)

    param_compare(torch_out, ms_out)


def test_multilabel_soft_margin_loss():
    np_data = np.random.randn(5, 2)
    np_target = np.sign(np.random.randn(5, 2))

    torch_input = torch.tensor(np_data, requires_grad=True)
    torch_target = torch.tensor(np_target)
    ms_input = ms_torch.tensor(np_data, requires_grad=True)
    ms_target = ms_torch.tensor(np_target)

    torch_loss = torch.nn.MultiLabelSoftMarginLoss(reduction="none")
    ms_loss = ms_torch.nn.MultiLabelSoftMarginLoss(reduction="none")

    torch_out = torch_loss(torch_input, torch_target)
    ms_out = ms_loss(ms_input, ms_target)

    param_compare(torch_out.detach(), ms_out.detach())

def test_triplet_margin_with_distance_loss():
    np_anc = np.random.randn(5, 6, 7).astype(np.float32)
    np_pos = np.random.randn(5, 6, 7).astype(np.float32)
    np_neg = np.random.randn(5, 6, 7).astype(np.float32)

    t_anc = torch.tensor(np_anc)
    t_pos = torch.tensor(np_pos)
    t_neg = torch.tensor(np_neg)
    ms_anc = ms_torch.tensor(np_anc)
    ms_pos = ms_torch.tensor(np_pos)
    ms_neg = ms_torch.tensor(np_neg)

    t_loss = torch.nn.TripletMarginWithDistanceLoss(distance_function=torch.nn.functional.cosine_similarity, swap=True)
    ms_loss = ms_torch.nn.TripletMarginWithDistanceLoss(distance_function=ms_torch.nn.functional.cosine_similarity, swap=True)

    torch_out = t_loss(t_anc, t_pos, t_neg)
    ms_out = ms_loss(ms_anc, ms_pos, ms_neg)

    param_compare(torch_out, ms_out)


@SKIP_ENV_ASCEND(reason="float64 is unsupport on Ascend.")
def test_ctc_loss():
    np_data = np.random.randn(24, 2, 10)
    np_target = np.random.rand(2, 10) * 10
    np_input_length = np.array([8, 10])
    np_target_length = np.array([5, 6])

    torch_input = torch.tensor(np_data, requires_grad=True)
    torch_target = torch.tensor(np_target)
    torch_input_length = torch.tensor(np_input_length)
    torch_target_length = torch.tensor(np_target_length)
    ms_input = ms_torch.tensor(np_data, requires_grad=True)
    ms_target = ms_torch.tensor(np_target)
    ms_input_length = ms_torch.tensor(np_input_length)
    ms_target_length = ms_torch.tensor(np_target_length)

    torch_loss = torch.nn.CTCLoss(reduction="none")
    ms_loss = ms_torch.nn.CTCLoss(reduction="none")

    torch_out = torch_loss(torch_input, torch_target, torch_input_length, torch_target_length)
    ms_out = ms_loss(ms_input, ms_target, ms_input_length, ms_target_length)

    param_compare(torch_out.detach(), ms_out.detach())

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: ms.ops.ctc_loss result not correct on Ascend.")
def test_ctc_loss_float32():
    T = 50      # Input sequence length
    C = 20      # Number of classes (including blank)
    N = 2      # Batch size
    S = 30      # Target sequence length of longest target in batch (padding length)
    S_min = 10  # Minimum target length, for demonstration purposes
    np_data = np.random.randn(T, N, C).astype(np.float32)
    np_target = np.random.randint(low=1, high=C, size=(N, S), dtype=np.int64)
    np_target_lengths = np.random.randint(low=S_min, high=S, size=(N,), dtype=np.int64)

    pt_input = torch.tensor(np_data).log_softmax(2).detach().requires_grad_()
    pt_target = torch.tensor(np_target)
    pt_input_lengths = torch.full(size=(N,), fill_value=T, dtype=torch.long)
    pt_target_lengths = torch.tensor(np_target_lengths)
    pt_ctc_loss = torch.nn.CTCLoss()
    pt_loss = pt_ctc_loss(pt_input, pt_target, pt_input_lengths, pt_target_lengths)

    ms_input = ms_torch.tensor(np_data).log_softmax(2).detach().requires_grad_()
    ms_target = ms_torch.tensor(np_target)
    ms_input_lengths = ms_torch.full(size=(N,), fill_value=T, dtype=ms_torch.long)
    ms_target_lengths = ms_torch.tensor(np_target_lengths)
    ms_ctc_loss = ms_torch.nn.CTCLoss()
    ms_loss = ms_ctc_loss(ms_input, ms_target, ms_input_lengths, ms_target_lengths)

    param_compare(pt_loss.detach(), ms_loss.detach())


def test_margin_ranking_loss():
    np_data1 = np.random.randn(5, 2).astype(np.float32)
    np_data2 = np.random.randn(5, 2).astype(np.float32)
    np_target = np.sign(np.random.randn(5, 2)).astype(np.float32)

    torch_input1 = torch.tensor(np_data1, requires_grad=True)
    torch_input2 = torch.tensor(np_data2, requires_grad=True)
    torch_target = torch.tensor(np_target)
    ms_input1 = ms_torch.tensor(np_data1, requires_grad=True)
    ms_input2 = ms_torch.tensor(np_data2, requires_grad=True)
    ms_target = ms_torch.tensor(np_target)

    torch_loss = torch.nn.MarginRankingLoss(reduction="none")
    ms_loss = ms_torch.nn.MarginRankingLoss(reduction="none")

    torch_out = torch_loss(torch_input1, torch_input2, torch_target)
    ms_out = ms_loss(ms_input1, ms_input2, ms_target)

    param_compare(torch_out.detach(), ms_out.detach())


if __name__ == '__main__':
    set_mode_by_env_config()
    test_smoothl1loss1()
    test_smoothl1loss2()
    test_smoothl1loss3()

    test_l1loss_reduction_none()
    test_l1loss_reduction_sum()
    test_l1loss_reduction_mean()

    test_mseloss_reduction_none()
    test_mseloss_reduction_sum()
    test_mseloss_reduction_mean()

    test_cross_entropy_reduction_none()
    test_cross_entropy_reduction_sum()
    test_cross_entropy_reduction_mean()

    test_bce_loss()
    test_binary_cross_entropy_with_logits()

    test_nllloss_reduction()

    test_huber_loss_mean()
    test_huber_loss_sum()
    test_huber_loss_none()

    test_soft_margin_loss_none()
    test_soft_margin_loss_mean()
    test_soft_margin_loss_sum()


    test_cosine_embedding_loss_none()
    test_cosine_embedding_loss_sum()
    test_cosine_embedding_loss_mean()

    test_triplet_margin_loss_none()
    test_triplet_margin_loss_sum()
    test_triplet_margin_loss_mean()

    test_multi_margin_loss_none()
    test_multi_margin_loss_weight()

    test_poisson_nll_loss()
    test_gaussian_nll_loss()
    test_gaussian_nll_loss_sum()
    test_hinge_embedding_loss_none()
    test_hinge_embedding_loss_mean()
    test_multilabel_margin_loss()
    test_multilabel_margin_loss_1d()
    test_multilabel_soft_margin_loss()
    test_triplet_margin_with_distance_loss()
    test_ctc_loss()
    test_ctc_loss_float32()
    test_margin_ranking_loss()
