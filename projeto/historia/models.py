from django.db import models
from persona.models import Personagem
from django.contrib.auth.models import User

class Historia(models.Model):
    nome = models.CharField(max_length=255, default="História sem nome")
    autores = models.TextField(default="Desconhecido")  # Lista de autores como texto, separados por vírgulas
    ilustradores = models.TextField(default="Desconhecido")  # Lista de ilustradores como texto, separados por vírgulas
    personagens = models.ManyToManyField(Personagem, related_name='historias')
    data_de_lancamento = models.DateField(default="2000-01-01")
    foto = models.ImageField(blank=True, null=True, upload_to='historia/fotos')
    descricao = models.CharField(max_length=10000)
    data = models.DateTimeField(auto_now_add=True)
    favorito = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, related_name='historias_armazenadas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def lista_autores(self):
        """Retorna a lista de autores como uma lista de strings."""
        return [autor.strip() for autor in self.autores.split(",")]

    def lista_ilustradores(self):
        """Retorna a lista de ilustradores como uma lista de strings."""
        return [ilustrador.strip() for ilustrador in self.ilustradores.split(",")]

    # personagem = models.ForeignKey(Personagem, related_name='historias', on_delete=models.CASCADE)
    # usuario = models.ForeignKey(User, related_name='historias_armazenadas', on_delete=models.CASCADE, default=1)