from django.db import models
# Usamos el modelo User de django
from django.contrib.auth.models import User

# Create your models here.

class Pago(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT)
    monto = models.FloatField(default=0)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=45)
