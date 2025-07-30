from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_reservations, name='liste_reservations'),
    path('ajouter/', views.ajouter_reservation, name='ajouter_reservation'),
]
