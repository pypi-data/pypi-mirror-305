# Standard Library
# from collections import defaultdict

# Django
from django.apps import apps
from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.views.generic import TemplateView


# from libs.bdnb_open_data.models import *

# from .constants_91 import DPE_ADEME_91_IDS


class BDNBAnalyzerAdminView(LoginRequiredMixin, TemplateView):
    template_name = "admin/bdnb_analyzer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Extraction DPE 91
        # nb_dpe_91 = (
        #     DpeLogement.objects.all()
        #     .filter(relbatimentgroupedpelogement__code_departement_insee="91")
        #     .distinct()
        #     .count()
        # )

        # Extraction communes
        # rel_bat_group_91 = (
        #     RelBatimentGroupeDpeLogement.objects.using("bdnb")
        #     .filter(code_departement_insee="91")
        #     .select_related("cle_interop_adr")
        # )
        # communes_set = set()

        # for rel_bat_group in rel_bat_group_91:
        #     communes_set.add(rel_bat_group.cle_interop_adr.libelle_commune)

        # for commune in communes_set:
        #     print(commune)

        # Extraction batiments groupes set
        # batiment_groupe_set = set()

        # rel_bat_group_91 = (
        #     RelBatimentGroupeDpeLogement.objects.using("bdnb")
        #     .filter(code_departement_insee="91")
        # )

        # for rel_bat_group in rel_bat_group_91:
        #     batiment_groupe_set.add(rel_bat_group.batiment_groupe_id)

        # Extraction communes nb dpe
        # rel_bat_group_91 = (
        #     RelBatimentGroupeDpeLogement.objects.using("bdnb")
        #     .filter(code_departement_insee="91")
        #     .distinct()
        #     .select_related("cle_interop_adr")
        # )
        # communes_count = defaultdict(int)

        # for rel_bat_group in rel_bat_group_91:
        #     communes_count[rel_bat_group.cle_interop_adr.libelle_commune] += 1

        # for commune, count in communes_count.items():
        #     print(f"{commune}: {count}")

        # Nombre de DPE représentatifs logements
        # dpe_representatif_logements = (
        #     BatimentGroupeDpeRepresentatifLogement.objects.using("bdnb").filter(
        #         code_departement_insee="91"
        #     )
        # )

        # nb_batiment_groupe_unique = set()

        # for dpe_representatif_logement in dpe_representatif_logements:
        #     nb_batiment_groupe_unique.add(dpe_representatif_logement.batiment_groupe_id)

        # nb_batiment_groupe_essonne = (
        #     BatimentGroupe.objects.using("bdnb")
        #     .filter(code_commune_insee__startswith="91")
        #     .distinct()
        #     .count()
        # )

        # nb_dpe_par_batiment_groupe = defaultdict(int)
        # rel_bat_group_91 = (
        #     RelBatimentGroupeDpeLogement.objects.using("bdnb")
        #     .filter(code_departement_insee="91")
        #     .distinct()
        # )

        # for rel_bat_group in rel_bat_group_91:
        #     nb_dpe_par_batiment_groupe[rel_bat_group.batiment_groupe_id] += 1

        # per_count_number = defaultdict(int)

        # for batiment_groupe, count in nb_dpe_par_batiment_groupe.items():
        #     if count > 1:
        #         per_count_number[count] += 1

        #     if count == 1990:
        #         bat_groupe_obj = BatimentGroupe.objects.using("bdnb").get(
        #             pk=batiment_groupe
        #         )

        #     rel_batiment_groupe_dpe_logements = (
        #         RelBatimentGroupeDpeLogement.objects.using("bdnb")
        #         .filter(batiment_groupe_id=batiment_groupe)
        #         .select_related("identifiant_dpe")
        #     )

        #     dpe_representatif = (
        #         bat_groupe_obj.batimentgroupedperepresentatiflogement
        #     )

        #     # Standard Library
        #     import pprint
        #     pprint.pprint(dpe_representatif.__dict__)

        # if count > 500:
        #     bat_groupe_obj = BatimentGroupe.objects.using("bdnb").get(
        #         pk=batiment_groupe
        #     )
        #     print(
        #         str(count)
        #         + " "
        #         + bat_groupe_obj.batimentgroupeadresse.libelle_adr_principale_ban
        #     )

        # per_count_number = dict(sorted(per_count_number.items()))

        # for count, number in per_count_number.items():
        #     print(f"{count}: {number}")

        # ademe_dpe_91_set = set(DPE_ADEME_91_IDS)
        # ademe_dpe_91_set_list = list(DPE_ADEME_91_IDS)

        # bdnb_dpe_91_set = set(
        #     DpeLogement.objects.using("bdnb")
        #     .filter(relbatimentgroupedpelogement__code_departement_insee="91")
        #     .values_list("identifiant_dpe", flat=True)
        # )

        # bdnb_dpe_91_set_list = list(bdnb_dpe_91_set)

        # common_dpe_91_set = ademe_dpe_91_set.intersection(bdnb_dpe_91_set)

        # only_in_ademe = ademe_dpe_91_set.difference(bdnb_dpe_91_set)
        # only_in_bdnb = bdnb_dpe_91_set.difference(ademe_dpe_91_set)

        # only_in_ademe_list = list(only_in_ademe)
        # only_in_bdnb_list = list(only_in_bdnb)

        # bdnb_dpe_91_set = (
        #     DpeLogement.objects.using("bdnb")
        #     .filter(
        #         relbatimentgroupedpelogement__code_departement_insee="91",
        #         classe_bilan_dpe__in=[
        #             "A",
        #             "B",
        #             "C",
        #             "D",
        #             "E",
        #             "F",
        #             "G",
        #             "a",
        #             "b",
        #             "c",
        #             "d",
        #             "e",
        #             "f",
        #             "g",
        #         ],
        #     )
        #     .distinct()
        # )

        # DPE dupliqués dans la BDNB
        # identifiants_dpe = (
        #     DpeLogement.objects.using("bdnb")
        #     .filter(relbatimentgroupedpelogement__code_departement_insee="91")
        #     .distinct()
        #     .values_list("identifiant_dpe", flat=True)
        # )

        # dpe_count = defaultdict(int)
        # for identifiant_dpe in identifiants_dpe:
        #     dpe_count[identifiant_dpe] += 1

        # dpe_count = dict(sorted(dpe_count.items(), key=lambda item: item[1]))

        # breakpoint()

        app_label = "bdnb_open_data"
        app_config = apps.get_app_config(app_label)
        context["app_label"] = app_label
        context["app_config"] = app_config
        context["title"] = _("Analyse des données de la BDNB")

        context.update(admin.site.each_context(self.request))
        return context
