from django.urls import path
from django.urls import include
from django.contrib.auth.decorators import login_required


#importamos la view
from .views import catalogo 

urlpatterns = [
	path('',catalogo, name= "catalogo_p"),  
    path('<efectoP>/',catalogo, name= "catalogo"), 

]
