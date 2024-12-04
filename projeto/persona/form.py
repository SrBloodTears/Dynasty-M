from django.forms import ModelForm
from persona.models import Personagem
from django import forms

class FormularioPersona(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = ['nome', 'descricao', 'poderes', 'grupos', 'raca', 'foto', 'alinhamento', 'pontosDeCombate', 'criador', 'favorito']
        widgets = {
            'poderes': forms.CheckboxSelectMultiple(),
            'grupos': forms.CheckboxSelectMultiple(),
        }
    
    def save(self, commit=True, request=None):
        persona = super().save(commit=False)
        if request:
            persona.usuario = request.user  # Atribui o usuário logado ao campo 'usuario'
        if commit:
            persona.save()
        return persona