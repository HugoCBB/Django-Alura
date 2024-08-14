from django.urls import path
from . views import home, imagem,FotoFR, buscar

urlpatterns = [
    path('', home, name='home'),
    path('imagem/<int:fotografia_id>', imagem, name='imagem'),
    path('novo/', FotoFR),
    path('buscar', buscar, name="buscar")

]
