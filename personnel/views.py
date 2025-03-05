from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import UpdateView,CreateView, ListView
from .models import Employe, Conge
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import CongeForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from .forms import EmployeForm  # Assure-toi d'avoir un formulaire valide

class AjouterEmployeView(CreateView):
    model = Employe
    form_class = EmployeForm
    template_name = "personnel/ajouter_employe.html"
    success_url = reverse_lazy("personnel:liste_employes")

    def form_valid(self, form):
        # Création automatique du User avec prénom + 4 chiffres aléatoires
        nom_utilisateur = f"{form.cleaned_data['prenom'].lower()}{get_random_string(4, '0123456789')}"
        mot_de_passe = get_random_string(8)  # Mot de passe aléatoire

        utilisateur = User.objects.create_user(
            username=nom_utilisateur,
            first_name=form.cleaned_data['prenom'],
            last_name=form.cleaned_data['nom'],
            password=mot_de_passe
        )

        # Associer l'utilisateur à l'employé avant l'enregistrement
        employe = form.save(commit=False)
        employe.utilisateur = utilisateur
        employe.save()

        return super().form_valid(form)


class ModifierEmployeView(UpdateView):
    model = Employe
    form_class = EmployeForm
    template_name = "personnel/modifier_employe.html"
    success_url = reverse_lazy("personnel:liste_employes")  # Redirection après modification


class ListeEmployesView(ListView):
    model = Employe
    template_name = "personnel/liste_employes.html"
    context_object_name = "employes"


class AjouterCongeView(CreateView):
    model = Conge
    form_class = CongeForm
    template_name = "personnel/ajouter_conge.html"
    success_url = reverse_lazy("personnel:liste_conges")


class ListeCongesView(ListView):
    model = Conge
    template_name = "personnel/liste_conges.html"
    context_object_name = 'conges'  # Nom de la variable pour la liste dans le template


class ModifierCongeView(UpdateView):
    model = Conge
    form_class = CongeForm
    template_name = "personnel/modifier_conge.html"
    success_url = reverse_lazy("personnel:liste_conges")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authentifier l'utilisateur
            user = form.get_user()
            login(request, user)
            # Rediriger vers une page spécifique après la connexion (par exemple, la liste des employés)
            return redirect('liste_employes')  # Remplace par l'URL appropriée
    else:
        form = AuthenticationForm()
    return render(request, 'personnel/login.html', {'form': form})