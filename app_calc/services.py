import sympy
from typing import Union


def evaluate_expression(expression: str, variables: dict) -> Union[float, str]:
    if variables:
        var_names = list(variables.keys())
    else:
        var_names = []
    try:
        expression = sympy.sympify(expression).replace(sympy.Function('lg'),
                                                       lambda x: sympy.log(x, 10))
    except:
        return 'Некорректное выражение'
    try:
        f = sympy.lambdify(var_names, expression)
    except:
        return 'Деление на ноль'
    result = f(*variables.values())
    return float(result)
