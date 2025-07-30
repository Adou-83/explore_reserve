from django.db import models

class Hotel(models.Model):
    TYPE_CHOICES = [
        ('hotel', 'Hôtel'),
        ('residence', 'Résidence'),
    ]

    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='hotel')
    prix_par_nuit = models.DecimalField(max_digits=10, decimal_places=2, default=10000)

    def __str__(self):
        return f"{self.nom} ({self.get_type_display()})"

class Chambre(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='chambres')
    numero = models.CharField(max_length=10)
    type_chambre = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Chambre {self.numero} - {self.type_chambre} - {self.hotel.nom}"
