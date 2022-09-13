from django.urls import path
from .views import listarEventos, evento, submit_evento

urlpatterns = [
    path('', listarEventos, name='agenda'),
    path('evento/', evento, name='evento'),
    path('evento/submit', submit_evento, name='evento'),
]