from django.shortcuts import render
from django.http import HttpResponse
from Apps.mainCatalogo.models import PublicacionPedal

# Create your views here.

def solicitud(request):
    
	solicitud = PublicacionPedal.objects.all()
	contexto = {'solicitudes': solicitud}
	return render (request,'admSolicitudes/admSolicitudes.html',contexto)

