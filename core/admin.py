from django.contrib import admin
from .models import Lieu, Decouverte, ProfilUtilisateur, Commentaire, Publicite

@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ville', 'adresse')
    search_fields = ('nom', 'ville', 'adresse')

@admin.register(Decouverte)
class DecouverteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')
    search_fields = ('titre', 'auteur')
    list_filter = ('date_publication',)

@admin.register(ProfilUtilisateur)
class ProfilUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'telephone')
    search_fields = ('utilisateur__username', 'telephone')

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('lieu', 'auteur', 'date')
    search_fields = ('lieu__nom', 'auteur__username', 'contenu')
    list_filter = ('date',)

@admin.register(Publicite)
class PubliciteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_debut', 'date_fin', 'actif')
    list_filter = ('actif', 'date_debut', 'date_fin')
    search_fields = ('titre',)
