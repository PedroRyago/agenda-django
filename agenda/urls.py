from django.urls import path
from .views import listarEventos, evento, submit_evento, delete_evento, JsonListaEventos
# , update_evento

urlpatterns = [
    path('', listarEventos, name='agenda'),
    path('lista/<int:id_usuario>', JsonListaEventos, name='lista'),
    path('evento/', evento, name='evento'),
    path('evento/submit', submit_evento, name='evento'),
    path('evento/delete/<int:id_evento>', delete_evento, name='delete_evento'),
    # path('evento/update/<int:id_evento>', update_evento, name='update_evento'),
]