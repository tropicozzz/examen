from django.db import models

# Create your models here.

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=[
        ('Compras', 'Compras'),
        ('Salarios', 'Salarios'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Otros', 'Otros')
    ])

    def __str__(self):
        return self.descripcion
    
class Alimento(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre

class ProductoMenu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    ingredientes = models.ManyToManyField(Alimento, related_name='productos')

    def __str__(self):
        return self.nombre