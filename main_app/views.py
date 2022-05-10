from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class MainAPIView(APIView):
    def post(self, request):
        res = {"message": "OK"}
        return Response(res)

    def get(self, request):
        integer_value = request.GET.get("integer")
        if integer_value:
            integer_value = int(integer_value)
            res = {}
            if (integer_value % 5 == 0) and (integer_value % 7 == 0):
                res = {"data": "LR"}
            elif integer_value % 5 == 0:
                res = {"data": "L"}
            elif integer_value % 7 == 0:
                res = {"data": "R"}
            else:
                res = {"data": integer_value}
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {"message": "Provide Integer"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
