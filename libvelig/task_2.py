import numpy as np

from scipy.linalg import hadamard
from typing import Tuple

from libvelig.common import coefficients_matrix


def solve(zhe_galkin_coefficients: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    '''
    Finds Fourier and Hadamard coefficients for a given Zhe_galking coefficients.

    @param zhe_galkin_coefficients - Zhe_galking coefficients of the function.
    @returns - tuple of type (fourier_coefficients, hadamard_coefficients)
    '''

    function = np.linalg.solve(np.linalg.inv(coefficients_matrix), zhe_galkin_coefficients) % 2

    H = hadamard(16)

    fourier_coefficients = H.dot(function)
    hadamard_coefficients = H.dot((-1) ** function)

    return fourier_coefficients, hadamard_coefficients
