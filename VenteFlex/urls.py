
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personnel/', include(('personnel.urls', 'personnel'), namespace='personnel')),  # Ajout du namespace
    path('stock/',include(('stock.urls', 'stock'), namespace = 'stock')),
]
