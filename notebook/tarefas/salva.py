from notebook.models import Notebook


def salvar_notebook(dados: dict) -> None:
    notebook, created = Notebook.objects.update_or_create(
        titulo=dados['titulo'],
        descricao=dados['descricao'],
        defaults={
            'preco': dados['preco'],
            'estrelas': dados['estrelas'],
            'reviews': dados['reviews']
        }
    )
