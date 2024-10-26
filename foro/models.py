from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.TextField()
    usuario= models.ForeignKey(User,on_delete=models.CASCADE)
    descripcion = models.TextField()
    subido = models.DateTimeField(auto_now=True)
    foto = models.ImageField(upload_to="blog")
    def __str__(self):
        return (self.titulo)
    
class Comentarios(models.Model):
    comentarios = models.TextField()
    subido = models.DateTimeField(auto_now=True)
    relacion = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="coments")
    def __str__(self):
        return (self.comentarios)
