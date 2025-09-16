"""
Módulo de visualizações da aplicação Galeria.

Este módulo contém as funções de visualização (views) para a aplicação Galeria,
responsáveis por renderizar as páginas web e interagir com o modelo Fotografia.
"""
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForm
from django.http import request


# Create your views here.
@login_required
def index(request,filtro_categoria=None):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)
    if filtro_categoria:
        fotografias = fotografias.filter(categoria=filtro_categoria)
    return render(request, 'galeria/index.html',{'cards':fotografias})

@login_required
def imagem(request,foto_id):
    fotografia = get_object_or_404(Fotografia,pk=foto_id) 
    return render(request, 'galeria/imagem.html',{'fotografia':fotografia})

@login_required
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

@login_required
def nova_imagem(request):
    form = FotografiaForm() 
    if request.method == 'POST':
        form = FotografiaForm(request.POST,request.FILES) 
        form.usuario = request.user        
        if form.is_valid():
            form.save()
            messages.success(request,'Nova fotografia cadastrada')
            return redirect('index')           
    return render(request,'galeria/nova_imagem.html',{'form':form})

@login_required
def editar_imagem(request,foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForm(instance=fotografia)
    if request.method == 'POST':
        form = FotografiaForm(request.POST,request.FILES,instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request,'Fotografia editada com sucesso')
            return redirect('imagem',foto_id=foto_id)    
    return render(request,'galeria/editar_imagem.html',{'form':form,'foto_id':foto_id})


@login_required
def deletar_imagem(request,foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request,'Fotografia excluída com sucesso')
    return redirect('index') 