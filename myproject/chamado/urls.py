from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('equipe/', views.equipe, name ='equipe'),
    path('addPessoa/', views.equipeAddPessoa, name ='addPessoa'),
]
