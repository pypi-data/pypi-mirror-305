# Django
from django.core.management.base import BaseCommand
from django.db import transaction

# Project
from django_bdtopo.apps.administratif.models import (
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
from django_bdtopo.apps.lieux_nommes.models import ZoneDHabitation
from django_bdtopo.apps.services_et_activites.models import ZoneDActiviteOuDInteret


class Command(BaseCommand):
    """
    Create links between all bdtopo models
    """

    def update_type_services_et_activites(self, type_object):
        """
        Fill foreign key between all objects in all models in administratif app to ZoneDActiviteOuDInteret.
        """
        to_update_objects = []
        for object in type_object.objects.all():
            if object.liens_vers_autorite_administrative and (
                zone_activite := ZoneDActiviteOuDInteret.objects.filter(
                    cleabs=object.liens_vers_autorite_administrative
                )
            ):
                object.autorite_administrative = zone_activite.first()
                to_update_objects.append(object)
        type_object.objects.bulk_update(
            to_update_objects,
            [
                "autorite_administrative",
            ],
            batch_size=1000,
        )

    def update_type_lieux_nommes(self, type_object):
        """
        Fill foreign key between all objects in all models in administratif app to ZoneDHabitation.
        """
        to_update_objects = []
        for object in type_object.objects.all():
            if object.lien_vers_lieu_dit and (
                zone_activite := ZoneDHabitation.objects.filter(
                    cleabs=object.lien_vers_lieu_dit
                )
            ):
                object.lieu_dit = zone_activite.first()
                to_update_objects.append(object)
        type_object.objects.bulk_update(
            to_update_objects,
            [
                "lieu_dit",
            ],
            batch_size=1000,
        )

    def handle(self, *args, **options):
        with transaction.atomic():
            departements_in_bulk = {d.code_insee: d for d in Departement.objects.all()}
            epcis_in_bulk = {e.code_siren: e for e in EPCI.objects.all()}
            regions_in_bulk = {r.code_insee: r for r in Region.objects.all()}

            # Link Departments
            print("Linking departments...")
            to_update_departements = []
            for departement in Departement.objects.all():
                region = regions_in_bulk.get(departement.code_insee_de_la_region)
                departement.region = region
                to_update_departements.append(departement)

            Departement.objects.bulk_update(to_update_departements, ["region"])
            print("✓ Departments linked ok")

            # Link Communes
            print("Linking communes...")
            to_update_communes = []
            for commune in Commune.objects.all():
                region = regions_in_bulk.get(commune.code_insee_de_la_region)
                departement = departements_in_bulk.get(
                    commune.code_insee_du_departement
                )

                if not departement:
                    print(
                        f"Departement {commune.code_insee_du_departement} not found, skipping..."
                    )
                    continue

                if not region:
                    print(
                        f"Region {commune.code_insee_de_la_region} not found, skipping..."
                    )
                    continue

                commune.region = region
                commune.departement = departement
                to_update_communes.append(commune)

            Commune.objects.bulk_update(
                to_update_communes, ["region", "departement"], batch_size=1000
            )

            print("Linking communes epci through...")
            to_update_communes_epcis = []
            EPCIThroughModel = Commune.epcis.through
            EPCIThroughModel.objects.all().delete()
            for commune in Commune.objects.all():
                if commune.codes_siren_des_epci:
                    epci_codes = commune.codes_siren_des_epci.split("/")

                    for epci_code in epci_codes:
                        epci = epcis_in_bulk.get(epci_code)
                        if epci:
                            to_update_communes_epcis.append(
                                EPCIThroughModel(commune=commune, epci=epci)
                            )

            EPCIThroughModel.objects.bulk_create(
                to_update_communes_epcis, batch_size=1000
            )

            print("✓ Communes epci through linked ok")
            print("✓ Communes linked ok")

            print("Linking autorite_administrative & lieu_dit...")

            type_objects = [
                Arrondissement,
                ArrondissementMunicipal,
                CollectiviteTerritoriale,
                Commune,
                Condominium,
                CommuneAssocieeOuDeleguee,
                Departement,
                EPCI,
                Region,
            ]
            for type_object in type_objects:
                if "models.Condominium" in str(type_object):
                    self.update_type_lieux_nommes(type_object)
                else:
                    self.update_type_services_et_activites(type_object)

            print("✓ autorite_administrative linked ok")

            print("✓ All links created successfully")
