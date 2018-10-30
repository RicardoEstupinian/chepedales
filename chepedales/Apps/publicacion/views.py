from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from Apps.mainCatalogo.models import PublicacionPedal, Efecto
from Apps.publicacion.forms import PublicacionForm
from django.views.generic import CreateView, ListView
from django.http import HttpResponse, HttpResponseRedirect

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

class MostrarPublicacion(ListView):
	model = PublicacionPedal
	template_name = 'publicacion/mostrar_publicacion.html'

	def post(self, request, *args, **kwargs):
		publicacion = PublicacionPedal.objects.get(id=self.kwargs['pk'])

		if 'btnAprobar' in request.POST:
			publicacion.aprobada = True
			publicacion.save()
			return HttpResponseRedirect(reverse('index'))

		if 'btnRechazar' in request.POST:
			publicacion.delete()
			return HttpResponseRedirect(reverse('index'))

		try:
			valor=float(request.POST.get('puntuacion'))
		except:
			return render(request, 'publicacion/mostrar_publicacion.html', {'publicacion': publicacion, 'error_message': 'vaya, hubo un error'})
		else:
			publicacion.puntuacion +=valor
			publicacion.save()

			return HttpResponseRedirect(reverse('index')) #Redireccionará a la pagina del top 10

	def get_context_data(self, **kwargs):
		context = super(MostrarPublicacion, self).get_context_data(**kwargs)
		o_publicacion = PublicacionPedal.objects.get(id=self.kwargs['pk'])

		context["o_publicacion"] = o_publicacion
		return context
