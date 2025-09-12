"""
Módulo de visualizações da aplicação Galeria.

Este módulo contém as funções de visualização (views) para a aplicação Galeria,
responsáveis por renderizar as páginas web e interagir com o modelo Fotografia.
"""
from django.shortcuts import render,get_object_or_404,redirect
from galeria.models import Fotografia
from django.contrib import messages

# Create your views here.
def index(request,filtro_categoria=None):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)
    if filtro_categoria:
        fotografias = fotografias.filter(categoria=filtro_categoria)
    return render(request, 'galeria/index.html',{'cards':fotografias})

def imagem(request,foto_id):
    fotografia = get_object_or_404(Fotografia,pk=foto_id) 
    return render(request, 'galeria/imagem.html',{'fotografia':fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar: 
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria/index.html',{'cards':fotografias})