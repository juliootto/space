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



# Create your views here.
def login(request):
    form = LoginForm()    
    return render(request,'usuarios/login.html',{'form':form})

def logout(request):
    return render(request,'usuarios/logout.html')

def cadastrar(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                return redirect ('cadastrar')
        
            nome = form.cleaned_data['nome_cadastro']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha_1']
            
            if User.objects.filter(username=nome).exists():
                return redirect('cadastrar')
            
            usuario = User.objects.create_user(username=nome,email=email,password=senha)
            usuario.save()
            
            return redirect('login')
        else:
            form = CadastroForms()
    return render(request,'usuarios/cadastrar.html',{'form':form})