from django.db import models

# Create your models here.
class man(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
class wife(models.Model):
    name=models.CharField(max_length=10)
    age = models.IntegerField()
    wife_man=models.OneToOneField(man,on_delete=models.CASCADE)
class country(models.Model):
    name=models.CharField(max_length=20)
    capital=models.CharField(max_length=20)
class province(models.Model):
    name=models.CharField(max_length=20)
    country = models.ForeignKey(country, on_delete=models.CASCADE)
