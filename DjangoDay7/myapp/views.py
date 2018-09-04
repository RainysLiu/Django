from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from myapp.models import *

# Create your views here.
def goaddstudent(request):
    clses=cls.objects.all()
    return render(request,"addstudent.html",locals())
def addstudent(request):
    n=request.POST.get("stuName")
    a = request.POST.get("stuAge")
    s = request.POST.get("sex")
    c=request.POST.get("classes")
    cobject=cls.objects.get(name=c).id
    student.objects.create(name=n,age=a,sex=s,stucls_id=cobject)
    print(n,"已加入student表")
    return render(request,"addstudentok.html",locals())
def goaddcls(request):
    return render(request, "addcls.html", locals())
def addcls(request):
    n = request.POST.get("clsName")
    cls.objects.create(name=n)
    print(n, "已加入cls表")
    return render(request, "addclsok.html", {'n':n})
def showstart(request):
    return render(request,"startui.html")
def showallstu(request):
    students = student.objects.all()
    clses=cls.objects.all()
    return render(request,"allstu.html",locals())
def showallcls(request):
    clses = cls.objects.all()
    return render(request,"allcls.html",{"clses":clses})
def showdelstu(request):
    students = student.objects.all()
    return render(request,"deletestu.html",locals())
def delstu(request):
    n=request.POST.get("delstu")
    student.objects.get(name=n).delete()
    print(n,"已经被删除")
    return render(request,"deletestuok.html",locals())



def pag_students(request,page_param=1):
    students = student.objects.all() # 查询所有的学生
    paginator = Paginator(students,4) # 创建分页器对象，第一个参数是记录的容器，第二个参数每页显示的记录数
    page = paginator.page(page_param)  # 获取指定页码的数据，以返回的Page对象封装这些数据
    return render(request,'pagestudents.html',{'paginator':paginator,'page':page})
