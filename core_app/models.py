from django.db import models
from django.contrib.auth.models import User

class ProfilUtilisateur(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20, default="0100000000")

    def __str__(self):
        return self.utilisateur.username

class Lieu(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='lieux/', blank=True, null=True)

    def __str__(self):
        return self.nom

class Decouverte(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='decouvertes/')
    contenu = models.TextField()
    date_publication = models.DateField(auto_now_add=True)
    auteur = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avis de {self.auteur.username} sur {self.lieu.nom}"

class Publicite(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='publicites/')
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.titre
