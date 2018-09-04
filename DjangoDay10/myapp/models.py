from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyModel(AbstractUser):
    tel = models.CharField(max_length=20)
    add = models.CharField(max_length=20, null=True)
class cls(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "班级"
class student(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    sex=models.CharField(max_length=10)
    stucls=models.ForeignKey(cls, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "学生"
