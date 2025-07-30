from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    prix_par_nuit = models.DecimalField(max_digits=10, decimal_places=2, default=10000)

    def __str__(self):
        return self.nom

class Chambre(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    capacite = models.IntegerField(default=2)

    def __str__(self):
        return f"Chambre {self.numero} - {self.hotel.nom}"

class ProfilUtilisateur(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20, default="0100000000")

    def __str__(self):
        return self.utilisateur.username

class Lieu(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100, default='')  # Champ ville avec valeur par défaut
    image = models.ImageField(upload_to='lieux/', blank=True, null=True)

    def __str__(self):
        return self.nom
