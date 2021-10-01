from django import forms
from .models import *

class NovoCadastro_User(forms.Form):
	PERMISSION_CHOICES = (('0', 'Administrador de Sistema'), ('1','Gerente de Atendimento'), ('2','Portaria'))
	nome =  forms.CharField(label='Nome', max_length=250)
	email = forms.CharField(label='Email', max_length=100)
	telefone = forms.CharField(label='Telefone', max_length=30)
	permissoes =  forms.ChoiceField(choices = PERMISSION_CHOICES, label='Permissões')
	foto  = forms.ImageField(label='Foto', required=False)
	cargo =  forms.CharField(label='Cargo', max_length=50) 
	user =  forms.CharField(label='Usuário', max_length=30)
	password =  forms.CharField(label='Senha', max_length=32)