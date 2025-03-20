from django.urls import path, include
from rest_framework import routers
from . import views

# Creamos el enrutados 
router = routers.DefaultRouter()
# Definimos las rutas para la vista CategoryViewSet
router.register(r'categories', views.CategoryViewSet)
# Definimos las rutas para la vista SerieViewSet
router.register(r'series', views.SerieViewSet)

# Generados el prefijo para todas la rutas que contiene router

# api/v1/categories/ (GET) -> listado de todas las categorías
# api/v1/categories/ (POST) -> crea una categoría
# api/v1/categories/<int:id> (GET) -> detalle de un categoría
# api/v1/categories/<int:id> (PUT) -> edita una categoría
# api/v1/categories/<int:id> (DELETE) -> elimina una categoría

# api/v1/series/ (GET) -> listado de todas las series
# api/v1/series (POST) -> crea una serie
# api/v1/series/<int:id> (GET) -> detalle de un serie
# api/v1/series/<int:id> (PUT) -> edita una serie
# api/v1/series/<int:id> (DELETE) -> elimina una serie
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/series/categories/<int:category_id>/', views.SerieByCategory.as_view()),
]