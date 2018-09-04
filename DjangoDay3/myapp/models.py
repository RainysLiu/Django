from django.db import models
# Create your models here.
class animal(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    age = models.IntegerField()