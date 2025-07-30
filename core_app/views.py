from django.shortcuts import render
from .models import Lieu

def liste_lieux(request):
    lieux = Lieu.objects.all()
    return render(request, 'core_app/lieu.html', {'lieu': lieux})

def accueil(request):
    return render(request, 'core_app/accueil.html')