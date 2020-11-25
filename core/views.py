from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import DigitalPessoa

from matplotlib import pyplot as plt
import numpy as np
import mahotas as mah
import cv2
from PIL import Image
from io import BytesIO


# Create your views here.

def login_user(request):                 
    return render(request,'login.html')  


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Usuario e senha invalido. Favor tentar novamente')
    return redirect('/login/')



@login_required(login_url='/login/')
def list_all_digitais(request):
    digital = DigitalPessoa.objects.filter(active=True) 
    #print (digital.query) #teste
    return render(request,'list.html',{'digital':digital})


@login_required(login_url='/login/')
def list_user_digitais(request):
    digital = DigitalPessoa.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'digital': digital})


def logout_user(request):
    #print(request.user) #teste saber quem esta logado
    logout(request)
    return redirect('/login')
        

@login_required(login_url='/login/')
def registro_digital(request):
    digital_id = request.GET.get('id')
    if digital_id:
        digital = DigitalPessoa.objects.get(id=digital_id)
        if digital.user == request.user:
            print(digital.nome)
            return render(request, 'registro-digital.html', {'digital':digital})
    return render(request, 'registro-digital.html')    
  

@login_required(login_url='/login/')
def set_digital(request): # cadastra digitais
    nome = request.POST.get('nome')
    foto_impress_dig = request.FILES.get('file')
    digital_id = request.POST.get('digital-id')
    user = request.user
    if digital_id:
        digital = DigitalPessoa.objects.get(id=digital_id)
    else:
        digital = DigitalPessoa.objects.create(nome=nome,foto_impress_dig=foto_impress_dig,user=user)
    url = '/digital/detalhe/{}/'.format(digital.id)
    return redirect(url)


def digital_detalhe(request, id):
    digital = DigitalPessoa.objects.get(active=True, id=id)
    print(digital.id) #teste saber usuario
    return render(request, 'digital.html', {'digital':digital})


@login_required(login_url='/login/')
def exclui_digital(request, id):
    digital = DigitalPessoa.objects.get(id=id)
    if digital.user == request.user:
        digital.delete()
    return redirect('/') #redireciona pagina principal


def filtro_digital(request, id):
    digital = DigitalPessoa.objects.get(active=True, id=id)
    pass

