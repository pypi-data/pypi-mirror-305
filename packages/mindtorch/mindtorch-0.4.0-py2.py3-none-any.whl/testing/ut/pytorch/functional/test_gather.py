
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()


def test_gather_2d():
    input = [[1, 2], [3, 4]]
    index = [[0, 0], [1, 0]]

    tourch_input = torch.tensor(input)
    tourch_index = torch.tensor(index)
    torch_out = torch.gather(tourch_input, 1, tourch_index)

    ms_input = ms_torch.tensor(input)
    ms_index = ms_torch.tensor(index)
    ms_out = ms_torch.gather(ms_input, 1, ms_index)
    assert np.allclose(torch_out.size(), ms_out.size())
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_gather_2d_long():
    x = [
    [2, 3, 4, 5, 0, 0],
    [1, 4, 3, 0, 0, 0],
    [4, 2, 2, 5, 7, 0],
    [1, 0, 0, 0, 0, 0]]
    input = torch.tensor(x)
    length = torch.LongTensor([[4], [3], [5], [1]])
    torch_out = torch.gather(input, 1, length - 1)

    ms_input = ms_torch.tensor(x)
    ms_length = ms_torch.LongTensor([[4], [3], [5], [1]])
    ms_out = ms_torch.gather(ms_input, 1, ms_length - 1)
    assert np.allclose(torch_out.size(), ms_out.size())
    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    return

def test_gather_3d():
    input = np.random.randn(2, 2, 2)
    index = [[[1, 0],[0, 0]],[[0, 1],[0, 1]]]

    tourch_input = torch.tensor(input)
    tourch_index = torch.tensor(index)
    torch_out = torch.gather(tourch_input, 2, tourch_index)

    ms_input = ms_torch.tensor(input)
    ms_index = ms_torch.tensor(index)
    ms_out = ms_torch.gather(ms_input, 2, ms_index)
    assert np.allclose(torch_out.size(), ms_out.size())
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_gather_diff_shape():
    input = [[1, 2], [3, 4], [5, 6]]
    index = [[1, 0], [1, 0]]

    tourch_input = torch.tensor(input)
    tourch_index = torch.tensor(index)
    torch_out = torch.gather(tourch_input, 1, tourch_index)

    ms_input = ms_torch.tensor(input)
    ms_index = ms_torch.tensor(index)
    ms_out = ms_torch.gather(ms_input, 1, ms_index)
    param_compare(torch_out, ms_out)

    @ms.jit()
    def gather_jit(input, index):
        return ms_torch.gather(input, 1, index)

    ms_jit_out = gather_jit(ms_input, ms_index)
    param_compare(ms_jit_out, ms_out)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_gather_2d()
    test_gather_2d_long()
    test_gather_3d()
    test_gather_diff_shape()
