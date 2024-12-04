from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from historia.models import Historia
from historia.form import FormularioHistoria
from persona.models import Personagem
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime, timedelta
from PIL import Image
import io

class TestesModelHistoria(TestCase):
    """
    Classe de testes para o model Historia
    """

    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)

        # Criação de personagens para o campo ManyToMany
        self.personagem1 = Personagem.objects.create(nome="Personagem 1", raça=1, alinhamento=1, pontosDeCombate=100)
        self.personagem2 = Personagem.objects.create(nome="Personagem 2", raça=2, alinhamento=2, pontosDeCombate=200)

        # Criação da história
        self.historia = Historia.objects.create(
            nome="História de Teste",
            descricao="Uma história de teste",
            data_de_lancamento="2023-01-01",
            usuario=self.user
        )
        self.historia.personagens.add(self.personagem1, self.personagem2)  # Associando personagens à história

    def test_tem_personagem(self):
        """
        Testa se a HQ possui personagens relacionados
        """
        personagens = self.historia.personagens.all()
        self.assertEqual(personagens.count(), 2)
        self.assertIn(self.personagem1, personagens)
        self.assertIn(self.personagem2, personagens)

    def test_new_history(self):
        """
        Testa se a data de lançamento da HQ é recente
        """
        data_atual = datetime.now().date()
        limite_minimo = data_atual - timedelta(days=2 * 365)  # Aproximadamente 2 anos
        data_lancamento = datetime.strptime(self.historia.data_de_lancamento, '%Y-%m-%d').date()

        self.assertGreaterEqual(data_lancamento, limite_minimo)

class TestesViewListarHistorias(TestCase):
    """
    Classe de testes para a view ListarHistorias
    """

    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)

        self.historia1 = Historia.objects.create(
            nome="Guerras Secretas",
            usuario=self.user,
            favorito=True,
        )
        self.historia2 = Historia.objects.create(
            nome="Guerras Infinitas",
            usuario=self.user,
            favorito=False,
        )

        self.url = reverse('listar-historias')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['historias_favoritas']), 1)
        self.assertEqual(len(response.context['outras_historias']), 1)

class TestesViewCriarHistorias(TestCase):
    """
    Classe de testes para a view CriarHistorias
    """

    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)

        # Criação de personagens para o campo ManyToMany
        self.personagem1 = Personagem.objects.create(nome="Personagem 1", raça=1, alinhamento=1, pontosDeCombate=100)
        self.personagem2 = Personagem.objects.create(nome="Personagem 2", raça=2, alinhamento=2, pontosDeCombate=200)

        # URL para criação de histórias
        self.url_criar = reverse('criar-historias')

    def criar_imagem_simulada(self):
        """
        Cria uma imagem simulada para ser usada no teste de Historia.
        """
        imagem = Image.new('RGB', (100, 100), color='blue')
        arquivo = io.BytesIO()
        imagem.save(arquivo, format='JPEG')
        arquivo.seek(0)
        return SimpleUploadedFile(name='test_image.jpg', content=arquivo.read(), content_type='image/jpeg')

    def test_get(self):
        response = self.client.get(self.url_criar)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioHistoria)

    def test_post(self):
        imagem = self.criar_imagem_simulada()

        data = {
            'nome': 'História Teste',
            'descricao': 'Descrição da nova história',
            'autores': 'Autor 1, Autor 2',
            'ilustradores': 'Ilustrador 1, Ilustrador 2',
            'personagens': [self.personagem1.id, self.personagem2.id],
            'favorito': False,
            'data_de_lancamento': '2023-01-01',
            'foto': imagem,
        }

        response = self.client.post(self.url_criar, data)

        if response.context and 'form' in response.context:
            print("Erros do formulário:", response.context['form'].errors)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-historias'))

        self.assertEqual(Historia.objects.count(), 1)
        historia = Historia.objects.first()
        self.assertEqual(historia.usuario, self.user)
        self.assertIn('test_image', historia.foto.name)


class TestesViewEditarHistorias(TestCase):
    """
    Classe de testes para a view EditarHistorias
    """

    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)
        
        # Criação de personagens para o campo ManyToMany
        self.personagem1 = Personagem.objects.create(nome="Personagem 1", raça=1, alinhamento=1, pontosDeCombate=100)
        
        # Criação da instância de Historia para editar
        self.instancia = Historia.objects.create(
            nome="História Teste",
            descricao="Descrição de teste",
            usuario=self.user,
        )
        self.instancia.personagens.add(self.personagem1)

        # URL para edição de histórias
        self.url_editar = reverse('editar-historias', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url_editar)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Historia)
        self.assertIsInstance(response.context.get('form'), FormularioHistoria)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)

    def test_post(self):
        data = {
            'nome': 'História Editada',
            'descricao': 'Descrição editada',
            'autores': 'Novo Autor',
            'ilustradores': 'Novo Ilustrador',
            'personagens': [self.personagem1.id],
            'favorito': True,
            'data_de_lancamento': '2023-01-01',
        }

        response = self.client.post(self.url_editar, data)

        if response.context and 'form' in response.context:
            print("Erros do formulário:", response.context['form'].errors)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-historias'))

        historia = Historia.objects.get(pk=1)
        self.assertEqual(historia.nome, 'História Editada')
        self.assertEqual(historia.autores, 'Novo Autor')
        self.assertTrue(historia.favorito)



class TestesViewDeletarHistorias(TestCase):
    """
    Classe de testes para a view DeletarHistorias
    """

    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)
        self.instancia = Historia.objects.create(
            nome="História para Deletar",
            descricao="Descrição de teste para deletar",
            usuario=self.user,
        )
        self.url = reverse('deletar-historias', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Historia)

    def test_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-historias'))
        self.assertEqual(Historia.objects.count(), 0)
