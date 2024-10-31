#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, type_shape_compare, TestNet, graph_lax_level
set_mode_by_env_config()

def test_empty1():
    ms_result = ms_torch.empty(2, 3, dtype=ms_torch.float32)
    torch_result = torch.empty(2, 3, dtype=torch.float32)
    type_shape_compare(ms_result, torch_result)

def test_empty2():
    ms_result = ms_torch.empty((2, 3), dtype=ms_torch.float32)
    torch_result = torch.empty((2, 3), dtype=torch.float32)
    type_shape_compare(ms_result, torch_result)

def test_empty_key_value_size():
    ms_result = ms_torch.empty(size=(2, 3))
    torch_result = torch.empty(size=(2, 3))
    type_shape_compare(ms_result, torch_result)

def test_empty_graph1():
    empty_net = TestNet(ms_torch.empty)
    ms_result = empty_net((2, 3), dtype=ms_torch.int)
    torch_result = torch.empty(size=(2, 3), dtype=torch.int)
    type_shape_compare(ms_result, torch_result)

def test_empty_graph2():
    empty_net = TestNet(ms_torch.empty)
    ms_result = empty_net((), dtype=ms_torch.int)
    torch_result = torch.empty((), dtype=torch.int)
    type_shape_compare(ms_result, torch_result)

def test_empty_graph3():
    empty_net = TestNet(ms_torch.empty)
    ms_result = empty_net([], dtype=ms_torch.int)
    torch_result = torch.empty([], dtype=torch.int)
    type_shape_compare(ms_result, torch_result)

# TODO: Currently, empty with dynamic shapes are not supported
# def test_empty_dynamic():
#     @ms.jit(input_signature=ms_torch.cast_to_adapter_tensor(ms.tensor(shape=[None, 3], dtype=ms.int32)))
#     def empty_dynamic(x):
#         x_shape = x.shape
#         return ms_torch.empty(x_shape, dtype=ms_torch.int32)
#
#     input = ms_torch.tensor(np.random.randn(2, 3), dtype=ms_torch.int32)
#     ms_result = empty_dynamic(input)
#     torch_result = torch.empty(size=(2, 3), dtype=torch.int32)
#     type_shape_compare(ms_result, torch_result)

def test_empty_like_graph():
    data = np.zeros((2,3))
    empty_net = TestNet(ms_torch.empty_like)
    ms_tensor = ms_torch.tensor(data)
    ms_result = empty_net(ms_tensor)

    torch_tensor = torch.tensor(data)
    torch_result = torch.empty_like(torch_tensor)
    type_shape_compare(ms_result, torch_result)

def test_empty_shape_tensor():
    empty_net = TestNet(ms_torch.empty)
    ms_result = empty_net((2, ms_torch.tensor(3)), dtype=ms_torch.int)
    torch_result = torch.empty(size=(2, torch.tensor(3)), dtype=torch.int)
    type_shape_compare(ms_result, torch_result)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_empty1()
    test_empty2()
    test_empty_graph1()
    test_empty_graph2()
    test_empty_graph3()
    # test_empty_dynamic()
    test_empty_like_graph()
    test_empty_shape_tensor()