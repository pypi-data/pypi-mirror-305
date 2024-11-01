# Original IGN django generated model as of 2024-10-24
from django.contrib.gis.db import models


class BassinVersantTopographique(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    liens_vers_cours_d_eau_principal = models.CharField(blank=True, null=True)
    code_bdcarthage = models.CharField(max_length=4, blank=True, null=True)
    code_du_bassin_hydrographique = models.CharField(
        max_length=2, blank=True, null=True
    )
    commentaire_sur_l_objet_hydro = models.CharField(blank=True, null=True)
    origine = models.CharField(blank=True, null=True)
    bassin_fluvial = models.CharField(max_length=30, blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    mode_d_obtention_des_coordonnees = models.CharField(blank=True, null=True)
    precision_planimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )
    methode_d_acquisition_planimetrique = models.CharField(blank=True, null=True)
    identifiants_sources = models.CharField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    libelle_du_bassin_hydrographique = models.CharField(
        max_length=30, blank=True, null=True
    )
    toponyme = models.CharField(blank=True, null=True)
    code_hydrographique = models.CharField(max_length=19, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)

    class Meta:
        db_table = "hydrographie_bassin_versant_topographique"


class CoursDEau(models.Model):
    geometrie = models.MultiLineStringField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_hydrographique = models.CharField(max_length=19, blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    importance = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    identifiants_sources = models.CharField(blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    influence_de_la_maree = models.BooleanField(blank=True, null=True)
    caractere_permanent = models.BooleanField(blank=True, null=True)
    commentaire_sur_l_objet_hydro = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "hydrographie_cours_d_eau"


class DetailHydrographique(models.Model):
    geometrie = models.PointField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    nature_detaillee = models.CharField(blank=True, null=True)
    persistance = models.CharField(blank=True, null=True)
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
    identifiant_voie_ban = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "hydrographie_detail_hydrographique"


class LimiteTerreMer(models.Model):
    geometrie = models.LineStringField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_hydrographique = models.CharField(max_length=19, blank=True, null=True)
    code_du_pays = models.CharField(max_length=8, blank=True, null=True)
    type_de_limite = models.CharField(blank=True, null=True)
    niveau = models.CharField(blank=True, null=True)
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
    mode_d_obtention_des_coordonnees = models.CharField(blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    origine = models.CharField(blank=True, null=True)
    commentaire_sur_l_objet_hydro = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "hydrographie_limite_terre_mer"


class NoeudHydrographique(models.Model):
    geometrie = models.PointField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_hydrographique = models.CharField(max_length=19, blank=True, null=True)
    code_du_pays = models.CharField(max_length=8, blank=True, null=True)
    categorie = models.CharField(blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
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
    mode_d_obtention_des_coordonnees = models.CharField(blank=True, null=True)
    mode_d_obtention_de_l_altitude = models.CharField(blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    commentaire_sur_l_objet_hydro = models.CharField(blank=True, null=True)
    liens_vers_cours_d_eau_amont = models.CharField(blank=True, null=True)
    liens_vers_cours_d_eau_aval = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "hydrographie_noeud_hydrographique"


class PlanDEau(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_hydrographique = models.CharField(max_length=19, blank=True, null=True)
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
    statut = models.CharField(blank=True, null=True)
    influence_de_la_maree = models.BooleanField(blank=True, null=True)
    caractere_permanent = models.BooleanField(blank=True, null=True)
    altitude_moyenne = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )
    referentiel_de_l_altitude_moyenne = models.CharField(
        max_length=30, blank=True, null=True
    )
    mode_d_obtention_de_l_altitude_moy = models.CharField(blank=True, null=True)
    precision_de_l_altitude_moyenne = models.CharField(blank=True, null=True)
    hauteur_d_eau_maximale = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    mode_d_obtention_de_la_hauteur = models.CharField(blank=True, null=True)
    commentaire_sur_l_objet_hydro = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "hydrographie_plan_d_eau"


class SurfaceHydrographique(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_hydrographique = models.CharField(max_length=19, blank=True, null=True)
    code_du_pays = models.CharField(max_length=8, blank=True, null=True)
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
    mode_d_obtention_des_coordonnees = models.CharField(blank=True, null=True)
    mode_d_obtention_de_l_altitude = models.CharField(blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    persistance = models.CharField(blank=True, null=True)
    salinite = models.BooleanField(blank=True, null=True)
    origine = models.CharField(blank=True, null=True)
    commentaire_sur_l_objet_hydro = models.CharField(blank=True, null=True)
    liens_vers_plan_d_eau = models.CharField(blank=True, null=True)
    liens_vers_cours_d_eau = models.CharField(blank=True, null=True)
    lien_vers_entite_de_transition = models.CharField(
        max_length=24, blank=True, null=True
    )
    cpx_toponyme_de_plan_d_eau = models.CharField(blank=True, null=True)
    cpx_toponyme_de_cours_d_eau = models.CharField(blank=True, null=True)
    cpx_toponyme_d_entite_de_transition = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "hydrographie_surface_hydrographique"


class ToponymieHydrographie(models.Model):
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
        db_table = "hydrographie_toponymie_hydrographie"


class TronconHydrographique(models.Model):
    geometrie = models.LineStringField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_hydrographique = models.CharField(max_length=19, blank=True, null=True)
    code_du_pays = models.CharField(max_length=8, blank=True, null=True)
    nature = models.CharField(blank=True, null=True)
    fictif = models.BooleanField(blank=True, null=True)
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
    mode_d_obtention_des_coordonnees = models.CharField(blank=True, null=True)
    mode_d_obtention_de_l_altitude = models.CharField(blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    persistance = models.CharField(blank=True, null=True)
    fosse = models.BooleanField(blank=True, null=True)
    navigabilite = models.BooleanField(blank=True, null=True)
    salinite = models.BooleanField(blank=True, null=True)
    numero_d_ordre = models.CharField(max_length=2, blank=True, null=True)
    strategie_de_classement = models.CharField(max_length=30, blank=True, null=True)
    origine = models.CharField(blank=True, null=True)
    perimetre_d_utilisation_ou_origine = models.CharField(
        max_length=30, blank=True, null=True
    )
    sens_de_l_ecoulement = models.CharField(blank=True, null=True)
    reseau_principal_coulant = models.BooleanField(blank=True, null=True)
    delimitation = models.BooleanField(blank=True, null=True)
    classe_de_largeur = models.CharField(blank=True, null=True)
    type_de_bras = models.CharField(blank=True, null=True)
    commentaire_sur_l_objet_hydro = models.CharField(blank=True, null=True)
    code_du_cours_d_eau_bdcarthage = models.CharField(
        max_length=8, blank=True, null=True
    )
    liens_vers_cours_d_eau = models.CharField(blank=True, null=True)
    liens_vers_surface_hydrographique = models.CharField(blank=True, null=True)
    lien_vers_entite_de_transition = models.CharField(
        max_length=24, blank=True, null=True
    )
    cpx_toponyme_de_cours_d_eau = models.CharField(blank=True, null=True)
    cpx_toponyme_d_entite_de_transition = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "hydrographie_troncon_hydrographique"
