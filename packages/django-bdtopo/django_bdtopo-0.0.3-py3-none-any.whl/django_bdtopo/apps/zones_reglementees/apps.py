# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BDTOPOZonesReglementeesConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "django_bdtopo.apps.zones_reglementees"
    verbose_name = _("BDTOPO Zones Reglementees")
