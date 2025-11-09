from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.zgadnij_liczbe, name='zgadnij_liczbe'),
    path('', views.kolko_i_krzyzyk, name='kolko_i_krzyzyk'),
]
