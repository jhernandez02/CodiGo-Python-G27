from django.urls import path
from . import views

app_name = 'auto'

urlpatterns = [
    path('', views.index, name='index'),
    path('detalle/<int:auto_id>', views.detalle, name="detalle"),
    path('categoria/<int:categoria_id>', views.categoria, name="categoria"),
    path('marca/<int:marca_id>', views.marca, name="marca")
]