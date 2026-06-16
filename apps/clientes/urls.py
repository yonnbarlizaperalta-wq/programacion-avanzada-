from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('nuevo/', views.formulario_cliente, name='formulario_cliente'),

    path('', views.inicio, name='inicio'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('inmuebles/', views.lista_inmuebles, name='lista_inmuebles'),
    path('arriendos/', views.lista_arriendos, name='lista_arriendos'),

 ] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)