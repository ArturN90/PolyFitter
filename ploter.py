#!/usr/bin/env python

import matplotlib.pyplot as plt
from functions import fun8, fun7, fun6


def plotter(deg, x, popt):
    if deg == 8:
        plt.plot(
            x,
            fun8(x, *popt),
            "r-",
            label="Poly8: a=%5.3f, b=%5.3f, c=%5.3f, d=%f, e=%5.3f, f=%f, g=%5.3f, h=%5.3f, i=%5.3f"
            % tuple(popt),
        )
    if deg == 7:
        plt.plot(
            x,
            fun7(x, *popt),
            "y-",
            label="Poly7: a=%5.3f, b=%5.3f, c=%5.3f, d=%f, e=%5.3f, f=%f, g=%5.3f, h=%5.3f"
            % tuple(popt),
        )
    if deg == 6:
        plt.plot(
            x,
            fun6(x, *popt),
            "b-o",
            label="Poly6: a=%5.3f, b=%5.3f, c=%5.3f, d=%f, e=%5.3f, f=%f, g=%5.3f"
            % tuple(popt),
        )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
