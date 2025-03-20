from django.shortcuts import render
from .models import Auto, Categoria, Marca

# Create your views here.

def index(request):
    # SELECT * FROM autos WHERE portada='1'
    lista_autos = Auto.objects.filter(portada='1')
    context = {
        'autos': lista_autos
    }
    # Pasamos context a la plantilla index.html
    return render(request, 'autos/index.html', context)

def detalle(request, auto_id):
    # SELECT * FROM autos WHERE id=auto_id
    auto = Auto.objects.get(pk=auto_id)
    context = {
        'auto': auto
    }
    return render(request, 'autos/detalle.html', context)

def categoria(request, categoria_id):
    # SELECT * FROM categorias WHERE id=categoria_id
    categoria = Categoria.objects.get(pk=categoria_id)
    # SELECT * FROM autos WHERE categoria_id=categoria_id
    lista_autos = Auto.objects.filter(categoria=categoria_id)
    context = {
        'categoria': categoria,
        'autos': lista_autos
    }
    return render(request, 'autos/categoria.html', context)

def marca(request, marca_id):
    # SELECT * FROM marcas WHERE id=marca_id
    marca = Marca.objects.get(pk=marca_id)
    # SELECT * 
    # FROM autos 
    # JOIN modelos ON modelos.id = autos.modelo_id
    # JOIN marcas ON marcas.id = modelos.marca_id 
    # WHERE modelos.marca_id=marca_id
    lista_autos = Auto.objects.filter(modelo__marca__id=marca_id)
    context = {
        'marca': marca,
        'autos': lista_autos
    }
    return render(request, 'autos/marca.html', context)