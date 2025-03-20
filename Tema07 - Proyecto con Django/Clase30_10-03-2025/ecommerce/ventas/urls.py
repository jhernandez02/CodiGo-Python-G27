from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ventas import views

router = DefaultRouter()
router.register(r'pedidos', views.PedidoViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]