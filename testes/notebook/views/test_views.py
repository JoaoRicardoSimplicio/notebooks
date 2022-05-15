from django.test import TestCase, Client
from model_bakery import baker

from notebook.models import Notebook


class TestViews(TestCase):

    def setUp(self):
        self.notebooks = baker.make(Notebook, _quantity=3)

    def test_lista_notebooks_api_view(self):
        resposta = self.client.get('/')
        self.assertEqual(resposta.json()['count'], 3)
        self.assertEqual(resposta.status_code, 200)
        
    def test_obtem_notebook_api_view(self):
        resposta = self.client.get(f'/{self.notebooks[0].id}/')
        self.assertEqual(resposta.json()['id'], self.notebooks[0].id)
        self.assertEqual(resposta.status_code, 200)

    def test_falha_obter_notebook_api_view(self):
        resposta = self.client.get('/50/')
        self.assertEqual(resposta.status_code, 404)
