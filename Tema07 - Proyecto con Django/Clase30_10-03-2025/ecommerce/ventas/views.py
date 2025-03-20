from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Pedido
from .serializers import PedidoSerializer
from .permissions import IsOwner, CanEdit, CanDelete

# Create your views here.

# /ventas/api/v1/pedidos/   [GET]       <- El usuario solo puede ver sus pedidos
# /ventas/api/v1/pedidos/10 [GET]       <- El usuario solo puede ver el detalle de su pedido
# /ventas/api/v1/pedidos/   [POST]
# /ventas/api/v1/pedidos/10 [PUT]       <- Solo por superadmin
# /ventas/api/v1/pedidos/10 [DELETE]    <- Solo por superadmin
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'retrieve': # Solicita el detalle de un pedido
            permission_classes = [IsAuthenticated, IsOwner]
        elif self.action == 'update': # Solicita actualizar un pedido
            permission_classes = [IsAuthenticated, CanEdit]
        elif self.action == 'destroy': # Solicita eliminar un pedido
            permission_classes = [IsAuthenticated, CanDelete]
        else: # list, create y partial_update
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        user_id = self.request.user.id
        # Seleccionamos solo los pedidos del cliente autenticado
        pedidos = Pedido.objects.filter(cliente_id=user_id)
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)
