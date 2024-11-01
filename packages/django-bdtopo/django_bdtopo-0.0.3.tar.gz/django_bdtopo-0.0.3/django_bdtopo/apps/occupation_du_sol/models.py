# Original IGN django generated model as of 2024-10-24
from django.contrib.gis.db import models


class Haie(models.Model):
    geometrie = models.LineStringField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    hauteur = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    largeur = models.IntegerField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    identifiants_sources = models.CharField(blank=True, null=True)
    methode_d_acquisition_planimetrique = models.CharField(blank=True, null=True)
    precision_planimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )

    class Meta:
        db_table = "occupation_du_sol_haie"


class ZoneDEstran(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
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
        db_table = "occupation_du_sol_zone_d_estran"


class ZoneDeVegetation(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True)
    nature = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    methode_d_acquisition_planimetrique = models.CharField(blank=True, null=True)
    precision_planimetrique = models.FloatField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    identifiants_sources = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "occupation_du_sol_zone_de_vegetation"
