from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages


def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
        
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            usuario = auth.authenticate(
                request,
                username = nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, 'Login realizado com sucesso')
                
                return redirect('index')
                
            else:
                messages.error(request, 'erro ao efetuar Login')
                return redirect('login')    
            



    return render(request, 'usuarios/login.html', {'form': form})
    


def cadastro(request):
    form = CadastroForms()

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível inserir espaços dentro do campo usuário")
            else:
                return nome

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request, 'As senhas não são iguais')
                return redirect('cadastro')
        nome= form['nome_cadastro'].value()
        email= form['email'].value()
        senha = form['senha_1'].value()

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Nome de usuário já em uso')
            return redirect('cadastro')
        
        usuario = User.objects.create_user(
            username=nome,
            email=email,
            password=senha
        )

        usuario.save()
        messages.success(request, 'Usuário autenticado')
        return redirect('login')
    





    return render(request, 'usuarios/cadastro.html', {'form':form})




def logout(request):
    auth.logout(request)
    messages.success(request, 'Usuário desconectado')
    return redirect('login')
