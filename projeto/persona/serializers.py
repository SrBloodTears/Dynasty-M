from rest_framework import serializers
from persona.models import Personagem, Grupo, Poder

class SerializadorPersona(serializers.ModelSerializer):
    grupos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Grupo.objects.all(), required=False
    )
    poderes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Poder.objects.all(), required=False
    )

    class Meta:
        model = Personagem
        fields = ['nome', 'descricao', 'raca', 'alinhamento', 'pontosDeCombate', 'criador', 'favorito', 'grupos', 'poderes']

    def create(self, validated_data):
        grupos = validated_data.pop('grupos', [])
        poderes = validated_data.pop('poderes', [])
        personagem = Personagem.objects.create(**validated_data)
        personagem.grupos.set(grupos)
        personagem.poderes.set(poderes)
        return personagem

    def update(self, instance, validated_data):
        grupos = validated_data.pop('grupos', [])
        poderes = validated_data.pop('poderes', [])
        instance.grupos.set(grupos)
        instance.poderes.set(poderes)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
