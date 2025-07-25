#Archivo que cree para poder poner todos las url aca y no en myproyect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registro/', views.registro, name='registro'),
]
