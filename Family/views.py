from django.shortcuts import render
from django.http import HttpResponse
from Family.models import Familiares
from django.template import loader
# Create your views here.

def hermano(self):
    hermano = Familiares(nombre='Jonas', apellido= 'Villarrubia', tipo= 'hermano', edad='46', cumpleanos='1975-05-02')
    #papa.save()
    diccionario = {'hermano': hermano}
    template = loader.get_template('hermano.html')
    doc = template.render(diccionario)
    
    
    return HttpResponse(doc)

def hermana(self):
    hermana = Familiares(nombre='Marisa', apellido= 'Villarrubia', tipo= 'hermana', edad='50', cumpleanos='1970-05-03')
    #mama.save()
    
    diccionario = {'hermana': hermana}
    template = loader.get_template('hermana.html')
    doc = template.render(diccionario)
    
    return HttpResponse(doc)
    
def sobrina(self):
    
    sobrina = Familiares(nombre='Monica', apellido= 'Villarrubia', tipo= 'sobrina', edad='16', cumpleanos='2005-04-12')
    #hija.save()
    
    diccionario = {'sobrina': sobrina}
    template = loader.get_template('sobrina.html')
    doc = template.render(diccionario)
    
    return HttpResponse(doc)