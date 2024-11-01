# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BDTOPOTransportConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "django_bdtopo.apps.transport"
    verbose_name = _("BDTOPO Transport")
