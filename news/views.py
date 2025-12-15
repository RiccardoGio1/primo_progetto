from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista

# Create your views here.
def home(request):

    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render (request, "news/homepage.html", context)
"""
Questa funzione stampa la Navbar
E la scritta Benvenuto
"""

def articoloDetailView(request, pk):
    # articolo Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render (request, "news/articolo_detail.html", context)

"""
def home (request):
    a = []
    g = []
    for art in Articolo.objects.all():
        a.append(art.titolo)
    for gio in Giornalista.objects.all(): 
        g.append(gio.nome)
    response = str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse("<h1>" + response + "</h1>")

Questa funzione stampa:
['primo articolo!', 'Secondo articolo!']
['Guido', 'Mario', 'Nome']
"""


"""
def home(request):
    a=""
    g=""
    for art in Articolo.objects.all():
        a+=(art.titolo + "<br>")
    for gio in Giornalista.objects.all():
        g+= (gio.nome + "<br>")
    response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g
        
    
    return HttpResponse("<h1>"+response+"</h1>")

Questa funzione home stampa: 
Articoli:
primo articolo!
Secondo articolo!

Giornalisti:
Guido
Mario
Nome
"""