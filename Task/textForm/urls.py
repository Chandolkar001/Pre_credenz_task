from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
path('', views.index, name='sign-up'),
path('login', views.login, name='login'),
path('logout', views.logout, name='logout'),
path('userHome', views.userHome, name='userHome'),
]