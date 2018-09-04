from django.urls import path
from myapp.views import *
urlpatterns = [
    path('welcome/', hello),
    path('showtest/',showtest),
    path('showduanzi/',showduanzi),
    path('showMM/',showMM),
    path('reg/',show_reg),
    path('regaction/',reg_action),
    path('sun/',show_sun),
    path('star/',show_star),
    path('login/',show_login),
    path('login_action/',login_action),
    path('urlsuccess/',url_success),
    path('url/',url)
]



