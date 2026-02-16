from django.shortcuts import render

# Create your views here.
voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
            'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
            'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
#1) lista delle materie
def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    return render(request, 'voti/materie.html', {'materie': materie})

#2) visualizzare il contenuto del seguente dizionario dei voti : studente : [(materia,voto,assenze)]:
def view_b(request):
    # Passa tutto il dizionario al template
    return render(request, 'voti/StudentiConVoto.html', {'voti': voti})

#3) visualizzare la media dei voti di ciascuno studente
def view_c(request):
    
    medie = {}
    for studente,materie in voti.items():
        somma=0
        for nomeM,voto,assenze in materie:
            somma+=voto   
        media=somma/len(materie)  # divisione per il numero corretto di materie
        medie[studente]=media #assegno a ogni studente la media dei voti
    
    return render(request, 'voti/media_studenti.html', {'medie': medie})

#4) visualizzare i voti massimo e minimo, le materie in cui si sono registrati e gli studenti che li hanno ottenuti
def view_d(request):
        
    min=10
    max=0
    StudentiMax=[]
    StudentiMin=[]
    for studente,materie in voti.items():
        for nomeM,voto,assenze in materie:
            if(voto>max):
                max=voto
            
            if(voto<min):
                min=voto
                            
    for studente,materie in voti.items():
        for nomeM,voto,assenze in materie:
            if(voto==max):
                studente_max=studente
                materie_max=nomeM
                StudentiMax.append((studente_max,materie_max))
                
            if(voto==min):
                studente_min=studente
                materie_min=nomeM
                StudentiMin.append((studente_min,materie_min))
            
        context = {
        'max':max,
        'min':min,
        'studenti_max': StudentiMax,
        'studenti_min': StudentiMin
        }    
    return render(request, 'voti/Max_Min.html',context)     
           

def index5(request):
    return render(request,'voti/index5.html')