from django.shortcuts import render
from django.urls import reverse_lazy
from Apps.mainCatalogo.models import PublicacionPedal
from Apps.publicacion.forms import PublicacionForm
from django.views.generic import CreateView

# Create your views here.
class PublicacionCreate(CreateView):
	model = PublicacionPedal
	form_class = PublicacionForm
	template_name = 'publicacion/registrar_publicacion.html'
	success_url = reverse_lazy('index')

def listar_publicacion(request):
	publicaciones = PublicacionPedal.objects.all().order_by('id')
	contexto = {'publicaciones': publicaciones}
	return render(request, 'publicacion/listar_publicacion.html', contexto)

