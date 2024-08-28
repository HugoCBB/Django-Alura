from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from . form import FotografiaForms
from . models import Fotografia

# Responsavel por mostrar os dados retirados do banco para o template
# Order_by: ordena o itens criados como sendo o primeiro o mais novo a ser adicionado
# Filter: filtra por cada item publicado
def home(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuario não logado')
        return redirect('login')

    fotografia = Fotografia.objects.order_by('data').filter(publicada=True)
    return render(request,'galeria/home.html',{"cards":fotografia})

def imagem(request, fotografia_id):
    if not request.user.is_authenticated:
        messages.error(request,'Usuario não logado')
        return redirect('login')
    
    fotografia = get_object_or_404(Fotografia, pk=fotografia_id)
    return render(request, 'galeria/imagem.html', {"fotografia":fotografia})

# Viwer responsavel por criar um formulario
# def FotoFR(request):
#     form = FotografiaForm(request.POST or None)
#     try:
#         if form.is_valid:
#             form.save(request)
#             return home(request)
#     except Exception as e:
#         print(e)
    
#     return render(request,'galeria/form.html',{"form":form})

def buscar(request):
    fotografia = Fotografia.objects.order_by('data').filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografia = fotografia.filter(nome__icontains=nome_a_buscar)
    
    return render(request, 'galeria/buscar.html',{'cards':fotografia})


def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuario não logado')
        return redirect('login')
    
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, 'Nova fotogradia adicionada com sucesso')
            return redirect('home')

    form = FotografiaForms()
    return render(request, 'galeria/nova_imagem.html', {'form':form})

def editar_imagem(request):
    pass
def deletar_imagem(request):
    pass