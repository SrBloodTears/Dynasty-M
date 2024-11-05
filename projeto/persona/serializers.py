from rest_framework import serializers
from persona.models import Personagem


class SerializadorPersona(serializers.ModelSerializer):
    """
    Serializador para o model Persona
    """
    nome_marca = serializers.SerializerMethodField()
    nome_cor = serializers.SerializerMethodField()
    nome_combustivel = serializers.SerializerMethodField()

    class Meta:
        model = Personagem
        exclude = []

    def get_nome_alinhamento(self, instancia):
        return instancia.get_alinhamento_display()

    def get_nome_grupo(self, instancia):
        return instancia.get_grupo_display()
    
    def get_nome_raca(self, instancia):
        return instancia.get_raca_display()
    