from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    sex=models.CharField(max_length=10)
