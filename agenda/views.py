from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse
from django.contrib.auth.models import User
# Create your views here.

# def index(request):
#     return redirect('/agenda/')

@login_required(login_url='/login/')
def listarEventos(request):
    data_atual = datetime.now() - timedelta(hours=1)
    usuario = request.user
    title = 'Agenda'
    eventos = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual)
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

@login_required(login_url='/login/')
def evento(request):
    if request.GET.get('id'):
        id_evento = request.GET.get('id')
        if id_evento:
            title = 'Editar evento'
            evento = Evento.objects.get(id=id_evento)
            dados = {'evento': evento, 'title': title}
            return render(request, 'agenda/evento.html', dados)
    else:
        dados = {'title': 'Novo evento'}
        return render(request, 'agenda/evento.html', dados)


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        id_evento = request.POST.get('id')
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.save()
            # Evento.objects.filter(id=id_evento).update(titulo=titulo, data_evento=data_evento, descricao=descricao)
        else:
            Evento.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
        if usuario == evento.usuario:
            evento.delete()
        else:
            messages.error(request, 'Você não tem permissão para excluir este evento.')
    except Exception:
        raise Http404()
    return redirect('/')

# @login_required(login_url='/login/')
def JsonListaEventos(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    eventos = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(eventos), safe=False)

# def update_evento(request, id_evento):
#     usuario = request.user
#     try:
#         evento = Evento.objects.get(id=id_evento)
#         if usuario == evento.usuario:
#             dados = {'evento': evento}
#             return render(request, 'agenda/update_evento.html', dados)
#         else:
#             messages.error(request, 'Você não tem permissão para editar este evento.')
#     except Exception:
#         messages.error(request, 'Evento não encontrado.')
#     return redirect('/')