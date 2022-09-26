# -*- coding: utf -8  -*-
import csv
import numpy as np


def read_csv(filename="dane.csv"):
    f = open(filename)
    dane = f.read()
    dane = dane.split("\n")
    dane = [l.split(",") for l in dane]
    f.close()
    return dane


def prepare_data(dane):
    xdata = []
    ydata = []

    header = dane.pop(0)
    dane.pop()
    for x in range(len(dane)):
        xdata.append(float(dane[x][0]))
        ydata.append(float(dane[x][1]))
    xdata = np.array(xdata)
    ydata = np.array(ydata)
    return xdata, ydata
