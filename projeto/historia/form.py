from django.forms import ModelForm
from historia.models import Historia

class FormularioHistoria(ModelForm):
    """
    formulario para o model Historia
    """

    class Meta:
        model = Historia
        exclude = ['usuario']