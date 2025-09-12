"""
Módulo de views para gerenciar autenticação de usuários.

Este módulo contém as funções de view para:
- `login`: Exibe o formulário de login e processa a autenticação do usuário.
- `logout`: Realiza o logout do usuário.
- `cadastrar`: Exibe o formulário de cadastro e processa o registro de novos usuários.
"""
from django.shortcuts import redirect, render
from usuarios.forms import LoginForm, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth,messages

# Create your views here.
def login(request):
    form = LoginForm() 
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome_login']
            senha = form.cleaned_data['senha']
            usuario = auth.authenticate(request,username=nome,password=senha)
            if usuario is not None:
                auth.login(request,usuario)
                messages.success(request,'Login realizado com sucesso!')
                return redirect('index')
            else:
                messages.error(request,'Erro ao efetuar login')
                return redirect('login')
               
    return render(request,'usuarios/login.html',{'form':form})

def logout(request):
    if auth.get_user(request).is_authenticated:
        auth.logout(request)
        messages.success(request,'Logout realizado com sucesso!')
    return redirect('login')

def cadastrar(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():   
        
            nome = form.cleaned_data['nome_cadastro']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha_1']
            
            if User.objects.filter(username=nome).exists():
                messages.error(request,'Usuário já cadastrado') 
                return render(request,'usuarios/cadastrar.html',{'form':form})
            
            usuario = User.objects.create_user(username=nome,email=email,password=senha)
            usuario.save()
            messages.success(request,'Usuário cadastrado com sucesso')
            return redirect('login')
        else:
            messages.error(request,'Erro ao cadastrar usuário')
            return render(request,'usuarios/cadastrar.html',{'form':form}) 
    return render(request,'usuarios/cadastrar.html',{'form':form})