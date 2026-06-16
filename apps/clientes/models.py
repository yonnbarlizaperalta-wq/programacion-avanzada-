from django.db import models

# 👤 CLIENTE
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


from django.db import models

class Inmueble(models.Model):
    tipo = models.CharField(max_length=50, default='Apartamento')
    ciudad = models.CharField(max_length=50, default='Ciudad')
    direccion = models.CharField(max_length=100, default='Dirección')
    precio = models.DecimalField(max_length=15, max_digits=12, decimal_places=2, default=0.0)
    habitaciones = models.IntegerField(default=1)
    banos = models.IntegerField(default=1)
    area = models.FloatField(default=0.0)
    imagen = models.ImageField(upload_to='inmuebles/', null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.ciudad}"


# 📄 ARRIENDO
class Arriendo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.cliente} - {self.inmueble}"


class Pago(models.Model):
    arriendo = models.ForeignKey(Arriendo, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pago {self.id}"