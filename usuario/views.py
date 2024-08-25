from django.shortcuts import render, redirect
from . form import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth, messages
# Create your views here.
def login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        
        if form.is_valid():
            nome = form['nome'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )
            #Validação
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso')
                return redirect('home')
            else:
                messages.error(request, 'Nome de usuario ou senha incorretas')
                return redirect('login')
            
    return render(request,'usuarios/login.html',{'form':form})

def cadastro(request):

    form = CadastroForm(request.POST or None)
    
    if request.method == 'POST':
        
        if form.is_valid():
            if form.cleaned_data['senha1'] != form.cleaned_data['senha2']:
                messages.error(request, 'Senhas não são iguais')
                return redirect('cadastro')                
            else:
                nome = form.cleaned_data['nome_cadastro']
                email = form.cleaned_data['email']
                senha = form.cleaned_data['senha1']
            
            nome = form['nome_cadastro'].value()
            email = form['email'].value()        
            senha = form['senha1'].value()

            # Validação se o nome ja existe
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuario já existente')
                return redirect('cadastro')
            else:
                usuario = User.objects.create_user(
                    username=nome,
                    email=email,
                    password=senha
                    )
                usuario.save()
                messages.success(request, 'Cadastro efetuado com sucesso')
                return redirect('login')
            
    return render(request,'usuarios/cadastro.html',{'form':form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('login')