from django.contrib import admin
from django.urls import path
# Importamos todas tus funciones desde el archivo views de clientes
from apps.clientes import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # RUTA DE INICIO
    path('', views.inicio, name='inicio'),
    
    # RUTAS DE CLIENTES
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/nuevo/', views.formulario_cliente, name='formulario_cliente'),
    
    # RUTAS DE INMUEBLES (Las que te faltaban o causaban conflicto)
    path('inmuebles/', views.lista_inmuebles, name='lista_inmuebles'),
    path('inmuebles/nuevo/', views.formulario_inmueble, name='formulario_inmueble'),
    path('inmuebles/crear/', views.crear_inmueble, name='crear_inmueble'),
    
    # RUTAS DE ARRIENDOS
    path('arriendos/', views.lista_arriendos, name='lista_arriendos'),
]
