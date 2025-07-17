from django import forms
from .models import TarefaModel # O "." significa para pegar arquivos a partir da pasta que estamos atualmente

class TarefaForm(forms.ModelForm): # O django oferece uma interface de  criação de formulários (ModelForm), onde podemos criar um formulário automaticamente a partir de modelos
    class Meta: # A classe Meta é uma classe de configuração para o nosso formulário
        model = TarefaModel # Modelo que iremos usar para criar o nosso forms
        fields = [ # Diz para o HTML quais campos do model ele deve considerar ao fazer o formulário
            'nome',
            'descricao',
            'concluido'
        ]