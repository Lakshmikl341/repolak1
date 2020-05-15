from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import RegistersModel,CreateTaskModel
from . import models

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
      model = RegistersModel
      fields = ['name','email','password']
#
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegistersModel
        fields=['email','password']

class TaskSerializer(serializers.Serializer):
    class Meta:
        model=CreateTaskModel
        fields=['tittle','status']
