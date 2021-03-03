from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from apps.pessoas.models import Pessoa
from django.contrib.auth.models import User
from django.contrib import auth, messages
from  django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def index(request):
    if request.user.is_authenticated:
        id = request.user.id
        pessoas = Pessoa.objects.order_by('-date_pessoa').filter(usuario=id)


        pessoas = Pessoa.objects.order_by('-date_pessoa').filter(usuario=id)
        paginator = Paginator(pessoas, 6)
        page = request.GET.get('page')
        pessoas_por_pagina = paginator.get_page(page)

        dados = {
            'pessoas' : pessoas_por_pagina
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('home')

def pessoa(request, usuario_id):
    pessoa = get_object_or_404(Pessoa, pk=usuario_id)

    pessoas_a_exibir = {
        'pessoa' : pessoa
    }

    return render(request,'pessoas/pessoas.html', pessoas_a_exibir)

def cria_pessoa(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        endereco = request.POST['endereco']
        sexo = request.POST['sexo']
        user = get_object_or_404(User, pk=request.user.id)
        foto_pessoa = request.FILES['foto_pessoa']
        pessoa = Pessoa.objects.create(usuario=user,nome=nome, cpf=cpf, endereco=endereco,sexo=sexo,foto_pessoa = foto_pessoa)
        pessoa.save()
        return redirect('dashboard')
    else:
        return render(request, 'pessoas/cria_pessoa.html')

def deleta_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, pk=pessoa_id )
    pessoa.delete()
    return redirect('dashboard')

def edita_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, pk=pessoa_id)
    pessoa_a_editar = { 'pessoa':pessoa }
    return render(request, 'pessoas/edita_pessoa.html', pessoa_a_editar)

def atualiza_pessoa(request):
    if request.method == 'POST':
        pessoa_id = request.POST['pessoa_id']
        print(pessoa_id)
        r = Pessoa.objects.get(pk=pessoa_id)
        r.nome = request.POST['nome']
        r.cpf = request.POST['cpf']
        r.endereco = request.POST['endereco']
        r.sexo = request.POST['sexo']
        if 'foto_pessoa' in request.FILES:
            r.foto_pessoa = request.FILES['foto_pessoa']
        r.save()
        return redirect('dashboard')

def visualizar(request, nome):
    if request.user.is_authenticated:
        pessoas = Pessoa.objects.order_by('-date_pessoa').filter(nome=nome)
        paginator = Paginator(pessoas, 6)
        page = request.GET.get('page')
        pessoas_por_pagina = paginator.get_page(page)

        dados = {
            'pessoas' : pessoas_por_pagina,
            'pessoa_name': nome
        }
        return render(request, 'usuarios/dashboard_pessoa.html', dados)
    else:
        return redirect('home')

