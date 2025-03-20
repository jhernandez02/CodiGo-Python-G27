from django import template
from ..models import Marca

register = template.Library()

@register.inclusion_tag('autos/shared/header_marca_menu.html')
def header_marcas_menu():
    lista_marcas = Marca.objects.all()
    return {'marcas':lista_marcas}

@register.inclusion_tag('autos/shared/footer_marca_menu.html')
def footer_marcas_menu():
    lista_marcas = Marca.objects.all()
    return {'marcas':lista_marcas}