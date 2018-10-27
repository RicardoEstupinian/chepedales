from django.db import models


# Create your models here.

class Efecto(models.Model):
	nombre_efecto = models.CharField(max_length=50)
	descripcion_efecto = models.CharField(max_length=500)

	def __str__(self):
		return self.nombre_efecto

class PublicacionPedal(models.Model):
	efecto = models.ForeignKey(Efecto, null=True, blank=True, on_delete=models.PROTECT)
	nombre_pedal = models.CharField(max_length=50)
	marca = models.CharField(max_length=50)
	modelo = models.CharField(max_length=50)
	descripcion_pedal = models.CharField(max_length=1000)
	precio = models.FloatField()
	imgPedal = models.ImageField(upload_to='static/img', blank=True)
	urlVideo = models.CharField(max_length=50)
	puntuacion = models.FloatField()
	fecha_publicacion = models.DateField()
	autor_publicacion = models.CharField(max_length=50)
	evaluada = models.BooleanField(default=False)
	aprobada = models.BooleanField(default=False)

	def __str__(self):
		return self.nombre_pedal




