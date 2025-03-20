from django.shortcuts import render
from .models import Auto

# Create your views here.

def index(request):
    lista_autos = Auto.objects.filter(portada='1')
    context = {
        'autos': lista_autos
    }
    return render(request, 'autos/index.html', context)

def detalle(request, auto_id):
    auto = Auto.objects.get(pk=auto_id)
    context = {
        'titulo': 'Detalle del auto',
        'auto': auto
    }
    return render(request, 'autos/detalle.html', context)
