from django.contrib import admin
from .models import Categoria, Marca, Modelo, Auto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')
    ordering = ('descripcion',)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')
    ordering = ('descripcion',)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'descripcion')
    ordering = ('marca__descripcion','descripcion')
    list_filter = ('marca__descripcion',)

class AutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'placa', 'get_marca' ,'modelo','portada','anio')
    ordering = ('categoria__descripcion','modelo__marca__descripcion', 'modelo__descripcion')
    list_filter = ('categoria__descripcion','modelo__marca__descripcion','anio')
    search_fields = ('placa','anio','categoria__descripcion','modelo__descripcion')
    
    def get_marca(self, obj):
        return obj.modelo.marca.descripcion
    
    # Asignamos el título de la columna en el admin
    get_marca.short_description = 'Marca'

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Auto, AutoAdmin)