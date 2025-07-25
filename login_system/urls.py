# login_system/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página de login (index.html)
    path('registro/', views.registro, name='registro'),  # Página de registro (registro.html)
    path('', views.login_view, name='index'),  # Login (index.html)
    path('bienvenida/', views.bienvenida_view, name='bienvenida'),
]
