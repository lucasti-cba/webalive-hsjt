from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


class Imagem(models.Model):
	imagens = models.ImageField(upload_to='images/', blank=False, null=False)

class Visitante(models.Model):
    Nome =  models.TextField( blank=False, null=False)
    foto = models.ManyToManyField(Imagem)
    

class Visita(models.Model):
    visitante =  models.OneToOneField(Visitante, on_delete=models.SET_NULL, null=True)
    hora_entrada = models.DateTimeField()
    hora_saida = models.DateTimeField()
    autorizador =  models.OneToOneField(User, on_delete=models.SET_NULL, null=True) 


class Paciente(models.Model):
    nome  =  models.TextField( blank=False, null=False)
    quarto  =  models.TextField( blank=False, null=False)
    recebe_visita =  models.BooleanField()
    visita = models.ManyToManyField(Visita)
    recebe_acompanhante =  models.BooleanField()
    acompanhante = models.ManyToManyField(Imagem)


