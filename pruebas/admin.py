from django.contrib import admin
from .models import Maquina, Emulador, Prueba, Marca, Placa, SO
# se importa el formateador html:
from django.utils.html import format_html
    

class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lanzamiento', 'imagen', 'fabricante')

    list_filter = ('fabricante', )

    # cargar imagenes en admin:
    def imagen(self, obj):
        return format_html("<img src={} height='75' />", obj.foto.url)

class EmuladorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lanzamiento', 'imagen')

    # cargar imagenes en admin:
    def imagen(self, obj):
        return format_html("<img src={} height='75' />", obj.logo.url)

class PruebaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'maquina', 'placa', 'so', 'emulador', 'observaciones')


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fundacion', 'imagen')

    # cargar imagenes en admin:
    def imagen(self, obj):
        return format_html("<img src={} height='75' />", obj.logo.url)

class PlacaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lanzamiento', 'marca', 'imagen')

    # cargar imagenes en admin:
    def imagen(self, obj):
        return format_html("<img src={} height='75' />", obj.foto.url)

class SOAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'version', 'logotipo')

    def logotipo(self, obj):
        return format_html("<img src={} height='75' />", obj.logo.url)

admin.site.register(Maquina, MaquinaAdmin)
admin.site.register(Emulador, EmuladorAdmin)
admin.site.register(Prueba, PruebaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Placa, PlacaAdmin)
admin.site.register(SO, SOAdmin)