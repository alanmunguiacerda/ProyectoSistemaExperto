from django.contrib import admin
from apps.lenguajes.models import Lenguaje, Tipo, Paradigma

# Register your models here.


class LenguajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo',)
    search_fields = ('nombre',)
    pass


class TipoAdmin(admin.ModelAdmin):
    list_dispay = ('nombre', 'paradigma',)
    search_fields = ('nombre',)
    pass


class ParadigmaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    pass


admin.site.register(Tipo, TipoAdmin)
admin.site.register(Paradigma, ParadigmaAdmin)
admin.site.register(Lenguaje, LenguajeAdmin)