from django.db import models

class Hotel(models.Model):
    TYPE_HOTEL_CHOICES = [
        ('Hotel', 'Hotel'),
        ('Residence', 'Residence'),
    ]
    
    nom = models.CharField(max_length=100)
    type_hotel = models.CharField(max_length=50, choices=TYPE_HOTEL_CHOICES, default='Hotel')
    prix_nuit = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        return self.nom


class Chambre(models.Model):
    TYPE_CHAMBRE_CHOICES = [
        ('Standard', 'Standard'),
        ('Suite', 'Suite'),
        ('Deluxe', 'Deluxe'),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='chambres')
    nom = models.CharField(max_length=100, default='Chambre1')
    type_chambre = models.CharField(max_length=50, choices=TYPE_CHAMBRE_CHOICES, default='Standard')
    prix = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to='chambres/', blank=True, null=True)

    def __str__(self):
        return f"{self.nom} - {self.hotel.nom}"
