from django.shortcuts import render
from django.http import HttpResponse
from Apps.mainCatalogo.models import PublicacionPedal

# Create your views here.
def top(request):
	topPu = PublicacionPedal.objects.all().order_by('-puntuacion')[:10]
	for top in topPu:
		top.puntuacion = round(top.puntuacion,2)
	contexto = {'topPu': topPu}
	return render(request, 'top10/top10.html', contexto)