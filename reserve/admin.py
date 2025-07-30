from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'chambre', 'date_arrivee', 'date_depart', 'statut', 'date_reservation')
    list_filter = ('statut', 'date_arrivee', 'date_depart')
    search_fields = ('client__username', 'chambre__numero')
