from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Category, Serie
from . serializer import CategorySerializer, SerieSerializer

# El ModelViewset es una clase de vista que proporciona
# un conjuto de operaciones (CRUD) para un modelo específico
class CategoryViewSet(viewsets.ModelViewSet):
    # Definimos qué datos del modelo estarán disponibles 
    # para ser consultados y modificados
    queryset = Category.objects.all().order_by('description')
    # Se especifica el serializador que se utilizará
    # para transformar los datos entre el modelo Category
    # y los formatos de respuesta (JSON)
    serializer_class = CategorySerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all().order_by('name')
    serializer_class = SerieSerializer

class SerieByCategory(APIView):
    # Ejecutamos con el método GET
    def get(self, request, category_id):
        series = Serie.objects.filter(category=category_id)
        serializer = SerieSerializer(series, many=True)
        return Response(serializer.data)
