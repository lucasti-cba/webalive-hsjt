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

# Funções Reutilizaveis 
def get_perfil(user):
    perfil = get_object_or_404(Perfil, user = user)
    return perfil
# Create your views here.


def cadastro_visitante(request):
    return render(request, 'cadastro_visitante.html', { 'perfil': get_perfil(request.user.id) })


def visitante(request):
    return render(request, 'visitante.html', { 'perfil': get_perfil(request.user.id) })

def acompanhante(request):
    return render(request, 'acompanhante.html', { 'perfil': get_perfil(request.user.id) })