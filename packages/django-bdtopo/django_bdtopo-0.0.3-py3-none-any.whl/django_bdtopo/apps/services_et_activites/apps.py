# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BDTOPOServicesEtActivitesConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "django_bdtopo.apps.services_et_activites"
    verbose_name = _("BDTOPO Services Et Activites")
