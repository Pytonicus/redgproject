from django.db import models
from general.models import Genero, Desarrollador

class Fabricante(models.Model):
    """ Fabricante de sistemas """

    nombre = models.CharField(max_length=200, verbose_name="Marca")
    fundacion = models.DateField(verbose_name="Año de Fundación", blank=True)
    logo = models.ImageField(upload_to='pruebas/logos', verbose_name="Logo", blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add = True, verbose_name="Creado el")
    fecha_edicion = models.DateField(auto_now = True, verbose_name="Editado el")

    class Meta:
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Sistema(models.Model):
    """ Modelo de Sistemas """

    GENERACION = [
        ('1', '1ª Generación'),
        ('2', '2ª Generación'),
        ('3', '3ª Generación'),
        ('4', '4ª Generación'),
        ('5', '5ª Generación'),
        ('6', '6ª Generación'),
        ('7', '7ª Generación'),
        ('8', '8ª Generación')
    ]

    nombre = models.CharField(max_length=200, verbose_name="Sistema")
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, verbose_name="Fabricante")
    fecha_lanzamiento = models.DateField(verbose_name="Fecha de lanzamiento", blank=True)
    generacion = models.CharField(max_length=200, choices=GENERACION, verbose_name="Generación")
    logo = models.ImageField(upload_to='retrogames/logos', verbose_name="Logo", blank=True)
    consola = models.ImageField(upload_to='retrogames/consolas', verbose_name="Consola", blank=True)
    icono = models.ImageField(upload_to='retrogames/iconos', verbose_name="Icono", blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add = True, verbose_name="Creado el")
    fecha_edicion = models.DateField(auto_now = True, verbose_name="Editado el")

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    """ Modelo de videojuego retro """

    JUGADORES = [
        ('1','1'),
        ('2','2'),
        ('3', '3'),
        ('4', '4')
    ]

    nombre = models.CharField(max_length=200, verbose_name="Título")
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, verbose_name="Sistema")
    lanzamiento = models.DateField(verbose_name="Fecha de lanzamiento", blank=True, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Género", blank=True, null=True)
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE, verbose_name="Desarrollador", blank=True, null=True)
    jugadores = models.CharField(max_length=20, choices=JUGADORES, verbose_name="Nº de Jugadores", blank=True, null=True)
    valoracion = models.FloatField(verbose_name="Valoración", blank=True, null=True)
    favorito = models.BooleanField(verbose_name="Juego favorito")
    caja = models.ImageField(upload_to='retrogames/portadas', verbose_name="Portada", blank=True)
    video = models.FileField(upload_to='retrogames/videosnaps', verbose_name="Video preview", blank=True)
    descripcion = models.TextField(verbose_name="Descripción", blank=True)
    descarga = models.URLField(verbose_name="Link de descarga", blank=True, null=True)

    class Meta:
        verbose_name="Videojuego retro"
        verbose_name_plural="Videojuegos retro"
        ordering=["nombre"]

    def __str__(self):
        return self.nombre