# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BDTOPOConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "django_bdtopo"
    verbose_name = _("Django BDTOPO")
