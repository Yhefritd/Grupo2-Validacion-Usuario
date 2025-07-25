from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from .models import ValidacionUser


def index(request):
    return render(request, 'index.html')


def registro(request):
    if request.method == 'POST':
        # Recibimos los datos del formulario
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        password = request.POST['password']

        if not nombre or not correo or not telefono or not password:
            return render(request, 'registro.html', {'error': 'Por favor complete todos los campos.'})

        # Encriptamos la contraseña
        password_encriptada = make_password(password)

        # Creamos un nuevo usuario y lo guardamos en la base de datos
        nuevo_usuario = ValidacionUser(
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            password=password_encriptada
        )
        nuevo_usuario.save()

        # Redirigimos a la página de login (o a donde desees)
        return redirect('index')

    return render(request, 'registro.html')

def login_view(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        password = request.POST['password']

        # Autenticamos al usuario
        user = authenticate(request, username=correo, password=password)

        if user is not None:
            # Si el usuario es autenticado correctamente, iniciamos sesión
            login(request, user)
            return redirect('bienvenida')  # Redirige a la página de bienvenida
        else:
            # Si las credenciales son incorrectas, mostramos un error
            return render(request, 'index.html', {'error': 'Credenciales incorrectas'})

    return render(request, 'index.html')

def bienvenida_view(request):
    if request.user.is_authenticated:
        return render(request, 'bienvenida.html')  # Solo mostrar si el usuario está autenticado
    else:
        return redirect('index')  # Si el usuario no está autenticado, redirigir a login
