# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BDTOPOOccupationDuSolConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "django_bdtopo.apps.occupation_du_sol"
    verbose_name = _("BDTOPO Occupation Du Sol")
