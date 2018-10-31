from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from Apps.login.forms import Registrar

# Create your views here.


def login(request):
    return render(request, 'login/login.html')


class registro(CreateView):
    model = User
    template_name = 'login/login.html'
    form_class = Registrar
    success_url = reverse_lazy('publicacion:publicacion_registrar')

