from django.urls import path
from myapp.views import show_hello,show_person,sum
urlpatterns = [
    path('hello/',show_hello),
    path('person/<name>/<age>/<sex>/',show_person),
    path('sum/<int:a>/<int:b>/',sum)
]