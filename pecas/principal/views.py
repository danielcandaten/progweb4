from django.http import HttpResponse
from django.shortcuts import render
from .models import Produto, Fornecedor
from .forms import FormLogin, FormProduto
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    lista_produtos = Produto.objects.all()
    lista_fornecedores = Fornecedor.objects.all()
    contexto = {'lista_produtos': lista_produtos, 'lista_fornecedores': lista_fornecedores }
    return render(request, 'principal/index.html', contexto)

###excluir
def excluir(request, id):
    if request.user.is_authenticated:
       if request.user.is_superuser:   
         p = Produto.objects.get(id=id)
         p.delete()
       else: 
            return HttpResponse('sem permissao')
    else: 
         return HttpResponse('Seu usuario malandrinho')
    return HttpResponseRedirect('/principal/')


### LOGIN	
def fazer_login(request):
    
    if request.method == 'POST':
       form = FormLogin(request.POST)
       if form.is_valid(): 
          ### FAZ LOGIN 
          nome_usuario = form.cleaned_data['username']
          senha = form.cleaned_data['password']
          usuario = authenticate(request, username=nome_usuario, password=senha)
          if usuario is not None:
             login(request, usuario)
             # Redireciona para uma página de sucesso ou para a página inicial.
             return HttpResponseRedirect('/principal/')
          else:
             # Recarrega a view de login exibindo uma mensagem de erro 
             return HttpResponseRedirect('/principal/fazer_login/')
          return HttpResponseRedirect('/principal/') 
    else:
       form = FormLogin() 

    contexto = {"form": form}
    return render(request, 'principal/login.html', contexto)

### LOGOUT	
def fazer_logout(request):
    logout(request)
    return HttpResponseRedirect('/principal/') 

### Novo Produto
def novo_produto(request):
    
    if request.method == 'POST':
       form = FormProduto(request.POST) #form Produto
       if form.is_valid():
           
          ### Salva a mensagem 
          p = Produto()
          p.nome_produto = form.cleaned_data['nome_produto']
          p.aplicacao = form.cleaned_data['aplicacao']
          p.usuario = request.user
          p.fornecedor = form.cleaned_data['nome_fornecedor']
          p.save()

          return HttpResponseRedirect('/principal/') 
    else:
       form = FormProduto()

    contexto = {"form": form}
    return render(request, 'principal/novo_produto.html', contexto)


