#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import mindtorch.torch as torch
import mindtorch.torch.nn as nn

from testing.ut.utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason="weight_norm not supported in GRAPH_MODE")
def test_weight_norm():
    input = torch.randn(3, 4, dtype=torch.float)
    m = nn.Linear(4, 5).to(dtype=torch.float)
    expected_output = m(input)

    # add weight normalization
    m = torch.nn.utils.weight_norm(m)
    assert m.weight_v.size() == m.weight.size()
    assert m.weight_g.size() == (5, 1)
    param_compare(m(input), expected_output)

    # remove weight norm
    m = torch.nn.utils.remove_weight_norm(m)
    assert not hasattr(m, 'weight_g')
    assert not hasattr(m, 'weight_v')
    param_compare(m(input), expected_output)

    # test with dim=1
    m = torch.nn.utils.weight_norm(m, dim=1)
    assert m.weight_v.size() == m.weight.size()
    assert m.weight_g.size() == (1, 4)
    param_compare(m(input), expected_output)

    # test with dim=None
    m = nn.Linear(4, 5).to(dtype=torch.float)
    expected_output = m(input)
    m = torch.nn.utils.weight_norm(m, dim=None)
    param_compare(m(input), expected_output)

    with pytest.raises(RuntimeError):
        m = torch.nn.utils.weight_norm(m)
        m = torch.nn.utils.weight_norm(m)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_weight_norm()
