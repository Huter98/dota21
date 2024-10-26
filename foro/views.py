from django.shortcuts import render,redirect,HttpResponse
from . models import Post
from . forms import crearpost,crearcomentario
from django.contrib.auth.models import User

# Create your views here.

def forum(request):
    if request.method == "GET":
        post = Post.objects.all().order_by("-id")
        
        return render(request,"forum.html",{"post":post,"comentar":crearcomentario})
    else:
        
        comen = crearcomentario(request.POST)
        if comen.is_valid():
           comen.save()
           return redirect ("forum")
        else:
            return HttpResponse("Todos los campos son obligatorios, asegurese de incluir una foto")
  
def crear(request):
    if request.method == "GET":
        
        
        return render(request, "crear.html",{"form":crearpost})
    else:
        form = crearpost(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return redirect ("forum")
        else:
            return HttpResponse("Todos los campos son obligatorios, asegurese de incluir una foto")
        
    