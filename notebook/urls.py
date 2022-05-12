from django.urls import path

from notebook.views import (
    NotebookListView,
    NotebookRetrieveView
)


app_name = 'notebooks'


urlpatterns = [
    path('', NotebookListView.as_view(), name='notebooks'),
    path('<int:pk>/', NotebookRetrieveView.as_view(), name='notebooks')
]
