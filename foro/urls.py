
from . import views
from django.urls import path 


urlpatterns = [
    path('forum/', views.forum, name="forum"),
    path('crear_blog/', views.crear, name="crear"),

] 
