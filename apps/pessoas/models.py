
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Pessoa(models.Model):
    usuario = models.ForeignKey(User,related_name='usuario'   , on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14,null=False)
    endereco = models.CharField(max_length=200)
    sexo = models.CharField(max_length=2)
    lista_sentimentos = models.TextField(null=True)
    date_pessoa = models.DateTimeField(default=datetime.now, blank=True)
    foto_pessoa= models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)
    def __str__(self):
        return self.nome