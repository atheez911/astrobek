"""
URL configuration for astro_koinot project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('astronomy.urls')),
]
