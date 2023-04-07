from rest_framework import serializers
from .models import *

class Math_theorySerializer(serializers.Serializer):
    number_theory = serializers.IntegerField()
    title = serializers.CharField()
    content = serializers.CharField()
    condition = serializers.CharField()