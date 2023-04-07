from rest_framework import serializers
from .models import *

class Math_theorySerializer(serializers.Serializer):
    number_theory = serializers.IntegerField()
    title = serializers.CharField()
    content = serializers.CharField()
    condition = serializers.CharField()


class Math_taskSerializer(serializers.Serializer):
    number_task = serializers.IntegerField()
    condition = serializers.CharField()
    answer = serializers.CharField(max_length=255)
