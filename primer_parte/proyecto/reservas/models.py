from django.db import models

class ActividadTuristica(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    actividad = models.ForeignKey(ActividadTuristica, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    fecha_reserva = models.DateField()
    personas = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_cliente} - {self.actividad.nombre}"
