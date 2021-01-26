from praktikum_num import round_correctly
from scipy.stats._stats_mstats_common import LinregressResult
from typing import *
from numbers import *


def lin_fit_label(sol: LinregressResult, xstr: str) -> str:
    """
    Makes a label for a Plot.
    :param sol:
        The solution of scipy.stats.linregress() that needs a label
    :param xstr:
        The label of the x-axis e.g. 'l /m' for a length in meter
    :return:
        The generated label
    """
    return '$Fit = ' + string_correctly(sol.slope, sol.stderr) + ' \\cdot ' + xstr + ' + ' + string_correctly(
        sol.intercept, sol.intercept_stderr) + '$;  $R^2 = ' + str(round(sol.rvalue ** 2, 3)) + '$'


def string_correctly(val: Real, err: Real) -> str:
    """
    Makes a latex string which presents the value with error correctly.
    :param val:
        The value which should be presented
    :param err:
        The error of the presented value
    :return:
        The Presentation in Latex Code
    """
    val, err, pot = round_correctly(val, err)
    return ' ( ' + str(val) + ' \pm ' + str(err) + ' )' + (' \\cdot 10^{' + str(pot) + '} ') * (pot != 0)
