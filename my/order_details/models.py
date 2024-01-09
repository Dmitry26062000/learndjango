from django.db import models
class Order(models.Model):
    adress=models.CharField(max_length=50)
    Cgoods=models.IntegerField(max_length=3)
# Create your models here.
