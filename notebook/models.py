from django.db import models


class Notebook(models.Model):
    titulo = models.CharField(max_length=40) 
    descricao = models.TextField()
    reviews = models.IntegerField()
    estrelas = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_edicao = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('titulo', 'descricao')

    def __str__(self):
        return self.titulo
