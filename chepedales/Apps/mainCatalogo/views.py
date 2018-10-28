from django.shortcuts import render
from django.http import HttpResponse
from Apps.mainCatalogo.models import Efecto, PublicacionPedal
from django.shortcuts import redirect

# Create your views here.

def catalogo(request, efectoP='Distorsion'):
	if efectoP == 'Distorsion':
		activo = ['actives','','','','','','','']
	if efectoP == 'Delay':
		activo = ['','actives','','','','','','']
	if efectoP == 'Overdrive':
		activo = ['','','actives','','','','','']
	if efectoP == 'Reverb':
		activo = ['','','','actives','','','','']
	if efectoP == 'Phaser':
		activo = ['','','','','actives','','','']
	if efectoP == 'Flanger':
		activo = ['','','','','','actives','','']
	if efectoP == 'Wah':
		activo = ['','','','','','','actives','']
	if efectoP == 'Chorus':
		activo = ['','','','','','','','actives']

	efecto_obj = Efecto.objects.filter(nombre_efecto = efectoP)
	hay_pedales = PublicacionPedal.objects.filter(efecto= efecto_obj[0]).exists()
	if hay_pedales: 
		pedales = PublicacionPedal.objects.filter(efecto= efecto_obj[0])
	else:
		pedales = ''
	if request.method=='POST':
		return redirect('catalogo',efectoP = efectoP)

	contexto = {
	'hay_pedales':hay_pedales,
	'efecto': efectoP,
	'activo' : activo,
	'pedales' : pedales,
	}
	return render (request, 'catalogoTemplate/catalogoTemplate.html', contexto)