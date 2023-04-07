from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.

class Math_theoryAPIView(APIView):
    def get(self, request):
        w = Math_theory.objects.all()
        return Response({'posts': Math_theorySerializer(w, many=True).data})
