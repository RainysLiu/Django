from django.core.cache import cache
from django.shortcuts import render,HttpResponseRedirect
from myapp.forms import *
from myapp.models import *
# Create your views here.
def user_form(request):
    if request.method=='POST':
        myuser=User(request.POST)
        if myuser.is_valid():
            uname=myuser.cleaned_data['name']
            pwd=myuser.cleaned_data['passwd']
            uemil=myuser.cleaned_data['email']
            useraccounts.objects.create(name=uname,pwd=pwd,emil=uemil)
            print('用户'+uname+'完成了注册！')
            print('绑定邮箱为'+uemil)
            return render(request,'regok.html',locals())
        else:
            return HttpResponseRedirect('/myapp/reg/')
    else:
        u=User()
        return render(request,'reg.html',locals())

def get_allstu(request):
    value = cache.get("allstu")  # 使用底层cache API尝试获取缓存中的数据
    if value:  # 缓存中存在
        return render(request, 'allstu.html', {"students": value, "msg": "恭喜，缓存命中了!"})
    else:  # 缓存中不存在
        allstu = student.objects.all()  # 查询MySQL数据库
        cache.set("allstu" , allstu, 30)  # 设置缓存
        return render(request, 'allstu.html', {'students': allstu, "msg": "从MySQL数据库中查询的数据..."})
