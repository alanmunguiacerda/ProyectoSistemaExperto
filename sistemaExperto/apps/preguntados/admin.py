from django.contrib import admin
from apps.preguntados.models import Pregunta, Respuesta

# Register your models here.


class PreguntasAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'paradigma',)
    search_fields = ('paradigma',)
    pass


class RespuestasAdmin(admin.ModelAdmin):
    list_display = ('respuesta', 'pregunta', 'lenguaje',)
    search_fields = ('lenguaje',)
    pass

admin.site.register(Pregunta, PreguntasAdmin)
admin.site.register(Respuesta, RespuestasAdmin)