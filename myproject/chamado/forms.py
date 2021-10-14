from django import forms
from .models import *

class AddPessoaEquipe(forms.Form):
	pessoa =  forms.IntegerField(label='Pessoa')
	equipe  = forms.IntegerField(label='Equipe')
