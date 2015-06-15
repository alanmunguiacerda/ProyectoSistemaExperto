# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from apps.lenguajes.models import Lenguaje, Tipo, Paradigma
from apps.preguntados.models import Pregunta, Respuesta


def landing(request, urlInfo):
    q = request.GET.get('q', "")
    p = request.GET.getlist('p', "")
    if q == "" and p == "":
        template_name = 'indexParadigmas.html'
        nombre = "Selecciona un paradigma"
        datos = Paradigma.objects.all()
        return render(request, template_name, locals())
    elif p == "":
        template_name = 'indexTipos.html'
        datosPregunta = Pregunta.objects.get(paradigma=q)  # lint:ok
        datos = Respuesta.objects.filter(pregunta=datosPregunta)
        return render(request, template_name, locals())
    else:
        template_name = 'indexLenguajes.html'
        nombre = "Lenguaje(s) sugeridos"  # lint:ok
        busqueda = list()
        datos = Lenguaje.objects.all()
        for i in p:
            if i != "&" and i != "p" and i != "=":
                busqueda.append(i)
                datos = datos.filter(tipos=i)  # lint:ok
        return render(request, template_name, locals())