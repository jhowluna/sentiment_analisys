from apps.pessoas.models import Pessoa
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

def busca(request):
    lista_pessoas = Pessoa.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = lista_pessoas.filter(nome__icontains=nome_a_buscar)

    dados = {
        'pessoas' : lista_receitas
    }

    return render(request, 'pessoas/buscar.html', dados)