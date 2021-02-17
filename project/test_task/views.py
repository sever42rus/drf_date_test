import time

from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from .serializers import YearSerializer
# Create your views here.


class Main(TemplateView):
    template_name = 'test_task/index.html'


class Task1(TemplateView):
    template_name = 'test_task/task_1.html'


class Task2(TemplateView):
    template_name = 'test_task/task_2.html'


class FormAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = YearSerializer(data=request.data)
        time.sleep(4)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
