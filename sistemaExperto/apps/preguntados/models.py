from django.db import models
from apps.lenguajes.models import Paradigma, Tipo

# Create your models here.


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=200)
    paradigma = models.ForeignKey(Paradigma)

    class Meta:
        ordering = ['paradigma']
        verbose_name_plural = "Preguntas"

    def __unicode__(self):
        return self.pregunta
        pass
    pass


class Respuesta(models.Model):
    respuesta = models.CharField(max_length=30)
    pregunta = models.ForeignKey(Pregunta)
    lenguaje = models.ForeignKey(Tipo)

    class Meta:
        ordering = ['pregunta']
        verbose_name_plural = "Respuestas"

    def __unicode__(self):
        return self.respuesta
        pass
    pass