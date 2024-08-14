from django.contrib import admin
from . models import Fotografia, Categoria

class ListandoFotografias(admin.ModelAdmin):
    # Adiciona tabelas do objeto dentro do banco
    list_display = ('id','nome','descricao','categoria', 'publicada')
    
    # Filtrar por categoria
    list_filter = ('categoria',)
    
    # Itens clicaveis dentro do admin
    list_display_links = ('id','nome')
    
    # Adiciona inputs para a publicação dentro do admin
    list_editable = ('publicada',) 

# Register your models here.
admin.site.register(Fotografia, ListandoFotografias)
admin.site.register(Categoria)