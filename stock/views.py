from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, MouvementStock
from django.contrib.auth.decorators import login_required
from .forms import ProduitForm, MouvementStockForm

# Vue pour afficher tous les produits
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'stock/liste_produits.html', {'produits': produits})

# Vue pour ajouter un produit
def ajouter_produit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock:lister_produits')
    else:
        form = ProduitForm()
    return render(request, 'stock/ajouter_produit.html', {'form': form})

def ajouter_mouvement(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)  # Récupérer l'objet produit
    if request.method == 'POST':
        mouvement = MouvementStock(
            produit=produit,  # Assigner l'objet produit
            quantite=request.POST['quantite'],
            type_mouvement=request.POST['type_mouvement'],
            user=request.user,  # Assigner l'utilisateur connecté
            fournisseur=request.POST.get('fournisseur'),
            client=request.POST.get('client'),
            entree_liee=request.POST.get('entree_liee')
        )
        mouvement.save()
        return redirect('some_view')
    return render(request, 'stock/enregistrer_mouvement.html', {'produit': produit})
