from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Login(AbstractUser):
    user_type = models.CharField(max_length=30)
    view_password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_type


class Customer(models.Model):
    loginId = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True, default="PENDING")
    image = models.FileField(upload_to='file', null=True)


class Seller(models.Model):
    loginId = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True, default="PENDING")
    image = models.FileField(upload_to='file', null=True)

