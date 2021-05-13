from django.contrib import admin
from .models import Genero, Desarrollador


class DesarrolladorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fundacion', 'imagen')


    # cargar imagenes en admin:
    def imagen(self, obj):
        return format_html("<img src={} height='75' />", obj.logo.url)

admin.site.register(Genero)
admin.site.register(Desarrollador, DesarrolladorAdmin)
