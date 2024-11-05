from django.views.generic import View
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from persona.models import Personagem
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from persona.form import FormularioPersona
from persona.serializers import SerializadorPersona
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

class ListarPersonagens(LoginRequiredMixin, ListView):
    """
    View para listar personagens cadastrados.
    """
    model = Personagem
    context_object_name = 'personagens'
    template_name = 'persona/listar.html'

class CriarPersonagens(LoginRequiredMixin, CreateView):
    """
    View para criar personagens.
    """
    model = Personagem
    form_class = FormularioPersona
    template_name = 'persona/novo.html'
    success_url = reverse_lazy('listar-personagens')

class EditarPersonagens(LoginRequiredMixin, UpdateView):
    """
    View para a edição de personagens já cadastrados
    """
    model = Personagem
    form_class = FormularioPersona
    template_name = 'persona/editar.html'
    success_url = reverse_lazy('listar-personagens')

class DeletarPersonagens(LoginRequiredMixin, DeleteView):
    """
    View para a exclusão de personagens
    """
    model = Personagem
    template_name = 'persona/deletar.html'
    success_url = reverse_lazy('listar-personagens')

class FotoPersonagem(View):
    """
    View para retornar a foto dos personagens.
    """

    def get(self, request, arquivo):
        try:
            persona = Personagem.objects.get(foto='persona/fotos/{}'.format(arquivo))
            return FileResponse(persona.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não-autorizado!")
        except Exception as exception:
            raise exception
        
class APIListarPersonagens(ListAPIView):
    """
    View para listar instancias de personagens (por meio da API Rest)
    """
    serializer_class = SerializadorPersona
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return Personagem.objects.all()