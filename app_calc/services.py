import sympy
from typing import Union


def viewname(func):
    def wrapper(*args):
        print(func.__name__)
        return func(*args)

    return wrapper


def my_lg(x):
    if x <= 0:
        raise ValueError
    return sympy.log(x, 10)


def my_asin(x):
    if x < -1 or x > 1:
        raise ValueError
    return sympy.asin(x)


def my_acos(x):
    if x < -1 or x > 1:
        raise ValueError
    return sympy.acos(x)


def my_atan(x):
    if x < -1 or x > 1:
        raise ValueError
    return sympy.atan(x)


def my_ln(x):
    if x <= 0:
        raise ValueError
    return sympy.log(x, 2.71828)


def evaluate_expression(expression: str, variables: dict) -> Union[float, str]:
    sympy.ln = my_ln
    sympy.asin = my_asin
    sympy.acos = my_acos
    sympy.atan = my_atan
    if variables:
        var_names = list(variables.keys())
    else:
        var_names = []
    try:
        expression = sympy.sympify(expression).replace(sympy.Function('lg'),
                                                       lambda x: my_lg(x))
    except:
        return 'Некорректное выражение'
    try:
        f = sympy.lambdify(var_names, expression)
    except:
        return 'Деление на ноль'
    result = f(*variables.values())
    return float(result)
