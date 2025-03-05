from django import forms
from .models import Employe, Conge


class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'titre_poste', 'departement', 'telephone', 'date_embauche']


class CongeForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['utilisateur', 'type_conge', 'date_debut', 'date_fin']