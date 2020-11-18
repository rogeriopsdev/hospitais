from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Aqui é o indice</h1>")

def hospital(request):
    return HttpResponse("<h1>Aqui é a área de hospitais</h1>")