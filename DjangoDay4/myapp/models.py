from django.db import models

# Create your models here.
class school(models.Model):
    schoolname=models.CharField(max_length=20)
    schoolcity=models.CharField(max_length=20)
class student(models.Model):
    stuname=models.CharField(max_length=20)
    stusex=models.CharField(max_length=10)
    stuscore=models.FloatField()
    stuschool=models.ForeignKey(school,on_delete=models.CASCADE)
class person(models.Model):
    pass
class card(models.Model):
    pass
