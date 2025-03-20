from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.RESTRICT)

    def __str__(self):
        return self.titulo
