from django.urls import path
from . views import home, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem

urlpatterns = [
    path('', home, name='home'),
    path('imagem/<int:fotografia_id>', imagem, name='imagem'),
    path('buscar', buscar, name="buscar"),
    path('nova-imagem', nova_imagem, name="nova_imagem"),
    path('editar-imagem', editar_imagem, name="editar-imagem"),
    path('deletar-imagem', deletar_imagem, name="deletar_imagem"),

]
