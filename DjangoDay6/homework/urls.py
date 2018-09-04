from django.contrib import admin
from django.urls import path
from homework.views import *
urlpatterns = [
    path('login/',showlogin),
    path('login/check/<acc>/<pwd>/',check),
    path('login/success/',success),
]


