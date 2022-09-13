from django.urls import path
from .views import listarEventos

urlpatterns = [
    path('', listarEventos, name='agenda'),
]