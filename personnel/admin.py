from django.contrib import admin
from .models import Conge, TypeConge, TitrePoste, Presence, Horaire, Departement, Employe

admin.site.register(TitrePoste)
admin.site.register(Departement)
admin.site.register(Employe)
admin.site.register(Horaire)
admin.site.register(Presence)
admin.site.register(Conge)
admin.site.register(TypeConge)
