from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),              # Page d'accueil
    path('lieux/', views.liste_lieux, name='liste_lieux') # Liste des lieux touristiques
]
