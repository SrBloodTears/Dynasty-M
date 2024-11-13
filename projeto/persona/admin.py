from django.contrib import admin
from persona.models import Personagem, Poder  # Importa o modelo Personagem e Poder

@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grupo', 'raça', 'alinhamento')  # Colunas exibidas no admin
    search_fields = ('nome',)  # Barra de pesquisa pelo nome
    list_filter = ('grupo', 'raça', 'alinhamento')  # Filtros laterais para grupo, raça e alinhamento
    filter_horizontal = ('poderes',)  # Configuração para seleção múltipla de poderes

    fieldsets = (
        (None, {
            'fields': ('nome', 'grupo', 'raça', 'alinhamento', 'descricao', 'foto', 'poderes')
        }),
    )

@admin.register(Poder)
class PoderAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao')  # Exibe código e descrição do poder
    search_fields = ('descricao',)  # Barra de pesquisa pela descrição
