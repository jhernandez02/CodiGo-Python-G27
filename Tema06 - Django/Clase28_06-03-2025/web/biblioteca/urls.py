from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'generos', views.GeneroViewSet)
router.register(r'libros', views.LibroViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))
]