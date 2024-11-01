# Original IGN django generated model as of 2024-10-24
from django.contrib.gis.db import models


class ForetPublique(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    importance = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    identifiants_sources = models.CharField(blank=True, null=True)
    methode_d_acquisition_planimetrique = models.CharField(blank=True, null=True)
    precision_planimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )

    class Meta:
        db_table = "zones_reglementees_foret_publique"


class ParcOuReserve(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    nature_detaillee = models.CharField(blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    fictif = models.BooleanField(blank=True, null=True)
    etat_de_l_objet = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    identifiants_sources = models.CharField(blank=True, null=True)
    methode_d_acquisition_planimetrique = models.CharField(blank=True, null=True)
    precision_planimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )

    class Meta:
        db_table = "zones_reglementees_parc_ou_reserve"


class ToponymieZonesReglementees(models.Model):
    geometrie = models.PointField(srid=2154, blank=True, null=True)
    cleabs_de_l_objet = models.CharField(blank=True, null=True)
    classe_de_l_objet = models.CharField(blank=True, null=True)
    nature_de_l_objet = models.CharField(blank=True, null=True)
    graphie_du_toponyme = models.CharField(blank=True, null=True)
    source_du_toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    date_du_toponyme = models.DateField(blank=True, null=True)
    langue_du_toponyme = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "zones_reglementees_toponymie_zones_reglementees"
