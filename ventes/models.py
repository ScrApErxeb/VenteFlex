from django.db import models
from personnel.models import Employe  # Lien avec l'application personnel
from stock.models import Produit  # Lien avec les produits du stock

class Client(models.Model):
    nom = models.CharField(max_length=255)
    numero = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nom

class Vente(models.Model):
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
    vendeur = models.ForeignKey(Employe, on_delete=models.CASCADE)  # Chaque vente doit avoir un vendeur
    date_vente = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Vente {self.id} - {self.date_vente.strftime('%Y-%m-%d')}"

class LigneVente(models.Model):
    vente = models.ForeignKey(Vente, related_name='lignes', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Récupérer le prix du produit et recalculer le total
        self.prix_unitaire = self.produit.prix_vente
        super().save(*args, **kwargs)
        self.vente.total = sum(l.prix_unitaire * l.quantite for l in self.vente.lignes.all())
        self.vente.save()

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"

from django.db import models
from ventes.models import Vente
from stock.models import Produit  # Assurez-vous d'importer le modèle Produit
from django.db.models import Sum

class VenteSum(models.Model):
    total_ventes = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_benefice = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"Total des ventes : {self.total_ventes}, Total des bénéfices : {self.total_benefice}"

    @classmethod
    def update_total_sum(cls):
        # Calculer la somme des prix de vente
        total_ventes = Vente.objects.aggregate(Sum('total'))['total__sum'] or 0

        # Calculer le total des bénéfices
        total_benefice = 0
        ventes = Vente.objects.all()
        for vente in ventes:
            for ligne in vente.lignes.all():  # Utiliser 'ligneventes' au lieu de 'lignevente_set'
                produit = ligne.produit  # Le produit de la ligne de vente
                benefice_par_produit = produit.prix_vente - produit.prix_achat  # Bénéfice pour ce produit
                total_benefice += benefice_par_produit * ligne.quantite  # Multiplié par la quantité du produit vendu

        # Mettre à jour ou créer l'instance de VenteSum avec les nouvelles valeurs
        vente_sum, created = cls.objects.get_or_create(id=1)
        vente_sum.total_ventes = total_ventes
        vente_sum.total_benefice = total_benefice
        vente_sum.save()
