from django.contrib import admin
from .models import Cliente, Inmueble, Arriendo, Pago


admin.site.register(Cliente)
admin.site.register(Inmueble)
admin.site.register(Arriendo)
admin.site.register(Pago)