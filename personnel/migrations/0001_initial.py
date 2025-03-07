# Generated by Django 5.1.6 on 2025-03-05 02:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TitrePoste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeConge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour_de_semaine', models.CharField(choices=[('lundi', 'Lundi'), ('mardi', 'Mardi'), ('mercredi', 'Mercredi'), ('jeudi', 'Jeudi'), ('vendredi', 'Vendredi'), ('samedi', 'Samedi'), ('dimanche', 'Dimanche')], max_length=9)),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('pause', models.DurationField(help_text='Durée de la pause (ex: 1 heure)')),
                ('type_horaire', models.CharField(choices=[('fixe', 'Fixe'), ('flexible', 'Flexible')], max_length=10)),
                ('poste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horaires', to='personnel.titreposte')),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=8)),
                ('date_embauche', models.DateField()),
                ('actif', models.BooleanField(default=True)),
                ('departement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personnel.departement')),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('horaire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personnel.horaire')),
                ('titre_poste', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personnel.titreposte')),
            ],
        ),
        migrations.CreateModel(
            name='Conge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('statut', models.CharField(choices=[('en_attente', 'En attente'), ('approuve', 'Approuvé'), ('refuse', 'Refusé')], default='en_attente', max_length=10)),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conges', to=settings.AUTH_USER_MODEL)),
                ('type_conge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conges', to='personnel.typeconge')),
            ],
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heure_arrivee', models.TimeField()),
                ('heure_depart', models.TimeField()),
                ('est_present', models.BooleanField(default=True)),
                ('horaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presences', to='personnel.horaire')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presences', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('utilisateur', 'horaire', 'date')},
            },
        ),
    ]
