from django.urls import path
from . import views
from django.views.generic import CreateView, ListView
from .views import AjouterCongeView, ListeCongesView, ModifierCongeView
from .views import ModifierEmployeView, ListeEmployesView, AjouterEmployeView
from django.contrib.auth import views as auth_views  # Import de la vue de déconnexion



app_name = 'personnel'  # Définition du namespace

urlpatterns = [

    #employé
    path('', ListeEmployesView.as_view(), name='liste_employes'),
    path('ajouter/', AjouterEmployeView.as_view(), name='ajouter_employe'),
    path('modifier/<int:pk>/', ModifierEmployeView.as_view(), name='modifier_employe'),    
    path('liste/', ListeEmployesView.as_view(), name='liste_employes'),
      

      #congés
    path('ajouterconge/', AjouterCongeView.as_view(), name='ajouter_conge'),
    path('listeconge/', ListeCongesView.as_view(), name='liste_conges'),
    path('modifierconge/<int:pk>/', ModifierCongeView.as_view(), name='modifier_conge'),

  # Connexion
    path('login/', views.login_view, name='login'),
   


  # Ajoute les vues de réinitialisation du mot de passe
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]  # Assure-toi que cette ligne existe


