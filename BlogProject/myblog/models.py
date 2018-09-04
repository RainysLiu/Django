from django.contrib.auth.models import AbstractUser
from django.db import models

# Create AbstractUseryour models here.
class MyUser(AbstractUser):
    tel = models.CharField(max_length=20)
    qq = models.CharField(max_length=20, null=True)

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"
        ordering = ["id"]
class Tag(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="标签"
        verbose_name_plural = "标签"
        ordering = ["-id"]
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_publish = models.DateField(auto_now_add=True)
    desc = models.CharField(max_length=50)
    click_count = models.IntegerField()
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag,through="ArticleTagRelation")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="文章"
        verbose_name_plural = "文章"
        ordering = ["-date_publish","-id"]
class ArticleTagRelation(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    def __str__(self):
        return self.article.title+"---->"+self.tag.name
    class Meta:
        verbose_name="文章管理标签"
        verbose_name_plural = "文章管理标签"
        ordering = ["-id"]
class Comment(models.Model):
    content = models.TextField(max_length=50)
    date_public = models.DateField(auto_now=True)
    user = models.ForeignKey(MyUser,blank=True,null=True,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,blank=True,null=True,on_delete=models.CASCADE)
    pid = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username+'的评论'

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
        ordering = ["date_public"]

