import os
import mock

from unittest import TestCase

from notebook.servicos.crawler import ETLNotebooks


BASE_PATH = os.path.dirname(__file__)


def obtem_fixture_pagina_notebook() -> str:
    with open(f'{BASE_PATH}/fixtures/notebook_page.html', 'r') as f:
        return f.read()


class TestCrawler(TestCase):

    def setUp(self):
        self.etlnotebooks = ETLNotebooks()

    @mock.patch(
        'requests.get',
        return_value=mock.MagicMock(status_code=200, text=obtem_fixture_pagina_notebook())
    )
    def test_obtem_pagina_notebooks(self, mock_request_notebooks_page):
        self.etlnotebooks._baixa_pagina_notebooks()
        mock_request_notebooks_page.assert_called_once()

    def test_parser_pagina_notebooks(self):
        self.etlnotebooks._parser_notebooks(obtem_fixture_pagina_notebook())
        self.assertEqual(len(self.etlnotebooks.notebooks), 20)
