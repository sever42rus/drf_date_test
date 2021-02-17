from django.urls import path
from .views import Main, Task1, Task2, FormAPI

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('task_1/', Task1.as_view(), name='task_1'),
    path('task_2/', Task2.as_view(), name='task_2'),
    path('api/form/', FormAPI.as_view(), name='form_api')
]
