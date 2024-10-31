#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE

set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason="fx no need test on GRAPH mode")
def test_fx_proxy():
    a=ms_torch.tensor([1.0])
    assert isinstance(a, ms_torch.fx.Proxy) == False


if __name__ == '__main__':
    set_mode_by_env_config()
    test_fx_proxy()

