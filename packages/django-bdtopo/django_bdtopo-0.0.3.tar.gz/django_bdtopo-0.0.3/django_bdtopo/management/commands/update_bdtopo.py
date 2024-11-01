# Standard Library
import subprocess

# Django
from django.conf import settings
from django.core.management.base import BaseCommand

# Project
from django_bdtopo.mixins import LogTimeMessageMixin


class Command(LogTimeMessageMixin, BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "--all",
            action="store_true",
            help="Do not ask, import all tables for all apps.",
            default=False,
        )

    def handle(self, *args, **options):

        print("Begin update bdtopo command")

        # (from https://geoservices.ign.fr/bdtopo)
        DUMP_URL = "https://data.geopf.fr/telechargement/download/BDTOPO/BDTOPO_3-3_TOUSTHEMES_SQL_LAMB93_FXX_2024-03-15/BDTOPO_3-3_TOUSTHEMES_SQL_LAMB93_FXX_2024-03-15.7z.00"
        self.DB_NAME = settings.DBTOPO_DB_NAME
        self.DB_HOST = settings.DBTOPO_DB_HOST
        self.DB_PORT = settings.DBTOPO_DB_PORT
        self.DB_USER = settings.DBTOPO_DB_USER

        print("Mkdir folder")
        subprocess.run("mkdir -p ./data/extract; ", shell=True)

        print("Download files (~12GB, may be slow)")
        for i in range(1, 4):
            subprocess.run(
                f"wget -cO './data/BDTOPO_3-3_TOUSTHEMES_SQL_LAMB93_FXX_2024-03-15.7z.00{i}' '{DUMP_URL}{i}'",
                shell=True,
            )

        subprocess.run("rm -rf ./data/extract/", shell=True)
        subprocess.run("mkdir -p ./data/extract/", shell=True)

        apps = [
            "ADMINISTRATIF",
            "BATI",
            "HYDROGRAPHIE",
            "OCCUPATION_DU_SOL",
            "TRANSPORT",
            "ZONES_REGLEMENTEES",
        ]
        apps_to_import = [
            "SERVICES_ET_ACTIVITES",  # mandatory
            "LIEUX_NOMMES",  # mandatory
        ]

        # ask for import one time
        for app in apps:
            if not options["all"]:
                if input(
                    f"Do you want to import data related to app '{app.capitalize()}'?\n[y/N] "
                ) not in ["y", "Y", "yes", "yes, please"]:
                    print(f"Ok, skipping {app.capitalize()}.")
                    continue
            apps_to_import.append(app)

        # now import all apps selected
        for app in apps_to_import:
            print(
                f"\n\n--------\nImporting tables for app {app.capitalize()}\n--------"
            )
            print("\n\n- Extract data")
            # Extract all .sql files in {app} folder (in the .7z file)
            subprocess.run(
                f"cd data; 7z -ba e BDTOPO_3-3_TOUSTHEMES_SQL_LAMB93_FXX_2024-03-15.7z.001 -o./extract/ BDTOPO_3-3_TOUSTHEMES_SQL_LAMB93_FXX_2024-03-15/BDTOPO/1_DONNEES_LIVRAISON_2024-04-00082/BDT_3-3_SQL_LAMB93_FXX-ED2024-03-15/{app}",
                shell=True,
            )

            # get list_of_tables (list of sql files), something like ['/ADMINISTRATIF/arrondissement.sql', '/ADMINISTRATIF/epci.sql', ...]
            list_of_tables = (
                subprocess.check_output(
                    f"cd data; 7z -ba -slt l BDTOPO_3-3_TOUSTHEMES_SQL_LAMB93_FXX_2024-03-15.7z.001 | grep Path | awk -F'03-15' '{{print $3}}' | grep '{app}/'",
                    shell=True,
                )
                .decode("utf-8")
                .split("\n")
            )

            for table in list_of_tables:
                if table == "":
                    continue
                # from '/ADMINISTRATIF/epci.sql' to "epci"
                table_name = table.split("/")[-1].split(".sql")[0]
                print(f"\n\n--------\n- Table {table_name}\n--------")
                self.run_subcommands(table_name, app.lower())

            print("\n\n- Rm sql files")
            subprocess.run("rm -f ./data/extract/*.sql", shell=True)

        print("Import finished!")

    def run_subcommands(self, table_name, app_name):
        """
        Small function used to import sql file in the database, then rename the table (from table_name to app_name_table_name), and analyze it.
        """
        print("\n\n- Import raw sql data in postgresql")
        subprocess.run(
            f"cd data/extract; cat {table_name}.sql | psql -h {self.DB_HOST} -p {self.DB_PORT} -U {self.DB_USER} -d {self.DB_NAME} -f -",
            shell=True,
        )
        print("\n\n- Rename table")
        subprocess.run(
            f"psql -h {self.DB_HOST} -p {self.DB_PORT} -U {self.DB_USER} -d {self.DB_NAME} -c 'ALTER TABLE {table_name} RENAME TO {app_name}_{table_name};'",
            shell=True,
        )
        print("\n\n- Launch ANALYZE on table")
        subprocess.run(
            f"psql -h {self.DB_HOST} -p {self.DB_PORT} -U {self.DB_USER} -d {self.DB_NAME} -c 'ANALYZE {app_name}_{table_name};'",
            shell=True,
        )
