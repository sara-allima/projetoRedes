from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_views import TarefaViewSet
from . import views

router = DefaultRouter()
router.register(r'tarefas', TarefaViewSet)
app_name = 'tarefas'

urlpatterns = [
    path('', views.tarefas_home, name='home'),
    path('adicionar/', views.tarefas_adicionar, name='adicionar'),
    path('remover/<int:id>', views.tarefas_remover, name='remover'),
    path('editar/<int:id>', views.tarefas_editar, name='editar')
]