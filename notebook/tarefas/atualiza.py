from notebook.tarefas.salva import salvar_notebook

from notebook.servicos.crawler import ETLNotebooks


def atualiza_notebooks() -> None:
    etlnotebooks = ETLNotebooks()
    etlnotebooks.executar()
    for notebook in etlnotebooks.notebooks:
        salvar_notebook(notebook)
    
