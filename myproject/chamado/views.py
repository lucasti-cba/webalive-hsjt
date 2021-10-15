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

#Equipes Visualização de equipes, criação, inclusão de pessoas atendentes.
@login_required(redirect_field_name='index')
def equipe(request):
    equipes = Equipe.objects.all()
    perfils = Perfil.objects.all()
    return render(request, 'equipe.html', {'equipes':equipes , 'perfils': perfils , 'perfil': get_perfil(request.user.id) })


@login_required(redirect_field_name='index')
def addEquipe(request):
    if request.method == "POST":
        form = AddEquipe(request.POST, request.FILES)   
        if form.is_valid():
            equipe = form.cleaned_data['equipe']
            equipeS = Equipe(nome = equipe)
            equipeS.save()
            return redirect('equipe')
    return redirect('equipe')


@login_required(redirect_field_name='index')
def delEquipe(request):
    if request.method == "POST":
        form = DelEquipe(request.POST, request.FILES)   
        if form.is_valid():
            equipe = form.cleaned_data['equipe']
            equipeS = get_object_or_404(Equipe, id = equipe)
            equipeS.delete()
            
            return redirect('equipe')
    return redirect('equipe')



@login_required(redirect_field_name='index')
def equipeAddPessoa(request):
    if request.method == "POST":
        form = AddPessoaEquipe(request.POST, request.FILES)   
        if form.is_valid():
            pessoa = form.cleaned_data['pessoa']
            equipe = form.cleaned_data['equipe']
            equipeS = get_object_or_404(Equipe, id = equipe)
            userP = get_object_or_404(User, id = pessoa )
            equipeS.pessoa.add(userP)
            equipeS.save()
            return redirect('equipe')
    return redirect('equipe')

@login_required(redirect_field_name='index')
def equipeDelPessoa(request):
    if request.method == "POST":
        form = DelPessoaEquipe(request.POST, request.FILES)   
        if form.is_valid():
            pessoaS = form.cleaned_data['pessoa']
            equipe = form.cleaned_data['equipe']
            equipeS = get_object_or_404(Equipe, id = equipe)
            userP = get_object_or_404(User, id = pessoaS )
            equipeS.pessoa.remove(userP)
            equipeS.save()
            return redirect('equipe')
    return redirect('equipe')

@login_required(redirect_field_name='index')
def cadastrarEquipe(request):
    return render(request, 'cadastrarEquipe.html')
    
@login_required(redirect_field_name='index')
def cadastrarTipo(request):
    return render(request, 'cadastrarTipo.html')

@login_required(redirect_field_name='index')
def cadastrarCategoria(request):
    return render(request, 'cadastrarCategoria.html')

@login_required(redirect_field_name='index')
def cadastrarProcedimento(request):
    return render(request, 'cadastrarProcedimento.html')

@login_required(redirect_field_name='index')
def cadastrarTicket(request):
    return render(request, 'cadastrarTicket.html')

