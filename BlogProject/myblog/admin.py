from django.contrib import admin
from myblog.models import *
# Register your models here.
admin.site.register([MyUser,Category,Article,Tag,ArticleTagRelation,Comment])
