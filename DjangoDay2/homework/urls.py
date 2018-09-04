from django.urls import path
from homework.views import show_hello,show_login,login_action,getTime
urlpatterns = [
    path('hello/',show_hello),
    path('login/',show_login),
    path('loginReaction/',login_action),
    path('getTime/',getTime)
]