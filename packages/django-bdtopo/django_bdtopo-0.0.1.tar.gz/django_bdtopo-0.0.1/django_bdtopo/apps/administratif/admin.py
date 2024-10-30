# Django
from django.contrib.gis import admin, admin as gis_admin

# Local application / specific library imports
from .models import (
    EPCI,
    Arrondissement,
    ArrondissementMunicipal,
    CollectiviteTerritoriale,
    Commune,
    CommuneAssocieeOuDeleguee,
    Condominium,
    Departement,
    Region,
)


# Batiment, Cimetiere, ConstructionLineaire, ConstructionPonctuelle, ConstructionSurfacique, LigneOrographique, Pylone, Reservoir, TerrainDeSport, ToponymieBati, BassinVersantTopographique, CoursDEau, DetailHydrographique, LimiteTerreMer, NoeudHydrographique, PlanDEau, SurfaceHydrographique, ToponymieHydrographie, TronconHydrographique, DetailOrographique, LieuDitNonHabite, ToponymieLieuxNommes, ZoneDHabitation, Haie, ZoneDEstran, ZoneDeVegetation, Canalisation, Erp, LigneElectrique, PosteDeTransformation, ToponymieServicesEtActivites, ZoneDActiviteOuDInteret, Aerodrome, EquipementDeTransport, ItineraireAutre, NonCommunication, PisteDAerodrome, PointDAcces, PointDeRepere, PointDuReseau, RouteNumeroteeOuNommee, SectionDePointsDeRepere, ToponymieTransport, TransportParCable, TronconDeRoute, TronconDeVoieFerree, VoieFerreeNommee, VoieNommee, VoieNommeeBeta, ForetPublique, ParcOuReserve, ToponymieZonesReglementees


class GeoAdminReadOnlyMixin:
    # Allow change otherwise OSM maps are not working properly, but not add and delete
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Arrondissement)
class ArrondissementAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
    list_display = (
        "cleabs",
        "nom_officiel",
        "code_insee_de_l_arrondissement",
        "date_creation",
        "date_modification",
    )
    search_fields = (
        "nom_officiel",
        "code_insee_de_l_arrondissement",
    )
    readonly_fields = [
        "cleabs",
        "nom_officiel",
        "code_insee_de_l_arrondissement",
        "code_insee_du_departement",
        "code_insee_de_la_region",
        "liens_vers_autorite_administrative",
        "date_creation",
        "date_modification",
        "date_d_apparition",
        "date_de_confirmation",
        "autorite_administrative",
    ]
    modifiable = False
    raw_id_fields = ("autorite_administrative",)


@admin.register(ArrondissementMunicipal)
class ArrondissementMunicipalAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
    list_display = (
        "cleabs",
        "nom_officiel",
        "code_insee",
        "code_postal",
        "date_creation",
        "date_modification",
    )
    search_fields = (
        "nom_officiel",
        "code_insee",
        "code_postal",
    )
    readonly_fields = [
        "cleabs",
        "code_insee",
        "code_insee_de_la_commune_de_rattach",
        "nom_officiel",
        "date_creation",
        "date_modification",
        "date_d_apparition",
        "date_de_confirmation",
        "lien_vers_chef_lieu",
        "liens_vers_autorite_administrative",
        "code_postal",
        "population",
        "autorite_administrative",
    ]
    modifiable = False
    raw_id_fields = ("autorite_administrative",)


@admin.register(CollectiviteTerritoriale)
class CollectiviteTerritorialeAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
    list_display = (
        "cleabs",
        "nom_officiel",
        "code_insee",
        "date_creation",
        "date_modification",
    )
    readonly_fields = [
        "cleabs",
        "code_insee",
        "code_insee_de_la_region",
        "nom_officiel",
        "date_creation",
        "date_modification",
        "date_d_apparition",
        "date_de_confirmation",
        "liens_vers_autorite_administrative",
        "code_siren",
        "autorite_administrative",
    ]
    modifiable = False
    raw_id_fields = ("autorite_administrative",)


@admin.register(Commune)
class CommuneAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
    list_display = (
        "cleabs",
        "nom_officiel",
        "code_insee",
        "code_postal",
        "population",
        "surface_en_ha",
        "date_creation",
        "date_modification",
    )
    search_fields = ("nom_officiel", "code_insee", "code_postal")
    readonly_fields = [
        "cleabs",
        "code_insee",
        "code_insee_de_l_arrondissement",
        "code_insee_de_la_collectivite_terr",
        "region",
        "departement",
        "epcis",
        "code_insee_du_departement",
        "code_insee_de_la_region",
        "population",
        "surface_en_ha",
        "date_creation",
        "date_modification",
        "date_d_apparition",
        "date_de_confirmation",
        "code_postal",
        "nom_officiel",
        "chef_lieu_d_arrondissement",
        "chef_lieu_de_collectivite_terr",
        "chef_lieu_de_departement",
        "chef_lieu_de_region",
        "capitale_d_etat",
        "date_du_recensement",
        "organisme_recenseur",
        "codes_siren_des_epci",
        "lien_vers_chef_lieu",
        "liens_vers_autorite_administrative",
        "code_siren",
        "autorite_administrative",
    ]
    modifiable = False
    raw_id_fields = ("autorite_administrative",)


@admin.register(CommuneAssocieeOuDeleguee)
class CommuneAssocieeOuDelegueeAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
    list_display = (
        "cleabs",
        "nom_officiel",
        "code_insee",
        "code_postal",
        "nature",
        "population",
        "date_creation",
        "date_modification",
    )
    search_fields = ("nom_officiel", "code_insee", "code_postal")
    readonly_fields = [
        "cleabs",
        "code_insee",
        "code_insee_de_la_commune_de_rattach",
        "nature",
        "nom_officiel",
        "date_creation",
        "date_modification",
        "date_d_apparition",
        "date_de_confirmation",
        "code_postal",
        "lien_vers_chef_lieu",
        "liens_vers_autorite_administrative",
        "population",
        "code_siren",
        "autorite_administrative",
    ]
    modifiable = False
    raw_id_fields = ("autorite_administrative",)


@admin.register(Condominium)
class CondominiumAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
    list_display = ("cleabs",)
    readonly_fields = [
        "cleabs",
        "unites_administratives_souveraines",
        "date_creation",
        "date_modification",
        "date_d_apparition",
        "date_de_confirmation",
        "lien_vers_lieu_dit",
        "lieu_dit",
    ]


@admin.register(Departement)
class DepartementAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
    list_display = (
        "cleabs",
        "nom_officiel",
        "code_insee",
        "date_creation",
        "date_modification",
    )
    search_fields = (
        "nom_officiel",
        "code_insee",
    )
    readonly_fields = [
        "cleabs",
        "code_insee",
        "code_insee_de_la_region",
        "nom_officiel",
        "date_creation",
        "date_modification",
        "date_d_apparition",
        "date_de_confirmation",
        "liens_vers_autorite_administrative",
        "code_siren",
        "autorite_administrative",
    ]
    modifiable = False
    raw_id_fields = ("autorite_administrative",)


@admin.register(EPCI)
class EPCIAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
    list_display = ("cleabs", "nom_officiel", "date_creation", "date_modification")
    search_fields = ("nom_officiel",)
    readonly_fields = [
        "cleabs",
        "code_siren",
        "nature",
        "nom_officiel",
        "date_creation",
        "date_modification",
        "date_d_apparition",
        "date_de_confirmation",
        "liens_vers_autorite_administrative",
        "autorite_administrative",
    ]
    modifiable = False
    raw_id_fields = ("autorite_administrative",)


@admin.register(Region)
class RegionAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
    list_display = (
        "cleabs",
        "nom_officiel",
        "code_insee",
        "date_creation",
        "date_modification",
    )
    search_fields = (
        "nom_officiel",
        "code_insee",
    )
    readonly_fields = [
        "cleabs",
        "code_insee",
        "nom_officiel",
        "date_creation",
        "date_modification",
        "date_d_apparition",
        "date_de_confirmation",
        "liens_vers_autorite_administrative",
        "code_siren",
        "autorite_administrative",
    ]
    modifiable = False
    raw_id_fields = ("autorite_administrative",)


# TODO: move these admin views to their apps

# @admin.register(Batiment)
# class BatimentAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "usage_1", "usage_2", "nombre_de_logements", "nombre_d_etages", "date_creation", "date_modification")
#     search_fields = ("usage_1", "usage_2",)


# @admin.register(Cimetiere)
# class CimetiereAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "nature", "nature_detaillee", "date_creation", "date_modification")
#     search_fields = ("nature", "nature_detaillee",)


# @admin.register(ConstructionLineaire)
# class ConstructionLineaireAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "nature", "nature_detaillee", "date_creation", "date_modification")
#     search_fields = ("nature", "nature_detaillee",)


# @admin.register(ConstructionPonctuelle)
# class ConstructionPonctuelleAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "nature", "nature_detaillee", "date_creation", "date_modification")
#     search_fields = ("nature", "nature_detaillee",)


# @admin.register(ConstructionSurfacique)
# class ConstructionSurfaciqueAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "nature", "nature_detaillee", "date_creation", "date_modification")
#     search_fields = ("nature", "nature_detaillee",)


# @admin.register(LigneOrographique)
# class LigneOrographiqueAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "nature", "date_creation", "date_modification")
#     search_fields = ("nature",)


# @admin.register(Pylone)
# class PyloneAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")
#     search_fields = ("cleabs",)


# @admin.register(Reservoir)
# class ReservoirAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "nature", "date_creation", "date_modification")
#     search_fields = ("nature",)


# @admin.register(TerrainDeSport)
# class TerrainDeSportAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "nature", "nature_detaillee", "date_creation", "date_modification")
#     search_fields = ("nature", "nature_detaillee")


# @admin.register(ToponymieBati)
# class ToponymieBatiAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs_de_l_objet", "nature_de_l_objet",)
#     search_fields = ("nature_de_l_objet",)


# @admin.register(BassinVersantTopographique)
# class BassinVersantTopographiqueAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("code_bdcarthage", "code_du_bassin_hydrographique", "commentaire_sur_l_objet_hydro", "date_creation", "date_modification")
#     search_fields = ("code_bdcarthage", "code_du_bassin_hydrographique")


# @admin.register(CoursDEau)
# class CoursDEauAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "code_hydrographique", "date_creation", "date_modification")
#     search_fields = ("code_hydrographique",)


# @admin.register(DetailHydrographique)
# class DetailHydrographiqueAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "nature", "nature_detaillee", "date_creation", "date_modification")
#     search_fields = ("nature", "nature_detaillee",)


# @admin.register(LimiteTerreMer)
# class LimiteTerreMerAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(NoeudHydrographique)
# class NoeudHydrographiqueAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(PlanDEau)
# class PlanDEauAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(SurfaceHydrographique)
# class SurfaceHydrographiqueAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(ToponymieHydrographie)
# class ToponymieHydrographieAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs_de_l_objet",)


# @admin.register(TronconHydrographique)
# class TronconHydrographiqueAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(DetailOrographique)
# class DetailOrographiqueAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(LieuDitNonHabite)
# class LieuDitNonHabiteAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(ToponymieLieuxNommes)
# class ToponymieLieuxNommesAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs_de_l_objet",)


# @admin.register(ZoneDHabitation)
# class ZoneDHabitationAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(Haie)
# class HaieAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(ZoneDEstran)
# class ZoneDEstranAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(ZoneDeVegetation)
# class ZoneDeVegetationAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(Canalisation)
# class CanalisationAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(Erp)
# class ErpAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(LigneElectrique)
# class LigneElectriqueAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(PosteDeTransformation)
# class PosteDeTransformationAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(ToponymieServicesEtActivites)
# class ToponymieServicesEtActivitesAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs_de_l_objet",)


# @admin.register(ZoneDActiviteOuDInteret)
# class ZoneDActiviteOuDInteretAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(Aerodrome)
# class AerodromeAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(EquipementDeTransport)
# class EquipementDeTransportAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(ItineraireAutre)
# class ItineraireAutreAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(NonCommunication)
# class NonCommunicationAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(PisteDAerodrome)
# class PisteDAerodromeAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(PointDAcces)
# class PointDAccesAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(PointDeRepere)
# class PointDeRepereAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(PointDuReseau)
# class PointDuReseauAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(RouteNumeroteeOuNommee)
# class RouteNumeroteeOuNommeeAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(SectionDePointsDeRepere)
# class SectionDePointsDeRepereAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(ToponymieTransport)
# class ToponymieTransportAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs_de_l_objet",)


# @admin.register(TransportParCable)
# class TransportParCableAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(TronconDeRoute)
# class TronconDeRouteAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(TronconDeVoieFerree)
# class TronconDeVoieFerreeAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(VoieFerreeNommee)
# class VoieFerreeNommeeAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(VoieNommee)
# class VoieNommeeAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(VoieNommeeBeta)
# class VoieNommeeBetaAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(ForetPublique)
# class ForetPubliqueAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(ParcOuReserve)
# class ParcOuReserveAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs", "date_creation", "date_modification")


# @admin.register(ToponymieZonesReglementees)
# class ToponymieZonesReglementeesAdmin(GeoAdminReadOnlyMixin, gis_admin.OSMGeoAdmin):
#     list_display = ("cleabs_de_l_objet",)
