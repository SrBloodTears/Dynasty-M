from django import forms
from persona.models import Personagem, Grupo, Poder

class FormularioPersona(forms.ModelForm):
    grupos = forms.ModelMultipleChoiceField(
        queryset=Grupo.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select'}),
        required=False,
        label="Grupos"
    )
    poderes = forms.ModelMultipleChoiceField(
        queryset=Poder.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select'}),
        required=False,
        label="Poderes"
    )

    class Meta:
        model = Personagem
        fields = ['nome', 'descricao', 'poderes', 'grupos', 'raca', 'foto', 'alinhamento', 'pontosDeCombate', 'criador', 'favorito']

    def save(self, commit=True, request=None):
        """
        Salva o formulário, atribuindo o usuário autenticado, se necessário, 
        e garantindo que os campos ManyToMany sejam tratados corretamente.
        """
        instance = super().save(commit=False)

        # Atribuir o usuário autenticado, se o request for passado
        if request:
            instance.usuario = request.user
        
        if commit:
            instance.save()  # Salva a instância do objeto para associar M2M corretamente
            self.save_m2m()  # Salva os campos ManyToMany

        return instance
