from django.urls import path
from historia.views import ListarHistorias, CriarHistorias, EditarHistorias, DeletarHistorias, FotoHistoria

urlpatterns = [
    path('', ListarHistorias.as_view(), name='listar-historias'),
    path('novoA/', CriarHistorias.as_view(), name='criar-historias'),
    path('fotos/<str:arquivo>/', FotoHistoria.as_view(), name='foto-historia'),
    path('<int:pk>/', EditarHistorias.as_view(), name='editar-historas'),
    path('deletarA/<int:pk>', DeletarHistorias.as_view(), name='deletar-historias'),
]