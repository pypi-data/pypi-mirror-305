# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BDTOPOBatiConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "django_bdtopo.apps.bati"
    verbose_name = _("BDTOPO Bati")
