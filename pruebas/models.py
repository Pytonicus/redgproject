from django.db import models
from retrojuegos.models import Videojuego

class Marca(models.Model):
    """ Marca fabricante """

    nombre = models.CharField(max_length=200, verbose_name="Marca")
    fundacion = models.DateField(verbose_name="Año de Fundación", blank=True)
    logo = models.ImageField(upload_to='retrogames/logos', verbose_name="Logo", blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add = True, verbose_name="Creado el")
    fecha_edicion = models.DateField(auto_now = True, verbose_name="Editado el")

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Placa(models.Model):
    """ Placa SBC usada """

    nombre = models.CharField(max_length=200, verbose_name="Modelo placa")
    lanzamiento = models.DateField(verbose_name="Fecha de lanzamiento")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca fabricante")
    foto = models.ImageField(upload_to="pruebas/foto", verbose_name="Foto")
    especificaciones = models.TextField(verbose_name="Especificaciones técnicas")

    fecha_creacion = models.DateTimeField(auto_now_add = True, verbose_name="Creado el")
    fecha_edicion = models.DateField(auto_now = True, verbose_name="Editado el")

    class Meta:
        verbose_name="Placa"
        verbose_name_plural="Placas"
        ordering=["nombre"]

    def __str__(self):
        return self.nombre

class Maquina(models.Model):
    """ Máquina a testear """

    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    lanzamiento = models.DateField(verbose_name="Fecha de lanzamiento")
    foto = models.ImageField(upload_to="pruebas/foto", verbose_name="Foto")
    fabricante = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Fabricante")
    especificaciones = models.TextField(verbose_name="Especificaciones técnicas")

    fecha_creacion = models.DateTimeField(auto_now_add = True, verbose_name="Creado el")
    fecha_edicion = models.DateField(auto_now = True, verbose_name="Editado el")

    class Meta:
        verbose_name="Máquina"
        verbose_name_plural="Máquinas"
        ordering=["nombre"]

    def __str__(self):
        return self.nombre

class Emulador(models.Model):
    """ Emulador a testear """

    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    lanzamiento = models.DateField(verbose_name="Fecha de lanzamiento")
    logo = models.ImageField(upload_to="pruebas/logos", verbose_name="Logo")
    
    fecha_creacion = models.DateTimeField(auto_now_add = True, verbose_name="Creado el")
    fecha_edicion = models.DateField(auto_now = True, verbose_name="Editado el")

    class Meta:
        verbose_name="Emulador"
        verbose_name_plural="Emuladores"
        ordering=["nombre"]

    def __str__(self):
        return self.nombre


class SO(models.Model):
    """ Modelo de sistemas operativos """

    nombre = models.CharField(max_length=200, verbose_name="Sistema")
    version = models.CharField(max_length=100, verbose_name="Versión", blank=True)
    logo = models.ImageField(upload_to="pruebas/so", verbose_name="Logotipo", blank=True)
    descarga = models.URLField(verbose_name="Link de descarga", blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add = True, verbose_name="Creado el")
    fecha_edicion = models.DateField(auto_now = True, verbose_name="Editado el")

    class Meta:
        verbose_name="Sistema Operativo"
        verbose_name_plural="Sistemas operativos"
        ordering=["nombre"]

    def __str__(self):
        return self.nombre

class Prueba(models.Model):
    """ Pruebas realizadas a máquinas con distintos emuladores """

    titulo = models.ForeignKey(Videojuego, on_delete=models.CASCADE, verbose_name="Juego")
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, verbose_name="Máquina")
    placa = models.ForeignKey(Placa, on_delete=models.CASCADE, verbose_name="Placa SBC")
    so = models.ForeignKey(SO, on_delete=models.CASCADE, verbose_name="Sistema operativo", blank=True, null=True)
    emulador = models.ForeignKey(Emulador, on_delete=models.CASCADE, verbose_name="Emulador")
    preferente = models.BooleanField(verbose_name="Mejor Emulador")
    observaciones = models.CharField(max_length=200, verbose_name="Observaciones", blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add = True, verbose_name="Creado el")
    fecha_edicion = models.DateField(auto_now = True, verbose_name="Editado el")

    class Meta:
        verbose_name="Prueba de rendimiento"
        verbose_name_plural="Pruebas de rendimiento"
        ordering=["titulo"]

    def __str__(self):
        return str(self.id)