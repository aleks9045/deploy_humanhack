from django.urls import path, include
from .views import *
from app_1.views import *

urlpatterns = [
    path('API/math/theory/1', Math_theoryAPIView.as_view()),
    path('API/math/task/1', Math_taskAPIView.as_view()),
]
