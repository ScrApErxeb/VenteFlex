# stock/urls.py
from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    # Liste des produits
    path('', views.liste_produits, name='lister_produits'),
    
    # Ajouter un produit
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),
    
    # Enregistrer un mouvement de stock pour un produit spécifique
    path('mouvement/<int:produit_id>/', views.ajouter_mouvement, name='enregistrer_mouvement'),
]
