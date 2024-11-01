# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BDTOPOLieuxNommesConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "django_bdtopo.apps.lieux_nommes"
    verbose_name = _("BDTOPO Lieux Nommes")
