from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from persona.models import *
from persona.form import *
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

class TestesModelPersonagem(TestCase):
    """
    Classe de testes para o model Personagem
    """
    def setUp(self):
        # Cria uma instância de Personagem com pontosDeCombate específicos para testar a definição de rank
        self.personagem = Personagem.objects.create(
            nome="Test Hero",
            descricao="Um personagem de teste",
            pontosDeCombate=450,  # Esse valor deverá definir o rank como 2 (AGENTE TREINADO)
            usuario=None
        )

    def test_rank_equal(self):
        """
        Testa se o rank é calculado corretamente baseado nos pontosDeCombate
        """
        self.assertEqual(self.personagem.rank, 2)  # Deve ser 'AGENTE TREINADO'

    def test_is_hero(self):
        """
        Testa se a pessoa com pontosDeCombate suficientes tem rank 2
        """
        self.personagem.pontosDeCombate = 2000
        self.personagem.save()
        self.assertEqual(self.personagem.rank, 3)  # Deve ser 'AMEACA DA VIZINHANCA'
        

class TestesViewListarPersonagens(TestCase):
    """
    Classe de testes para a view ListarPersonagens
    """
    def setUp(self):
        # Criação de um usuário para login
        self.user = User.objects.create(username='teste', password='123a5@teste')
        self.client.force_login(self.user)  # Faz login como usuário

        # Criar personagens com valores válidos para todos os campos obrigatórios
        self.personagem1 = Personagem.objects.create(
            nome="Heroi1", 
            usuario=self.user, 
            favorito=True,
            raça=1,  
            alinhamento=2
        )
        self.personagem2 = Personagem.objects.create(
            nome="Heroi2", 
            usuario=self.user, 
            favorito=False,
            raça=1,  
            alinhamento=2
        )

        self.url = reverse('listar-personagens')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['personas_favoritos']), 1)  # Apenas 1 favorito
        self.assertEqual(len(response.context['outros_personas']), 1)  # Apenas 1 não favorito


class TestesViewCriarPersonagens(TestCase):
    """
    Classe de testes para a view criarPersonagens
    """
    def setUp(self):
        self.user = User.objects.create(username='teste', password='1234@teste')
        self.client.force_login(self.user)  # Faz login como usuário
        self.url = reverse('criar-personagens')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioPersona)

    def test_post(self):
        data = {
            'nome': 'Novo Heroi',
            'descricao': 'Descrição do novo herói',
            'poderes': '',
            'grupos': '',
            'raça': 1,  # Exemplo de valor de raça
            'foto': None,
            'alinhamento': 1,  # Exemplo de valor de alinhamento
            'pontosDeCombate': 100,
            'criador': 'pai',
            'favorito': False
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)  # Redirecionamento após sucesso
        self.assertRedirects(response, reverse('listar-personagens'))

        self.assertEqual(Personagem.objects.count(), 1)  # Verifica que um personagem foi criado
        self.assertEqual(Personagem.objects.first().usuario, self.user)  # Verifica que o usuário foi atribuído corretamente


class TestesViewEditarPersonagens(TestCase):
    """
    Classe de testes para a view EditarPersonagens
    """
    def setUp(self):
        self.user = User.objects.create(username='teste', password='1234@teste')
        self.client.force_login(self.user)
        self.instancia = Personagem.objects.create(
            nome="Test Hero", 
            descricao="Descrição do herói",
            pontosDeCombate=100, 
            raça= 2,
            alinhamento= 3,
            usuario=self.user
        )
        self.url = reverse('editar-personagens', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Personagem)
        self.assertIsInstance(response.context.get('form'), FormularioPersona)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)

    from django.core.files.uploadedfile import SimpleUploadedFile

def test_post(self):
    # Criando um arquivo de imagem simulado
    imagem = SimpleUploadedFile(name='test_image.jpg', content=b'file_content', content_type='image/jpeg')

    # Criar ou pegar instâncias de poderes e grupos válidos
    poder = Poder.objects.create(nome=1)
    grupo = Grupo.objects.create(nome=1)

    data = {
        'nome': 'Test Hero Editado',
        'descricao': 'Nova descrição',
        'poderes': [poder.id],
        'grupos': [grupo.id],
        'raça': 1,
        'foto': imagem,  # Passando a imagem simulada
        'alinhamento': 1,
        'criador': 'novo criador',
        'pontosDeCombate': 200,
        'favorito': False
    }

    response = self.client.post(self.url, data)

    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('listar-personagens'))
    self.assertEqual(Personagem.objects.count(), 1)
    self.assertEqual(Personagem.objects.first().nome, 'Test Hero Editado')
    self.assertTrue(Personagem.objects.first().foto.name.endswith('test_image.jpg'))  


class TestesViewDeletarPersonagens(TestCase):
    """
    Classe de testes para a view DeletarPersonagens
    """
    def setUp(self):
        self.user = User.objects.create(username='teste', password='1234@teste')
        self.client.force_login(self.user)
        self.instancia = Personagem.objects.create(
            nome="Test Hero", 
            descricao="Descrição do herói",
            pontosDeCombate=100, 
            usuario=self.user
        )
        self.url = reverse('deletar-personagens', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Personagem)

    def test_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-personagens'))
        self.assertEqual(Personagem.objects.count(), 0)  # Verifica que o personagem foi excluído