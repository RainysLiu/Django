from django.contrib import admin
from django.urls import path
from myapp.views import *
app_name="myapp"
urlpatterns = [
    path('startui/',startui,name="gostartui"),
    path('allstu/',allstu,name="goallstu"),
]



