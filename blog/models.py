from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.TextField()
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="youtube")
    enlace = models.URLField()
    subido = models.DateTimeField(auto_now=True)
    def __str__(self):
        return (self.titulo)