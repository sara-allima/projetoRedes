from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import TarefaModel
from django.http import HttpRequest, HttpResponse


# Create your views here.
def tarefas_home(request):
    contexto = {
        "nome": "Sara",
        'tarefas': TarefaModel.objects.all() # Estamos enviando todos os registros dos objetos tarefas que foram criados
    }
    return render(request, 'tarefas/home.html', contexto)
def tarefas_adicionar(request:HttpRequest):
    print('Carregando view de adicionar tarefas_adicionar')
    if request.method == 'POST':
        formulario = TarefaForm(request.POST) # Pega todas as informações do formulário
        if formulario.is_valid(): # Verifica se as informações do formulário são válidas
            formulario.save() # Se as informações forem válidas, salva os dados
            return redirect('tarefas:home')

    contexto = {
        'form': TarefaForm
    }
    return render(request, 'tarefas/adicionar.html', contexto)
def tarefas_remover(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel ,id = id) # Ele vai tentar obter um item do banco de dados, se o objeto não for encontrado, vai retornar um erro 404
    tarefa.delete()
    return redirect('tarefas:home')
def tarefas_editar(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method == 'POST':
        formulario = TarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')
    formulario = TarefaForm(instance=tarefa)  # Cria um formulário novo, mas com os dados já inseridos (Esses dados vem da variável "tarefa" que acessamos com o id)
    contexto = {
        'form': formulario
    }
    return render(request, 'tarefas/editar.html', contexto)