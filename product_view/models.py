from django.db import models
from django.utils import timezone

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name='Nombre del producto')
    descripcion = models.TextField(verbose_name='Descripción del producto')
    condiciones = models.TextField(verbose_name='Condiciones del producto', null=True, blank=True)
    precio = models.PositiveIntegerField(verbose_name='Precio del producto')
    creado = models.DateTimeField(default=timezone.now, verbose_name='Fecha de creación')

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

class Subcatalogo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name='Nombre del subcatálogo')
    descripcion = models.TextField(verbose_name='Descripción del subcatálogo')
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'subcatalogos'
        verbose_name = 'Subcatálogo'
        verbose_name_plural = 'Subcatálogos'
        ordering = ['nombre']

class Catalogo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    subcatalogos = models.ManyToManyField(Subcatalogo)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'catalogos'
        verbose_name = 'Catálogo'
        verbose_name_plural = 'Catálogos'
        ordering = ['nombre']