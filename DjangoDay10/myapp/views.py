import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page

from DjangoDay10.settings import BASE_DIR
from myapp.models import *
def showreg(request):
    return render(request,'reg.html')
def reg(request):
    regname = request.POST["regname"]
    regpwd = request.POST["regpwd"]
    regadd = request.POST["regadd"]
    regtel = request.POST["regtel"]
    MyModel.objects.create_user(username=regname, password=regpwd, tel=regtel,add=regadd)  # 添加到数据库中的auth_user表,create_user()对密码加密
    return HttpResponseRedirect('/myapp/showlogin/')
def showlogin(request):
    return render(request,'login.html')
def u_login(request):
    logname = request.POST["logname"]
    logpwd = request.POST["logpwd"]
    user = authenticate(username=logname, password=logpwd)  # 认证用户，判断用户名和密码是否正确
    print("logname=", logname, "logpwd=", logpwd, "user=", user)
    if user:
        login(request, user)  # 将用户标识保存到session中
        return HttpResponseRedirect("/myapp/success/?login_name=" + logname)  # 重定向，并传递Get参数
    else:
        return render(request, 'login.html', {"msg": "用户名或密码错误，请重新登录！"})
def u_logout(request):
    logout(request)  # 登出
    return HttpResponseRedirect("/myapp/showlogin/")
def success(request):
    login_name = request.GET.get('login_name',"")
    return render(request,'success.html',locals())
@login_required(login_url="/myapp/showlogin/")
def govip(request):
    return render(request,'vip.html')







def showloadpicture(request):
    return render(request,'loadpicture.html')
def upload(request):
    upload_obj = request.FILES.get("mypicture")  # 接收域名为"mypicture"的上传文件
    dest_file = os.path.join(BASE_DIR, 'upload', 'uploadimg', upload_obj.name)  # 拼接上传文件的目标文件
    with open(dest_file, 'wb') as f:  # 以"wb"模式打开上传目标文件，准备写入
        for chunk in upload_obj.chunks():  # 对上传文件进行分块写入
            f.write(chunk)
    imgpath = 'uploadimg/' + upload_obj.name  # 取得刚才上传文件的网址
    return render(request, 'picturesuccess.html', {'imgpath': imgpath})



count = 0
@cache_page(60)  # 缓存视图结果60秒
def getallstu(request):
    global count
    count += 1
    print("第"+str(count)+"次调用my_view()视图函数")
    students =student.objects.all()# 查询MySQL数据库
    return render(request, 'allstu.html', {"students": students, "msg": "第"+str(count)+"次调用视图函数"})

