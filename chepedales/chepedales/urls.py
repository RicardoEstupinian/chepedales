"""chepedales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from chepedales import views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/',include('Apps.mainCatalogo.urls')),
    path('publicacion/', include(('Apps.publicacion.urls', 'publicacion'), namespace='publicacion')),
    
    path('administracion/',include('Apps.admSolicitudes.urls')),
     path('top/',include('Apps.top10.urls')),
    path('', include('Apps.login.urls','registro'),name='registro'),
    path('logout/',logout_then_login,name='logout'),
    path('Favoritos/', include('Apps.top10.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)