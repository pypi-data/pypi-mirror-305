#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindtorch.torch as torch
import mindtorch.torch.nn.utils.stateless as stateless

from testing.ut.utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason="stateless is not supported in GRAPH_MODE")
def test_functional_batch_norm():
    module = torch.nn.BatchNorm1d(10)
    module.train()  # Allow stats update
    # lets replace the running_mean buffer and check if its correctly updated
    x = torch.full((20, 10), 128.0)
    rm = torch.zeros(10)
    parameters = {'running_mean': rm}
    prev_rm = module.running_mean.clone()
    res = stateless.functional_call(module, parameters, x)
    cur_rm = module.running_mean
    param_compare(cur_rm, prev_rm)
    param_compare(rm, torch.full((10,), 12.8))
    # Now run functional without reparametrization and check that the module has
    # been updated
    res = stateless.functional_call(module, {}, x)
    param_compare(module.running_mean, torch.full((10,), 12.8))


if __name__ == '__main__':
    set_mode_by_env_config()
    test_functional_batch_norm()
