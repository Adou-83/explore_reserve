from django.urls import path
from . import views

app_name = 'reserve'

urlpatterns = [
    path('ajouter/', views.ajouter_reservation, name='ajouter_reservation'),
    path('liste/', views.liste_reservations, name='mes_reservations'),
]
