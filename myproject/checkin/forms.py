from django import forms
from .models import *

class NovoCadastro_Visitante(forms.Form):
	nome =  forms.CharField(label='Nome', max_length=250)
	foto  = forms.ImageField(label='Foto', required=False)
