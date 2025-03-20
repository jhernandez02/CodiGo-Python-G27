from django import template
from ..models import Categoria

register = template.Library()

@register.inclusion_tag('autos/shared/header_categoria_menu.html')
def obtener_categorias():
    lista_categorias = Categoria.objects.all()
    return {'categorias':lista_categorias}

@register.inclusion_tag('autos/shared/footer_categoria_menu.html')
def footer_categoria_menu():
    lista_categorias = Categoria.objects.all()
    return {'categorias':lista_categorias}