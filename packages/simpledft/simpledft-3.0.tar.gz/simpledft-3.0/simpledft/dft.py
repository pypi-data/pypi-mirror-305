import numpy as np

from .utils import sqrtm


def get_phi(op, n):
    """Solve the Poisson equation.
    Thesis: Eq. 2.48
    """
    return -4 * np.pi * op.Linv(op.O(op.J(n)))


def get_n_total(atoms, op, Y):
    """Calculate the total electronic density.
    Thesis: Eq. 2.36
            List. 3.23
    """
    Yrs = op.I(Y)
    n = atoms.f * np.real(Yrs.conj() * Yrs)
    return np.sum(n, axis=1)


def orth(op, W):
    """Orthogonalize coefficient matrix W.
    Thesis: Eq. 2.34 ff.
    """
    U = sqrtm(W.conj().T @ op.O(W))
    return W @ np.linalg.inv(U)


def get_grad(atoms, op, W, phi, vxc, Vreciproc):
    """Calculate the energy gradient with respect to W.
    Thesis: Eq. 2.43
            List. 3.24
    """
    F = np.diag(atoms.f)
    HW = H(op, W, phi, vxc, Vreciproc)
    WHW = W.conj().T @ HW
    OW = op.O(W)
    U = W.conj().T @ OW
    invU = np.linalg.inv(U)
    U12 = sqrtm(invU)
    Ht = U12 @ WHW @ U12
    return (HW - (OW @ invU) @ WHW) @ (U12 @ F @ U12) + OW @ (U12 @ Q(Ht @ F - F @ Ht, U))


def H(op, W, phi, vxc, Vreciproc):
    """Left-hand side of the eigenvalue equation.
    Thesis: Eq. 2.45 ff.
            List. 3.26
    """
    Veff = Vreciproc + op.Jdag(op.O(op.J(vxc) + phi))
    return -0.5 * op.L(W) + op.Idag(Veff[:, None] * op.I(W))


def Q(inp, U):
    """Operator needed to calculate gradients with non-constant occupations.
    Thesis: Eq. 2.47
            List. 3.25
    """
    mu, V = np.linalg.eig(U)
    mu = mu[:, None]
    denom = np.sqrt(mu) @ np.ones((1, len(mu)))
    denom2 = denom + denom.conj().T
    return V @ ((V.conj().T @ inp @ V) / denom2) @ V.conj().T
