from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalle/<int:auto_id>', views.detalle, name='detalle'),
]