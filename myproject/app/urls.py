from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
]