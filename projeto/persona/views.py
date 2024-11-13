from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from persona.models import Personagem
from persona.form import FormularioPersona
from persona.serializers import SerializadorPersona
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from django.contrib import messages

class ListarPersonagens(LoginRequiredMixin, ListView):
    """
    View para listar personagens cadastrados.
    """
    model = Personagem
    context_object_name = 'personagens'
    template_name = 'persona/listar.html'
    paginate_by = 10  # Adiciona paginação, 10 itens por página

class CriarPersonagens(LoginRequiredMixin, CreateView):
    """
    View para criar personagens.
    """
    model = Personagem
    form_class = FormularioPersona
    template_name = 'persona/novo.html'
    success_url = reverse_lazy('listar-personagens')

    def form_valid(self, form):
        messages.success(self.request, 'Personagem criado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao criar personagem. Verifique os dados informados.')
        return super().form_invalid(form)

class EditarPersonagens(LoginRequiredMixin, UpdateView):
    """
    View para a edição de personagens já cadastrados.
    """
    model = Personagem
    form_class = FormularioPersona
    template_name = 'persona/editar.html'
    success_url = reverse_lazy('listar-personagens')

    def form_valid(self, form):
        messages.success(self.request, 'Personagem atualizado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar personagem. Verifique os dados informados.')
        return super().form_invalid(form)

class DeletarPersonagens(LoginRequiredMixin, DeleteView):
    """
    View para a exclusão de personagens.
    """
    model = Personagem
    template_name = 'persona/deletar.html'
    success_url = reverse_lazy('listar-personagens')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Personagem excluído com sucesso!')
        return super().delete(request, *args, **kwargs)

class FotoPersonagem(View):
    """
    View para retornar a foto dos personagens.
    """

    def get(self, request, arquivo):
        try:
            persona = Personagem.objects.get(foto='persona/fotos/{}'.format(arquivo))
            return FileResponse(persona.foto.open('rb'), content_type='image/jpeg')
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada.")
        except Exception as exception:
            messages.error(request, 'Erro ao acessar a foto do personagem.')
            raise exception

class APIListarPersonagens(ListAPIView):
    """
    View para listar instâncias de personagens via API.
    """
    serializer_class = SerializadorPersona
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Personagem.objects.all()
