"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Appseminario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inscripcion/', views.inscripcion),
    path('inscripcion/listar_inscripcion/', views.listar_inscripcion),
    path('inscripcion/agregar_inscrito/', views.agregar_inscrito),
    path('inscripcion/eliminar_inscrito/<int:id>/', views.eliminar_inscrito),
    path('inscripcion/actualizar_inscrito/<int:id>/', views.actualizar_inscrito),

    path('inscripcionDB/', views.verinscritoDb),

    path('inscrito/', views.ListarInscrito.as_view()),

    path('inscrito/<int:pk>', views.DetalleInscrito.as_view()),
    path('institucion/', views.institucion_list),
    path('institucion/<int:pk>', views.institucion_detalle),
]
