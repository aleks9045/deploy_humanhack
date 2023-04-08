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


class Animals_theorySerializer(serializers.Serializer):
    number_theory = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    condition = serializers.CharField()


class Animals_taskSerializer(serializers.Serializer):
    number_task = serializers.IntegerField()
    text = serializers.CharField()
    condition = serializers.CharField()
    answer = serializers.CharField(max_length=255)


class Read_theorySerializer(serializers.Serializer):
    number_theory = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    condition = serializers.CharField()


class Read_taskSerializer(serializers.Serializer):
    number_task = serializers.IntegerField()
    text = serializers.CharField()
    condition = serializers.CharField()
    answer = serializers.CharField(max_length=255)


class English_theorySerializer(serializers.Serializer):
    number_theory = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    condition = serializers.CharField()


class English_taskSerializer(serializers.Serializer):
    number_task = serializers.IntegerField()
    text = serializers.CharField()
    condition = serializers.CharField()
    answer = serializers.CharField(max_length=255)
