from django.urls import path
from . import views

urlpatterns = [
    path('', views.kolko_i_krzyzyk, name='kolko_i_krzyzyk'),
]
