from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet,generics
from .models import RegistersModel,CreateTaskModel
from .serializers import RegisterSerializer,UserSerializer,TaskSerializer
# from rest_framework .authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from . import models
from  . import serializers


class User_Register(ModelViewSet):
    queryset = RegistersModel.objects.all()
    serializer_class = RegisterSerializer


class Login_user(generics.ListAPIView):
    queryset = RegistersModel.objects.all()
    serializer_class = UserSerializer
    authentication_classes = BasicAuthentication
    permission_classes = IsAuthenticatedOrReadOnly


# class UserListView(generics.ListAPIView):
#     queryset = models.RegistersModel.objects.all()
#     serializer_class = serializers.RegisterSerializer


def login(request):
    return render(request,'login.html')

def Login_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if RegistersModel.objects.get(email=email, password=password):
        return render(request,'TODO.html')
    else:
        messages.error(request, 'invalid username or password')
        return render(request,'login.html')
    authentication_classes = BasicAuthentication
    permission_classes = IsAuthenticatedOrReadOnly


class Creat_task(ModelViewSet):
    queryset = CreateTaskModel.objects.all()
    serializer_class = TaskSerializer


# class Creat_task(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = CreateTaskModel.objects.all()
#     serializer_class = Ta
#
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
