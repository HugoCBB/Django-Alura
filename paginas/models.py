from django.db import models
from datetime import datetime

# Create your models here.
class Categoria(models.Model):
    data = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
class Fotografia(models.Model):
    data = models.DateField(default=datetime.now, blank=False)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome