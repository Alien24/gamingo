from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('zgadnij_liczbe/', include('zgadnij_liczbe.urls')),
    path('kolko_i_krzyzyk/', include('kolko_i_krzyzyk.urls')),
    path('sudoku/', include('sudoku.urls')),
]
