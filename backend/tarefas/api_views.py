from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import TarefaModel
from .serializer import TarefaSerializer

class TarefaViewSet(ModelViewSet):
    queryset = TarefaModel.objects.all()
    serializer_class = TarefaSerializer