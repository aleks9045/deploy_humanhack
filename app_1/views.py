from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.

class Math_theoryAPIView(APIView):
    def get(self, request):
        w = Math_theory.objects.all()
        return Response({'theory': Math_theorySerializer(w, many=True).data})


class Math_taskAPIView(APIView):
    def get(self, request):
        w = Math_task.objects.all()
        return Response({'task': Math_taskSerializer(w, many=True).data})


class Animals_theoryAPIView(APIView):
    def get(self, request):
        w = Animals_theory.objects.all()
        return Response({'theory': Animals_theorySerializer(w, many=True).data})


class Animals_taskAPIView(APIView):
    def get(self, request):
        w = Animals_task.objects.all()
        return Response({'task': Animals_taskSerializer(w, many=True).data})


class Read_theoryAPIView(APIView):
    def get(self, request):
        w = Read_theory.objects.all()
        return Response({'theory': Read_theorySerializer(w, many=True).data})


class Read_taskAPIView(APIView):
    def get(self, request):
        w = Read_task.objects.all()
        return Response({'task': Read_taskSerializer(w, many=True).data})


class English_theoryAPIView(APIView):
    def get(self, request):
        w = English_theory.objects.all()
        return Response({'theory': English_theorySerializer(w, many=True).data})


class English_taskAPIView(APIView):
    def get(self, request):
        w = English_task.objects.all()
        return Response({'task': English_taskSerializer(w, many=True).data})
