#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torch
import math
import mindtorch.torch as ms_torch
from ....utils import set_mode_by_env_config, param_compare, TestNet, is_test_under_ascend_context
set_mode_by_env_config()

def scaled_dot_product_attention_torch(query, key, value, attn_mask=None, dropout_p=0.0, is_causal=False, scale=None):
    L, S = query.size(-2), key.size(-2)
    scale_factor = 1 / math.sqrt(query.size(-1)) if scale is None else scale
    attn_bias = torch.zeros(L, S, dtype=query.dtype)
    if is_causal:
        assert attn_mask is None
        temp_mask = torch.ones(L, S, dtype=torch.bool).tril(diagonal=0)
        attn_bias.masked_fill_(temp_mask.logical_not(), float("-inf"))
        attn_bias.to(query.dtype)

    if attn_mask is not None:
        if attn_mask.dtype == torch.bool:
            attn_mask.masked_fill_(attn_mask.logical_not(), float("-inf"))
        else:
            attn_bias += attn_mask
    attn_weight = query @ key.transpose(-2, -1) * scale_factor
    attn_weight += attn_bias
    attn_weight = torch.softmax(attn_weight, dim=-1)
    attn_weight = torch.dropout(attn_weight, dropout_p, train=True)
    return attn_weight @ value

def test_scaled_dot_product_attention():
    query = torch.rand(4, 2, 16, 8, dtype=torch.float32)
    key = torch.rand(4, 2, 16, 8, dtype=torch.float32)
    value = torch.rand(4, 2, 16, 8, dtype=torch.float32)
    torch_out = scaled_dot_product_attention_torch(query, key, value)

    query_np = query.numpy()
    key_np = key.numpy()
    value_np = value.numpy()
    query_ms = ms_torch.tensor(query_np, dtype=ms_torch.float32)
    key_ms = ms_torch.tensor(key_np, dtype=ms_torch.float32)
    value_ms = ms_torch.tensor(value_np, dtype=ms_torch.float32)
    scaled_dot_product_attention_net = TestNet(ms_torch.nn.functional.scaled_dot_product_attention)
    msa_out = scaled_dot_product_attention_net(query_ms, key_ms, value_ms)

    if is_test_under_ascend_context():
        param_compare(torch_out, msa_out, atol=1e-3)
    else:
        param_compare(torch_out, msa_out, atol=1e-5)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_scaled_dot_product_attention()
