from django.contrib import admin
from django.urls import path
from myapp.views import *
app_name="myapp"
urlpatterns = [
    path('startui/',showstart,name="gostartui"),
    path('showallcls/',showallcls,name="goallcls"),
    path('showallstu/',showallstu,name="goallstu"),
    path('goaddstudent/',goaddstudent,name="goaddstu"),
    path('addstudent/',addstudent),
    path('goaddcls/',goaddcls,name="goaddcls"),
    path('addcls/',addcls),
    path('godelstu/',showdelstu,name="godelstu"),
    path('delstu/',delstu),
    path('pagestudent/<int:page_param>/',pag_students,name='pagestudent')
]


