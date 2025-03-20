from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pagos', views.PagoViewSet)

urlpatterns = [
    path('api/v1/pagos/usuarios/', views.UsuarioPagosView.as_view()),
    path('api/v1/pagos/usuarios/<int:id>', views.UsuarioPagoDetalleView.as_view()),
    path('api/v1/', include(router.urls))
]
