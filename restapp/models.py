from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey('Autor', related_name='libros')
    anio = models.IntegerField()

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre