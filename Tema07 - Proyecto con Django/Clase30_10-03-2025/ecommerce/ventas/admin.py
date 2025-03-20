from django.contrib import admin
from .models import Pedido, PedidoDetalle

# Register your models here.

class PedidoDetalleInline(admin.TabularInline):
    model = PedidoDetalle
    extra = 0
    fields = ['producto', 'cantidad', 'precio', 'subtotal']
    readonly_fields = ['subtotal']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('producto')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'cliente', 'total', 'estado', 'fecha_venta')
    inlines = [PedidoDetalleInline]

admin.site.register(Pedido, PedidoAdmin)
