from django.shortcuts import render,HttpResponse
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def about(request):
    if request.method == "GET":
        return render(request, "about.html")
    else:
        subject= request.POST["asunto"]
        messege = request.POST["mensaje"] + "" + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["dota2.cuban@gmail.com"]
        send_mail(subject, messege, email_from, recipient_list)
        return HttpResponse("Mensaje enviado")