from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('home/', views.workhome, name ='workhome'),
    path('newUser/', views.criar_user, name = 'criar_user')
]