from django.urls import path
from Apps.login import views

urlpatterns=[
    path('',views.login, name="login")
]