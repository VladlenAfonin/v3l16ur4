#! python3

import argparse
import numpy as np

from libvelig import *


def main() -> None:
    '''
    Entry point.

    @returns - nothing.
    '''

    parser = argparse.ArgumentParser(description="Do the FOCKING homework!")

    parser.add_argument("-t", "--task", metavar="number", type=int, nargs=1, required=True)
    parser.add_argument("-a", "--args", metavar="arg", type=str, nargs="+", required=True)

    args = parser.parse_args()

    try:
        if (task_number := args.task[0]) == 1:
            function = np.array(eval(args.args[0]))

            zhe_galkin_coefficients, real_coefficients = task_1.solve(function)
            print("Zhe_galking: ", zhe_galkin_coefficients)
            print("Real       : ", real_coefficients)

        elif task_number == 2:
            zhe_galkin_coefficients = np.array(eval(args.args[0]))

            fourier_coefficients, hadamard_coefficients = task_2.solve(zhe_galkin_coefficients)

            print("Fourier:  ", fourier_coefficients)
            print("Hadamard: ", hadamard_coefficients)

        elif task_number == 3:
            p_ksi = np.array(eval(args.args[0]))
            p_eta = np.array(eval(args.args[1]))

            distribution = task_3.solve(p_ksi, p_eta)

            print("Distribution: ", distribution)

        elif task_number == 4:
            p_ksi = np.array(eval(args.args[0]))
            eps = eval(args.args[1])

            n = task_4.solve(p_ksi, eps)

            print(f"{n = }")

        else:
            raise ValueError()
    except Exception:
        print("You can't even pass the arguments correctly, can you?")


if __name__ == "__main__":
    main()
