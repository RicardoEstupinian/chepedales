from Apps.mainCatalogo.models import PublicacionPedal
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class PublicacionForm(forms.ModelForm):
	class Meta:
		model = PublicacionPedal
		fields = [
			'nombre_pedal',
			'marca',
			'modelo',
			'descripcion_pedal',
			'precio',
			'efecto',
			'fecha_publicacion',
			'autor_publicacion',
			'imgPedal',
			'video',
		]

		labels = {
			'nombrePedal': 'Nombre del pedal',
			'marca': 'Marca',
			'modelo': 'Modelo',
			'descripcion_pedal': 'Descripción',
			'precio': 'Precio',
			'efecto': 'Efecto',
			'fecha_publicacion': 'Fecha de publicación',
			'autor_publicacion': 'Autor de la publicación',
			'imgPedal': 'Imagen del pedal',
			'video': 'Video',
		}

		widgets = {
			'nombrePedal': forms.TextInput(),
			'marca': forms.TextInput(),
			'modelo': forms.TextInput(),
			'descripcion_pedal': forms.Textarea(),
			'precio': forms.TextInput(),
			'efecto': forms.Select(attrs={'class':'form-control'}),
			'fecha_publicacion': forms.DateInput(format='%d/%m/%Y'),
			'autor_publicacion': forms.TextInput(),
		}
