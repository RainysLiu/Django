# Create your views here.
from django.shortcuts import render,HttpResponse

def show_hello(request):
    return HttpResponse("<h3 style='color:red'>Hello! DjangoDay3!</h3>")
def show_person(request,name,age,sex):
    print("接收到的人名是：" + name + "；年龄：" + age)
    return render(request, 'person.html', {'person_name': name, 'person_age': age,'person_sex':sex})
def sum(request,a,b):
    print("接收到的两个数：" ,a,b)
    result=a+b
    return render(request, 'sum.html', {'a':a,'b':b,'re':result})
