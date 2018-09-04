from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from homework.models import  *
import json
# Create your views here.
def showlogin(request):
    # users=user.objects.all()
    # names=[]
    # for x in users:
    #     names.append(x.name)
    return render(request, 'login.html')
def success(request):
    n= request.POST.get('username')
    print('账户'+n+"登陆成功！")
    return render(request,'successful.html',locals())
def  check(request,acc,pwd):
    users= user.objects.all()
    uerlist=[]
    for u in users:
        uerlist.append(u.name)
    print(uerlist)
    if acc in uerlist:
        if (user.objects.get(name=acc).pwd)==pwd:
            json = "{\"info\":\"登入成功！\",\"isok\":\"ok\"}"
            print('登入成功！')
            status=1
            return HttpResponse(json)
            # return {'ss':status}
        else:
            json = "{\"info\":\"用户名不存在！\",\"isok\":\"sorry\"}"
            print('密码错误！')
            status = 0
            return HttpResponse(json)
            # return {'ss':status}
    else:
        json = "{\"info\":\"用户名不存在！\",\"isok\":\"sorry\"}"
        status=0
        print('用户名不存在！')
        return HttpResponse(json,{'ss':status})
        # return {'ss': status}