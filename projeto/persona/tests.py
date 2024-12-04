from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from persona.models import *
from persona.form import *

# Create your tests here.

class TestesModelPersonagem(TestCase):
    """
    Classe de testes para o model Persona
    """
    def setUp(self):
        self.instancia = Personagem(
            
        )
    
    def test_years_use(self):
        self.instancia.ano = datetime.now().year - 10
        self.assertEqual(self.instancia.anos_de_uso(), 10)

    def test_is_new(self):
        self.assertTrue(self.instancia.Persona_novo)
        self.instancia.ano =datetime.now().year - 5
        self.assertFalse(self.instancia.Persona_novo)

class TestesViewListarPersonagens(TestCase):
    """
    Classe de tests para a view ListarPersonas
    """
    def setUp(self):
        self.user = User.objects.create(username='teste', password='123a5@teste')
        self.client.force_login(self.user)
        self.url = reverse('listar-Personas')
        Personagem().save()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get('Personas')), 1)

class TestesViewCriarPersonagens(TestCase):
    """
    Classe de testss para a view criarPersonas
    """
    def setUp(self):
        self.user = User.objects.create(username='teste', password='1234@teste')
        self.client.force_login(self.user)
        self.url = reverse('criar-Personas')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioPersona)

    def test_post(self):
        data = {'marca': 1, 'modelo': 'ABCDE', 'ano': 2, 'cor': 3, 'combustivel': 4}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-Personas'))

        self.assertEqual(Personagem.objects.count(), 1)
        self.assertEqual(Personagem.objects.first().modelo, 'ABCDE')

class TestesViewEditarPersonas(TestCase):
    """
    Classe de testes para a view EditarPersonas
    """
    def setUp(self):
        self.user = User.objects.create(username='teste', password='1234@teste')
        self.client.force_login(self.user)
        self.instancia = Personagem.objects.create(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=4)
        self.url = reverse('editar-Personas', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Personagem)
        self.assertIsInstance(response.context.get('form'), FormularioPersona)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)
        self.assertEqual(response.context.get('object').marca, 1)

    def test_post(self):
        data = {'marca': 5, 'modelo': 'ABCDE', 'ano': 2, 'cor': 3, 'combustivel': 4}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-Personas'))
        self.assertEqual(Persona.objects.count(), 1)
        self.assertEqual(Persona.objects.first().marca, 5)
        self.assertEqual(Persona.objects.first().pk, self.instancia.pk)

class TestesViewDeletarPersonas(TestCase):
    """
    Classe de testes para a view DeletarPersonas
    """
    def setUp(self):
        self.user = User.objects.create(username='teste', password='1234@teste')
        self.client.force_login(self.user)
        self.instancia = Personagem.objects.create()
        self.url = reverse('deletar-Personas', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Personagem)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)

    def test_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-Personas'))
        self.assertEqual(Personagem.objects.count(), 0)
