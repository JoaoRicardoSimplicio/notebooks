from rest_framework import serializers

from notebook.models import Notebook


class NotebookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'titulo',
            'descricao',
            'reviews',
            'estrelas',
            'preco'
        )
        model = Notebook
