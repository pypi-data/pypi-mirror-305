# Original IGN django generated model as of 2024-10-24
from django.contrib.gis.db import models


class Batiment(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    usage_1 = models.CharField(blank=True, null=True)
    usage_2 = models.CharField(blank=True, null=True)
    construction_legere = models.BooleanField(blank=True, null=True)
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
    methode_d_acquisition_altimetrique = models.CharField(blank=True, null=True)
    precision_altimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )
    nombre_de_logements = models.IntegerField(blank=True, null=True)
    nombre_d_etages = models.IntegerField(blank=True, null=True)
    materiaux_des_murs = models.CharField(max_length=2, blank=True, null=True)
    materiaux_de_la_toiture = models.CharField(max_length=2, blank=True, null=True)
    hauteur = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    altitude_minimale_sol = models.DecimalField(
        max_digits=7, decimal_places=1, blank=True, null=True
    )
    altitude_minimale_toit = models.DecimalField(
        max_digits=7, decimal_places=1, blank=True, null=True
    )
    altitude_maximale_toit = models.DecimalField(
        max_digits=7, decimal_places=1, blank=True, null=True
    )
    altitude_maximale_sol = models.DecimalField(
        max_digits=7, decimal_places=1, blank=True, null=True
    )
    origine_du_batiment = models.CharField(blank=True, null=True)
    appariement_fichiers_fonciers = models.CharField(
        max_length=32, blank=True, null=True
    )

    class Meta:
        db_table = "bati_batiment"


class Cimetiere(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    nature_detaillee = models.CharField(blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    importance = models.CharField(blank=True, null=True)
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
    methode_d_acquisition_altimetrique = models.CharField(blank=True, null=True)
    precision_altimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )

    class Meta:
        db_table = "bati_cimetiere"


class ConstructionLineaire(models.Model):
    geometrie = models.LineStringField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    nature_detaillee = models.CharField(blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    importance = models.CharField(blank=True, null=True)
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
    methode_d_acquisition_altimetrique = models.CharField(blank=True, null=True)
    precision_altimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )

    class Meta:
        db_table = "bati_construction_lineaire"


class ConstructionPonctuelle(models.Model):
    geometrie = models.PointField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    nature_detaillee = models.CharField(blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    importance = models.CharField(blank=True, null=True)
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
    methode_d_acquisition_altimetrique = models.CharField(blank=True, null=True)
    precision_altimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )
    hauteur = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)

    class Meta:
        db_table = "bati_construction_ponctuelle"


class ConstructionSurfacique(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    nature_detaillee = models.CharField(blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    importance = models.CharField(blank=True, null=True)
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
    methode_d_acquisition_altimetrique = models.CharField(blank=True, null=True)
    precision_altimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )

    class Meta:
        db_table = "bati_construction_surfacique"


class LigneOrographique(models.Model):
    geometrie = models.LineStringField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    etat_de_l_objet = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    identifiants_sources = models.CharField(blank=True, null=True)
    methode_d_acquisition_planimetrique = models.CharField(blank=True, null=True)
    precision_planimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )
    methode_d_acquisition_altimetrique = models.CharField(blank=True, null=True)
    precision_altimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )

    class Meta:
        db_table = "bati_ligne_orographique"


class Pylone(models.Model):
    geometrie = models.PointField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
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
    methode_d_acquisition_altimetrique = models.CharField(blank=True, null=True)
    precision_altimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )
    hauteur = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)

    class Meta:
        db_table = "bati_pylone"


class Reservoir(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
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
    methode_d_acquisition_altimetrique = models.CharField(blank=True, null=True)
    precision_altimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )
    altitude_minimale_sol = models.DecimalField(
        max_digits=7, decimal_places=1, blank=True, null=True
    )
    altitude_minimale_toit = models.DecimalField(
        max_digits=7, decimal_places=1, blank=True, null=True
    )
    hauteur = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    altitude_maximale_toit = models.DecimalField(
        max_digits=7, decimal_places=1, blank=True, null=True
    )
    altitude_maximale_sol = models.DecimalField(
        max_digits=7, decimal_places=1, blank=True, null=True
    )
    origine_du_batiment = models.CharField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = "bati_reservoir"


class TerrainDeSport(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    nature_detaillee = models.CharField(blank=True, null=True)
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
    methode_d_acquisition_altimetrique = models.CharField(blank=True, null=True)
    precision_altimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )

    class Meta:
        db_table = "bati_terrain_de_sport"


class ToponymieBati(models.Model):
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
        db_table = "bati_toponymie_bati"
