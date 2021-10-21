import numpy as np

from common import generate_e_matrix


def solve(p: np.ndarray, eps: float) -> int:
    '''
    Returns number n such that n * ksi has property Sum((p_i - 1 / N) * 2) <= eps.

    @param p   - array of probabilities.
    @param eps - some number.
    @throws ValueError when probabilities don't add up to 1.
    @returns - n.
    '''

    if np.sum(p) != 1:
        raise ValueError("Fuck your probabilities, dumbo! They don't add up to 1!")

    n = len(p)
    E = generate_e_matrix(n)

    phi = E.dot(p)

    i, phi_eta = 1, phi
    while np.linalg.norm(phi_eta) ** 2 - 1 > eps:
        phi_eta *= phi
        i += 1

    return i
