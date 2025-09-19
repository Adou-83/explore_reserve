from django.db import models
from django.contrib.auth.models import User  


class Lieu(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lieux/', blank=True, null=True)

    def __str__(self):
        return self.nom


 
 
    

 