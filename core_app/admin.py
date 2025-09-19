from django.contrib import admin
from .models import Lieu, ProfilUtilisateur, Decouverte, Publicite

@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ville', 'adresse')
    search_fields = ('nom', 'ville')

@admin.register(ProfilUtilisateur)
class ProfilUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'telephone')
    search_fields = ('utilisateur__username',)

@admin.register(Decouverte)
class DecouverteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')
    search_fields = ('titre', 'auteur')
    list_filter = ('date_publication',)

@admin.register(Publicite)
class PubliciteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'actif')
    list_filter = ('actif',)
