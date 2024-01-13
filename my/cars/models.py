from django.db import models
from datetime import datetime
from datetime import date
# Create your models here.
class Order(models.Model):
    client=models.ForeignKey('Client',on_delete=models.PROTECT)
    res_price=models.IntegerField(null=True)
    num_car=models.ForeignKey('Car',on_delete=models.PROTECT,null=True)
    dateOfBuy=models.DateField(auto_now_add=True,null=True)

class Car(models.Model):
    brend=models.CharField(max_length=50)
    saler=models.ForeignKey('Saler',on_delete=models.PROTECT,null=True)
    marka=models.CharField(max_length=50)
    power=models.IntegerField(null=True)
    level=models.CharField(max_length=10)
    numOfpower=models.IntegerField(null=True)
    passport=models.IntegerField(null=True)
    yearOfput=models.DateField(auto_now_add=True,null=True)

class Saler(models.Model):
    brend_car=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
class Client(models.Model):
    document=models.IntegerField(null=True)
