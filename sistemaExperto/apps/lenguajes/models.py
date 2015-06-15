from django.db import models


class Paradigma(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Paradigmas"

    def __unicode__(self):
        return self.nombre
        pass

    pass


class Tipo(models.Model):
    nombre = models.CharField(max_length=30)
    paradigma = models.ForeignKey(Paradigma)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Tipos"

    def __unicode__(self):
        return self.nombre
        pass
    pass


class Lenguaje(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.ForeignKey(Tipo)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Lenguajes"

    def __unicode__(self):
        return self.nombre
        pass
    pass

