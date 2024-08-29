from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    dados = {
        1: {'nome':'Pilares da criação',
            'legenda':'Webbtelescope.org / NASA / James Webb',
            'tag': 'Formações'},
        2: {'nome':'Galáxia de Andromeda',
            'legenda':'nasa.org / NASA / Hubble',
            'tag':'Galáxias'}
    }
   
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')


# Create your views here.
