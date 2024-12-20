# Generated by Django 5.1.1 on 2024-12-02 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_alter_grupo_nome_alter_poder_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poder',
            name='nome',
            field=models.IntegerField(choices=[(1, 'SUPER FORÇA'), (2, 'VELOCIDADE SOBRE-HUMANA'), (3, 'VÔO'), (4, 'RAIOS DE ENERGIA'), (5, 'RAIOS LÁSER'), (6, 'INVISIBILIDADE'), (7, 'TELETRANSPORTE'), (8, 'INTANGIBILIDADE'), (9, 'TELECINESE'), (10, 'TELEPATIA'), (11, 'PROJEÇÃO ASTRAL'), (12, 'IMORTALIDADE'), (13, 'REGENERAÇÃO'), (14, 'SUPER-INTELIGÊNCIA'), (15, 'VISÃO DE RAIO-X'), (16, 'CAMUFLAGEM'), (17, 'MANIPULAÇÃO DE ELEMENTOS'), (18, 'CONTRAÇÃO'), (19, 'EXPANSÃO'), (20, 'ELASTICIDADE'), (21, 'METAMORFOSE'), (22, 'FATOR DE CURA'), (23, 'RAIOS CÓSMICOS'), (24, 'MANIPULAÇÃO DE SOM'), (25, 'ALTERAÇÃO DE REALIDADE'), (26, 'PIROQUINESE'), (27, 'CRIOQUINESE'), (28, 'ELETRICIDADE'), (29, 'MANIPULAÇÃO DE METAL'), (30, 'MANIPULAÇÃO DE LUZ'), (31, 'MANIPULAÇÃO DE TREVAS'), (32, 'CONTROLE DO TEMPO'), (33, 'MAGIA'), (34, 'SONICIDADE'), (35, 'LEVITAÇÃO'), (36, 'MANIPULAÇÃO DE GRAVIDADE'), (37, 'RAIO DE GELO'), (38, 'RAIO DE CALOR'), (39, 'CONTROLE ANIMAL'), (40, 'PODERES PSIÔNICOS'), (41, 'RAIOS DE ENERGIA SOLAR'), (42, 'FÔLEGO DE FOGO'), (43, 'FORÇA SOBRE-HUMANA'), (44, 'RAIOS DE PLASMA'), (45, 'FOTOGRAFIA'), (46, 'SENTIDO ARANHA'), (47, 'VIDÊNCIA'), (48, 'PROJEÇÃO DE ESCUDO'), (49, 'MANIPULAÇÃO DO TEMPO'), (50, 'MEMÓRIA EIDÉTICA'), (51, 'PROJEÇÃO DE CAMPOS DE FORÇA'), (52, 'MANIPULAÇÃO MOLECULAR'), (53, 'VISÃO NOTURNA'), (54, 'MANIPULAÇÃO DE EMOÇÕES'), (55, 'ENVELHECIMENTO ACELERADO'), (56, 'HABILIDADES DE COMBATE AVANÇADAS'), (57, 'ALTERAÇÃO CORPORAL'), (58, 'CONTROLAR VENTO'), (59, 'ESPINHOS PROJETÁVEIS'), (60, 'FUSÃO COM A SOMBRA'), (61, 'RESISTÊNCIA APRIMORADA'), (62, 'DURABILIDADE APRIMORADA'), (63, 'SENTIDOS APRIMORADOS'), (64, 'CAMPO DE REPULSÃO'), (65, 'FORMA ETÉREA'), (66, 'RAIO DE ALTA FREQUÊNCIA'), (67, 'RESISTÊNCIA A VENENOS'), (68, 'MENTE INDOMÁVEL'), (69, 'CONTROLAR TECIDOS CORPORAIS'), (70, 'CAMUFLAGEM AVANÇADA'), (71, 'GRITO SÔNICO'), (72, 'VISÃO MICROSCÓPICA'), (73, 'VISÃO TELESCÓPICA'), (74, 'ALTERAR DENSIDADE'), (75, 'DUPLICAÇÃO'), (76, 'INTUIÇÃO AVANÇADA'), (77, 'MANIPULAÇÃO DE MENTE'), (78, 'AMPLIFICAÇÃO DE PODER'), (79, 'RESISTÊNCIA SOBRENATURAL'), (80, 'LEVITAÇÃO AVANÇADA'), (81, 'INTIMIDAÇÃO ENERGÉTICA'), (82, 'TRANSMUTAÇÃO'), (83, 'TEIA ORGÂNICA'), (84, 'ENVENENAMENTO'), (85, 'COMUNICAÇÃO COM ANIMAIS'), (86, 'SUSPENSÃO DO ENVELHECIMENTO'), (87, 'CONTROLE DE TECNOLOGIA'), (88, 'CORPO QUÂNTICO'), (89, 'CONTROLE DE VEGETAÇÃO'), (90, 'RAIOS ULTRAVIOLETA'), (91, 'CONTROLE SOBRE O ESPAÇO'), (92, 'FORÇA GALÁCTICA'), (93, 'AURA DE PROTEÇÃO'), (94, 'MANIPULAÇÃO DE RAIOS'), (95, 'HABILIDADE MUSICAL SUPER-HUMANA'), (96, 'SENTIDO EXTRADIMENSIONAL'), (97, 'IMUNIDADE A DOENÇAS'), (98, 'MANIPULAÇÃO DE PESADELOS'), (99, 'PRESENÇA HIPNÓTICA'), (100, 'EMPATIA SOBRENATURAL'), (101, 'SEM PODERES')]),
        ),
    ]
