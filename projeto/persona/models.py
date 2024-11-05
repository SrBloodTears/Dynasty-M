from django.db import models
from persona.consts import *


class Personagem(models.Model):
    grupo = models.SmallIntegerField(choices=OPCOES_GRUPOS)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=10000)
    poderes = models.ManyToManyField('Poder', blank=True)
    raça = models.SmallIntegerField(choices=OPCOES_RACAS)
    foto = models.ImageField(blank=True, null=True, upload_to='persona/fotos')
    alinhamento = models.SmallIntegerField(choices=OPCOES_ALINHAMENTOS)

    def __str__(self):
        return '{0} - {1} ({2} / {3})'.format(
            self.nome,
            self.get_alinhamento_display(),
            self.get_raca_display(),
            self.get_grupo_display()
        )
    

class Poder(models.Model):
    codigo = models.SmallIntegerField(choices=OPCOES_PODERES, unique=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.get_codigo_display()