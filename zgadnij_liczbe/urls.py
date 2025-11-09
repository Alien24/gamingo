from django.urls import path
from . import views

urlpatterns = [
    path('', views.zgadnij_liczbe, name='zgadnij_liczbe'),
]
