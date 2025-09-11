from django.shortcuts import redirect, render
from usuarios.forms import LoginForm, CadastroForms


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

        if form["senha_1"].value() != form["senha_2"].value():
            return redirect ('cadastro')
    return render(request,'usuarios/cadastrar.html',{'form':form})