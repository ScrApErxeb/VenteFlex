from django.db import models
from django.contrib.auth.models import User


class TitrePoste(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Departement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.nom



class Horaire(models.Model):
    poste = models.ForeignKey(TitrePoste, on_delete=models.CASCADE, related_name="horaires")
    jour_de_semaine = models.CharField(max_length=9, choices=[
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'),
        ('samedi', 'Samedi'),
        ('dimanche', 'Dimanche'),
    ])
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    pause = models.DurationField(help_text="Durée de la pause (ex: 1 heure)")
    type_horaire = models.CharField(max_length=10, choices=[('fixe', 'Fixe'), ('flexible', 'Flexible')])

    def __str__(self):
        return f"{self.poste.nom} - {self.jour_de_semaine} ({self.heure_debut}-{self.heure_fin})"



class Employe(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=8)
    titre_poste = models.ForeignKey('TitrePoste', on_delete=models.SET_NULL, null=True)  # Référence au modèle TitrePoste
    departement = models.ForeignKey('Departement', on_delete=models.SET_NULL, null=True)  # Référence au modèle Departement
    date_embauche = models.DateField()
    actif = models.BooleanField(default=True)
    horaire = models.ForeignKey('Horaire', on_delete=models.CASCADE, null=True, blank=True)




    def deactiver(self):
        self.actif = False
        self.save()

    def get_horaire(self):
        return self.horaire

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.titre_poste.nom} ({self.departement.nom})"



class Presence(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="presences")
    horaire = models.ForeignKey(Horaire, on_delete=models.CASCADE, related_name="presences")
    date = models.DateField()  # Date de la présence
    heure_arrivee = models.TimeField()  # Heure d'arrivée
    heure_depart = models.TimeField()  # Heure de départ
    est_present = models.BooleanField(default=True)  # Indique si l'employé est présent ou non ce jour-là

    class Meta:
        unique_together = ('utilisateur', 'horaire', 'date')

    def __str__(self):
        return f"Présence de {self.utilisateur.username} le {self.date} - Poste: {self.horaire.poste.nom}"
    

class TypeConge(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom

class Conge(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conges")
    type_conge = models.ForeignKey(TypeConge, on_delete=models.CASCADE, related_name="conges")
    date_debut = models.DateField()  # Date de début du congé
    date_fin = models.DateField()    # Date de fin du congé
    statut = models.CharField(max_length=10, choices=[('en_attente', 'En attente'), ('approuve', 'Approuvé'), ('refuse', 'Refusé')], default='en_attente')
    commentaire = models.TextField(null=True, blank=True)  # Commentaire facultatif pour plus de détails

    def __str__(self):
        return f"{self.utilisateur.username} - {self.type_conge.nom} du {self.date_debut} au {self.date_fin} ({self.statut})"

    @property
    def duree_conge(self):
        return (self.date_fin - self.date_debut).days
