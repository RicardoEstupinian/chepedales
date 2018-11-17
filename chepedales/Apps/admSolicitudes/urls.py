from django.urls import path,re_path
from Apps.admSolicitudes import views
from django.contrib.auth.decorators import login_required
app_name = 'admSolicitudes'
urlpatterns = [
   
	path('solicitud', login_required(views.solicitud), name= "solicitud"),
     
] 