"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers

from enfermeros.views import agregar_enfermero, ver_enfermero, eliminar_enfermero, modificar_enfermero, generar_reporte, \
    EnfermeroViewSet, DatosViewSet, EnfermedadViewSet
from webapp.views import bienvenida2

router = routers.DefaultRouter()
router.register(r'api_enfermeros', EnfermeroViewSet)
router.register(r'api_datos', DatosViewSet)
router.register(r'api_enfermedad', EnfermedadViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', bienvenida2, name='inicio'),
    path('agregar_enfermero/', agregar_enfermero),
    path('ver_enfermero/<int:id>', ver_enfermero),
    path('eliminar_enfermero/<int:id>', eliminar_enfermero),
    path('modificar_enfermero/<int:id>', modificar_enfermero),
    path('generar_reporte/', generar_reporte),
]

urlpatterns += router.urls
