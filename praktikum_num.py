from typing import *
from numbers import *


def round_correctly(val: Real, err: Real) -> Tuple[Real, Real, Real]:
    """
    Rounds a value with an error to the correct decimal places.
    :param val:
        The value that gets rounded.
    :param err:
        The error of the rounded value.
    :return:
        The rounded value, the rounded error and the power as a multiple of three.
    """
    first_sign = 0
    while err // (10 ** first_sign) > 0:
        first_sign += 1
    while err // (10 ** first_sign) == 0:
        first_sign -= 1
    if err // (10 ** first_sign) < 3:
        first_sign -= 1
    pot = 3 * (first_sign // 3)
    round_pot = first_sign % 3 - 2
    return int(round(val * 10 ** - pot, round_pot)), int(round(err * 10 ** - pot, round_pot)), pot


def err_evolution(func: Callable[..., Real], params: List[Real], errors: List[Real]) -> Tuple[Real, Real]:
    """
    Evaluates the value with gaussian error of a function
    :param func:
        Function that gets evaluated
    :param params:
        List of parameters for which the function gets evaluated
    :param errors:
        List of errors corresponding to the list of parameters
    :return:
        The value of evaluated function and the error of the value
    """
    val = func(*params)
    err_q = 0
    for i in range(len(params)):
        _, _, pot = round_correctly(params[i], errors[i])
        h = 10 ** (pot - 5)
        upper = (params[j] + h * (j == i) for j in range(len(params)))
        lower = (params[j] - h * (j == i) for j in range(len(params)))
        diff = (func(*upper) - func(*lower)) / (2 * h)
        err_q += (diff * errors[i]) ** 2
    return val, err_q ** 0.5
