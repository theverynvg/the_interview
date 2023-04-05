from django.test import TestCase
from rest_framework.test import APIClient


class CalculationTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_default(self):
        data = {
            "expression": "4-2*a/(5*x-3)",
            "variables": {
                "a": 2.5,
                "x": 0
            }
        }
        response = self.client.post('', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': 5.666666666666667})

    def test_lg_ln(self):
        data = {
            "expression": "lg(4)-2*a/(5*x-ln(3))",
            "variables": {
                "a": 2.5,
                "x": 0
            }
        }
        response = self.client.post('', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': 5.153256124462149})

    def test_trigonometry_novariables(self):
        data = {
            "expression": "sin(1)+cos(1)+tan(1)-atan(1)*asin(1)+acos(1)",
            "variables": {}
        }
        response = self.client.post('', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': 1.7054804651947688})

    def test_pow(self):
        data = {
            "expression": "x^2",
            "variables": {'x': 5}
        }
        response = self.client.post('', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': 25.0})

    def test_calc(self):
        data = {
            "expression": "2^4/7+3.5-2^lg(45)",
            "variables": {}
        }
        response = self.client.post('', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': 2.640381833349441})

    def test_zero_division(self):
        data = {
            "expression": "5/0",
            "variables": {}
        }
        response = self.client.post('', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': None,
                                         "error": "Деление на ноль"})

    def test_varible_is_not_difined(self):
        data = {
            "expression": "x+5",
            "variables": {}
        }
        response = self.client.post('', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': None,
                                         "error": "Требуемая переменная 'x' не определена "})

    def test_func_is_not_defined(self):
        data = {
            "expression": "log(8)",
            "variables": {}
        }
        response = self.client.post('', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': None,
                                         "error": "Неподдерживаемая функция  'log' "})

    def test_invalid_symbol(self):
        data = {
            "expression": "5&7+2",
            "variables": {}
        }
        response = self.client.post('', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': None,
                                         "error": "Недопустимый символ '&' "})

    def test_invalid_expression(self):
        data = {
            "expression": "5+3+*9*0",
            "variables": {}
        }
        response = self.client.post('', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'result': None,
                                         "error": "Некорректное выражение"})
