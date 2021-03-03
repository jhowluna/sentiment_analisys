from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . import forms
import sys
import statistics
import pandas as pd
import plotly.express as px
from ..pessoas.models import Pessoa
from datetime import datetime

sys.path.insert(1, 'apps/model/')
import predict


def home(request):
    return render(request, 'pessoas/index.html')

def video_predict(request,pessoa_id):
    r = Pessoa.objects.get(pk=pessoa_id)
    list = predict.video(r.nome)
    r.nome = r.nome
    r.cpf = r.cpf
    r.endereco = r.endereco
    r.sexo = r.sexo
    r.lista_sentimentos = list
    r.save()

    return redirect('dashboard')

def gera_grafico(request,pessoa_id):
    current = datetime.now()
    data = current.strftime("%m-%d-%Y_%H")
    r = Pessoa.objects.get(pk=pessoa_id)
    nome = r.nome
    df = pd.read_csv(f'media/csv/{nome}{data}.csv')
    fig = px.line(df)
    grafico  = f'graficos/{nome}{current.strftime("%m-%d-%Y_%H")}.html'
    fig.write_html(f'templates/{grafico}')
    dados = {
        'pessoa_name': nome,
        'grafico': grafico,
        'data':data
    }
    return render(request, 'hist.html',dados)