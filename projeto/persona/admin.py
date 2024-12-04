from django.contrib import admin
from persona.models import Personagem, Poder, Grupo
from django.contrib import admin


@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'get_grupos', 'raca', 'alinhamento', 'rank', 'favorito', 'usuario')
    search_fields = ('nome',)
    list_filter = ('raca', 'alinhamento', 'rank')
    filter_horizontal = ('grupos', 'poderes')

    fieldsets = (
        (None, {
            'fields': ('nome', 'grupos', 'raca', 'alinhamento', 'descricao', 'foto', 'poderes', 'pontosDeCombate', 'criador', 'favorito', 'usuario')
        }),
    )

    readonly_fields = ('usuario',) 

    def get_grupos(self, obj):
        return ", ".join([grupo.get_nome_display() for grupo in obj.grupos.all()])
    get_grupos.short_description = "Grupos"

@admin.register(Poder)
class PoderAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
