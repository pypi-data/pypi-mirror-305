from enum import Enum, auto
import mindspore as ms
from mindspore import _no_grad as torch_no_grad
from mindtorch.torch.tensor import Tensor, cast_to_adapter_tensor, cast_to_ms_tensor
from mindtorch.torch.functional import eye as torch_eye, geqrf as torch_geqrf, \
    cat as torch_cat, matrix_exp as torch_matrix_exp, add as torch_add, randn as torch_randn, \
    zeros_like as torch_zeros_like, mv as torch_mv, dot as torch_dot
from mindtorch.torch.common.dtype import finfo as torch_finfo
from mindtorch.torch.linalg import householder_product, solve
from mindtorch.utils import unsupported_attr
from ..utils import parametrize
from ..modules.module import Module
from ..modules import ConvTranspose1d, ConvTranspose2d, ConvTranspose3d
from .. import functional as F



def _is_orthogonal(Q, eps=None):
    unsupported_attr(eps)
    n, k = Q.size(-2), Q.size(-1)
    Id = ms.ops.eye(k, None, Q.dtype)
    eps = 10. * n * torch_finfo(Q.dtype).eps
    Q = cast_to_ms_tensor(Q)
    # TODO: For allclose, the `equal_nan` must be True on Ascend.
    out = ms.ops.all(ms.ops.isclose(Q.mH @ Q, Id, atol=eps, equal_nan=True)).item()
    return cast_to_adapter_tensor(out)


def _make_orthogonal(A):
    input_ms = cast_to_ms_tensor(A)
    X, tau = ms.ops.geqrf(input_ms)
    Q = ms.ops.orgqr(X, tau)
    X_diagonal = X.diagonal(0, -2, -1)
    if 'Bool' in str(X_diagonal.dtype) or 'Int' in str(X_diagonal.dtype):
        type = X_diagonal.dtype
        X_diagonal = X_diagonal.astype(ms.float32)
        output = ms.ops.sgn(X_diagonal).astype(type)
    else:
        output = ms.ops.sgn(X_diagonal)
    Q *= output.unsqueeze(-2)
    return cast_to_adapter_tensor(Q)


class _OrthMaps(Enum):
    matrix_exp = auto()
    cayley = auto()
    householder = auto()


class _Orthogonal(Module):
    def __init__(self,
                 weight,
                 orthogonal_map,
                 *,
                 use_trivialization=True):
        super().__init__()
        if weight.is_complex() and orthogonal_map == _OrthMaps.householder:
            raise ValueError("The householder parametrization does not support complex tensors.")

        self.shape = weight.shape
        self.orthogonal_map = orthogonal_map
        if use_trivialization:
            self.register_buffer("base", None)

    def forward(self, X):
        n, k = X.size(-2), X.size(-1)
        transposed = n < k
        if transposed:
            X = X.mT
            n, k = k, n
        if self.orthogonal_map == _OrthMaps.matrix_exp or self.orthogonal_map == _OrthMaps.cayley:
            X = X.tril()
            if n != k:
                X = torch_cat([X, X.new_zeros(n, n - k).expand(*X.shape[:-2], -1, -1)], dim=-1)
            A = X - X.mH
            if self.orthogonal_map == _OrthMaps.matrix_exp:
                Q = torch_matrix_exp(A)
            elif self.orthogonal_map == _OrthMaps.cayley:
                Id = torch_eye(n, dtype=A.dtype, device=A.device)
                Q = solve(torch_add(Id, A, alpha=-0.5), torch_add(Id, A, alpha=0.5))
            if n != k:
                Q = Q[..., :k]
        else:
            A = X.tril(diagonal=-1)
            tau = 2. / (1. + (A * A).sum(dim=-2))
            Q = householder_product(A, tau)
            Q = Q * X.diagonal(dim1=-2, dim2=-1).int().unsqueeze(-2)

        if hasattr(self, "base"):
            Q = self.base @ Q
        if transposed:
            Q = Q.mT
        return Q

    @torch_no_grad()
    def right_inverse(self, Q):
        if Q.shape != self.shape:
            raise ValueError(f"Expected a matrix or batch of matrices of shape {self.shape}. "
                             f"Got a tensor of shape {Q.shape}.")

        Q_init = Q
        n, k = Q.size(-2), Q.size(-1)
        transpose = n < k
        if transpose:
            Q = Q.mT
            n, k = k, n

        if not hasattr(self, "base"):
            if self.orthogonal_map == _OrthMaps.cayley or self.orthogonal_map == _OrthMaps.matrix_exp:
                raise NotImplementedError("It is not possible to assign to the matrix exponential "
                                          "or the Cayley parametrizations when use_trivialization=False.")

            A, tau = torch_geqrf(Q)

            # TODO: Currently, there are defects in the combination of view and in-place scenarios.
            # A.diagonal(dim1=-2, dim2=-1).sign_()
            # A.diagonal(dim1=-2, dim2=-1)[tau == 0.] *= -1

            A_diagonal = A.diagonal(dim1=-2, dim2=-1)
            A_diagonal[:] = A_diagonal.sign()
            A_diagonal = A.diagonal(dim1=-2, dim2=-1)
            A_diagonal[tau == 0.] *= -1
            A.diagonal(dim1=-2, dim2=-1)[:] = A_diagonal

            return A.mT if transpose else A
        else:
            if n == k:
                if not _is_orthogonal(Q):
                    Q = _make_orthogonal(Q)
                else:
                    Q = Q.clone()
            else:
                N = torch_randn(*(Q.size()[:-2] + (n, n - k)), dtype=Q.dtype, device=Q.device)
                Q = torch_cat([Q, N], dim=-1)
                Q = _make_orthogonal(Q)
            self.base = Q

            neg_Id = torch_zeros_like(Q_init)

            # TODO: Currently, there are defects in the combination of view and in-place scenarios.
            # neg_Id.diagonal(dim1=-2, dim2=-1).fill_(-1.)
            neg_Id_diagonal = neg_Id.diagonal(dim1=-2, dim2=-1)
            neg_Id_diagonal[:] = -1.

            return neg_Id


def orthogonal(module,
               name='weight',
               orthogonal_map=None,
               *,
               use_trivialization=True):
    weight = getattr(module, name, None)
    if not isinstance(weight, Tensor):
        raise ValueError(
            "Module '{}' has no parameter ot buffer with name '{}'".format(module, name)
        )

    if weight.ndim < 2:
        raise ValueError("Expected a matrix or batch of matrices. "
                         f"Got a tensor of {weight.ndim} dimensions.")

    if orthogonal_map is None:
        orthogonal_map = "matrix_exp" if weight.size(-2) == weight.size(-1) or weight.is_complex() else "householder"

    orth_enum = getattr(_OrthMaps, orthogonal_map, None)
    if orth_enum is None:
        raise ValueError('orthogonal_map has to be one of "matrix_exp", "cayley", "householder". '
                         f'Got: {orthogonal_map}')
    orth = _Orthogonal(weight,
                       orth_enum,
                       use_trivialization=use_trivialization)
    parametrize.register_parametrization(module, name, orth, unsafe=True)
    return module


class _SpectralNorm(Module):
    def __init__(
        self,
        weight,
        n_power_iterations=1,
        dim=0,
        eps=1e-12
    ):
        super().__init__()
        ndim = weight.ndim
        if dim >= ndim or dim < -ndim:
            raise IndexError("Dimension out of range (expected to be in range of "
                             f"[-{ndim}, {ndim - 1}] but got {dim})")

        if n_power_iterations <= 0:
            raise ValueError('Expected n_power_iterations to be positive, but '
                             'got n_power_iterations={}'.format(n_power_iterations))
        self.dim = dim if dim >= 0 else dim + ndim
        self.eps = eps
        if ndim > 1:
            self.n_power_iterations = n_power_iterations
            weight_mat = self._reshape_weight_to_matrix(weight)
            h, w = weight_mat.size()

            u = weight_mat.new_empty(h).normal_(0, 1)
            v = weight_mat.new_empty(w).normal_(0, 1)
            self.register_buffer('_u', F.normalize(u, dim=0, eps=self.eps))
            self.register_buffer('_v', F.normalize(v, dim=0, eps=self.eps))

            self._power_method(weight_mat, 15)

    def _reshape_weight_to_matrix(self, weight):
        assert weight.ndim > 1

        if self.dim != 0:
            weight = weight.permute(self.dim, *(d for d in range(weight.dim()) if d != self.dim))

        return weight.flatten(1)

    @torch_no_grad()
    def _power_method(self, weight_mat, n_power_iterations):
        assert weight_mat.ndim > 1

        for _ in range(n_power_iterations):
            self._u = F.normalize(torch_mv(weight_mat, self._v),      # pylint: disable=E0203
                                  dim=0, eps=self.eps, out=self._u)
            self._v = F.normalize(torch_mv(weight_mat.t(), self._u),
                                  dim=0, eps=self.eps, out=self._v)

    def forward(self, weight):
        if weight.ndim == 1:
            return F.normalize(weight, dim=0, eps=self.eps)
        else:
            weight_mat = self._reshape_weight_to_matrix(weight)
            if self.training:
                self._power_method(weight_mat, self.n_power_iterations)
            u = self._u.clone()
            v = self._v.clone()
            sigma = torch_dot(u, torch_mv(weight_mat, v))
            return weight / sigma

    def right_inverse(self, value):
        return value


def spectral_norm(module,
                  name='weight',
                  n_power_iterations=1,
                  eps=1e-12,
                  dim=None):
    weight = getattr(module, name, None)
    if not isinstance(weight, Tensor):
        raise ValueError(
            "Module '{}' has no parameter or buffer with name '{}'".format(module, name)
        )

    if dim is None:
        if isinstance(module, (ConvTranspose1d,
                               ConvTranspose2d,
                               ConvTranspose3d)):
            dim = 1
        else:
            dim = 0
    parametrize.register_parametrization(module, name, _SpectralNorm(weight, n_power_iterations, dim, eps))
    return module
