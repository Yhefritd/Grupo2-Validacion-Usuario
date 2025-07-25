from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Administrador personalizado para gestionar usuarios
class CustomUserManager(BaseUserManager):
    def create_user(self, nombre, correo, telefono, password=None):
        if not correo:
            raise ValueError("El correo debe ser obligatorio")
        user = self.model(
            nombre=nombre,
            correo=correo,
            telefono=telefono
        )
        user.set_password(password)  # Esto encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, correo, telefono, password=None):
        user = self.create_user(
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Modelo de usuario
class ValidacionUser(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Contraseña encriptada por Django
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Campos de autenticación
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Definir el manager para el modelo
    objects = CustomUserManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'telefono']

    def __str__(self):
        return self.nombre