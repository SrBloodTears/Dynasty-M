from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import render
from historia.models import Historia
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from historia.form import FormularioHistoria

class ListarHistorias(LoginRequiredMixin, ListView):
    """
    View para listar as historias cadastradas.
    """

    model = Historia
    context_object_name = 'historias'
    template_name = 'historia/listarH.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['historias_favoritas'] = Historia.objects.filter(favorito=True, usuario=self.request.user)
        context['outras_historias'] = Historia.objects.filter(favorito=False, usuario=self.request.user)
        return context

class CriarHistorias(LoginRequiredMixin, CreateView):
    """
    View para criar as historias de personagens.
    """
    model = Historia
    form_class = FormularioHistoria
    template_name = 'historia/novoH.html'
    success_url = reverse_lazy('listar-historias')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Atribui o usuário logado
        return super().form_valid(form)

class EditarHistorias(LoginRequiredMixin, UpdateView):
    """
    View para a edição das historias já cadastrados
    """
    model = Historia
    form_class = FormularioHistoria
    template_name = 'historia/editarH.html'
    success_url = reverse_lazy('listar-historias')

class DeletarHistorias(LoginRequiredMixin, DeleteView):
    """
    View para a exclusão das historias
    """
    model = Historia
    template_name = 'historia/deletarH.html'
    success_url = reverse_lazy('listar-historias')

class FotoHistoria(View):
    """
    View para retornar a foto das historias.
    """

    def get(self, request, arquivo):
        try:
            historia = Historia.objects.get(foto='historia/fotos/{}'.format(arquivo))
            return FileResponse(historia.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não-autorizado!")
        except Exception as exception:
            raise exception