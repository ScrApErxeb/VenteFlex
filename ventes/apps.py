
from django.apps import AppConfig

class VentesConfig(AppConfig):
    name = 'ventes'

    def ready(self):
        import ventes.signals  # Assurez-vous que les signaux sont bien importés
