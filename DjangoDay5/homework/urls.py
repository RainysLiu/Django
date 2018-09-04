from django.contrib import admin
from django.urls import path
from homework.views import *
urlpatterns = [
    path('reg/',showreg),
    path('reg/check/<regvalue>/',check),
    path('reg/success/',success),
]


