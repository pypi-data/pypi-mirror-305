import matplotlib
import matplotlib.pyplot as plt
from typing import *
from os import PathLike

from .tools import *
from .math import *
import pandas as pd

import numpy as np
import enum


class GraphStyle(enum.Enum):
    DEFAULT = 'default'
    CLASSIC = 'classic'
    GRAYSCALE = 'grayscale'
    GGPLOT = 'ggplot'
    SEABORN = 'seaborn-v0_8'
    FAST = 'fast'
    BMH = 'bmh'
    SOLARIZED_LIGHT = 'Solarize_Light2'
    SEABORN_NOTEBOOK = 'seaborn-v0_8-notebook'


class ColorMap(enum.Enum):
    ACCENT = "Accent"
    BLUES = "Blues"
    BRBG = "BrBG"
    BUGN = "BuGN"
    BUPU = "BuPu"
    CMRMAP = "CMRmap"
    DARK2 = "Dark_2"
    GNBU = "GnBu"
    GRAYS = "Grays"
    GREENS = "Greens"
    GREYS = "Greys"
    ORRD = "OrRd"
    ORANGES = "Oranges"
    PRGN = "PRGn"
    PAIRED = "Paired"
    PASTEL1 = "Pastel1"
    PASTEL2 = "Pastel2"
    PIYG = "PiYG"
    PUBU = "PuBu"
    PUBUGN = "PuBuGn"
    PUOR = "PuOr"
    PURD = "PuRd"
    PURPLES = "Purples"
    RDBU = "RdBu"
    RDGY = "RdGy"
    RDPU = "RdPu"
    RDYLBU = "RdYlBu"
    RDYLGN = "RdYlGn"
    REDS = "Reds"
    SET1 = "Set1"
    SET2 = "Set2"
    SET3 = "Set3"
    SPECTRAL = "Spectral"
    WISTIA = "Wistia"
    YLGN = "YlGn"
    YLGNBU = "YlGnBu"
    YLORBT = "YlOrBt"
    YLORRD = "YlOrRd"
    AFMHOT = "afmhot"
    AUTUMN = "autumn"
    BINARY = "binary"
    BONE = "bone"
    BRG = "brg"
    BWR = "bwr"
    CIVIDIS = "cividis"
    COOL = "cool"
    COOLWARM = "coolwarm"
    COPPER = "copper"
    CUBEHELIX = "cubehelix"
    FLAG = "flag"
    GIST_EARTH = "gist_earth"
    GIST_GRAY = "gist_gray"
    GIST_HEAT = "gist_heat"
    GIST_NCAR = "gist_ncar"
    GIST_RAINBOW = "gist_rainbow"
    GIST_STERN = "gist_stern"
    GIST_YARG = "gist_yarg"
    GIST_YERG = "gist_yerg"
    GNUPLOT = "gnuplot"
    GNUPLOT2 = "gnuplot_2"
    GRAY = "gray"
    GREY = "grey"
    HOT = "hot"
    HSV = "hsv"
    INFERNO = "inferno"
    JET = "jet"
    MAGMA = "magma"
    NIPY_SPECTRAL = "nipy_spectral"
    OCEAN = "ocean"
    PINK = "pink"
    PLASMA = "plasma"
    PRISM = "prism"
    RAINBOW = "rainbow"
    SEISMIC = "seismic"
    SPRING = "spring"
    SUMMER = "summer"
    TAB10 = "tab_10"
    TAB20 = "tab_20"
    TAB20B = "tab_20_b"
    TAB20C = "tab_20_c"
    TERRAIN = "terrain"
    TRUBO = "trubo"
    TWILIGHT = "twilight"
    TWILIGHT_SHIFTED = "twilight_shifted"
    VIRIDIS = "viridis"
    WINTER = "winter"


class ColorFunction(enum.Enum):
    MAGNITUDE = lambda u, v, z: np.sqrt(u ** 2 + v ** 2)
    SUM = lambda u, v, z: abs(u) + abs(v)
    DIFFERENCE = lambda u, v, z: abs(u) - abs(v)
    PRODUCT = lambda u, v, z: u * v

    @staticmethod
    def LINEAR(axis: str = "x"):
        if axis == "x":
            return lambda u, v, z: u
        elif axis == "y":
            return lambda u, v, z: v
        elif axis == "z":
            return lambda u, v, z: z
        else:
            raise ValueError("Invalid Axis")

    @staticmethod
    def QUADRATIC(axis: str = "x"):
        if axis == "x":
            return lambda u, v, z: u * u
        elif axis == "y":
            return lambda u, v, z: v * v
        elif axis == "z":
            return lambda u, v, z: z * z
        else:
            raise ValueError("Invalid Axis")


class Graph2D:
    def __init__(self, name: str = "Graph 2D", style: GraphStyle = GraphStyle.DEFAULT):
        plt.style.use(style.value)
        self.name = name
        self.subplots = 0

    def addAxes(self):
        self.ax = plt.axes()
        self.ax.set_title(self.name)

    def addSubplot(self, row: int, col: int):
        self.subplots += 1
        self.ax = plt.subplot(row, col, self.subplots)

    def setTitle(self, title: str):
        plt.title(title)

    def setXLabel(self, label: str):
        plt.xlabel(label)

    def setYLabel(self, label: str):
        plt.ylabel(label)

    def plotPoint(self, point: Vector2, color: str = 'blue', label: str = None):
        return self.ax.scatter(point.x, point.y, color=color, label=label)

    def plotPoints(self, *points: Vector2, color: str = 'blue', label: str = None):
        return self.ax.scatter([i.x for i in points], [j.y for j in points], color=color, label=label)

    def drawLine(self, start: Vector2, end: Vector2, color: str = 'blue', linewidth: float = 2, linestyle: str = "-", label: str = None):
        line = self.ax.plot([start.x, end.x], [start.y, end.y], color=color, linestyle=linestyle, linewidth=linewidth, label=label)
        return line

    def linePlot(self, xVals: Sequence, yVals: Sequence, color: str = 'blue', marker: str = None, linewidth: float = 2,
                 linestyle: str = "-", label: str = None):
        if len(xVals) == len(yVals):
            if marker is None:
                return self.ax.plot(xVals, yVals, color, linestyle=linestyle, linewidth=linewidth, label=label)
            else:
                return self.ax.plot(xVals, yVals, color, marker=marker, linestyle=linestyle, linewidth=linewidth, label=label)
        else:
            raise ValueError(f"Length of both arrays should be same. Lengths - X: {len(xVals)}, Y: {len(yVals)}")

    def scatterPlot(self, xVals: Sequence, yVals: Sequence, color: str = 'blue', label: str = None):
        if len(xVals) == len(yVals):
            sctr = self.ax.scatter(xVals, yVals, color=color, label=label)
        else:
            raise ValueError(f"Length of both arrays should be same. Lengths - X: {len(xVals)}, Y: {len(yVals)}")
        return sctr

    def scatterPlotCF(self, xVals: Sequence, yVals: Sequence,
                      cfunction: Callable | ColorFunction = (lambda x, y, z: x + y), cmap: ColorMap = ColorMap.VIRIDIS,
                      colorBar: bool = False, label: str = None):
        c = [cfunction(item1, item2, 0) for item1, item2 in zip(xVals, yVals)]
        if len(xVals) == len(yVals):
            sctr = self.ax.scatter(xVals, yVals, cmap=cmap.value, c=c, label=label)
            if colorBar:
                plt.colorbar(sctr)
        else:
            raise ValueError(f"Length of both arrays should be same. Lengths - X: {len(xVals)}, Y: {len(yVals)}")

    def plotCSV(self, csvFilePath: Union[str, PathLike], xHeader: str, yHeader: str, color: str = 'blue',
                dots: bool = False, setAxisLabels: bool = True, label: str = None):
        data = pd.read_csv(csvFilePath)
        x = data[xHeader]
        y = data[yHeader]

        if setAxisLabels:
            self.setXLabel(xHeader)
            self.setXLabel(yHeader)

        if dots:
            self.ax.plot(x, y, color, marker="o")
        else:
            self.ax.plot(x, y, color)

    @staticmethod
    def legend(*args, **kwargs):
        plt.legend(*args, **kwargs)

    @staticmethod
    def show():
        plt.show()
