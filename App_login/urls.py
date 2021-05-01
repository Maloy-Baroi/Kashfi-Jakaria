from django.conf.urls import url
from django.urls import path

from App_login.views import *

app_name = 'App_login'

urlpatterns = [
    path('', login_view, name='defaultview'),
    path('signup/', signup_system, name='signup'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]
