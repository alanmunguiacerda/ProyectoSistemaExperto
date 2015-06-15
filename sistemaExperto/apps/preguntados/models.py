from django.db import models
from apps.lenguajes.models import Paradigma, Tipo, Lenguaje

# Create your models here.


class Respuesta(models.Model):
    respuesta = models.CharField(max_length=30)
    lenguaje = models.ForeignKey(Lenguaje)

    class Meta:
        ordering = ['lenguaje']
        verbose_name_plural = "Respuestas"

    def __unicode__(self):
        return self.respuesta
        pass
    pass


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tipo)
    respuestas = models.ManyToManyField(Respuesta)

    class Meta:
        ordering = ['tipo']
        verbose_name_plural = "Preguntas"

    def __unicode__(self):
        return self.pregunta
        pass
    pass
