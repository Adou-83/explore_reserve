from django.contrib import admin
from .models import Lieu

@admin.register(Lieu)
class LieuTouristiqueAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ville', 'adresse')
    search_fields = ('nom', 'ville')
