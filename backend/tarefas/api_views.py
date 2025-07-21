from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TarefaModel
from .serializer import TarefaSerializer

@api_view(['GET'])
def listar_tarefas(request):
    tarefas = TarefaModel.objects.all()
    serializer = TarefaSerializer(tarefas, many=True)
    return Response(serializer.data)
