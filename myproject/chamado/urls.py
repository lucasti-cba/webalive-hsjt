from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('equipe/', views.equipe, name ='equipe'),
    path('addEquipe/', views.addEquipe, name ='addEquipe'),
    path('delEquipe/', views.delEquipe, name ='delEquipe'),
    path('addPessoa/', views.equipeAddPessoa, name ='addPessoa'),
    path('delPessoa/', views.equipeDelPessoa, name ='delPessoa'),
]
