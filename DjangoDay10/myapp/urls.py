from django.contrib import admin
from django.urls import path,include
from myapp.views import *
app_name='myapp'
urlpatterns = [
    path('showreg/',showreg),
    path('reg/',reg,name='goreg'),
    path('showlogin/',showlogin,name='gologin'),
    path('login/',u_login,name='login'),
    path('success/',success),
    path('logout/',u_logout,name='logout'),
    path('showupload/',showloadpicture,name='goupload'),
    path('upload/',upload,name='upload'),
    path('getallstu/',getallstu),
    path('govip/',govip),
]






