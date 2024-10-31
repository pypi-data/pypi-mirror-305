#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import numpy as np
import mindtorch.torch as torch
import mindtorch.torch.nn as nn

from testing.ut.utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason="spectral_norm not supported in GRAPH_MODE")
def test_spectral_norm1():
    m = nn.Linear(5, 7)
    m = torch.nn.utils.spectral_norm(m)

    assert m.weight_u.size() == torch.Size([m.weight.size(0)])
    # weight_orig should be trainable
    assert hasattr(m, 'weight_orig')
    assert 'weight_orig' in m._parameters
    # weight_u should be just a reused buffer
    assert hasattr(m, 'weight_u')
    assert 'weight_u' in m._buffers
    assert 'weight_v' in m._buffers
    # weight should be a plain attribute, not counted as a buffer or a param
    assert 'weight' not in m._buffers
    assert 'weight' not in m._parameters
    # it should also be sharing storage as `weight_orig`
    # TODO: assert m.weight_orig.storage() == m.weight.storage()
    param_compare(m.weight_orig, m.weight)
    assert m.weight_orig.size() == m.weight.size()
    assert m.weight_orig.stride() == m.weight.stride()

    m = torch.nn.utils.remove_spectral_norm(m)
    assert not hasattr(m, 'weight_orig')
    assert not hasattr(m, 'weight_u')
    # weight should be converted back as a parameter
    assert hasattr(m, 'weight')
    assert 'weight' in m._parameters

    with pytest.raises(RuntimeError):
        m = torch.nn.utils.spectral_norm(m)
        m = torch.nn.utils.spectral_norm(m)

@SKIP_ENV_GRAPH_MODE(reason="spectral_norm not supported in GRAPH_MODE")
def test_spectral_norm2():
    m = nn.Linear(3, 4)
    m = torch.nn.utils.spectral_norm(m)
    wrapped_m = m
    assert hasattr(m, 'weight_u')
    u0 = m.weight_u.clone()
    v0 = m.weight_v.clone()

    # TEST TRAINING BEHAVIOR
    # assert that u and v are updated
    input = torch.randn(2, 3)
    out1 = wrapped_m(input)
    assert not np.allclose(u0.numpy(), m.weight_u.numpy())
    assert not np.allclose(v0.numpy(), m.weight_v.numpy())

    out2 = wrapped_m(input)
    assert not np.allclose(out1.numpy(), out2.numpy())

    # test removing
    pre_remove_out = wrapped_m(input)
    m = torch.nn.utils.remove_spectral_norm(m)
    param_compare(wrapped_m(input), pre_remove_out)

    m = torch.nn.utils.spectral_norm(m)
    for _ in range(3):
        pre_remove_out = wrapped_m(input)
    m = torch.nn.utils.remove_spectral_norm(m)
    param_compare(wrapped_m(input), pre_remove_out)

    # TEST EVAL BEHAVIOR
    m = torch.nn.utils.spectral_norm(m)
    wrapped_m(input)
    last_train_out = wrapped_m(input)
    last_train_u = m.weight_u.clone()
    last_train_v = m.weight_v.clone()
    wrapped_m.zero_grad()
    wrapped_m.eval()

    eval_out0 = wrapped_m(input)
    # assert eval gives same result as last training iteration
    param_compare(eval_out0, last_train_out)
    # assert doing more iteartion in eval don't change things
    param_compare(eval_out0, wrapped_m(input))
    param_compare(last_train_u, m.weight_u)
    param_compare(last_train_v, m.weight_v)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_spectral_norm1()
    test_spectral_norm2()
