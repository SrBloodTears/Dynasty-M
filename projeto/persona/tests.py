from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from persona.models import *
from persona.form import *
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io
from persona.models import Poder, Grupo

class TestesModelPersonagem(TestCase):

    """
    Classe de testes para o model Personagem
    """

    def setUp(self):

        # Cria uma instância de Personagem com pontosDeCombate específicos para testar a definição de rank

        self.personagem = Personagem.objects.create(
            nome="Test Hero",
            descricao="Um personagem de teste",
            pontosDeCombate=450,  
            raça=1,
            alinhamento=2,
            criador="Stan lee",
            usuario=None
        )

    def test_rank_equal(self):
        """
        Testa se o rank é calculado corretamente baseado nos pontosDeCombate
        """
        self.assertEqual(self.personagem.rank, 2)  

    def test_is_hero(self):
        """
        Testa se a pessoa com pontosDeCombate suficientes tem rank 2
        """
        self.personagem.pontosDeCombate = 2000
        self.personagem.save()
        self.assertEqual(self.personagem.rank, 4)  
        

class TestesViewListarPersonagens(TestCase):

    """
    Classe de testes para a view ListarPersonagens
    """

    def setUp(self):
        
        self.user = User.objects.create(username='teste', password='123a5@teste')
        self.client.force_login(self.user)  

        
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
        self.assertEqual(len(response.context['personas_favoritos']), 1)  
        self.assertEqual(len(response.context['outros_personas']), 1)  


class TestesViewCriarPersonagens(TestCase):
    """
    Classe de testes para a view criarPersonagens
    """

    def setUp(self):
        self.user = User.objects.create(username='teste', password='1234@teste')
        self.client.force_login(self.user)
        self.url = reverse('criar-personagens')

        # Criação de instâncias de Poder e Grupo
        self.poder = Poder.objects.create(nome=1)  # Substitua 1 por um valor válido em OPCOES_PODERES
        self.grupo = Grupo.objects.create(nome=1)  # Substitua 1 por um valor válido em OPCOES_GRUPOS

    def criar_imagem_simulada(self):
        """
        Cria uma imagem simulada para ser usada no teste.
        """

        # Cria uma imagem vermelha de 100x100
        imagem = Image.new('RGB', (100, 100), color='red')
        arquivo = io.BytesIO()
        imagem.save(arquivo, format='JPEG')
        arquivo.seek(0)
        return SimpleUploadedFile(name='test_image.jpg', content=arquivo.read(), content_type='image/jpeg')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioPersona)

    def test_post(self):
        imagem = self.criar_imagem_simulada()

        data = {
            'nome': 'Novo Heroi',
         'descricao': 'Descrição do novo herói',
         'poderes': [self.poder.id],
         'grupos': [self.grupo.id],
         'raça': 1,
         'foto': imagem,
         'alinhamento': 1,
         'pontosDeCombate': 100,
         'criador': 'pai',
         'favorito': False,
        }

        response = self.client.post(self.url, data)

         # Exibir erros do formulário, caso existam
        if response.context and 'form' in response.context:
         print("Erros do formulário:", response.context['form'].errors)

        self.assertEqual(response.status_code, 302)  # Espera redirecionamento
        self.assertRedirects(response, reverse('listar-personagens'))

        self.assertEqual(Personagem.objects.count(), 1)  # Verifica se o personagem foi criado
        personagem = Personagem.objects.first()
        self.assertEqual(personagem.usuario, self.user)  # Verifica se o usuário foi atribuído corretamente

        # Verifica se o nome da foto contém 'test_image.jpg'
        
        self.assertTrue(personagem.foto.name.startswith('persona/fotos/test_image_'))



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
    
    imagem = SimpleUploadedFile(name='test_image.jpg', content=b'file_content', content_type='image/jpeg')

    
    poder = Poder.objects.create(nome=1)
    grupo = Grupo.objects.create(nome=1)

    data = {
        'nome': 'Test Hero Editado',
        'descricao': 'Nova descrição',
        'poderes': [poder.id],
        'grupos': [grupo.id],
        'raça': 1,
        'foto': imagem,  
        'alinhamento': 1,
        'criador': 'novo criador',
        'pontosDeCombate': 200,
        'favorito': False
    }

    response = self.client.post(self.url, data)

    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('listar-personagens'))
    self.assertEqual(Personagem.objects.count(), 1)
    self.assertEqual(Personagem.objects.first().nome, 'Heroi Teste Editado')
    self.assertTrue(Personagem.objects.first().foto.name.endswith('test_image.jpg'))  


class TestesViewDeletarPersonagens(TestCase):

    """
    Classe de testes para a view DeletarPersonagens
    """

    def setUp(self):
        self.user = User.objects.create(username='teste', password='1234@teste')
        self.client.force_login(self.user)
        self.instancia = Personagem.objects.create(
            nome="Personagem Teste", 
            descricao="Descrição do herói da Lua minguante",
            pontosDeCombate=100,
            raça=1,
            alinhamento=1,
            criador="Criador Teste",
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
        self.assertEqual(Personagem.objects.count(), 0)