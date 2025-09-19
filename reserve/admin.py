from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('chambre', 'client', 'date_arrivee', 'date_depart', 'statut', 'date_reservation')
    search_fields = ('chambre__nom', 'client__username')
    list_filter = ('statut', 'date_arrivee', 'date_depart')
