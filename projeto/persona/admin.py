# persona/admin.py
from django.contrib import admin
from persona.models import Personagem  # Importa o modelo Personagem

@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grupo', 'raça', 'alinhamento')  # Colunas exibidas no admin
    search_fields = ('nome',)  # Adiciona uma barra de pesquisa pelo nome
    list_filter = ('grupo', 'raça', 'alinhamento')  # Filtros laterais para grupo, raça e alinhamento
