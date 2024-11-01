# Original IGN django generated model as of 2024-10-24
from django.contrib.gis.db import models


class Canalisation(models.Model):
    geometrie = models.LineStringField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    position_par_rapport_au_sol = models.CharField(blank=True, null=True)
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
        db_table = "services_et_activites_canalisation"


class Erp(models.Model):
    geometrie = models.PointField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    id_reference = models.CharField(max_length=24, blank=True, null=True)
    categorie = models.CharField(blank=True, null=True)
    type_principal = models.CharField(max_length=24, blank=True, null=True)
    types_secondaires = models.CharField(max_length=24, blank=True, null=True)
    activite_principale = models.CharField(blank=True, null=True)
    activites_secondaires = models.CharField(blank=True, null=True)
    libelle = models.CharField(blank=True, null=True)
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
    public = models.BooleanField(blank=True, null=True)
    ouvert = models.BooleanField(blank=True, null=True)
    capacite_d_accueil_du_public = models.IntegerField(blank=True, null=True)
    capacite_d_hebergement = models.IntegerField(blank=True, null=True)
    origine_de_la_geometrie = models.CharField(blank=True, null=True)
    type_de_localisation = models.CharField(blank=True, null=True)
    validation_ign = models.BooleanField(blank=True, null=True)
    insee_commune = models.CharField(max_length=5, blank=True, null=True)
    numero_siret = models.CharField(max_length=14, blank=True, null=True)
    adresse_numero = models.CharField(max_length=15, blank=True, null=True)
    adresse_indice_de_repetition = models.CharField(max_length=9, blank=True, null=True)
    adresse_designation_de_l_entree = models.CharField(blank=True, null=True)
    adresse_nom_1 = models.CharField(blank=True, null=True)
    adresse_nom_2 = models.CharField(blank=True, null=True)
    code_postal = models.CharField(max_length=5, blank=True, null=True)
    liens_vers_batiment = models.CharField(blank=True, null=True)
    liens_vers_enceinte = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "services_et_activites_erp"


class LigneElectrique(models.Model):
    geometrie = models.LineStringField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    voltage = models.CharField(blank=True, null=True)
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
        db_table = "services_et_activites_ligne_electrique"


class PosteDeTransformation(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
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
        db_table = "services_et_activites_poste_de_transformation"


class ToponymieServicesEtActivites(models.Model):
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
        db_table = "services_et_activites_toponymie_services_et_activites"


class ZoneDActiviteOuDInteret(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    categorie = models.CharField(blank=True, null=True)
    nature = models.CharField(blank=True, null=True)
    nature_detaillee = models.CharField(blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    importance = models.CharField(blank=True, null=True)
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
    identifiant_voie_ban = models.CharField(blank=True, null=True)
    nom_commercial = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "services_et_activites_zone_d_activite_ou_d_interet"

    def __str__(self):
        return str(self.cleabs)
