from django.shortcuts import render
import random

# Create your views here.
def index3(request):
    return render(request,"prova_pratica_0/index3.html")

def somma(request):
    var1=random.randint(1,10)
    var2=random.randint(1,10)
    context={
        'var1': var1,
        'var2':var2,
        'somma':var1+var2
    }
    return render(request,"prova_pratica_0/somma.html",context)

def media(request):
    list2= [1,2,3,4,5,6,7,8,9,10]
    somma=0
    media=0
    i=0
    while(i<10):
        somma+= list2[i]
        i+=1
    media=somma/10

    context={
        'list2': [1,2,3,4,5,6,7,8,9,10],
        'media':media
    }
    return render(request,"prova_pratica_0/media.html",context)
