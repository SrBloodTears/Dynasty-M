from rest_framework import serializers
from persona.models import Personagem


class SerializadorPersona(serializers.ModelSerializer):
    """
    Serializador para o model Personagem
    """
    nome_alinhamento = serializers.SerializerMethodField()
    nome_grupos = serializers.SerializerMethodField()
    nome_raca = serializers.SerializerMethodField()
    poderes = serializers.SerializerMethodField()  # Campo para listar poderes

    class Meta:
        model = Personagem
        exclude = []

    def get_nome_alinhamento(self, instancia):
        return instancia.get_alinhamento_display()

    def get_nome_grupos(self, instancia):
        # Obtém os nomes dos grupos associados e os retorna como uma lista
        return [grupo.nome for grupo in instancia.grupos.all()]

    def get_nome_raca(self, instancia):
        return instancia.get_raca_display()

    def get_poderes(self, instancia):
        # Obtém os nomes dos poderes associados e os retorna como uma lista
        return [poder.nome for poder in instancia.poderes.all()]
