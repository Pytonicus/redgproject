from django.db import models

class Genero(models.Model):
    """ Generos de videojuegos """

    genero = models.CharField(max_length=200, verbose_name="Género")

    def __str__(self):
        return self.genero

class Desarrollador(models.Model):
    """ Modelo de desarrolladores """

    nombre = models.CharField(max_length=200, verbose_name="Marca")
    fundacion = models.DateField(verbose_name="Año de Fundación", blank=True)
    logo = models.ImageField(upload_to='retrogames/logos', verbose_name="Logo", blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add = True, verbose_name="Creado el")
    fecha_edicion = models.DateField(auto_now = True, verbose_name="Editado el")

    class Meta:
        verbose_name = "Desarrollador"
        verbose_name_plural = "Desarrolladores"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre