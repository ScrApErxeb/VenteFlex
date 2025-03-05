from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import VenteSum  # Importez le modèle VenteSum de l'application ventes
from compta.models import JournalVente  # Importez le modèle de l'autre application
from .models import Vente  # Importez le modèle Vente de l'application ventes

@receiver(post_save, sender=Vente)
def create_journal_vente(sender, instance, created, **kwargs):
    if created:  # Si la vente est créée
        # Créer une entrée correspondante dans le JournalVente
        JournalVente.objects.create(vente=instance)


@receiver(post_save, sender=JournalVente)
def update_vente_sum(sender, instance, created, **kwargs):
    if created:  # Ne réagir qu'à la création d'un JournalVente
        VenteSum.update_total_sum()  # Mettre à jour la somme totale des ventes