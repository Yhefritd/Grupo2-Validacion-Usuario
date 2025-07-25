from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)  # ID auto_increment
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    contraseña = models.CharField(max_length=100)  # Para la contraseña encriptada

    def __str__(self):
        return self.nombre
