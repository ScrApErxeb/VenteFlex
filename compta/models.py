# Application Comptabilité pour VenteFlex

from django.db import models
from ventes.models import Vente

class JournalVente(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    date_enregistrement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Journal Vente {self.vente.id} - {self.date_enregistrement}"


class Compte(models.Model):
    TYPE_CHOICES = [
        ('CAISSE', 'Caisse'),
        ('BANQUE', 'Banque'),
        ('CREDIT', 'Crédit'),
    ]
    nom = models.CharField(max_length=255)
    type_compte = models.CharField(max_length=10, choices=TYPE_CHOICES, default='CAISSE')
    solde = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.nom} ({self.type_compte}) - Solde: {self.solde}€"

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('ENTREE', 'Entrée'),
        ('SORTIE', 'Sortie'),
    ]
    vente = models.ForeignKey(Vente, on_delete=models.SET_NULL, null=True, blank=True)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    type_transaction = models.CharField(max_length=10, choices=TYPE_CHOICES)
    date_transaction = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type_transaction} - {self.montant}€ ({self.date_transaction})"


