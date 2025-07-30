from django.contrib import admin
from .models import Hotel, Chambre, ProfilUtilisateur, Lieu

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'prix_par_nuit')
    list_filter = ('nom',)  # Par exemple on peut filtrer par nom d’hôtel

@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'numero', 'capacite')
    list_filter = ('hotel',)

@admin.register(ProfilUtilisateur)
class ProfilUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'telephone')
    list_filter = ('utilisateur',)

@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse')
    search_fields = ('nom',)
