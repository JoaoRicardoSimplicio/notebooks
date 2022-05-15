import re
import requests

from bs4 import BeautifulSoup


HEADERS = (
)


class ETLNotebooks:

    URL_BASE = 'https://webscraper.io/test-sites/e-commerce/allinone'

    def __int__(self) -> None:
        self.notebooks = []

    def executar(self) -> None:
        pagina_html = self._baixa_pagina_notebooks()
        self._parser_notebooks(pagina_html)

    def _baixa_pagina_notebooks(self) -> str:
        url_notebooks = f'{self.URL_BASE}/computers/laptops'
        resposta = requests.get(url_notebooks, headers=HEADERS)
        return resposta.text

    def _parser_notebooks(self, pagina_html : str) -> None:
        soup = BeautifulSoup(pagina_html, 'html.parser')
        notebook_divs = soup.find_all('div', class_='thumbnail')
        todos_notebooks = [self._extrai_dados_notebook(notebook_div) for notebook_div in notebook_divs]
        self.notebooks = self._obtem_notebooks_lenovo(todos_notebooks)

    def _extrai_dados_notebook(self, notebook_div) -> dict:
        return {
            'descricao': notebook_div.find('p', class_='description').text,
            'titulo': notebook_div.a.get('title'),
            'preco': float(self._obtem_preco(notebook_div)),
            'reviews': int(self._obtem_quantidade_reviews(notebook_div)),
            'estrelas': len(notebook_div.find('div', class_='ratings').find_all('span'))
        }

    def _obtem_quantidade_reviews(self, notebook_div: str) -> str:
        elemento_review = notebook_div.find('div', class_='ratings').find('p', class_='pull-right')
        regex_reviews = re.search('(?P<reviews>\d+).+', elemento_review.text)
        return regex_reviews.group('reviews')

    def _obtem_preco(self, notebook_div: str) -> float:
        elemento_preco = notebook_div.find('h4', class_="pull-right price")
        regex_preco = re.search('[\$R]+ *(?P<preco>[\d\.\,]+)', elemento_preco.text)
        return regex_preco.group('preco')

    def _obtem_notebooks_lenovo(self, notebooks: list) -> list:
        regex_notebook_lenovo = re.compile('.*(?P<marca>[Ll]enovo).*')
        return [notebook for notebook in notebooks if regex_notebook_lenovo.match(notebook['titulo'])]
