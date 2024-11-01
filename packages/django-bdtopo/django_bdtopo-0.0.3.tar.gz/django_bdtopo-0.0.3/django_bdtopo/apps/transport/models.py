# Original IGN django generated model as of 2024-10-24
from django.contrib.gis.db import models


class Aerodrome(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    categorie = models.CharField(blank=True, null=True)
    nature = models.CharField(blank=True, null=True)
    usage = models.CharField(blank=True, null=True)
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
    altitude = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )
    code_icao = models.CharField(max_length=4, blank=True, null=True)
    code_iata = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        db_table = "transport_aerodrome"


class EquipementDeTransport(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    nature_detaillee = models.CharField(blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    importance = models.CharField(blank=True, null=True)
    numero = models.CharField(max_length=12, blank=True, null=True)
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
    methode_d_acquisition_altimetrique = models.CharField(blank=True, null=True)
    precision_altimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )
    identifiant_voie_ban = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "transport_equipement_de_transport"


class ItineraireAutre(models.Model):
    geometrie = models.MultiLineStringField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    nature_detaillee = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    identifiants_sources = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "transport_itineraire_autre"


class NonCommunication(models.Model):
    geometrie = models.PointField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    lien_vers_troncon_entree = models.CharField(max_length=24, blank=True, null=True)
    liens_vers_troncon_sortie = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "transport_non_communication"


class PisteDAerodrome(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    fonction = models.CharField(blank=True, null=True)
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
        db_table = "transport_piste_d_aerodrome"


class PointDAcces(models.Model):
    geometrie = models.PointField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    methode_d_acquisition_planimetrique = models.CharField(blank=True, null=True)
    precision_planimetrique = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )
    sens = models.CharField(blank=True, null=True)
    mode = models.CharField(blank=True, null=True)
    lien_vers_point_d_interet = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        db_table = "transport_point_d_acces"


class PointDeRepere(models.Model):
    geometrie = models.PointField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    identifiants_sources = models.CharField(blank=True, null=True)
    route = models.CharField(max_length=18, blank=True, null=True)
    numero = models.CharField(max_length=5, blank=True, null=True)
    abscisse = models.IntegerField(blank=True, null=True)
    ordre = models.FloatField(blank=True, null=True)
    cote = models.CharField(blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    type_de_pr = models.CharField(blank=True, null=True)
    libelle = models.CharField(blank=True, null=True)
    identifiant_de_section = models.CharField(blank=True, null=True)
    code_insee_du_departement = models.CharField(max_length=3, blank=True, null=True)
    lien_vers_route_nommee = models.CharField(max_length=24, blank=True, null=True)
    gestionnaire = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "transport_point_de_repere"


class PointDuReseau(models.Model):
    geometrie = models.PointField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    nature_detaillee = models.CharField(blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
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
    identifiant_voie_ban = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "transport_point_du_reseau"


class RouteNumeroteeOuNommee(models.Model):
    geometrie = models.MultiLineStringField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    type_de_route = models.CharField(blank=True, null=True)
    numero = models.CharField(max_length=16, blank=True, null=True)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    identifiants_sources = models.CharField(blank=True, null=True)
    gestionnaire = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "transport_route_numerotee_ou_nommee"


class SectionDePointsDeRepere(models.Model):
    geometrie = models.LineStringField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    identifiant_de_section = models.CharField(blank=True, null=True)
    numero_de_route = models.CharField(blank=True, null=True)
    gestionnaire = models.CharField(blank=True, null=True)
    lien_vers_route_nommee = models.CharField(max_length=24, blank=True, null=True)
    code_insee_du_departement = models.CharField(max_length=3, blank=True, null=True)
    cote = models.CharField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "transport_section_de_points_de_repere"


class ToponymieTransport(models.Model):
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
        db_table = "transport_toponymie_transport"


class TransportParCable(models.Model):
    geometrie = models.LineStringField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
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
        db_table = "transport_transport_par_cable"


class TronconDeRoute(models.Model):
    geometrie = models.LineStringField(srid=2154, dim=3, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nature = models.CharField(blank=True, null=True)
    nom_collaboratif_gauche = models.CharField(blank=True, null=True)
    nom_collaboratif_droite = models.CharField(blank=True, null=True)
    importance = models.CharField(blank=True, null=True)
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
    nombre_de_voies = models.IntegerField(blank=True, null=True)
    largeur_de_chaussee = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )
    itineraire_vert = models.BooleanField(blank=True, null=True)
    prive = models.BooleanField(blank=True, null=True)
    sens_de_circulation = models.CharField(blank=True, null=True)
    reserve_aux_bus = models.CharField(blank=True, null=True)
    urbain = models.BooleanField(blank=True, null=True)
    vitesse_moyenne_vl = models.IntegerField(blank=True, null=True)
    acces_vehicule_leger = models.CharField(blank=True, null=True)
    acces_pieton = models.CharField(blank=True, null=True)
    periode_de_fermeture = models.CharField(blank=True, null=True)
    nature_de_la_restriction = models.CharField(blank=True, null=True)
    restriction_de_hauteur = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    restriction_de_poids_total = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    restriction_de_poids_par_essieu = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    restriction_de_largeur = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    restriction_de_longueur = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    matieres_dangereuses_interdites = models.BooleanField(blank=True, null=True)
    borne_debut_gauche = models.CharField(max_length=15, blank=True, null=True)
    borne_debut_droite = models.CharField(max_length=15, blank=True, null=True)
    borne_fin_gauche = models.CharField(max_length=15, blank=True, null=True)
    borne_fin_droite = models.CharField(max_length=15, blank=True, null=True)
    insee_commune_gauche = models.CharField(max_length=5, blank=True, null=True)
    insee_commune_droite = models.CharField(max_length=5, blank=True, null=True)
    alias_gauche = models.CharField(blank=True, null=True)
    alias_droit = models.CharField(blank=True, null=True)
    date_de_mise_en_service = models.DateField(blank=True, null=True)
    identifiant_voie_1_gauche = models.CharField(max_length=9, blank=True, null=True)
    identifiant_voie_1_droite = models.CharField(max_length=9, blank=True, null=True)
    liens_vers_route_nommee = models.CharField(blank=True, null=True)
    liens_vers_itineraire_autre = models.CharField(blank=True, null=True)
    cpx_numero = models.CharField(max_length=32, blank=True, null=True)
    cpx_numero_route_europeenne = models.CharField(max_length=32, blank=True, null=True)
    cpx_classement_administratif = models.CharField(blank=True, null=True)
    cpx_gestionnaire = models.CharField(blank=True, null=True)
    cpx_toponyme_route_nommee = models.CharField(blank=True, null=True)
    cpx_toponyme_itineraire_cyclable = models.CharField(blank=True, null=True)
    cpx_toponyme_voie_verte = models.CharField(blank=True, null=True)
    cpx_nature_itineraire_autre = models.CharField(blank=True, null=True)
    cpx_toponyme_itineraire_autre = models.CharField(blank=True, null=True)
    delestage = models.BooleanField(blank=True, null=True)
    source_voie_ban_gauche = models.CharField(blank=True, null=True)
    source_voie_ban_droite = models.CharField(blank=True, null=True)
    nom_voie_ban_gauche = models.CharField(blank=True, null=True)
    nom_voie_ban_droite = models.CharField(blank=True, null=True)
    lieux_dits_ban_gauche = models.CharField(blank=True, null=True)
    lieux_dits_ban_droite = models.CharField(blank=True, null=True)
    identifiant_voie_ban_gauche = models.CharField(blank=True, null=True)
    identifiant_voie_ban_droite = models.CharField(blank=True, null=True)
    sens_amenagement_cyclable_gauche = models.CharField(blank=True, null=True)
    sens_amenagement_cyclable_droit = models.CharField(blank=True, null=True)
    amenagement_cyclable_gauche = models.CharField(blank=True, null=True)
    amenagement_cyclable_droit = models.CharField(blank=True, null=True)
    aire_de_retournement_dfci = models.CharField(blank=True, null=True)
    gabarit_dfci = models.CharField(blank=True, null=True)
    impasse_dfci = models.BooleanField(blank=True, null=True)
    nature_detaillee_dfci = models.CharField(blank=True, null=True)
    ouvrage_d_art_limitant_dfci = models.BooleanField(blank=True, null=True)
    pente_maximale_dfci = models.IntegerField(blank=True, null=True)
    piste_dfci = models.BooleanField(blank=True, null=True)
    piste_dfci_debroussaillee = models.BooleanField(blank=True, null=True)
    piste_dfci_fosses = models.CharField(blank=True, null=True)
    sens_de_circulation_dfci = models.CharField(blank=True, null=True)
    tout_terrain_dfci = models.BooleanField(blank=True, null=True)
    vitesse_moyenne_dfci = models.IntegerField(blank=True, null=True)
    zone_de_croisement_dfci = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "transport_troncon_de_route"


class TronconDeVoieFerree(models.Model):
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
    electrifie = models.BooleanField(blank=True, null=True)
    largeur = models.CharField(blank=True, null=True)
    nombre_de_voies = models.IntegerField(blank=True, null=True)
    usage = models.CharField(blank=True, null=True)
    vitesse_maximale = models.IntegerField(blank=True, null=True)
    liens_vers_voie_ferree_nommee = models.CharField(blank=True, null=True)
    cpx_toponyme = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "transport_troncon_de_voie_ferree"


class VoieFerreeNommee(models.Model):
    geometrie = models.MultiLineStringField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    toponyme = models.CharField(blank=True, null=True)
    statut_du_toponyme = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    sources = models.CharField(blank=True, null=True)
    identifiants_sources = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "transport_voie_ferree_nommee"


class VoieNommee(models.Model):
    geometrie = models.MultiLineStringField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    id_pseudo_fpb = models.CharField(blank=True, null=True)
    type_voie = models.CharField(blank=True, null=True)
    type_d_adressage = models.CharField(blank=True, null=True)
    nom_minuscule = models.CharField(blank=True, null=True)
    nom_initial_troncon = models.CharField(blank=True, null=True)
    mot_directeur = models.CharField(blank=True, null=True)
    validite = models.BooleanField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    code_insee = models.CharField(blank=True, null=True)
    code_postal = models.CharField(blank=True, null=True)
    alias_initial_troncon = models.CharField(blank=True, null=True)
    alias_minuscule = models.CharField(blank=True, null=True)
    type_liaison = models.CharField(blank=True, null=True)
    qualite_passage_maj_min = models.CharField(blank=True, null=True)
    fiabilite = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "transport_voie_nommee"


class VoieNommeeBeta(models.Model):
    geometrie = models.MultiLineStringField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    identifiant_voie_ban = models.CharField(blank=True, null=True)
    nom_voie_ban = models.CharField(blank=True, null=True)
    source_voie_ban = models.CharField(blank=True, null=True)
    nom_collaboratif = models.CharField(blank=True, null=True)
    type_voie = models.CharField(blank=True, null=True)
    mot_directeur = models.CharField(max_length=32, blank=True, null=True)
    lieux_dits_ban = models.CharField(blank=True, null=True)
    liens_vers_supports = models.CharField(blank=True, null=True)
    insee_communes_deleguees_ban = models.CharField(blank=True, null=True)
    noms_communes_deleguees_ban = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    nom_normalise = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        db_table = "transport_voie_nommee_beta"
