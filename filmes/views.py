from django.shortcuts import render

filmes = [
    {
        'id': 1,
        'titulo': 'Interestelar',
        'categoria': 'Ficção Científica',
        'descricao': 'Viagem espacial em busca da sobrevivência humana.',
        'diretor': 'Christopher Nolan',
        'ano': 2014
    },
    {
        'id': 2,
        'titulo': 'Batman Begins',
        'categoria': 'Ação',
        'descricao': 'A origem do Batman.',
        'diretor': 'Christopher Nolan',
        'ano': 2005
    },
    {
        'id': 3,
        'titulo': 'Vingadores',
        'categoria': 'Super-herói',
        'descricao': 'Os maiores heróis unidos.',
        'diretor': 'Joss Whedon',
        'ano': 2012
    },
]

def home(request):
    return render(request, 'filmes/home.html')

def lista_filmes(request):
    context = {
        'filmes': filmes
    }

    return render(request, 'filmes/lista.html', context)

def detalhe_filme(request, id):
    filme = None

    for item in filmes:
        if item['id'] == id:
            filme = item

    context = {
        'filme': filme
    }

    return render(request, 'filmes/detalhe.html', context)