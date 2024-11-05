from django.urls import path
from persona.views import ListarPersonagens, FotoPersonagem, CriarPersonagens, EditarPersonagens, DeletarPersonagens, APIListarPersonagens

urlpatterns = [
    path('', ListarPersonagens.as_view(), name='listar-personagens'),
    path('novo/', CriarPersonagens.as_view(), name='criar-personagens'),
    path('fotos/<str:arquivo>/', FotoPersonagem.as_view(), name='foto-personagem'),
    path('<int:pk>/', EditarPersonagens.as_view(), name='editar-personagens'),
    path('deletar/<int:pk>', DeletarPersonagens.as_view(), name='deletar-personagens'),
    path('api/', APIListarPersonagens.as_view(), name='api-listar-personagens'),
]