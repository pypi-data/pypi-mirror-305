#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import pytest

import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context
import math

from ....utils import set_mode_by_env_config, is_test_under_ascend_context, SKIP_ENV_CPU, SKIP_ENV_GPU, TestNet
set_mode_by_env_config()

@SKIP_ENV_CPU(reason="prompt_flash_attention is not supported on cpu.")
@SKIP_ENV_GPU(reason="prompt_flash_attention is not supported on gpu.")
def test_prompt_flash_attention_shape():
    B = 1
    N = 16
    S = 256
    D = 16

    query = ms_torch.randn((B, N, S, D), dtype=ms_torch.float16)
    key = ms_torch.randn((B, N, S, D), dtype=ms_torch.float16)
    value = ms_torch.randn((B, N, S, D), dtype=ms_torch.float16)
    attn_mask = ms_torch.zeros((B, 1, S, S), dtype=ms_torch.float16)

    pfa_net = TestNet(ms_torch.nn.functional.prompt_flash_attention)
    pfa_output = pfa_net(query, key, value, attn_mask=attn_mask,
                         num_heads=N, scale_value=1.0, pre_tokens=2147483547, next_tokens=0,
                         input_layout='BNSD', num_key_value_heads=0)
    assert pfa_output.shape == (B, N, S, D)

def compute_prompt_flash_attention_no_padding(query, key, value, attn_mask, N, D):
    pfa_net = TestNet(ms_torch.nn.functional.prompt_flash_attention)
    scale_value = 1 / math.sqrt(D)
    pfa_output = pfa_net(query, key, value, attn_mask=attn_mask,
                         num_heads=N, scale_value=scale_value,
                         next_tokens=65535, input_layout='BNSD', num_key_value_heads=N)
    sdpa_net = TestNet(ms_torch.nn.functional.scaled_dot_product_attention)
    sdpa_output = sdpa_net(query, key, value, attn_mask=attn_mask, dropout_p=0.0, is_causal=False)
    return pfa_output, sdpa_output

@SKIP_ENV_CPU(reason="prompt_flash_attention is not supported on cpu.")
@SKIP_ENV_GPU(reason="prompt_flash_attention is not supported on gpu.")
def test_prompt_flash_attention_no_padding():
    B = 2
    N = 8
    S = 256
    D = 80

    query = ms_torch.randn((B, N, S, D), dtype=ms_torch.float16)
    key = ms_torch.randn((B, N, S, D), dtype=ms_torch.float16)
    value = ms_torch.randn((B, N, S, D), dtype=ms_torch.float16)
    attn_mask = None
    pfa_output, sdpa_output = compute_prompt_flash_attention_no_padding(query, key, value, attn_mask, N, D)
    assert np.allclose(pfa_output.numpy(), sdpa_output.numpy(), rtol=1e-3, atol=1e-3)

    query = ms_torch.randn((B, N, S, D), dtype=ms_torch.float16)
    key = ms_torch.randn((B, N, 77, D), dtype=ms_torch.float16)
    value = ms_torch.randn((B, N, 77, D), dtype=ms_torch.float16)
    attn_mask = None
    pfa_output, sdpa_output = compute_prompt_flash_attention_no_padding(query, key, value, attn_mask, N, D)
    assert np.allclose(pfa_output.numpy(), sdpa_output.numpy(), rtol=1e-3, atol=1e-3)

if __name__ == "__main__":
    test_prompt_flash_attention_shape()
    test_prompt_flash_attention_no_padding()
