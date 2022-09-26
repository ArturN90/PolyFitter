from scipy.optimize import curve_fit

from functions import fun8, fun7, fun6


def pick_fun_variant(x):
    n_b = len(x)

    if n_b > 9:
        deg_min = 6
        deg_max = 8
    elif n_b > 8:
        deg_min = 6
        deg_max = 7
    else:
        deg_min = 6
        deg_max = deg_min

    print(f"Avaialble are polynomial in degree {deg_min} to {deg_max}")
    deg = int(input("Pick the polynomial by typing the degree: "))
    if deg in (6, 7, 8):
        return deg
    else:
        deg = 6
        return deg


def calculate(deg, x, y):
    if deg == 6:
        popt, pcov = curve_fit(fun6, x, y)
        diff = fun6(x, *popt) - y
        return popt, pcov, diff

    if deg == 7:
        popt, pcov = curve_fit(fun7, x, y)
        diff = fun7(x, *popt) - y
        return popt, pcov, diff

    popt, pcov = curve_fit(fun8, x, y)
    diff = fun8(x, *popt) - y
    return popt, pcov, diff
