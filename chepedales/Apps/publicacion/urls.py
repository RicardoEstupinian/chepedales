from django.urls import path
from Apps.publicacion import views

app_name = "publicacion"

urlpatterns = [
	path('registrar/', views.PublicacionCreate.as_view(), name="publicacion_registrar"),
	path('listar/', views.listar_publicacion, name="listar_publicacion")
]