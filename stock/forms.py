from django import forms
from .models import Produit, MouvementStock, Fournisseur

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['categorie','nom', 'description', 'prix_achat', 'prix_vente']

class MouvementStockForm(forms.ModelForm):
    class Meta:
        model = MouvementStock
        fields = ['produit', 'quantite', 'type_mouvement']

    