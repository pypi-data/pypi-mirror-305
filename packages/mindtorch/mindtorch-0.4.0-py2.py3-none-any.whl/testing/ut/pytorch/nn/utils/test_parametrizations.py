#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import numpy as np
import mindtorch.torch as torch
import mindtorch.torch.nn as nn
import mindtorch.torch.nn.utils.parametrize as parametrize
import mindspore as ms
from itertools import product
from testing.ut.utils import set_mode_by_env_config, param_compare, SKIP_ENV_GPU, SKIP_ENV_CPU, SKIP_ENV_GRAPH_MODE, \
    enable_backward
set_mode_by_env_config()


@SKIP_ENV_GPU(reason="Unsupported op [MatrixExp] on GPU.")
@SKIP_ENV_CPU(reason="Unsupported op [MatrixExp] on CPU.")
@SKIP_ENV_GRAPH_MODE(reason="orthogonal is not supported in GRAPH_MODE")
def test_orthogonal_parametrization():
    def assert_is_orthogonal(X):
        n, k = X.size(-2), X.size(-1)
        if n < k:
            X = X.mT
            n, k = k, n
        Id = torch.eye(k, dtype=X.dtype, device=X.device).expand(*(X.size()[:-2]), k, k)
        param_compare(X.mH @ X, Id, atol=1e-3, rtol=1e-3)

    def assert_weight_allclose_Q(weight, W):
        # Test that weight is equal to the Q part of the QR decomposition of W
        # (or of its transpose if the matrix is wide)
        wide_matrix = W.size(-2) < W.size(-1)
        if wide_matrix:
            W = W.mT
        Q, R = torch.linalg.qr(W)
        Q *= R.diagonal(dim1=-2, dim2=-1).sgn().unsqueeze(-2)
        if wide_matrix:
            Q = Q.mT
        param_compare(Q, weight, atol=1e-3, rtol=1e-3)

    with enable_backward():
        for shape, dtype, use_linear in product(((4, 4), (5, 3), (3, 5)),  # square/ tall / wide
                                                (torch.float32,),
                                                (True, False)):
            # Conv2d does not support complex yet
            if not use_linear:
                continue

            if use_linear:
                input = torch.randn(3, shape[0], dtype=dtype)
            else:
                input = torch.randn(2, 2, shape[0] + 2, shape[1] + 1, dtype=dtype)

            for parametrization, use_trivialization in product(("matrix_exp", "cayley", "householder"),
                                                               (False, True)):
                can_initialize = use_trivialization or parametrization == "householder"

                if use_linear:
                    m = nn.Linear(*shape, dtype=dtype)
                else:
                    m = nn.Conv2d(2, 3, shape, dtype=dtype)

                w_init = m.weight.clone()
                if parametrization == "householder" and m.weight.is_complex():
                    msg = "householder parametrization does not support complex tensors"
                    with pytest.raises(ValueError, match=msg):
                        torch.nn.utils.parametrizations.orthogonal(m,
                                                                   "weight",
                                                                   parametrization,
                                                                   use_trivialization=use_trivialization)
                    continue

                wide_matrix = w_init.size(-2) < w_init.size(-1)
                torch.nn.utils.parametrizations.orthogonal(m,
                                                           "weight",
                                                           parametrization,
                                                           use_trivialization=use_trivialization)
                # Forwards works as expected
                assert w_init.shape == m.weight.shape
                assert_is_orthogonal(m.weight)
                if can_initialize:
                    assert_weight_allclose_Q(m.weight, w_init)

                # Intializing with a given orthogonal matrix works
                X = torch.randn_like(m.weight)
                if wide_matrix:
                    X = X.mT
                w_new = torch.linalg.qr(X).Q
                if wide_matrix:
                    w_new = w_new.mT
                if can_initialize:
                    m.weight = w_new
                    param_compare(w_new, m.weight, atol=1e-3, rtol=1e-3)
                else:
                    msg = "assign to the matrix exponential or the Cayley parametrization"
                    with pytest.raises(NotImplementedError, match=msg):
                        m.weight = w_new

                # Intializing with a non-orthogonal matrix makes m.weight be the Q part of the given matrix
                w_new = torch.randn_like(m.weight)
                if can_initialize:
                    m.weight = w_new
                    assert_weight_allclose_Q(m.weight, w_new)
                else:
                    msg = "assign to the matrix exponential or the Cayley parametrization"
                    with pytest.raises(NotImplementedError, match=msg):
                        m.weight = w_new

                opt = torch.optim.SGD(m.parameters(), lr=0.1)

                # TODO: cayley:`solve`, which implement through the numpy API, can not backward currently.
                #  householder: Orgqr's bprop not defined.
                if parametrization in ("cayley", "householder"):
                    continue

                for _ in range(2):
                    opt.zero_grad()
                    m(input).norm().backward()
                    grad = m.parametrizations.weight.original.grad
                    assert grad is not None
                    if grad.size(-2) >= grad.size(-1):
                        zeros_grad = grad.triu(1)
                    else:
                        zeros_grad = grad.tril(-1)
                    param_compare(zeros_grad, torch.zeros_like(zeros_grad))
                    diag_grad = grad.diagonal(dim1=-2, dim2=-1)
                    if grad.is_complex():
                        diag_grad = diag_grad.real
                    param_compare(diag_grad, torch.zeros_like(diag_grad))
                    opt.step()
                    assert_is_orthogonal(m.weight)


@SKIP_ENV_GRAPH_MODE(reason="parametrize.cached is not supported in GRAPH_MODE")
def test_caching_parametrization():
    class Skew(nn.Module):
        def forward(self, X):
            X = X.tril(-1)
            return X - X.T

    class Orthogonal(nn.Module):
        def forward(self, X):
            Id = torch.eye(X.size(0), device=X.device)
            return torch.linalg.solve(Id + X, Id - X)

    model = nn.Linear(5, 5)
    parametrize.register_parametrization(model, "weight", Skew())
    parametrize.register_parametrization(model, "weight", Orthogonal())

    with parametrize.cached():
        X = model.weight
        Y = model.weight
        assert id(X) == id(Y)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_orthogonal_parametrization()
    test_new_spectral_norm()
    test_caching_parametrization()
