#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE

set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason="jit no need test on GRAPH mode")
def test_jit_script():
    @ms_torch.jit.script 
    def foo(a, b): 
        return a+b

    a = ms_torch.tensor([1.0])
    b = ms_torch.tensor([2.0])
    out = foo(a, b)
    assert out.asnumpy() == 3.0
    
    assert ms_torch.jit.is_tracing() == False
    assert ms_torch.jit.is_scripting() == False


@SKIP_ENV_GRAPH_MODE(reason="jit no need test on GRAPH mode")
def test_jit_ignore():
    @ms_torch.jit.ignore 
    def foo1(a, b): 
        return a+b

    @ms_torch.jit.ignore 
    def foo2(a, b): 
        return a+b

    a = ms_torch.tensor([1.0])
    b = ms_torch.tensor([2.0])
    out1 = foo1(a, b)
    out2 = foo2(a, b)
    assert out1.asnumpy() == out2.asnumpy()


def test_jit_final():
    ms_torch.jit.Final[bool]

if __name__ == '__main__':
    set_mode_by_env_config()
    test_jit_script()
    test_jit_ignore()
    test_jit_final()

