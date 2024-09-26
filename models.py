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


class Feedback(models.Model):
    sellerId = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    feedback = models.CharField(max_length=500, null=True)


class Chat(models.Model):
    sellerid = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    time = models.CharField(max_length=100)
    utype = models.CharField(max_length=100)


class Product(models.Model):
    sellerid = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    productName = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    image = models.FileField(upload_to='file', null=True)
    amount = models.CharField(max_length=100, null=True)
    bidstatus = models.CharField(max_length=100, null=True, default="PENDING")
    bidStartDate = models.CharField(max_length=100, null=True)
    paymentStatus = models.CharField(max_length=100, null=True)
    # status = models.CharField(max_length=100, null=True)



class BidTable(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    amount = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)


class Bid(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bidDate = models.DateTimeField(auto_now_add=True)