from django.contrib import admin
from .models import JournalVente, Transaction, Compte
from ventes.models import VenteSum

admin.site.register(JournalVente)
admin.site.register(Transaction)
admin.site.register(Compte)
admin.site.register(VenteSum)
