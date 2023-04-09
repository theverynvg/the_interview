import sympy
from typing import Union
from math import e as E


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
    if x > 1:
        raise ValueError
    return sympy.asin(x)


def my_acos(x):
    if x > 1:
        raise ValueError
    return sympy.acos(x)


def my_atan(x):
    if x > 1:
        raise ValueError
    return sympy.atan(x)


def my_ln(x):
    if x <= 0:
        raise ValueError
    return sympy.log(x, E)


def evaluate_expression(expression: str, variables: dict) -> Union[float, str]:
    sympy.ln = my_ln
    if variables:
        var_names = list(variables.keys())
    else:
        var_names = []
    try:
        d_func = {sympy.Function('lg'): lambda x: my_lg(x),
                  sympy.asin: lambda x: my_asin(x),
                  sympy.acos: lambda x: my_acos(x),
                  sympy.atan: lambda x: my_atan(x),
                  }
        for f in d_func:
            expression = sympy.sympify(expression).replace(f, d_func[f])
    except:
        return 'Некорректное выражение'
    try:
        f = sympy.lambdify(var_names, expression)
    except:
        return 'Деление на ноль'
    result = f(*variables.values())
    return float(result)
