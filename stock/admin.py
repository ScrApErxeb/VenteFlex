from django.contrib import admin
from .models import Categorie, Produit, MouvementStock, Fournisseur

admin.site.register(Categorie)
admin.site.register(Fournisseur)


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix_achat', 'prix_vente', 'stock_actuel', 'benefice')

@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin):
    list_display = ('produit', 'quantite', 'type_mouvement', 'date', 'user', 'fournisseur')
    list_filter = ('type_mouvement', 'date')