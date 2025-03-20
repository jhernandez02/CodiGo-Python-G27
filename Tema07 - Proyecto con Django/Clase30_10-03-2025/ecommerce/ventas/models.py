from django.db import models
from almacen.models import Producto
# Create your models here.

class Pedido(models.Model):

    ESTADOS_LISTA = (
        ('Pendiente', 'PENDIENTE'),
        ('Completado', 'COMPLETADO'),
        ('Cancelado', 'CANCELADO')
    )

    codigo = models.CharField(max_length=100)
    total = models.FloatField()
    estado = models.CharField(max_length=10, choices=ESTADOS_LISTA) # Pendiente, Completado, Cancelado
    fecha_venta = models.DateTimeField(auto_now_add=True)
    # related_name define el nombre de la relación inversa
    # que se podrá usar para acceder a los pedidos de un usuario
    # Ej: usuario = User.objects.get(pk=36)
    #     pedidos_del_usuario = usuario.pedidos.all()
    cliente = models.ForeignKey(
        'auth.User', 
        on_delete=models.RESTRICT, 
        related_name='pedidos'
    )

    def __str__(self):
        return f'Pedido {self.codigo}'

class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    subtotal = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        # Calculamos el subtotal antes de guardar el objeto
        self.subtotal = self.cantidad * self.precio
        # Guardamos el detalle
        super().save(*args, **kwargs)
