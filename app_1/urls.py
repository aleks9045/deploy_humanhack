from django.urls import path, include
from .views import *
from app_1.views import *

urlpatterns = [
    path('API/math/theory/1', Math_theoryAPIView.as_view()),
    path('API/math/task/1', Math_taskAPIView.as_view()),
    path('API/animals/theory/1', English_theoryAPIView.as_view()),
    path('API/animals/task/1', English_taskAPIView.as_view()),
    path('API/read/theory/1', Read_theoryAPIView.as_view()),
    path('API/read/task/1', Read_taskAPIView.as_view()),
    path('API/english/theory/1', English_theoryAPIView.as_view()),
    path('API/english/task/1', English_taskAPIView.as_view()),
]
