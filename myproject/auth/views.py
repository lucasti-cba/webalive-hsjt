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

def get_perfil(user):
    perfil = get_object_or_404(Perfil, user = user)
    return perfil
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

    return render(request, 'workhome.html', {'perfil': get_perfil(request.user.id) })

def criar_user(request):

    user = request.user

    form = NovoCadastro_User()
    if request.method == "POST":
        form = NovoCadastro_User(request.POST, request.FILES)   
        if form.is_valid():           
            nome =  form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            permissoes =  form.cleaned_data['permissoes']
            foto  = form.cleaned_data['foto']
            cargo = form.cleaned_data['cargo']
            user = form.cleaned_data['user']
            password =  form.cleaned_data['password']
            imagens = Imagem(imagens=foto) 
            imagens.save()
            userC =  User.objects.create_user(user, email, password)
            userC.first_name = nome
            userC.save()
            perfil = Perfil(user = userC, nome = nome, email = email, telefone = telefone, cargo = cargo)
            perfil.save()
            perfil.foto.add(imagens)
            print(permissoes)
            if permissoes == '0':
                group = Group.objects.get(name='Admin')
                userC.groups.add(group)
            if permissoes == '1':
                group = Group.objects.get(name='Gerencia')
                userC.groups.add(group)
            if permissoes == '2':
                group = Group.objects.get(name='Portaria')
                userC.groups.add(group)
            userC.save()
            return redirect('workhome')


    return render(request, 'newUser.html', { 'form': form ,'perfil': get_perfil(request.user.id)})