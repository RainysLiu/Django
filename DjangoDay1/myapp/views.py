from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h3 style='color:red'>Hello! DjangoDay3!</h3>")
def showtest(request):
    return render(request,'test.html')
def showduanzi(request):
    return render(request,'duanzi.html')
def showMM(request):
    return render(request,'MM.html')
def show_reg(request):
    return render(request,'reg/reg.html')
def show_successful(request):
    return render(request,'reg/success.html')
def reg_action(request):
    print("注册的用户名是：",request.POST.get("username"))
    print("注册的密码是：",request.POST.get("pwd"))
    print("注册的QQ是：",request.POST.get("QQ"))
    return render(request,'reg/success.html')
def show_sun(request):
    print('返回的数据：灿烂的太阳')
    return render(request,'sun.html')
def show_star(request):
    print('返回的数据：闪烁的星星')
    return render(request, 'star.html')
def show_login(request):
    return render(request,'login.html')
def fail(request):
    return render(request,'fail.html')
def login_action(request):
    if request.POST.get("username")=='tom' and request.POST.get("pwd")=='123456':
        print('用户',request.POST.get("username"),'登陆成功！')
        return render(request,'reg/success.html')
    else:
        return render(request, 'fail.html')
def url(request):
    return render(request, 'url.html')
def url_success(request):
    print('获取的数据：',request.GET.get('hobby'))
    return render(request, 'reg/success.html')







