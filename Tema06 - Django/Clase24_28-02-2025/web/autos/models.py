from django.db import models

# Create your models here.

class Auto(models.Model):

    TRANSMISION_LISTA = (
        ('A','Automático'),
        ('M','Mecánico')
    )

    COMBUSTIBLE_LISTA = (
        ('P','GLP'),
        ('V','GNV'),
        ('G','Gasolina'),
        ('D','Diesel'),
        ('E','Electricidad'),
    )

    PORTADA_LISTA = (
        ('0','No'),
        ('1','Sí'),
    )

    categoria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=6)
    anio = models.CharField(max_length=4)
    color = models.CharField(max_length=25)
    transmision = models.CharField(max_length=15, choices=TRANSMISION_LISTA)
    combustible = models.CharField(max_length=15, choices=COMBUSTIBLE_LISTA)
    precio = models.FloatField(default=0.0)
    portada = models.CharField(max_length=1, default='0', choices=PORTADA_LISTA)