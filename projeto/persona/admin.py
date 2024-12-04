from django.contrib import admin
from persona.models import Personagem, Poder, Grupo

@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'get_grupos', 'raca', 'alinhamento', 'rank', 'favorito', 'usuario')
    search_fields = ('nome', 'descricao', 'criador', 'usuario__username')
    list_filter = ('raca', 'alinhamento', 'rank', 'favorito')
    filter_horizontal = ('grupos', 'poderes')

    fieldsets = (
        ("Informações Básicas", {
            'fields': ('nome', 'grupos', 'poderes', 'descricao', 'foto')
        }),
        ("Atributos e Classificações", {
            'fields': ('raca', 'alinhamento', 'pontosDeCombate', 'rank', 'favorito')
        }),
        ("Informações do Criador", {
            'fields': ('criador', 'usuario')
        }),
    )

    readonly_fields = ('rank', 'usuario')

    def get_grupos(self, obj):
        """Exibe os grupos associados como uma string no admin."""
        return ", ".join([str(grupo) for grupo in obj.grupos.all()])
    get_grupos.short_description = "Grupos"

@admin.register(Poder)
class PoderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_nome_display')
    search_fields = ('get_nome_display',)

    def get_nome_display(self, obj):
        """Corrige a exibição do nome dos poderes no Django Admin."""
        return obj.__str__()
    get_nome_display.short_description = "Nome"

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_nome_display')
    search_fields = ('get_nome_display',)

    def get_nome_display(self, obj):
        """Corrige a exibição do nome dos grupos no Django Admin."""
        return obj.__str__()
    get_nome_display.short_description = "Nome"
