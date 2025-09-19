from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from .models import Lieu, Decouverte

# Accueil
def accueil(request):
    lieux = Lieu.objects.all()[:5]           # exemple : 5 lieux
    decouvertes = Decouverte.objects.all()[:5]  # exemple : 5 découvertes
    return render(request, 'core_app/accueil.html', {'lieux': lieux, 'decouvertes': decouvertes})

# Liste des lieux
def liste_lieux(request):
    lieux = Lieu.objects.all()
    return render(request, 'core_app/liste_lieux.html', {'lieux': lieux})

# Détail d'un lieu
def detail_lieu(request, pk):
    lieu = get_object_or_404(Lieu, pk=pk)
    commentaires = lieu.commentaires.all() if hasattr(lieu, 'commentaires') else []
    return render(request, 'core_app/detail_lieu.html', {'lieu': lieu, 'commentaires': commentaires})

# Liste des découvertes
def page_decouverte(request):
    decouvertes = Decouverte.objects.all()
    return render(request, 'core_app/decouverte.html', {'decouvertes': decouvertes})

# Détail d'une découverte

def detail_decouverte(request, pk):
    # Récupère la découverte correspondant à l'id (pk)
    decouverte = get_object_or_404(Decouverte, pk=pk)
    return render(request, 'core_app/decouverte_detail.html', {'decouverte': decouverte})
# Inscription
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core_app:accueil')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Connexion
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core_app:accueil')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Déconnexion
def logout_view(request):
    logout(request)
    return redirect('core_app:accueil')
