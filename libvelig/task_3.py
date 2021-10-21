import numpy as np

from libvelig.common import generate_e_matrix


def solve(p_ksi: np.ndarray, p_eta: np.ndarray) -> np.ndarray:
    '''
    Builds the distribution of sum of random variables ksi and eta.

    @param p_ksi - random variable 1.
    @param p_eta - random variable 2.
    @throws - ValueError in case of invalid parameters passed.
    @returns - p_ksi and p_eta sum distribution.
    '''
    if np.sum(p_ksi) != 1 or np.sum(p_eta) != 1:
        raise ValueError("Fuck your probabilities, dumbo! They don't add up to 1!")

    n = len(p_ksi)
    if len(p_eta) != n:
        raise ValueError("FUck yoU! They are DIFFERENT SIZES!!! FUKC!!!")

    E = generate_e_matrix(n)

    phi_ksi = E.dot(p_ksi)
    phi_eta = E.dot(p_eta)

    E_inv = 1.0 / n * np.conjugate(E)

    return E_inv.dot(phi_ksi * phi_eta)
