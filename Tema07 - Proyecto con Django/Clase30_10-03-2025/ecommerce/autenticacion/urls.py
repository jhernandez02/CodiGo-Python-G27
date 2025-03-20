from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/v1/login', views.LoginView.as_view()),
    path('api/v1/refresh', TokenRefreshView.as_view()),
]