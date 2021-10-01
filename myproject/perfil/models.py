from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
# Create your models here.


class Imagem(models.Model):
	imagens = models.ImageField(upload_to='images/', blank=False, null=False)


class Perfil(models.Model):
    user  =  models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    nome = models.TextField( blank=False, null=False)
    email = models.TextField( blank=False, null=False)
    telefone = models.TextField( blank=False, null=False)
    cargo = models.TextField( blank=False, null=False)
    foto  = models.ManyToManyField(Imagem)
    def __str__(self):
        return self.nome