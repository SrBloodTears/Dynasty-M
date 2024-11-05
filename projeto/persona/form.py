from django.forms import ModelForm
from persona.models import Personagem

class FormularioPersona(ModelForm):
    """
    formulario para o model Personagem
    """

    class Meta:
        model = Personagem
        exclude = []