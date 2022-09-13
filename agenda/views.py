from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# def index(request):
#     return redirect('/agenda/')

@login_required(login_url='/login/')
def listarEventos(request):
    usuario = request.user
    title = 'Agenda'
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos, 'title': title}
    return render(request, 'agenda/listar.html', dados)

def user_login(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    return redirect('/')

def user_logout(request):
    logout(request)
    return redirect('/')