from django.test import TestCase
from model_bakery import baker
from unittest import mock

from notebook.models import Notebook
from notebook.servicos.crawler import ETLNotebooks
from notebook.tarefas.atualiza import atualiza_notebooks


class TestTarefas(TestCase):

    def setUp(self):
        self.notebooks = [
            baker.make(Notebook, **notebook)
            for notebook in [
                {"titulo": "NotebookB", "descricao": "B", "reviews": 13, "estrelas": 8, "preco": 2000.23},
            ]
        ]

    @mock.patch('notebook.tarefas.atualiza.ETLNotebooks')
    def test_atualiza_notebok_salvo(self, mock_etlnotebooks):
        etlnotebooks = mock_etlnotebooks.return_value
        etlnotebooks.executar.return_value = mock.Mock(return_value=None)
        etlnotebooks.notebooks = [
            {"titulo": "NotebookB", "descricao": "B", "reviews": 10, "estrelas": 4, "preco": 1000.23}
        ]
        atualiza_notebooks()
        notebook = Notebook.objects.get(titulo="NotebookB")
        self.assertEqual(Notebook.objects.count(), 1)
        self.assertEqual(notebook.preco.to_eng_string(), "1000.23")
        self.assertEqual(notebook.reviews, 10)

    @mock.patch('notebook.tarefas.atualiza.ETLNotebooks')
    def test_salva_notebok_novo(self, mock_etlnotebooks):
        etlnotebooks = mock_etlnotebooks.return_value
        etlnotebooks.executar.return_value = mock.Mock(return_value=None)
        etlnotebooks.notebooks = [
            {"titulo": "NotebookA", "descricao": "A", "reviews": 20, "estrelas": 7, "preco": 3500.93}
        ]
        atualiza_notebooks()
        self.assertEqual(Notebook.objects.count(), 2)
        self.assertTrue(Notebook.objects.filter(titulo="NotebookA", descricao="A").exists())
