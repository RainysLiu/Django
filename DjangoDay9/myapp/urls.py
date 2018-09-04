from django.contrib import admin
from django.urls import path,include
from myapp.views import *
app_name='myapp'
urlpatterns = [
    path('reg/',user_form,name='goreg'),
    path('getallstu/',get_allstu)
]
