from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models.deletion import CASCADE
from django.db.models.fields.json import DataContains
from django.db.models.fields.related import ForeignKey


class Imagem(models.Model):
	imagens = models.ImageField(upload_to='images/', blank=False, null=False)


class Equipe(models.Model):
    nome =  models.TextField( blank=False, null=False)
    pessoa = models.ManyToManyField(User)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome =  models.TextField( blank=False, null=False)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, null = True )

class Categoria(models.Model):
    nome =  models.TextField( blank=False, null=False)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null = True )

class Procedimento(models.Model):
    data  = models.DateTimeField()
    realizado_por  = models.OneToOneField(User, on_delete=models.CASCADE)
    titulo  =  models.TextField( blank=False, null=False)
    descricao  =  models.TextField( blank=False, null=False)
    foto  = models.ManyToManyField(Imagem)

class Ticket(models.Model):
    titulo =  models.TextField( blank=False, null=False)
    status =  models.TextField( blank=False, null=False)
    tipo = models.OneToOneField(Tipo, on_delete=models.CASCADE, related_name='tipo')
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE, related_name='categoria')
    data_abertura   = models.DateTimeField()
    data_finalizado   = models.DateTimeField()
    descricao =  models.TextField( blank=False, null=False)
    solicitante  = models.OneToOneField(User, on_delete=models.CASCADE, related_name='solicitante')
    atendentes = models.ForeignKey(User, on_delete=models.CASCADE , related_name='atendente')
    finalizado  = models.OneToOneField(User, on_delete=models.CASCADE, related_name='finalizador')
    procedimentos  = models.ManyToManyField(Procedimento)
    foto = models.ManyToManyField(Imagem)




    



