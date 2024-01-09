from django.db import models


# Create your models here.
class Media(models.Model):
    description=models.CharField(max_length=120)