from django.db import models

# Create your models here.
class TarefaModel(models.Model):
    nome = models.CharField(max_length=100) # "CharField" é basicamente uma string e poderá ter, no máximo, 100 caracteres
    descricao = models.TextField(null=True, blank=True) # É um campo de texto maior e pode ser vazio (é o que está configurado em seus parâmetros)
    concluido = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True) # A partir do momento que a tarefa for criada, a data dela será setada

    def __str__(self):
        return self.nome
