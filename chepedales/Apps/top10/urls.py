from django.conf.urls import url, include
from Apps.top10 import views
from Apps.top10.views import top
from django.urls import path

urlpatterns=[
    path('top/', views.top, name="top"),
]