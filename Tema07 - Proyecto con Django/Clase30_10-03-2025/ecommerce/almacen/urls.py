from django.urls import path
from almacen import views

urlpatterns = [
    path('api/v1/categorias', views.CategoriaListView.as_view()),
    path('api/v1/productos', views.ProductoListView.as_view()),
    path('api/v1/productos/<int:pk>', views.ProductoDetailView.as_view()),
]