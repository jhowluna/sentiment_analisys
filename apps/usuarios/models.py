from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    senha = models.TextField()
    senha2 = models.TextField()
    def __str__(self):
        return self.nome
