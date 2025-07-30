from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'adresse', 'prix_par_nuit')
    list_filter = ('type',)
    search_fields = ('nom', 'adresse')
