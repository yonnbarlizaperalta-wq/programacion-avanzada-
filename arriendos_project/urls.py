from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # rutas de apps
    path('clientes/', include('apps.clientes.urls')),
]