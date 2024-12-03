from django.forms import ModelForm
from persona.models import Personagem
from django import forms

class FormularioPersona(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = ['nome', 'descricao', 'poderes', 'grupos', 'raça', 'foto', 'alinhamento', 'pontosDeCombate', 'criador']
        widgets = {
            'poderes': forms.CheckboxSelectMultiple(),
            'grupos': forms.CheckboxSelectMultiple(),
        }
