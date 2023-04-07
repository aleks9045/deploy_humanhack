from django.urls import path, include
from .views import *
from app_1.views import *

urlpatterns = [
    path('API/math/theory/1?format=json', Math_theoryAPIView.as_view()),
    path('API/math/task/1?format=json', Math_taskAPIView.as_view()),
]
