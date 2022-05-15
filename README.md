# Notebooks

Aplicação que obtem informações de notebooks no site `https://webscraper.io/test-sites/e-commerce/allinone`
e as disponibiliza via api. Estão sendo obtidos todos os notebooks do site, entretanto, apenas os
notebooks da marca `Lenovo` estão sendo preservados pelo crawler.



### Índice

[Requirements](#requirements)
[Testes](#testes)



### Requirements


- Python 3.8.*
- docker-compose 1.29.*



#### Executando o projeto 


Crie um ambiente virtual
```bash
$ python3.8 -m venv env
```

Ative o ambiente virtual
```bash
$ source env/bin/activate
```

Instale as dependências:
```bash
$ pip install -r core/requirements/base.txt
```

Suba os containers da stack
```bash
$ docker-compose up -d
```

Rode as migrations do projeto
```bash
DJANGO_SETTINGS_MODULE=core.settings.base python3 manage.py migrate
```



### Testes


Rode o tox:
```bash
$ pytest
```
