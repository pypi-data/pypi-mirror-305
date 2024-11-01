# Django
from django.contrib.gis import admin
from django.contrib.gis.admin.options import GISModelAdmin

# Local application / specific library imports
from .models import ZoneDActiviteOuDInteret


@admin.register(ZoneDActiviteOuDInteret)
class ZoneDActiviteOuDInteretAdmin(GISModelAdmin):
    list_display = ("cleabs",)
    # search_fields = ("nom_officiel", "code_insee", "code_postal",)
