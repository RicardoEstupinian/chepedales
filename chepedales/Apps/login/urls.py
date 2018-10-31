from django.urls import path
from Apps.login import views
from django.contrib.auth.views import login

urlpatterns=[
    path('accounts/login/',login,{'template_name':'login/login.html'}, name="login"),
]