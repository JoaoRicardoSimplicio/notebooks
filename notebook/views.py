from rest_framework import generics
from rest_framework.filters import OrderingFilter

from notebook.models import Notebook
from notebook.serializer import NotebookSerializer


class NotebookListView(generics.ListAPIView):

    description = 'Lista todos os notebooks'
    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['preco', 'reviews', 'estrelas']
    ordering = 'preco'


class NotebookRetrieveView(generics.RetrieveAPIView):

    description = 'Obtem notebook específico'
    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()
    lookup_fields = ['id']
