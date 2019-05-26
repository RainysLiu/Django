from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from myblog.blog_page import getblog_bypage
from myblog.models import *

def goreg(request):
    return render(request,'reg.html')
def reg(request):
    regname = request.POST["regname"]
    regpwd = request.POST["regpwd"]
    regqq = request.POST["regqq"]
    regemmil = request.POST["regemail"]
    regtel= request.POST["regtel"]
    MyUser.objects.create_user(username=regname, password=regpwd, email=regemmil,qq=regqq,tel=regtel)  # 添加到数据库中的auth_user表,create_user()对密码加密
    return HttpResponseRedirect('/myblog/gologin/')
def gologin(request):
    return render(request,'login.html')
def my_login(request):
    logname = request.POST["logname"]
    logpwd = request.POST["logpwd"]
    user = authenticate(username=logname, password=logpwd)  # 认证用户，判断用户名和密码是否正确
    if user:
        login(request, user)  # 将用户标识保存到session中
        return HttpResponseRedirect("/myblog/goindex/")  # 重定向到首页
    else:
        return render(request, 'login.html', {"msg": "用户名或密码错误，请重新登录！"})
def my_logout(request):
    logout(request)  # 登出
    return HttpResponseRedirect("/myblog/gologin/")


@login_required(login_url="/myblog/gologin/")
def goindex(request):
    article_list = Article.objects.all()
    article_list = getblog_bypage(request, article_list)
    return render(request, 'index.html', locals())


def gocate(request):
    try:
        category_id = request.GET.get('cid', "")
        article_list = Article.objects.filter(category_id=category_id)
        article_list = getblog_bypage(request, article_list)
        return render(request,'index.html',locals())
    except:
        article_list = Article.objects.all()
        article_list = getblog_bypage(request, article_list)
        return render(request, 'index.html', locals())


def goarticle(request):
    article_id = request.GET.get('id',"")
    article = Article.objects.get(id=article_id)
    Article.objects.filter(id=article_id).update(click_count=article.click_count + 1)
    category_id=article.category.id
    comment_list=Comment.objects.filter(article_id=article_id)
    crtcile_list_length=comment_list.count()
    return render(request, 'article.html', locals())

def addcomment(request):
    content = request.POST['comment_content']
    u_id = request.GET.get('uid')
    a_id = request.GET.get('aid')
    try:
        Comment.objects.create(content=content,user_id=u_id,article_id=a_id)
        return HttpResponseRedirect('/myblog/goarticle?id=' + a_id, {'msg': '评论成功！'})
    except:
        return HttpResponseRedirect('/myblog/goarticle?id='+a_id,{'msg':'评论失败！'})


