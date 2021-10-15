from django import forms
from .models import *

class AddPessoaEquipe(forms.Form):
	pessoa =  forms.IntegerField(label='Pessoa')
	equipe  = forms.IntegerField(label='Equipe')

class AddEquipe(forms.Form):
	equipe  = forms.CharField(label='Equipe')


class DelEquipe(forms.Form):
	equipe  = forms.IntegerField(label='Equipe')


class DelPessoaEquipe(forms.Form):
	pessoa =  forms.IntegerField(label='Pessoa')
	equipe  = forms.IntegerField(label='Equipe')
