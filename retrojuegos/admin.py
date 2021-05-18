from django.contrib import admin
from .models import Sistema, Fabricante, Videojuego
from django.utils.html import format_html


class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fundacion', 'imagen')

    # cargar imagenes en admin:
    def imagen(self, obj):
        return format_html("<img src={} height='75' />", obj.logo.url)

class SistemaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fabricante', 'fecha_lanzamiento', 'generacion', 'marca', 'videoconsola', 'miniatura')

    list_filter = ('fabricante', 'fecha_lanzamiento', 'generacion')

    # cargar imagenes en admin:
    def marca(self, obj):
        return format_html("<img src={} height='75' />", obj.logo.url)

    def videoconsola(self, obj):
        return format_html("<img src={} height='75' />", obj.consola.url)

    def miniatura(self, obj):
        return format_html("<img src={} height='75' />", obj.icono.url)

class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sistema', 'lanzamiento', 'genero', 'desarrollador', 'jugadores','valoracion', 'caratula')

    list_filter = ('genero', 'desarrollador', 'jugadores', 'valoracion')

    # cargar imagenes en admin:
    def caratula(self, obj):
        try:
            result = format_html("<img src={} height='75' />", obj.caja.url)
        except:
            result = obj.caja
        return result
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Sistema, SistemaAdmin)
admin.site.register(Videojuego, VideojuegoAdmin)


    