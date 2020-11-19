from django.shortcuts import render
from django.http import HttpResponse
from .forms import Hospitalform
from .models import Hospital


# Create your views here.


def index(request):
    #return HttpResponse("<h1>Aqui é o indice</h1>")
    return render(request, 'hospitais/index.html')


def hospitais(request):
    #return HttpResponse("<h1>Aqui é a área de hospitais</h1>")
    hospitais = Hospital.objects.all()
    return render(request, 'hospitais/hospitais.html', {'hospitais':hospitais})


def criar_hospital (request):
	form = Hospitalform(request.POST)
	if request.method == "POST":
		form = Hospitalform(request.POST, request.FILES)
		if form.is_valid():
			hosp = form.save()
			hosp.save()
			form =Hospitalform()
	return render(request, 'hospitais/criar_hospitais.html',{'form':form})



