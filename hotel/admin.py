from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'prix_par_nuit')  # supprime 'ville'
    list_filter = ('type',)  # supprime 'ville'
