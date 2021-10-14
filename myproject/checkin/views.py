from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from .models import *
from .forms import *
import os
import time
from django.template import Library
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime
from django import template
from  perfil.models import *
from django.contrib.auth.models import Group

register = Library()
# Funções Reutilizaveis 
def get_perfil(user):
    perfil = get_object_or_404(Perfil, user = user)
    return perfil
# Create your views here.

@login_required(redirect_field_name='index')
def cadastro_visitante(request):
    form = NovoCadastro_Visitante()
    if request.method == "POST":
        form = NovoCadastro_Visitante(request.POST, request.FILES)   
        if form.is_valid():           
            nome =  form.cleaned_data['nome']
            foto = form.cleaned_data['foto']
            imagens = Imagem(imagens=foto) 
            imagens.save()
            visitante = Visitante(Nome = nome)
            visitante.save()
            visitante.foto.add(imagens)
            visitante.save()
            return redirect('index')
    return render(request, 'cadastro_visitante.html', { 'perfil': get_perfil(request.user.id) })

@login_required(redirect_field_name='index')
def visitante(request):
    return render(request, 'visitante.html', { 'perfil': get_perfil(request.user.id) })

@login_required(redirect_field_name='index')
def acompanhante(request):
    return render(request, 'acompanhante.html', { 'perfil': get_perfil(request.user.id) })