#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config
set_mode_by_env_config()

def test_pixel_shuffle1():
    data = np.arange(0, 240).reshape(1, 2, 8, 3, 5)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.pixel_shuffle(torch_input, 2)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.pixel_shuffle(ms_input, 2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_pixel_shuffle2():
    data = np.arange(0, 36).reshape(4, 3, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.pixel_shuffle(torch_input, 2)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.pixel_shuffle(ms_input, 2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_pixel_unshuffle1():
    data = np.arange(0, 240).reshape(1, 2, 2, 6, 10)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.pixel_unshuffle(torch_input, 2)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.pixel_unshuffle(ms_input, 2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_pixel_unshuffle2():
    data = np.arange(0, 36).reshape(1, 6, 6).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.pixel_unshuffle(torch_input, 2)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.pixel_unshuffle(ms_input, 2)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


if __name__ == '__main__':
    set_mode_by_env_config()
    test_pixel_shuffle1()
    test_pixel_shuffle2()
    test_pixel_unshuffle1()
    test_pixel_unshuffle2()

