from django.contrib import admin
from .models import Client, Vente, LigneVente

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'numero')

class LigneVenteInline(admin.TabularInline):
    model = LigneVente
    extra = 1

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_vente', 'client', 'vendeur', 'total')
    inlines = [LigneVenteInline]

@admin.register(LigneVente)
class LigneVenteAdmin(admin.ModelAdmin):
    list_display = ('vente', 'produit', 'quantite', 'prix_unitaire')
