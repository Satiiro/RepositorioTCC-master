from django.urls import path

from .views import *

urlpatterns = [
    path('', TccHome.as_view() , name='index'),

    path('criar/autor/', AutorCreate.as_view(), name='criar_autor'),
    path('editar/autor/<int:pk>/', AutorUpdate.as_view(), name='editar_autor'),
    path('deletar/autor/<int:pk>/', AutorDelete.as_view(), name='deletar_autor'),
    path('tabela/autores/', AutorList.as_view(), name='tabela_autores'),

    path('criar/curso/', CursoCreate.as_view(), name='criar_curso'),
    path('editar/curso/<int:pk>/', CursoUpdate.as_view(), name='editar_curso'),
    path('deletar/curso/<int:pk>/', CursoDelete.as_view(), name='deletar_curso'),
    path('tabela/cursos/', CursoList.as_view(), name='tabela_cursos'),

    path('criar/orientador/', OrientadorCreate.as_view(), name='criar_orientador'),
    path('editar/orientador/<int:pk>/', OrientadorUpdate.as_view(), name='editar_orientador'),
    path('informacao/orientador/<int:pk>/', OrientadorDelete.as_view(), name='deletar_orientador'),
    path('tabela/orientadores/', OrientadorList.as_view(), name='tabela_orientadores'),

    path('criar/tcc/', TccCreate.as_view(), name='criar_tcc'),
    path('editar/tcc/<int:pk>/', TccUpdate.as_view(), name='editar_tcc'),
    path('deletar/tcc/<int:pk>/', TccDelete.as_view(), name='deletar_tcc'),
    path('tabela/tccs/', TccList.as_view(), name='tabela_tccs'),
    path('informacao/tcc/<int:pk>', TccDetail.as_view(), name='detalhar_tcc'),

]

