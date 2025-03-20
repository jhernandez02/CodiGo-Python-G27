from rest_framework import serializers
from .models import Pedido, PedidoDetalle

class PedidoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoDetalle
        fields = ['producto', 'cantidad', 'precio', 'subtotal']

class PedidoSerializer(serializers.ModelSerializer):
    
    detalles = PedidoDetalleSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['cliente', 'codigo', 'total', 'estado', 'fecha_venta', 'detalles']

    def create(self, validated_data):
        # Obtenemos y quitamos el detalle del pedido
        detalle_pedido = validated_data.pop('detalles')
        # Creamos el pedido
        pedido = Pedido.objects.create(**validated_data)
        # Creamos los detalles del pedido
        for detalle in detalle_pedido:
            PedidoDetalle.objects.create(pedido=pedido, **detalle)
        
        return pedido
