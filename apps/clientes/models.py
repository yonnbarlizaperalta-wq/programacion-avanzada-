from django.db import models

# 👤 CLIENTE
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


from django.db import models

class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='inmuebles/')

    def __str__(self):
        return self.nombre

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