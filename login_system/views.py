
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.
def index(request):
    return render(request, 'index.html')


def registro(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']
        telefono = request.POST.get('telefono', '')

        print(f"Nombre: {nombre}, Correo: {correo}, Contraseña: {contraseña}, Teléfono: {telefono}")  # Para depuración

        # Crea un nuevo usuario y guárdalo en la base de datos
        usuario = Usuario(
            nombre=nombre,
            correo=correo,
            contraseña=contraseña,  # Recuerda que deberías encriptar la contraseña antes de guardarla
            telefono=telefono
        )
        usuario.save()

        # Redirige a una página de éxito o de inicio de sesión
        return redirect('login')  # O la URL a la que quieras redirigir

    return render(request, 'register.html')
