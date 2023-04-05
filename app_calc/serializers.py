from rest_framework import serializers
import re
from rest_framework.serializers import ValidationError


class ExpressionSerializer(serializers.Serializer):
    expression = serializers.CharField()
    variables = serializers.DictField()

    def validate(self, attrs):
        pattern = r'[\+\-\*\/\^\(\)]|\d*\.?\d+|[a-zA-Z]+|[!@#$%&{}=<>\?\_\'\"]'
        tokens = re.findall(pattern, attrs['expression'])
        pattern = r"^([+\-*/^()]|\d*\.?\d+|lg|ln|sin|cos|tan|asin|acos|atan)$"
        if attrs['variables']:
            p = "".join(f"{key}" for key in attrs['variables'])
            pattern += f"|^[{p}]$"
        for token in tokens:
            if not re.fullmatch(pattern, token):
                if token in '!@#$%&{}=<>?_\'\"':
                    raise ValidationError(f"Недопустимый символ '{token}' ")
                elif len(token) == 1:
                    raise ValidationError(f"Требуемая переменная '{token}' не определена ")
                else:
                    raise ValidationError(f"Неподдерживаемая функция  '{token}' ")
        attrs['expression'] = attrs['expression'].replace('^', '**')
        return attrs
