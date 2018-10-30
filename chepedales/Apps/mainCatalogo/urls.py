from django.urls import path
from django.urls import include


#importamos la view
from .views import catalogo 

urlpatterns = [
	path('',catalogo, name= "catalogo_p"),  
    path('<efectoP>/',catalogo, name= "catalogo"), 

]
