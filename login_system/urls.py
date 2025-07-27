# login_system/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='index'),  # Página de login (index.html)
    path('registro/', views.registro, name='registro'),  # Página de registro (registro.html)
    path('bienvenida/', views.bienvenida_view, name='bienvenida'),  # Página de bienvenida
]