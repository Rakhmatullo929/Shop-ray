from django.contrib.auth import logout
from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

from django.conf import settings

urlpatterns = [
    path('login/', Login.as_view(), name='log_in'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', log_out , name='log_out'),
]
