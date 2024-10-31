#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mindtorch.torch import Tensor
import mindtorch.torch.nn as nn
import numpy as np
import torch

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_pairwise_distance1():
    ms_distance = nn.PairwiseDistance(keepdim=True)
    torch_distance = torch.nn.PairwiseDistance(keepdim=True)
    data1 = np.array([[[-1, 0, 1, -2],
                     [2, 2, 3, 4]
                     ]]).astype(np.float32)
    data2 = np.array([[-1, 5, 1, 6],
                     [-2, 12, -7, 1.4]
                     ]).astype(np.float32)

    torch_input1 = torch.Tensor(data1)
    torch_input2 = torch.Tensor(data2)
    torch_out = torch_distance(torch_input1, torch_input2)

    ms_input1 = Tensor(data1.astype(np.float32))
    ms_input2 = Tensor(data2.astype(np.float32))
    ms_out = ms_distance(ms_input1, ms_input2)

    param_compare(ms_out, torch_out)


def test_pairwise_distance2():
    ms_distance = nn.PairwiseDistance(p=-2, eps=10)
    torch_distance = torch.nn.PairwiseDistance(p=-2, eps=10)
    data1 = np.array([[-2, -2],
                     [-2, -2]
                     ]).astype(np.float32)
    data2 = np.array([[8, 8],
                     [8, 8]
                     ]).astype(np.float32)

    torch_input1 = torch.Tensor(data1)
    torch_input2 = torch.Tensor(data2)
    torch_out = torch_distance(torch_input1, torch_input2)

    ms_input1 = Tensor(data1.astype(np.float32))
    ms_input2 = Tensor(data2.astype(np.float32))
    ms_out = ms_distance(ms_input1, ms_input2)

    param_compare(ms_out, torch_out)


def test_pairwise_distance3():
    ms_distance = nn.PairwiseDistance(p=2.1, eps=1)
    torch_distance = torch.nn.PairwiseDistance(p=2.1, eps=1)
    data1 = np.array([[[[0]],
                     [[0]],
                     [[0]]]]).astype(np.float32)
    data2 = np.array([[[[2, -1],
                        [0, 0]],
                       [[2, -1],
                        [0, 0]],
                       [[2, -1],
                        [0, 0]]]]).astype(np.float32)

    torch_input1 = torch.Tensor(data1)
    torch_input2 = torch.Tensor(data2)
    torch_out = torch_distance(torch_input1, torch_input2)

    ms_input1 = Tensor(data1.astype(np.float32))
    ms_input2 = Tensor(data2.astype(np.float32))
    ms_out = ms_distance(ms_input1, ms_input2)

    param_compare(ms_out, torch_out)


def test_cosine_similarity1():
    ms_distance = nn.CosineSimilarity(dim=1, eps=1e-5)
    torch_distance = torch.nn.CosineSimilarity(dim=1, eps=1e-5)
    data1 = np.array([[[1],
                     [-1]]]).astype(np.float32)
    data2 = np.array([[1, 1],
                     [2, 1]]).astype(np.float32)

    torch_input1 = torch.Tensor(data1)
    torch_input2 = torch.Tensor(data2)
    torch_out = torch_distance(torch_input1, torch_input2)

    ms_input1 = Tensor(data1.astype(np.float32))
    ms_input2 = Tensor(data2.astype(np.float32))
    ms_out = ms_distance(ms_input1, ms_input2)

    param_compare(ms_out, torch_out)


def test_cosine_similarity2():
    ms_distance = nn.CosineSimilarity(eps=1e-5)
    torch_distance = torch.nn.CosineSimilarity(eps=1e-5)
    data1 = np.array([[-1, 0, 1, -2],
                     [2, 2, 3, 4]]).astype(np.float32)
    data2 = np.array([[-1, 5, 1, 6],
                     [-2, 12, -7, 1.4]]).astype(np.float32)

    torch_input1 = torch.Tensor(data1)
    torch_input2 = torch.Tensor(data2)
    torch_out = torch_distance(torch_input1, torch_input2)

    ms_input1 = Tensor(data1.astype(np.float32))
    ms_input2 = Tensor(data2.astype(np.float32))
    ms_out = ms_distance(ms_input1, ms_input2)

    param_compare(ms_out, torch_out)


def test_cosine_similarity3():
    ms_distance = nn.CosineSimilarity(dim=0)
    torch_distance = torch.nn.CosineSimilarity(dim=0)
    data1 = np.array([[[[1]],
                       [[-1]],
                       [[2]]]]).astype(np.float32)
    data2 = np.array([[[1, 1],
                       [2, 1]],
                      [[1, 3],
                       [2, -0.5]],
                      [[0, 0],
                       [-1, 2]]]).astype(np.float32)

    torch_input1 = torch.Tensor(data1)
    torch_input2 = torch.Tensor(data2)
    torch_out = torch_distance(torch_input1, torch_input2)

    ms_input1 = Tensor(data1.astype(np.float32))
    ms_input2 = Tensor(data2.astype(np.float32))
    ms_out = ms_distance(ms_input1, ms_input2)

    param_compare(ms_out, torch_out)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_pairwise_distance1()
    test_pairwise_distance2()
    test_pairwise_distance3()
    test_cosine_similarity1()
    test_cosine_similarity2()
    test_cosine_similarity3()
