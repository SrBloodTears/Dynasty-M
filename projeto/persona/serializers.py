from rest_framework import serializers
from persona.models import Personagem, Poder


class SerializadorPersona(serializers.ModelSerializer):
    """
    Serializador para o model Personagem
    """
    nome_alinhamento = serializers.SerializerMethodField()
    nome_grupo = serializers.SerializerMethodField()
    nome_raca = serializers.SerializerMethodField()
    poderes = serializers.SerializerMethodField()  # Campo para listar poderes

    class Meta:
        model = Personagem
        exclude = []

    def get_nome_alinhamento(self, instancia):
        return instancia.get_alinhamento_display()

    def get_nome_grupo(self, instancia):
        return instancia.get_grupo_display()
    
    def get_nome_raca(self, instancia):
        return instancia.get_raca_display()

    def get_poderes(self, instancia):
        # Obtém os nomes dos poderes associados e os retorna como uma lista
        return [poder.get_codigo_display() for poder in instancia.poderes.all()]
