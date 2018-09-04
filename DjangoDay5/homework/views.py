from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from homework.models import  *
import json
# Create your views here.
def showreg(request):
    # users=user.objects.all()
    # names=[]
    # for x in users:
    #     names.append(x.name)
    return render(request, 'login.html')
def success(request):
    name = request.POST.get('username')
    passwd  =request.POST.get('pwd')
    s = request.POST.get('sex')
    user.objects.create(name=name,pwd=passwd,sex=s)
    print('注册成功！已将数据存入数据库！\n账户:'+name)
    print('密码为:' + passwd)
    print('性别:' + s)
    return render(request,'successful.html',locals())
def  check(request,regvalue):
    userexit= user.objects.filter(name=regvalue)
    print(regvalue)
    if userexit:
        json = "{\"info\":\"该用户名已存在，请选择其他用户名！\",\"isok\":\"sorry\"}"
        return HttpResponse(json)
    else:
        json = "{\"info\":\"恭喜，可以使用该用户名\",\"isok\":\"ok\"}"
        return HttpResponse(json)