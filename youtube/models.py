from django.db import models
from datetime import datetime

# Create your models here.

class youtube(models.Model):
    titulo = models.TextField()
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="youtube")
    enlace = models.URLField()
    subido = models.DateTimeField(auto_now=True)
    def __str__(self):
        return (self.titulo)
