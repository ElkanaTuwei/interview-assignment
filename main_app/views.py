from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class MainAPIView(APIView):
    def post(self, request):
        res = {"message": "OK"}
        return Response(res)

    def get(self, request):
        integer_value = request.GET.get("integer")
        # check to verify that the value is passed in the params
        if integer_value:
            # parse integer value of parameter
            integer_value = int(integer_value)
            res = {}
            # check if the integer is  multiple of both five and seven
            if (integer_value % 5 == 0) and (integer_value % 7 == 0):
                res = {"data": "LR"}
            # check if the integer is  multiple of five
            elif integer_value % 5 == 0:
                res = {"data": "L"}
            # check if the integer is  multiple of seven
            elif integer_value % 7 == 0:
                res = {"data": "R"}
            # return the integer value if none of the conditions is matched
            else:
                res = {"data": integer_value}
            return Response(res, status=status.HTTP_200_OK)
        else:
            # return error response if integer is not included in request
            res = {"message": "Provide Integer"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
