from django.db import models
from django.contrib.auth.models import User


class Fournisseur(models.Model):
    nom = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom



class Categorie(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

    def total_quantite(self):
        """Retourne la somme des stocks de tous les produits de cette catégorie."""
        return sum(produit.stock_actuel for produit in self.produits.all())


class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    prix_achat = models.IntegerField()
    prix_vente = models.IntegerField()
    stock_actuel = models.PositiveIntegerField(default=0)
    seuil_reapprovisionnement = models.PositiveIntegerField(default=10)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')

    def __str__(self):
        return self.nom

    def benefice(self):
        """ calcul du benef"""
        return self.prix_vente - self.prix_achat

    def mettre_a_jour_stock(self, quantite):
        """Mise à jour du stock du produit."""
        self.stock_actuel += quantite
        self.save()


class MouvementStock(models.Model):
    TYPE_MOUVEMENT = [
        ('ENTREE', 'Entrée'),
        ('SORTIE', 'Sortie'),
    ]

    produit = models.ForeignKey(Produit, related_name='mouvements', on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    type_mouvement = models.CharField(max_length=7, choices=TYPE_MOUVEMENT)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, null=True, blank=True, on_delete=models.SET_NULL)
    client = models.CharField(max_length=255, blank=True, null=True)
    entree_liee = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.type_mouvement} - {self.produit.nom} - {self.quantite}"

    def save(self, *args, **kwargs):
        """Mise à jour automatique du stock en fonction du mouvement."""
        if self.pk is None:  # Seulement pour les nouvelles entrées
            if self.type_mouvement == 'ENTREE':
                self.produit.mettre_a_jour_stock(self.quantite)
            elif self.type_mouvement == 'SORTIE':
                self.produit.mettre_a_jour_stock(-self.quantite)
        super().save(*args, **kwargs)


