from django.db import models


class RegistersModel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=8)


class CreateTaskModel(models.Model):
    tittle=models.CharField(max_length=20)
    # ORDER_STATUS=((0,'pending'),(1,'Done'))
    status=models.CharField(max_length=10)