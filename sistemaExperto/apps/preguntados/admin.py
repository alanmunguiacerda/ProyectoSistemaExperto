from django.contrib import admin
from apps.preguntados.models import Pregunta, Respuesta

# Register your models here.


class PreguntasAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'tipo',)
    search_fields = ('tipo',)
    fields = ('pregunta', 'tipo', 'respuestas',)
    filter_horizontal = ('respuestas',)
    pass


class RespuestasAdmin(admin.ModelAdmin):
    list_display = ('respuesta', 'lenguaje',)
    search_fields = ('lenguaje',)
    pass

admin.site.register(Pregunta, PreguntasAdmin)
admin.site.register(Respuesta, RespuestasAdmin)