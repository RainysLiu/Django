# Create your views here.
from django.shortcuts import render,HttpResponse
import datetime
def show_hello(request):
    return HttpResponse("<h3 style='color:red'>Hello! DjangoDay3!</h3>")
def show_login(request):
    return render(request,'login.html')
def login_action(request):
    username=request.POST.get('username')
    pwd=request.POST.get('pwd')
    sex=request.POST.get('sex')
    print('注册成功!\n账户:'+username)
    print('密码:'+pwd)
    print('性别:'+sex )
    return render(request,'loginsuccess.html',{'acc':username,'pwd':pwd,'sex':sex})
def getTime(request):
    a = datetime.datetime(1989,6,4).now()
    return render(request,'time.html',{'time':a})



