from django.db import models

# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    imagen = models.ImageField(upload_to='peliculas/', null=True, blank=True)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE, related_name='peliculas')
    precio = models.DecimalField(max_digits=6, decimal_places=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Ticket(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='tickets')
    nombre_cliente = models.CharField(max_length=100)
    correo_cliente = models.EmailField()
    cant_entradas = models.PositiveIntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)
    hora_compra = models.TimeField(auto_now_add=True)
    id_ticket = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Ticket - {self.id_ticket}"