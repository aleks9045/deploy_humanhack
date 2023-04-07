from django.urls import path, include
from .views import *
from app_1.views import *

urlpatterns = [
    path('a/', Math_theoryAPIView.as_view()),
]