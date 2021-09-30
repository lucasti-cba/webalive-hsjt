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



# Create your views here.
def index(request):
    mensagem = None 
    if request.user.id is not None:
        return redirect('workhome')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            auth_login(request, usuario)
            user = request.user.id
        else:
            mensagem = 'Usuario ou senha invalido.'
    return render(request, 'login.html')

def workhome(request):
    return render(request, 'workhome.html')