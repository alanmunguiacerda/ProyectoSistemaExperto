# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from apps.lenguajes.models import Lenguaje, Tipo, Paradigma


def landing(request, urlInfo, urlInfo2, urlInfo3):
    if urlInfo == "":
        template_name = 'indexParadigmas.html'
        nombre = "Selecciona un paradigma"
        datos = Paradigma.objects.all()
        return render(request, template_name, locals())
    elif urlInfo3 == "":
        template_name = 'indexTipos.html'
        nombre = "Selecciona un tipo"
        datos = Tipo.objects.filter(paradigma=urlInfo)
        return render(request, template_name, locals())
    else:
        template_name = 'indexLenguajes.html'
        nombre = "Lenguaje(s) sugeridos"  # lint:ok
        datos = Lenguaje.objects.filter(tipo=urlInfo3)  # lint:ok
        return render(request, template_name, locals())
