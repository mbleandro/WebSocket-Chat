# coding: utf-8
from django.contrib.auth.models import User
from core.models import Atendimento, Group, Usuario
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, todo_svc, globalsettings_svc
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from random import random


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = Usuario.objects.get(id=user.id).to_dict_json()
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated else {'authenticated': False}
    return JsonResponse(i_am)


def settings(request):
    le_settings = globalsettings_svc.list_settings()
    return JsonResponse(le_settings)

@ajax_login_required
def add_todo(request):
    todo = todo_svc.add_todo(request.POST['new_task'])
    return JsonResponse(todo)


@ajax_login_required
def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({'todos': todos})


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d


def list_atendimento_messages(request):
    loggeduser = request.user if request.user.is_authenticated else None
    usuario = Usuario.objects.get(id=loggeduser.id)
    if usuario.is_atendente:
        atendimento = Atendimento.objects.filter(atendente_id=loggeduser.id, ativo=True).first()
        if not atendimento:
            response = {
                'error': "Você ainda não possui um atendimento"
            }
    else:
        try:
            atendimento = Atendimento.objects.get(atendido_id=loggeduser.id, ativo=True)
        except Atendimento.DoesNotExist:
            atendimento = _inicia_atendimento(usuario)
    if atendimento:
        response = {
            'messages': [m.to_dict_json() for m in list(atendimento.atendimentomessage_set.all())],
            'link': atendimento.link,
            'id': atendimento.id
        }
    else:
        response = {
            'error': "Você ainda não possui um atendimento" if usuario.is_atendente else "Nenhum atendente disponível no momento! :<("
        }
        
    return JsonResponse(response, safe=False)


@ajax_login_required
def list_group_messages(request):
    group_id = 1
    grupo = Group.objects.get(id=group_id)
    response = {
        'messages': [m.to_dict_json() for m in list(grupo.groupmessage_set.all())],
        'link': grupo.link
    }
    return JsonResponse(response, safe=False)


def _inicia_atendimento(usuario):
    atendente = Usuario.objects.filter(is_atendente=True, disponivel=True).first()
    response = None
    if atendente:
        url = f'ws://localhost:8000/ws/chat/{atendente.id}{usuario.id}id{int(1000*random())}/'
        atendimento = Atendimento.objects.create(atendido=usuario, atendente=atendente, link=url)
        atendente.disponivel = False
        atendente.save()
        response = atendimento
    # else:
    #     response = {'error': 'Nenhum atendente disponível no momento! :<('}
    return response



@ajax_login_required
def encerra_atendimento(request):
    atendimento_id = request.POST.get('atendimento_id')
    atendimento = Atendimento.objects.get(id=atendimento_id)
    atendimento.ativo = False
    atendimento.atendente.disponivel = True
    atendimento.atendente.save()
    atendimento.save()
    return JsonResponse(True, safe=False)


@ajax_login_required
def change_user_mode(request):
    loggeduser = request.user if request.user.is_authenticated else None
    usuario = Usuario.objects.get(id=loggeduser.id)
    change_to = request.POST['change_to']
    if change_to == 'CLIENTE':
        usuario.is_atendente = False
        usuario.disponivel = False
    else:
        usuario.is_atendente = True
        atendimento = Atendimento.objects.filter(atendente_id=loggeduser.id, ativo=True)
        usuario.disponivel = False if atendimento else True
    usuario.save()
    return JsonResponse(usuario.to_dict_json(), safe=False)


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d


def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
