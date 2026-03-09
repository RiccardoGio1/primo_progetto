from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignUpForm

# Create your views here.
def signup(request):    #x Registrarsi
    
    if (request.method)=='POST':
        form = SignUpForm(request.POST) #crea l'istanza con l'inupt dell'utente
        
        if(form.is_valid()): #effettua la validazione
            user=  form.save()
            login(request,user)
            return redirect('/')
        
    else: #richiesta di tipo get mostro il form vuoto
        form= SignUpForm()
    
    return render(request, 'registration/signup.html', {'form':form})



"""
# Create your views here.
def signup(request):    #x Registrarsi
    
    if (request.method)=='POST':
        form = SignUpForm(request.POST) #crea l'istanza con l'inupt dell'utente
        
        if(form.is_valid()): #effettua la validazione
            form.save()
            return redirect('login')  #che si può personalizzare
        
    else: #richiesta di tipo get mostro il form vuoto
        form= SignUpForm()
    
    return render(request, 'registration/signup.html', {'form':form})

"""