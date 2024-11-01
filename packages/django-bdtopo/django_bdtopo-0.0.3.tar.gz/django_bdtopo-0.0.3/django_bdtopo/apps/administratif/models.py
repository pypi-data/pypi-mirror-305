# Original IGN django generated model as of 2024-10-24
from django.contrib.gis.db import models


class Arrondissement(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    nom_officiel = models.CharField(blank=True, null=True)
    code_insee_de_l_arrondissement = models.CharField(
        max_length=5, blank=True, null=True
    )
    code_insee_du_departement = models.CharField(max_length=5, blank=True, null=True)
    code_insee_de_la_region = models.CharField(max_length=5, blank=True, null=True)
    liens_vers_autorite_administrative = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)

    # 2024-10-28 :
    # Add field "autorite_administrative" to the model
    autorite_administrative = models.ForeignKey(
        "services_et_activites.ZoneDActiviteOuDInteret",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="arrondissements",
        verbose_name="Autorité administrative",
    )

    class Meta:
        db_table = "administratif_arrondissement"

    # 2024-10-25 :
    # Add __str__ method
    def __str__(self):
        return f"{self.nom_officiel} ({self.code_insee_de_l_arrondissement})"


class ArrondissementMunicipal(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_insee = models.CharField(max_length=5, blank=True, null=True)
    code_insee_de_la_commune_de_rattach = models.CharField(
        max_length=5, blank=True, null=True
    )
    nom_officiel = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    lien_vers_chef_lieu = models.CharField(max_length=24, blank=True, null=True)
    liens_vers_autorite_administrative = models.CharField(blank=True, null=True)
    code_postal = models.CharField(max_length=5, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)

    # 2024-10-28 :
    # Add field "autorite_administrative" to the model
    autorite_administrative = models.ForeignKey(
        "services_et_activites.ZoneDActiviteOuDInteret",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="arrondissements_municipaux",
        verbose_name="Autorité administrative",
    )

    class Meta:
        db_table = "administratif_arrondissement_municipal"

    # 2024-10-25 :
    # Add __str__ method
    def __str__(self):
        return f"{self.nom_officiel} ({self.code_insee})"


class CollectiviteTerritoriale(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_insee = models.CharField(max_length=5, blank=True, null=True)
    code_insee_de_la_region = models.CharField(max_length=5, blank=True, null=True)
    nom_officiel = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    liens_vers_autorite_administrative = models.CharField(blank=True, null=True)
    code_siren = models.CharField(max_length=9, blank=True, null=True)

    # 2024-10-28 :
    # Add field "autorite_administrative" to the model
    autorite_administrative = models.ForeignKey(
        "services_et_activites.ZoneDActiviteOuDInteret",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="collectivites_territoriales",
        verbose_name="Autorité administrative",
    )

    class Meta:
        db_table = "administratif_collectivite_territoriale"

    # 2024-10-25 :
    # Add __str__ method
    def __str__(self):
        return f"{self.nom_officiel} ({self.code_insee})"


class Commune(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_insee = models.CharField(max_length=5, blank=True, null=True)
    code_insee_de_l_arrondissement = models.CharField(
        max_length=5, blank=True, null=True
    )
    code_insee_de_la_collectivite_terr = models.CharField(
        max_length=5, blank=True, null=True
    )
    code_insee_du_departement = models.CharField(max_length=5, blank=True, null=True)
    code_insee_de_la_region = models.CharField(max_length=5, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    surface_en_ha = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    code_postal = models.CharField(max_length=5, blank=True, null=True)
    nom_officiel = models.CharField(blank=True, null=True)
    chef_lieu_d_arrondissement = models.BooleanField(blank=True, null=True)
    chef_lieu_de_collectivite_terr = models.BooleanField(blank=True, null=True)
    chef_lieu_de_departement = models.BooleanField(blank=True, null=True)
    chef_lieu_de_region = models.BooleanField(blank=True, null=True)
    capitale_d_etat = models.BooleanField(blank=True, null=True)
    date_du_recensement = models.DateField(blank=True, null=True)
    organisme_recenseur = models.CharField(max_length=16, blank=True, null=True)
    codes_siren_des_epci = models.CharField(max_length=32, blank=True, null=True)
    lien_vers_chef_lieu = models.CharField(max_length=24, blank=True, null=True)
    liens_vers_autorite_administrative = models.CharField(blank=True, null=True)
    code_siren = models.CharField(max_length=9, blank=True, null=True)

    # 2024-10-28 :
    # Add field "autorite_administrative" to the model
    autorite_administrative = models.ForeignKey(
        "services_et_activites.ZoneDActiviteOuDInteret",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="communes",
        verbose_name="Autorité administrative",
    )

    # 2024-10-25 :
    # Add field "region" to the model
    region = models.ForeignKey(
        "administratif.Region",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="communes",
        verbose_name="Région",
    )

    # 2024-10-25 :
    # Add field "departement" to the model
    departement = models.ForeignKey(
        "administratif.Departement",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="communes",
        verbose_name="Département",
    )

    # 2024-10-25 :
    # Add field "epcis" to the model
    epcis = models.ManyToManyField(
        "administratif.EPCI",
        blank=True,
        related_name="communes",
        verbose_name="EPCIs",
    )

    class Meta:
        db_table = "administratif_commune"

    # 2024-10-25 :
    # Add __str__ method
    def __str__(self):
        return f"{self.nom_officiel} ({self.code_insee})"


class CommuneAssocieeOuDeleguee(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_insee = models.CharField(max_length=5, blank=True, null=True)
    code_insee_de_la_commune_de_rattach = models.CharField(
        max_length=5, blank=True, null=True
    )
    nature = models.CharField(blank=True, null=True)
    nom_officiel = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    code_postal = models.CharField(max_length=5, blank=True, null=True)
    lien_vers_chef_lieu = models.CharField(max_length=24, blank=True, null=True)
    liens_vers_autorite_administrative = models.CharField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    code_siren = models.CharField(max_length=9, blank=True, null=True)

    # 2024-10-28 :
    # Add field "autorite_administrative" to the model
    autorite_administrative = models.ForeignKey(
        "services_et_activites.ZoneDActiviteOuDInteret",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="communes_associees_ou_deleguees",
        verbose_name="Autorité administrative",
    )

    class Meta:
        db_table = "administratif_commune_associee_ou_deleguee"

    # 2024-10-25 :
    # Add __str__ method
    def __str__(self):
        return f"{self.nom_officiel} ({self.code_insee})"


class Condominium(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    unites_administratives_souveraines = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    lien_vers_lieu_dit = models.CharField(max_length=24, blank=True, null=True)

    # 2024-10-28 :
    # Add field "autorite_administrative" to the model
    lieu_dit = models.ForeignKey(
        "lieux_nommes.ZoneDHabitation",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="condominiums",
        verbose_name="Lieu dit",
    )

    class Meta:
        db_table = "administratif_condominium"

    # 2024-10-25 :
    # Add __str__ method
    def __str__(self):
        return f"{self.unites_administratives_souveraines}"


class Departement(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_insee = models.CharField(max_length=5, blank=True, null=True)
    code_insee_de_la_region = models.CharField(max_length=5, blank=True, null=True)
    nom_officiel = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    liens_vers_autorite_administrative = models.CharField(blank=True, null=True)
    code_siren = models.CharField(max_length=9, blank=True, null=True)

    # 2024-10-28 :
    # Add field "autorite_administrative" to the model
    autorite_administrative = models.ForeignKey(
        "services_et_activites.ZoneDActiviteOuDInteret",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="departements",
        verbose_name="Autorité administrative",
    )

    # 2024-10-25:
    # Add field "region" to the model
    region = models.ForeignKey(
        "administratif.Region",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="departements",
        verbose_name="Région",
    )

    class Meta:
        db_table = "administratif_departement"

    # 2024-10-25 :
    # Add __str__ method
    def __str__(self):
        return f"{self.nom_officiel} ({self.code_insee})"


class EPCI(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_siren = models.CharField(max_length=9, blank=True, null=True)
    nature = models.CharField(blank=True, null=True)
    nom_officiel = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    liens_vers_autorite_administrative = models.CharField(blank=True, null=True)

    # 2024-10-28 :
    # Add field "autorite_administrative" to the model
    autorite_administrative = models.ForeignKey(
        "services_et_activites.ZoneDActiviteOuDInteret",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="epcis",
        verbose_name="Autorité administrative",
    )

    class Meta:
        db_table = "administratif_epci"

    # 2024-10-25 :
    # Add __str__ method
    def __str__(self):
        return f"{self.nom_officiel} ({self.code_siren})"


class Region(models.Model):
    geometrie = models.MultiPolygonField(srid=2154, blank=True, null=True)
    cleabs = models.CharField(primary_key=True, max_length=24)
    code_insee = models.CharField(max_length=5, blank=True, null=True)
    nom_officiel = models.CharField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)
    date_d_apparition = models.DateField(blank=True, null=True)
    date_de_confirmation = models.DateField(blank=True, null=True)
    liens_vers_autorite_administrative = models.CharField(blank=True, null=True)
    code_siren = models.CharField(max_length=9, blank=True, null=True)

    # 2024-10-28 :
    # Add field "autorite_administrative" to the model
    autorite_administrative = models.ForeignKey(
        "services_et_activites.ZoneDActiviteOuDInteret",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="region",
        verbose_name="Autorité administrative",
    )

    class Meta:
        db_table = "administratif_region"

    # 2024-10-25 :
    # Add __str__ method
    def __str__(self):
        return f"{self.nom_officiel} ({self.code_insee})"
