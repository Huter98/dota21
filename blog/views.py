from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from . models import Noticia
from youtube.models import youtube
from foro.models import Post
# Create your views here.
def index(request):
    newfoto = Noticia.objects.last()
    
    youfoto = youtube.objects.last()
    
    blogfoto = Post.objects.last()
    

    return render(request, "index.html",{"newfoto":newfoto,"youfoto":youfoto,"blogfoto":blogfoto})


    
def sing_up(request):
    if request.method == "GET" :
        return render(request, "sing_up.html", {"form": UserCreationForm })
    else:
        if request.POST["password1"] == request.POST["password2"]:
           try:
               user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
               user.save()
               login(request, user)
               return render(request, "index.html")
           except:
               return render(request,"sing_up.html",{"form": UserCreationForm,
                   "error": "Usuario ya existe"
               })
        else:
            return render(request,"sing_up.html",{"form": UserCreationForm,
                   "error": "Contraseña incorrecta"
               })

        
def cerrar(request):
    logout(request)
    return redirect("index")

def iniciar_sesion(request):

    if request.method == "GET":
        return render(request,"singin.html",{"form": AuthenticationForm})
    else:
       user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
       if user is None:
           return render(request,"singin.html",{"form": AuthenticationForm, "error":"Username or password is incorrect"})
       else:
           login(request, user)
           return  redirect("index")
       
def noticias(request):
    form = Noticia.objects.all().order_by("-id")
    return render(request, "noticias.html",{"form":form})