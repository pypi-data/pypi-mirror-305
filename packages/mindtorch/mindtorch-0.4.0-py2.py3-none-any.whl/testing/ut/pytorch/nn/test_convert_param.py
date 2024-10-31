#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindspore as ms
import mindtorch.torch as ms_torch
import mindtorch.torch.nn as nn

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, SKIP_ENV_PYNATIVE_MODE
set_mode_by_env_config()

@SKIP_ENV_GRAPH_MODE(reason="`model.parameters()` has `yield`, that unspport on Graph mode.")
def test_parameters_to_vector():
        conv1 = nn.Conv2d(3, 10, 5)
        fc1 = nn.Linear(10, 20)
        model = nn.Sequential(conv1, fc1)

        vec = nn.utils.parameters_to_vector(model.parameters())
        assert (vec.size(0) == 980)
        assert isinstance(vec[0], ms_torch.Tensor)


@SKIP_ENV_PYNATIVE_MODE(reason=" testcase only for Graph mode")
def test_parameters_to_vector_2():
        para1 = ms_torch.nn.Parameter(ms_torch.tensor([1.0, 2.0]), name="name_1")
        para2 = ms_torch.nn.Parameter(ms_torch.tensor([3.0, 4.0]))
        params_vec = [para1, para2]
        @ms.jit
        def fn():
            vec = nn.utils.parameters_to_vector(params_vec)
            return vec
        vec = fn()
        assert isinstance(vec[0], ms_torch.Tensor)


@SKIP_ENV_GRAPH_MODE(reason="Unsupport to set attribute for a parameter on Graph mode.")
def test_vector_to_parameters():
    conv1 = nn.Conv2d(3, 10, 5)
    fc1 = nn.Linear(10, 20)
    model = nn.Sequential(conv1, fc1)

    vec = ms_torch.arange(0., 980)
    nn.utils.vector_to_parameters(vec, model.parameters())

    sample = next(model.parameters())[0, 0, 0]
    assert (ms_torch.equal(sample.data, vec.data[:5]))


@SKIP_ENV_GRAPH_MODE(reason="Unsupport to set attribute for a parameter on Graph mode.")
def test_vector_to_parameters_2():
        import torch as ms_torch
        vec = ms_torch.arange(0., 8).reshape(2, 4)
        params = (ms_torch.nn.Parameter(ms_torch.ones(2, 4)),)
        ms_torch.nn.utils.vector_to_parameters(vec, params)
        assert (ms_torch.equal(params[0].data, vec.data))

if __name__ == '__main__':
    set_mode_by_env_config()
    test_parameters_to_vector()
    test_parameters_to_vector_2()
    test_vector_to_parameters()
    test_vector_to_parameters_2()