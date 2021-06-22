from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre categoria')
    
    def __str__(self):
        return self.nombreCategoria
    
class Aeronave(models.Model):
    numeroSerie = models.CharField(max_length=8, primary_key=True, verbose_name='Numero serie')
    marca = models.CharField(max_length=20, verbose_name='Marca Aeronave')
    modelo = models.CharField(max_length=20, verbose_name='Modelo de la aeronave')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.numeroSerie
    