from django.forms import ModelForm
from .models import Post, Comentarios


class crearpost(ModelForm):
    class Meta:
        model = Post
        fields = ["titulo","descripcion","foto","usuario"]

class crearcomentario(ModelForm):
    class Meta:
          model = Comentarios
          fields = ["comentarios","relacion"]