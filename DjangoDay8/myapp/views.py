from django.http import JsonResponse
from django.shortcuts import render
from myapp.models import *
import memcache
# Create your views here.

def startui(request):
    return render(request, 'startui.html')
def allstu(request):
    mc = memcache.Client(["127.0.0.1:11211"])
    value = mc.get('allstu')  # 从Memcahed缓存系统中获取key为"cake"的值
    if value:   # 如果从缓存中查到了，则直接返回
        return render(request,'allstu.html',{'msg':'恭喜，缓存命中!','students':value})
    else:   # 缓存没有找到的情况
        students = student.objects.all()   # 从MySQL数据库查询
        mc.set('allstu',students,60)   # 将数据存储到Memcached中，保存30秒
        return render(request, 'allstu.html', {'msg': '这是从MySQL中查到的...', 'students': students})