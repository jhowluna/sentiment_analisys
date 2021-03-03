from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('video_predict/<int:pessoa_id>', views.video_predict, name='video_predict'),
    path('grafico/<int:pessoa_id>', views.gera_grafico, name='grafico')
]

