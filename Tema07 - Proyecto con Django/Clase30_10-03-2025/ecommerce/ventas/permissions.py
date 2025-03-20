from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print('token:', request.user)
        print('pedido:', obj.cliente)
        return request.user == obj.cliente

class CanEdit(BasePermission):
    # Permiso que permite editar un pedido otorgado a los super administradores
    def has_permission(self, request, view):
        return request.method=='PUT' and request.user.is_superuser

class CanDelete(BasePermission):
    # Permiso que permite eliminar un pedido otorgado a los super administradores
    def has_permission(self, request, view):
        return request.method=='DELETE' and request.user.is_superuser
