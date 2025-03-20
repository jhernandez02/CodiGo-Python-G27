from rest_framework import viewsets, views
from rest_framework.response import Response 
# Importamos el permiso IsAdminUser
from rest_framework.permissions import IsAdminUser
from . models import Pago
from . serializer import PagoSerializer
from . permissions import isOwnerPayment

# Create your views here.

class UsuarioPagoDetalleView(views.APIView):
    permission_classes = [isOwnerPayment]
    def get(self, request, id):
        try:
            pago = Pago.objects.get(pk=id)
            serializer = PagoSerializer(pago)
            return Response(serializer.data)
        except Exception:
            return Response({'detail':'Pago no encontrado'}), 404

class UsuarioPagosView(views.APIView):
    def get(self, request):
        # Accedemos al id del usuario autenticado
        user_id = request.user.id
        # Obtenemos la lista de pagos del usuario autenticado
        pagos = Pago.objects.filter(usuario=user_id)
        serializer = PagoSerializer(pagos, many=True)
        return Response(serializer.data)

class PagoViewSet(viewsets.ModelViewSet):
    # Asignanos el permiso solo para los administradores
    permission_classes = [IsAdminUser]
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer