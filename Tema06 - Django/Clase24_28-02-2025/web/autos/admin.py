from django.contrib import admin
from .models import Auto

class AutoAdmin(admin.ModelAdmin):
    list_display = ('id','categoria','placa','marca','modelo','portada')

# Register your models here.
admin.site.register(Auto, AutoAdmin)