from django.shortcuts import render
from django.http import HttpResponse
from Apps.mainCatalogo.models import PublicacionPedal

# Create your views here.

def solicitud(request):
    
	solicitudes = PublicacionPedal.objects.all().filter(evaluada=False)
	contexto = {'solicitudes': solicitudes}
	return render (request,'admSolicitudes/admSolicitudes.html',contexto)

