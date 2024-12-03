from django.db.models.signals import post_migrate
from django.dispatch import receiver
from persona.models import Poder, Grupo
from persona.consts import OPCOES_PODERES, OPCOES_GRUPOS

@receiver(post_migrate)
def carregar_poderes(sender, **kwargs):
    # Verifica se é o app correto
    if sender.name == "persona":
        for opcao in OPCOES_PODERES:
            Poder.objects.get_or_create(nome=opcao[0])  # Cria apenas se não existir

        for opcao in OPCOES_GRUPOS:
            Grupo.objects.get_or_create(nome=opcao[0])  # Cria apenas se não existir