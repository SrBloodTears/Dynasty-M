from django.contrib import admin
from .models import Historia

@admin.register(Historia)
class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_de_lancamento', 'get_autores', 'get_ilustradores', 'get_personagens', 'usuario')
    search_fields = ('nome', 'descricao')
    list_filter = ('data_de_lancamento',)
    filter_horizontal = ('personagens',)

    fieldsets = (
        (None, {
            'fields': ('nome', 'data_de_lancamento', 'foto', 'descricao', 'autores', 'ilustradores', 'personagens')
        }),
    )

    def save_model(self, request, obj, form, change):
        """Associa automaticamente o usuário logado ao campo 'usuario'."""
        if not obj.usuario_id:  # Verifica se o campo ainda não foi preenchido
            obj.usuario = request.user  # Define o usuário logado como criador
        super().save_model(request, obj, form, change)

    def get_autores(self, obj):
        return ", ".join(obj.lista_autores())
    get_autores.short_description = "Autores"

    def get_ilustradores(self, obj):
        return ", ".join(obj.lista_ilustradores())
    get_ilustradores.short_description = "Ilustradores"

    def get_personagens(self, obj):
        personagens = obj.personagens.all()
        return ", ".join([personagem.nome for personagem in personagens[:5]]) + ("..." if personagens.count() > 5 else "")
    get_personagens.short_description = "Personagens"
