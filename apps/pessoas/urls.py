from django.urls import path

from .views import pessoas , busca

urlpatterns = [
    path('pessoas', pessoas.index, name='index'),
    path('buscar', busca.busca, name='buscar'),
    path('<int:pessoa_id>', pessoas.pessoa, name='pessoa'),
    path('cria/pessoa', pessoas.cria_pessoa, name='cria_pessoa'),
    path('deleta/<int:pessoa_id>',pessoas.deleta_pessoa, name='deleta_pessoa'),
    path('edita/<int:pessoa_id>',pessoas.edita_pessoa, name='edita_pessoa'),
    path('atualiza_pessoa', pessoas.atualiza_pessoa, name='atualiza_pessoa'),
    path('visualizar/<str:nome>', pessoas.visualizar, name='visualizar'),

]