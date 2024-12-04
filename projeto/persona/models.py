from django.db import models
from django.contrib.auth.models import User
from persona.consts import *

class Grupo(models.Model):
    nome = models.IntegerField(choices=OPCOES_GRUPOS)

    def __str__(self):
        return dict(OPCOES_GRUPOS).get(self.nome, "Desconhecido")

class Poder(models.Model):
    nome = models.IntegerField(choices=OPCOES_PODERES)

    def __str__(self):
        return dict(OPCOES_PODERES).get(self.nome, "Desconhecido")

class Personagem(models.Model):
    grupos = models.ManyToManyField(Grupo, related_name='personagens')
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=10000)
    poderes = models.ManyToManyField(Poder, related_name='personagens')
    raça = models.SmallIntegerField(choices=OPCOES_RACAS)
    foto = models.ImageField(blank=True, null=True, upload_to='persona/fotos')
    alinhamento = models.SmallIntegerField(choices=OPCOES_ALINHAMENTOS)
    rank = models.SmallIntegerField(choices=OPCOES_RANKS, editable=False, default=1)
    pontosDeCombate = models.IntegerField(default=0)
    criador = models.CharField(max_length=100, default="Criador desconhecido")
    usuario = models.ForeignKey(User, related_name='personagens', on_delete=models.CASCADE, null=True, blank=True)
    favorito = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Personagens"

    def save(self, *args, **kwargs):
        self.rank = self.definir_rank()
        super().save(*args, **kwargs)

    def definir_rank(self):
        if self.pontosDeCombate < 100:
            return 1  # CIVIL
        elif self.pontosDeCombate < 500:
            return 2  # AGENTE TREINADO
        elif self.pontosDeCombate < 1000:
            return 3  # AMEACA DA VIZINHANCA
        elif self.pontosDeCombate < 5000:
            return 4  # ARRASA QUARTEIRAO
        elif self.pontosDeCombate < 10000:
            return 5  # CIDADE EM PERIGO
        elif self.pontosDeCombate < 50000:
            return 6  # DIVINO
        elif self.pontosDeCombate < 100000:
            return 7  # ARAUTO COSMICO
        elif self.pontosDeCombate < 500000:
            return 8  # FIM DO MUNDO
        elif self.pontosDeCombate < 1000000:
            return 9  # DEVORADOR DE PLANETAS
        elif self.pontosDeCombate < 5000000:
            return 10  # DESTRUIDOR DO UNIVERSO
        elif self.pontosDeCombate < 10000000:
            return 11  # PERIGO MULTIVERSAL
        elif self.pontosDeCombate < 50000000:
            return 12  # ABSTRATO
        elif self.pontosDeCombate < 100000000:
            return 13  # ONIPOTENTE
        else:
            return 14  # DESCONHECIDO

    def __str__(self):
        grupos = ", ".join([grupo.get_nome_display() for grupo in self.grupos.all()])
        poderes = ", ".join([poder.get_nome_display() for poder in self.poderes.all()])
        return '{0} - {1} ({2} / {3} / {4} / {5} - {6} / {7})'.format(
            self.nome,
            self.get_alinhamento_display(),
            self.get_raça_display(),
            grupos,
            poderes,
            self.get_rank_display(),
            self.pontosDeCombate,
            self.criador
    )