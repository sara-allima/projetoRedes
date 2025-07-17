from rest_framework import serializers
from .models import TarefaModel

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarefaModel
        fields = '__all__'
