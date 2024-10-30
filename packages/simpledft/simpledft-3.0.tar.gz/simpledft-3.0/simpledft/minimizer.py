from .dft import get_grad, get_n_total, get_phi, orth
from .energies import get_E
from .xc import lda_c_chachiyo, lda_x


def scf_step(scf):
    """Perform one SCF step for a DFT calculation."""
    scf.Y = orth(scf.op, scf.W)
    scf.n = get_n_total(scf.atoms, scf.op, scf.Y)
    scf.phi = get_phi(scf.op, scf.n)
    x, c = lda_x(scf.n), lda_c_chachiyo(scf.n)
    scf.exc = x[0] + c[0]
    scf.vxc = x[1] + c[1]
    return get_E(scf)


def sd(scf, Nit, etol=1e-6, beta=1e-5):
    """Steepest descent minimization algorithm.
    Thesis: List. 3.21
            Fig. 3.2
    """
    Elist = []

    for i in range(Nit):
        E = scf_step(scf)
        Elist.append(E)
        print("Nit: {}  \tEtot: {:.6f} Eh".format(i + 1, E), end="\r")
        if i > 1 and abs(Elist[i - 1] - Elist[i]) < etol:
            print("\nSCF converged.")
            return E
        g = get_grad(scf.atoms, scf.op, scf.W, scf.phi, scf.vxc, scf.pot)
        scf.W = scf.W - beta * g
    print("\nSCF not converged!")
    return E
