"""Implement various linear algebra algorithms for low rank matrices.
"""

__all__ = ["svd_lowrank", "pca_lowrank"]

from typing import Optional, Tuple

from mindtorch.torch.linalg import qr, svd
from mindtorch.torch.tensor import Tensor
from mindtorch.torch.functional import randn
from mindtorch.torch._linalg_utils import get_floating_dtype, s_matmul, \
    transjugate, transpose, conjugate, is_sparse


def get_approximate_basis(
    A: Tensor, q: int, niter: Optional[int] = 2, M: Optional[Tensor] = None
) -> Tensor:
    """Return tensor :math:`Q` with :math:`q` orthonormal columns such
    that :math:`Q Q^H A` approximates :math:`A`. If :math:`M` is
    specified, then :math:`Q` is such that :math:`Q Q^H (A - M)`
    approximates :math:`A - M`.

    .. note:: The implementation is based on the Algorithm 4.4 from
              Halko et al, 2009.

    .. note:: For an adequate approximation of a k-rank matrix
              :math:`A`, where k is not known in advance but could be
              estimated, the number of :math:`Q` columns, q, can be
              choosen according to the following criteria: in general,
              :math:`k <= q <= min(2*k, m, n)`. For large low-rank
              matrices, take :math:`q = k + 5..10`.  If k is
              relatively small compared to :math:`min(m, n)`, choosing
              :math:`q = k + 0..2` may be sufficient.

    .. note:: To obtain repeatable results, reset the seed for the
              pseudorandom number generator

    Args::
        A (Tensor): the input tensor of size :math:`(*, m, n)`

        q (int): the dimension of subspace spanned by :math:`Q`
                 columns.

        niter (int, optional): the number of subspace iterations to
                               conduct; ``niter`` must be a
                               nonnegative integer. In most cases, the
                               default value 2 is more than enough.

        M (Tensor, optional): the input tensor's mean of size
                              :math:`(*, 1, n)`.

    References::
        - Nathan Halko, Per-Gunnar Martinsson, and Joel Tropp, Finding
          structure with randomness: probabilistic algorithms for
          constructing approximate matrix decompositions,
          arXiv:0909.4061 [math.NA; math.PR], 2009 (available at
          `arXiv <http://arxiv.org/abs/0909.4061>`_).
    """

    niter = 2 if niter is None else niter
    _, n = A.shape[-2:]
    dtype = get_floating_dtype(A)

    R = randn(n, q, dtype=dtype)

    # The following code could be made faster using torch.geqrf + torch.ormqr
    # but geqrf is not differentiable
    A_H = transjugate(A)
    if M is None:
        Q = qr(s_matmul(A, R)).Q
        for dummy_i in range(niter):
            Q = qr(s_matmul(A_H, Q)).Q
            Q = qr(s_matmul(A, Q)).Q
    else:
        M_H = transjugate(M)
        Q = qr(s_matmul(A, R) - s_matmul(M, R)).Q
        for dummy_i in range(niter):
            Q = qr(s_matmul(A_H, Q) - s_matmul(M_H, Q)).Q
            Q = qr(s_matmul(A, Q) - s_matmul(M, Q)).Q

    return Q

def svd_lowrank(
    A: Tensor,
    q: Optional[int] = 6,
    niter: Optional[int] = 2,
    M: Optional[Tensor] = None,
) -> Tuple[Tensor, Tensor, Tensor]:
    q = 6 if q is None else q
    m, n = A.shape[-2:]
    if M is None:
        M_t = None
    else:
        M_t = transpose(M)
    A_t = transpose(A)

    # Algorithm 5.1 in Halko et al 2009, slightly modified to reduce
    # the number conjugate and transpose operations
    if m < n or n > q:
        # computing the SVD approximation of a transpose in
        # order to keep B shape minimal (the m < n case) or the V
        # shape small (the n > q case)
        Q = get_approximate_basis(A_t, q, niter=niter, M=M_t)
        Q_c = conjugate(Q)
        if M is None:
            B_t = s_matmul(A, Q_c)
        else:
            B_t = s_matmul(A, Q_c) - s_matmul(M, Q_c)
        assert B_t.shape[-2] == m, (B_t.shape, m)
        assert B_t.shape[-1] == q, (B_t.shape, q)
        assert B_t.shape[-1] <= B_t.shape[-2], B_t.shape
        U, S, Vh = svd(B_t, full_matrices=False)
        V = Vh.mH
        V = Q.matmul(V)
    else:
        Q = get_approximate_basis(A, q, niter=niter, M=M)
        Q_c = conjugate(Q)
        if M is None:
            B = s_matmul(A_t, Q_c)
        else:
            B = s_matmul(A_t, Q_c) - s_matmul(M_t, Q_c)
        B_t = transpose(B)
        assert B_t.shape[-2] == q, (B_t.shape, q)
        assert B_t.shape[-1] == n, (B_t.shape, n)
        assert B_t.shape[-1] <= B_t.shape[-2], B_t.shape
        U, S, Vh = svd(B_t, full_matrices=False)
        V = Vh.mH
        U = Q.matmul(U)

    return U, S, V


def pca_lowrank(
    A: Tensor, q: Optional[int] = None, center: bool = True, niter: int = 2
) -> Tuple[Tensor, Tensor, Tensor]:
    r"""Performs linear Principal Component Analysis (PCA) on a low-rank
    matrix, batches of such matrices, or sparse matrix.

    This function returns a namedtuple ``(U, S, V)`` which is the
    nearly optimal approximation of a singular value decomposition of
    a centered matrix :math:`A` such that :math:`A = U diag(S) V^T`.

    .. note:: The relation of ``(U, S, V)`` to PCA is as follows:

                - :math:`A` is a data matrix with ``m`` samples and
                  ``n`` features

                - the :math:`V` columns represent the principal directions

                - :math:`S ** 2 / (m - 1)` contains the eigenvalues of
                  :math:`A^T A / (m - 1)` which is the covariance of
                  ``A`` when ``center=True`` is provided.

                - ``s_matmul(A, V[:, :k])`` projects data to the first k
                  principal components

    .. note:: Different from the standard SVD, the size of returned
              matrices depend on the specified rank and q
              values as follows:

                - :math:`U` is m x q matrix

                - :math:`S` is q-vector

                - :math:`V` is n x q matrix

    .. note:: To obtain repeatable results, reset the seed for the
              pseudorandom number generator

    Args:

        A (Tensor): the input tensor of size :math:`(*, m, n)`

        q (int, optional): a slightly overestimated rank of
                           :math:`A`. By default, ``q = min(6, m,
                           n)``.

        center (bool, optional): if True, center the input tensor,
                                 otherwise, assume that the input is
                                 centered.

        niter (int, optional): the number of subspace iterations to
                               conduct; niter must be a nonnegative
                               integer, and defaults to 2.

    References::

        - Nathan Halko, Per-Gunnar Martinsson, and Joel Tropp, Finding
          structure with randomness: probabilistic algorithms for
          constructing approximate matrix decompositions,
          arXiv:0909.4061 [math.NA; math.PR], 2009 (available at
          `arXiv <http://arxiv.org/abs/0909.4061>`_).

    """
    (m, n) = A.shape[-2:]

    if q is None:
        q = min(6, m, n)
    elif not 0 <= q <= min(m, n):
        raise ValueError(
            "q(={}) must be non-negative integer"
            " and not greater than min(m, n)={}".format(q, min(m, n))
        )
    if niter < 0:
        raise ValueError("niter(={}) must be non-negative integer".format(niter))

    if not center:
        return svd_lowrank(A, q, niter=niter, M=None)

    if is_sparse(A):
        raise NotImplementedError('A is a sparse matrix, pca is not implemented.')
    else:
        C = A.mean(dim=(-2,), keepdim=True)
        return svd_lowrank(A - C, q, niter=niter, M=None)
