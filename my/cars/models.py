from django.db import models

# Create your models here.
class Car(models.Model):
    brend=models.CharField(max_length=50)
    marka=models.CharField(max_length=50)
    power=models.IntegerField()
    level=models.CharField(max_length=10)
