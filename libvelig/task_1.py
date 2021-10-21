import numpy as np

from typing import Tuple

from libvelig.common import coefficients_matrix


def solve(function: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    '''
    Finds Zhe_galking and read polynomials coefficients for a given function's truth table.

    @param function - function's truth table as iterable.
    @returns - tuple of type (zhe_galkin_coefficients, real_coefficients).
    '''

    real_coefficients = np.linalg.solve(coefficients_matrix, function)
    zhe_galkin_coefficients = real_coefficients % 2

    return zhe_galkin_coefficients, real_coefficients
