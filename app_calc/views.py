from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ExpressionSerializer
from .services import evaluate_expression


class ExpressionView(APIView):

    @staticmethod
    def post(request):
        result = {"result": None}
        serializer = ExpressionSerializer(data=request.data)
        if serializer.is_valid():
            calculated = evaluate_expression(serializer.validated_data['expression'],
                                             serializer.validated_data['variables'])
            if isinstance(calculated, str):
                result['error'] = calculated
            else:
                result['result'] = calculated
        else:
            result['error'] = serializer.errors['non_field_errors'][0]
        return Response(result)

    @staticmethod
    def get(request):
        return Response({'message': f'Hello!'})
