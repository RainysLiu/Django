from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=10)
    author=models.CharField(max_length=10)
    price=models.FloatField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "书籍"
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

