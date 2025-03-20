from rest_framework.permissions import BasePermission
from . models import Pago

class isOwnerPayment(BasePermission):
    def has_permission(self, request, view):
        # Accedemos al id del empleado autenticado
        user_id = request.user.id
        # Obtener el valor del id del pago enviado desde la url
        pago_id = int(view.kwargs.get('id'))
        pago = Pago.objects.get(pk=pago_id)
        return pago.usuario.id == user_id