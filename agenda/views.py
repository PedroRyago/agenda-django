from django.shortcuts import render, redirect
from .models import Evento

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def listarEventos(request):
    usuario = request.user
    title = 'Agenda'
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos, 'title': title}
    return render(request, 'agenda/listar.html', dados)