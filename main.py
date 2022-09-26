# -*- coding: utf -8  -*-
import csv
import numpy as np

from read_csv import *
from calculate_spectro import *
from ploter import *
from spectro import *


def main():

    xdata, ydata = prepare_data(read_csv())
    deg = pick_fun_variant(xdata)
    p, c, diff = calculate(deg, xdata, ydata)

    plotter(deg, xdata, p)
    print("Differences between Poly8 and data points:")
    print("Absolute sum of differences: ", np.sum(abs(diff)))
    print("square root error:           ", np.sqrt(np.dot(diff, diff)))
    spectro_data(deg, p)


if __name__ == "__main__":
    main()
