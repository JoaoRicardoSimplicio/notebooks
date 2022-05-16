# Lista Notebooks

Use essa url para listar os notebooks

**URL** : `/`

**Método** : `GET`

**Autenticação requerida** : `NO`

**Modelo Requisição**

```bash
    curl -X GET http://127.0.0.1:8080/'
```

**Conteúdo Resposta**:
```bash
{
    "count": 4785,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 11,
            "titulo": "Lenovo ThinkPad L460",
            "descricao": "Lenovo ThinkPad L460, 14\" FHD IPS, Core i7-6600U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": 14,
            "estrelas": 4,
            "preco": "1096.02"
        },
        {
            "id": 13,
            "titulo": "Lenovo Legion Y520",
            "descricao": "Lenovo Legion Y520, 15.6\" FHD, Core i7-7700HQ, 8GB, 128 GB SSD + 1TB HDD, GTX 1050 4GB, Windows 10 Home",
            "reviews": 13,
            "estrelas": 1,
            "preco": "1133.91"
        }
    ]
}
```


---


# Obtem Notebook

Use essa url para obter um notebook

**URL** : `/<int:pk>/`

**Método** : `GET`

**Autenticação requerida** : `NO`

**Modelo Requisição**

```bash
    curl -X GET http://127.0.0.1:8080/1/'
```

**Conteúdo Resposta**:
```bash
{
    "id": 11,
    "titulo": "Lenovo ThinkPad L460",
    "descricao": "Lenovo ThinkPad L460, 14\" FHD IPS, Core i7-6600U, 8GB, 256GB SSD, Windows 10 Pro",
    "reviews": 14,
    "estrelas": 4,
    "preco": "1096.02"
}
```
