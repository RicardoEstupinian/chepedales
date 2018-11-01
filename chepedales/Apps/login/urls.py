from django.urls import path
from Apps.login import views
from django.contrib.auth.views import login
from Apps.login.views import registro

app_name= "registro"

urlpatterns=[
    path('accounts/login/',login,{'template_name':'login/login.html'}, name="login"),
    path('registro/',registro.as_view(), name="registro_usuario"),
]