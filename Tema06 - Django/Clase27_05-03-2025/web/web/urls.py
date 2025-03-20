"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # series/api/v1/categories/ (GET)
    # series/api/v1/categories (POST)
    # series/api/v1/categories/<int:id>
    # series/api/v1/categories/<int:id>
    # series/api/v1/categories/<int:id>
    # series/api/v1/series/ (GET)
    # series/api/v1/series (POST)
    # series/api/v1/series/<int:id> (GET)
    # series/api/v1/series/<int:id> (PUT)
    # series/api/v1/series/<int:id> (DELETE)
    path('series/', include('series.urls'))
]
