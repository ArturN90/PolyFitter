import numpy as np


def fun8(x, a, b, c, d, e, f, g, h, i):
    return (
        a * x**8
        + b * x**7
        + c * x**6
        + d * x**5
        + e * x**4
        + f * x**3
        + g * x**2
        + h * x
        + i
    )


def fun7(x, a, b, c, d, e, f, g, h):
    return (
        a * x**7
        + b * x**6
        + c * x**5
        + d * x**4
        + e * x**3
        + f * x**2
        + g * x
        + h
    )


def fun6(x, a, b, c, d, e, f, g):
    return a * x**6 + b * x**5 + c * x**4 + d * x**3 + e * x**2 + f * x + g


def morse_6(x, re, de, b0, b1, b2, b3, b4, b5, b6):
    x = b0 * (x - re) / re
    return (
        -de
        + de
        * (
            1
            - np.exp(
                -x
                * (
                    1
                    + b1 * x
                    + b2 * x**2
                    + b3 * x**3
                    + b4 * x**4
                    + b5 * x**5
                    + b6 * x**6
                )
            )
        )
        ** 2
    )
