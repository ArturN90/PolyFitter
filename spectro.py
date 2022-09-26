from scipy import optimize
from math import sqrt
from functions import *

# constants
m_p = 1836.152701
d_x = 0.0001
dx_b = d_x * 1.889726
# range
x_0 = 1.625
x_k = 1.875
# mass
m_1 = 15.9949
m_2 = 238.0508
m_u = m_1 * m_2 / (m_1 + m_2) * m_p


def spectro_data(deg, popt):

    if deg == 8:
        r_e = optimize.fminbound(fun8, x_0, x_k, args=(*popt,))
        f_min = fun8(r_e, *popt)
        k_f = (
            -fun8(r_e - 2 * d_x, *popt)
            + 16 * fun8(r_e - d_x, *popt)
            - 30 * fun8(r_e, *popt)
            + 16 * fun8(r_e + d_x, *popt)
            - fun8(r_e + 2 * d_x, *popt)
        ) / (12 * dx_b**2)
    if deg == 7:
        r_e = optimize.fminbound(fun7, x_0, x_k, args=(*popt,))
        f_min = fun7(r_e, *popt)
        k_f = (
            -fun7(r_e - 2 * d_x, *popt)
            + 16 * fun7(r_e - d_x, *popt)
            - 30 * fun7(r_e, *popt)
            + 16 * fun7(r_e + d_x, *popt)
            - fun7(r_e + 2 * d_x, *popt)
        ) / (12 * dx_b**2)
    if deg == 6:
        r_e = optimize.fminbound(fun6, x_0, x_k, args=(*popt,))
        f_min = fun6(r_e, *popt)
        k_f = (
            -fun6(r_e - 2 * d_x, *popt)
            + 16 * fun6(r_e - d_x, *popt)
            - 30 * fun6(r_e, *popt)
            + 16 * fun6(r_e + d_x, *popt)
            - fun6(r_e + 2 * d_x, *popt)
        ) / (12 * dx_b**2)

    omega_e = sqrt(k_f / m_u) * 219474.63
    print(f"Polynomial {deg} degree ", r_e)
    print("fmin", f_min)
    print("omega_e", omega_e)
