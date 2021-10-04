from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_visitante, name ='cadastro_visitante'),
    path('visitante/', views.visitante, name ='visitante'),
    path('acompanhante/', views.acompanhante, name ='acompanhante'),
]
