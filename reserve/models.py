from django.db import models
from django.contrib.auth.models import User
from hotel.models import Chambre

class Reservation(models.Model):
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date_arrivee = models.DateField()
    date_depart = models.DateField()
    statut = models.CharField(max_length=20, default='en attente')
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Réservation de {self.client.username} pour {self.chambre.nom}"
