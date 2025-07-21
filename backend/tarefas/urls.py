from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.routers import DefaultRouter
from . import api_views
from . import views


app_name = 'tarefas'

urlpatterns = [
    path('', views.tarefas_home, name='home'),
    path('adicionar/', views.tarefas_adicionar, name='adicionar'),
    path('remover/<int:id>', views.tarefas_remover, name='remover'),
    path('editar/<int:id>', views.tarefas_editar, name='editar'),
    path('api/', api_views.listar_tarefas, name='listar_tarefas'),
]