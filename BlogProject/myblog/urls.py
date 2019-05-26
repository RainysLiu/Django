from django.urls import path
from myblog.views import *
app_name='myblog'
urlpatterns = [
    path('goreg/',goreg,name='goreg'),
    path('reg/', reg, name='reg'),
    path('gologin/', gologin, name='gologin'),
    path('login/', my_login, name='login'),
    path('logout/',my_logout,name='logout'),
    path('',goindex,name='goindex'),
    path('gocate/',gocate,name='gocate'),
    path('goarticle/',goarticle,name='goarticle'),
    path('addcomment/',addcomment,name='addcomment')

]




