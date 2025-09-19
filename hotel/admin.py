from django.contrib import admin
from .models import Hotel, Chambre

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_hotel', 'prix_nuit')
    list_filter = ('type_hotel',)
    search_fields = ('nom', 'type_hotel')
    ordering = ('nom',)

@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'hotel', 'type_chambre', 'prix')
    list_filter = ('type_chambre', 'hotel')
    search_fields = ('nom', 'hotel__nom')
