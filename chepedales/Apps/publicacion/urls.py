from django.urls import path
from Apps.publicacion import views
from django.contrib.auth.decorators import login_required

app_name = "publicacion"

urlpatterns = [
	path('registrar/', login_required(views.PublicacionCreate.as_view()), name="publicacion_registrar"),
	path('listar/', (views.listar_publicacion), name="listar_publicacion"),
	path('mostrar/<pk>/', (views.MostrarPublicacion.as_view()), name="mostrar_publicacion"),
]
