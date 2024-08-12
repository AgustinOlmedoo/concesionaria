from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario.username} - {self.fecha_creacion}'

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class ModeloAuto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.marca.nombre})"

class Auto(models.Model):
    marca = models.CharField(max_length=100)  
    modelo = models.CharField(max_length=100)  
    año = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='autos/')

    def __str__(self):
        return f'{self.marca} {self.modelo}'
