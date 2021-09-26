from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _



class AwardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'awards'

    def ready(self):
        import awards.signals
