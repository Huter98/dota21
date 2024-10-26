from django.shortcuts import render
from .models import youtube

# Create your views here.
def yout_ube(request):
    carta = youtube.objects.all().order_by("-id")
    return render(request, "youtube.html",{"carta":carta})
