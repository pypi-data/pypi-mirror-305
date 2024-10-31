#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import mindtorch.torch as torch

from testing.ut.utils import set_mode_by_env_config, type_shape_compare, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason="skip_init is not supported in GRAPH_MODE")
def test_skip_init():
    torch.manual_seed(1)
    m_initialized = torch.nn.Linear(5, 1)

    torch.manual_seed(1)
    m_uninitialized = torch.nn.utils.skip_init(torch.nn.Linear, 5, 1)

    type_shape_compare(m_initialized.weight, m_uninitialized.weight)
    assert not np.allclose(m_initialized.weight.numpy(), m_uninitialized.weight.numpy())


if __name__ == '__main__':
    set_mode_by_env_config()
    test_skip_init()
