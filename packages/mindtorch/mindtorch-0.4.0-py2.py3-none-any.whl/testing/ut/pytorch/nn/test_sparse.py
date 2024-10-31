#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import SKIP_ENV_ASCEND, SKIP_ENV_CPU, SKIP_ENV_GPU, set_mode_by_env_config, param_compare, \
    enable_backward
set_mode_by_env_config()


class TrainNet(ms.nn.Cell):
    def __init__(self, net):
        super(TrainNet, self).__init__()
        self.net = net
        self.net.set_grad()
    def construct(self, index):
        out = self.net(index)
        loss = out - ms.ops.ones_like(out)
        loss = loss.sum()
        loss = ms.ops.square(loss)
        return loss

class Torch_TrainNet(torch.nn.Module):
    def __init__(self, net):
        super(Torch_TrainNet, self).__init__()
        self.net = net
    def forward(self, index):
        out = self.net(index)
        loss = out - torch.ones_like(out)
        loss = loss.sum()
        loss = torch.square(loss)
        return loss

def test_embedding():
    index_np = np.array([[1, 2, 3], [4, 5, 0]]).astype(np.int32)

    ms_index = ms_torch.tensor(index_np)
    net = ms_torch.nn.Embedding(10, 2)
    result_ms = net(ms_index)
    train_net = TrainNet(net)
    train_net.set_grad()
    grad_fn = ms.value_and_grad(train_net, grad_position=None, weights=train_net.trainable_params())
    _, grads = grad_fn(ms_index)

    assert not np.allclose(grads[0][1].asnumpy(), ms.ops.ZerosLike()(grads[0][1]).asnumpy())

    torch_index = torch.tensor(index_np)
    result_torch = torch.nn.Embedding(10, 2)(torch_index)

    assert result_ms.asnumpy().shape == result_torch.detach().numpy().shape

def test_embedding_with_weight():
    index_np = np.array([[1, 2, 3], [0, 2, 1]]).astype(np.int32)
    weight_np = np.array([[2.3, 4.5], [6.0, 7.1], [3.5, 6.], [8.9, 4]]).astype(np.float32)

    ms_index = ms_torch.tensor(index_np)
    ms_weight = ms_torch.tensor(weight_np)
    net = ms_torch.nn.Embedding(4, 2, _weight=ms_weight)
    result_ms = net(ms_index)
    train_net = TrainNet(net)
    train_net.set_grad()
    grad_fn = ms.value_and_grad(train_net, grad_position=None, weights=train_net.trainable_params())
    _, grads = grad_fn(ms_index)

    assert not np.allclose(grads[0][1].asnumpy(), ms.ops.ZerosLike()(grads[0][1]).asnumpy())

    torch_index = torch.tensor(index_np)
    torch_weight = torch.tensor(weight_np)
    result_torch = torch.nn.Embedding(4, 2, _weight=torch_weight)(torch_index)

    assert result_ms.asnumpy().shape == result_torch.detach().numpy().shape
    assert np.allclose(result_ms.asnumpy(), result_torch.detach().numpy())


def test_embedding_from_pretrained():
    index_np = np.array([[1, 2, 3], [0, 2, 1]]).astype(np.int32)
    weight_np = np.array([[2.3, 4.5], [6.0, 7.1], [3.5, 6.], [8.9, 4]]).astype(np.float32)

    ms_index = ms_torch.tensor(index_np)
    ms_weight = ms_torch.tensor(weight_np)
    net = ms_torch.nn.Embedding.from_pretrained(ms_weight)
    result_ms = net(ms_index)
    train_net = TrainNet(net)
    train_net.set_grad()
    grad_fn = ms.value_and_grad(train_net, grad_position=None, weights=train_net.trainable_params())
    _, grads = grad_fn(ms_index)
    assert not grads

    torch_index = torch.tensor(index_np)
    torch_weight = torch.tensor(weight_np)
    result_torch = torch.nn.Embedding.from_pretrained(torch_weight)(torch_index)

    assert result_ms.asnumpy().shape == result_torch.detach().numpy().shape
    assert np.allclose(result_ms.asnumpy(), result_torch.detach().numpy())


def test_embedding_weight_grad_with_padding_idx():
    with enable_backward():
        index_np = np.array([[1, 2, 3], [0, 2, 1]]).astype(np.int32)
        weight_np = np.array([[2.3, 4.5], [6.0, 7.1], [3.5, 6.], [8.9, 4]]).astype(np.float32)

        _padding_idx = 1

        torch_index = torch.tensor(index_np)
        torch_weight = torch.tensor(weight_np)
        torch_net = torch.nn.Embedding(4, 2, _weight=torch_weight, padding_idx=_padding_idx)
        torch_net = Torch_TrainNet(torch_net)
        result_torch = torch_net(torch_index)
        result_torch.backward()

        ms_index = ms_torch.tensor(index_np)
        ms_weight = ms_torch.tensor(weight_np)
        net = ms_torch.nn.Embedding(4, 2, _weight=ms_weight, padding_idx=_padding_idx)
        train_net = TrainNet(net)

        # Automatic differentiation method 1
        grad_fn = ms.value_and_grad(train_net, grad_position=None, weights=train_net.trainable_params())
        _, grads = grad_fn(ms_index)
        param_compare(grads[0], torch_net.net.weight.grad)

        # Automatic differentiation method 2
        # [CI] ms 2.3 0327 AUTOGRAD: There is an accuracy issue in backward
        # result_ms = train_net(ms_index)
        # result_ms.backward()
        # param_compare(train_net.net.weight.grad, torch_net.net.weight.grad)


@SKIP_ENV_ASCEND(reason="Embedding currently not support float64 weight on Ascend")
def test_embedding_weight_grad_with_padding_idx_fp64():
    with enable_backward():
        index_np = np.array([[1, 2, 3], [0, 2, 1]]).astype(np.int32)
        weight_np = np.array([[2.3, 4.5], [6.0, 7.1], [3.5, 6.], [8.9, 4]])
        _padding_idx = 1

        torch_index = torch.tensor(index_np)
        torch_weight = torch.tensor(weight_np)
        torch_net = torch.nn.Embedding(4, 2, _weight=torch_weight, padding_idx=_padding_idx)
        torch_net = Torch_TrainNet(torch_net)
        result_torch = torch_net(torch_index)
        result_torch.backward()

        ms_index = ms_torch.tensor(index_np)
        ms_weight = ms_torch.tensor(weight_np)
        net = ms_torch.nn.Embedding(4, 2, _weight=ms_weight, padding_idx=_padding_idx)
        train_net = TrainNet(net)

        # Automatic differentiation method 1
        grad_fn = ms.value_and_grad(train_net, grad_position=None, weights=train_net.trainable_params())
        _, grads = grad_fn(ms_index)
        param_compare(grads[0], torch_net.net.weight.grad)

        # Automatic differentiation method 2
        # [CI] ms 2.3 0327 AUTOGRAD: There is an accuracy issue in backward
        # result_ms = train_net(ms_index)
        # result_ms.backward()
        # param_compare(train_net.net.weight.grad, torch_net.net.weight.grad)


def test_embedding_output_with_padding_idx():
    index_np = np.array([[1, 2, 3], [0, 2, 1]]).astype(np.int32)
    weight_np = np.array([[2.3, 4.5], [6.0, 7.1], [3.5, 6.], [8.9, 4]]).astype(np.float32)

    ms_index = ms_torch.tensor(index_np)
    ms_weight = ms_torch.tensor(weight_np)
    result_ms = ms_torch.nn.Embedding(4, 2, _weight=ms_weight, padding_idx=1)(ms_index)

    torch_index = torch.tensor(index_np)
    torch_weight = torch.tensor(weight_np)
    result_torch = torch.nn.Embedding(4, 2, _weight=torch_weight, padding_idx=1)(torch_index)

    param_compare(result_ms, result_torch.detach())

@SKIP_ENV_ASCEND(reason="Embedding currently not support float64 weight on Ascend")
def test_embedding_output_with_padding_idx_fp64():
    index_np = np.array([[1, 2, 3], [0, 2, 1]]).astype(np.int32)
    weight_np = np.array([[2.3, 4.5], [6.0, 7.1], [3.5, 6.], [8.9, 4]])

    ms_index = ms_torch.tensor(index_np)
    ms_weight = ms_torch.tensor(weight_np)
    result_ms = ms_torch.nn.Embedding(4, 2, _weight=ms_weight, padding_idx=1)(ms_index)

    torch_index = torch.tensor(index_np)
    torch_weight = torch.tensor(weight_np)
    result_torch = torch.nn.Embedding(4, 2, _weight=torch_weight, padding_idx=1)(torch_index)

    param_compare(result_ms, result_torch.detach())

if __name__ == '__main__':
    set_mode_by_env_config()
    test_embedding()
    test_embedding_with_weight()
    test_embedding_from_pretrained()
    test_embedding_weight_grad_with_padding_idx()
    test_embedding_output_with_padding_idx()
    test_embedding_weight_grad_with_padding_idx_fp64()
    test_embedding_output_with_padding_idx_fp64()