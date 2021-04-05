import json
from typing import Any, Dict, List

from django.core.management.base import BaseCommand, CommandError

from mystery_planet.persons.models import Company

DEFAULT_DATA_FILE = "resources/companies.json"


class Command(BaseCommand):
    help = "Loads data into the model person.model.Company"

    def add_arguments(self, parser):

        parser.add_argument(
            "--data-file",
            default=DEFAULT_DATA_FILE,
            dest="data-file",
            help="Data file containing the company data with path.",
        )

    def handle(self, *args, **options):
        data_file: str = options["data-file"]

        self.stdout.write("Start reading the company data from file...\n")
        try:
            with open(data_file, "r") as f:
                try:
                    data: List[Dict[str, str]] = json.load(f)
                except json.decoder.JSONDecodeError as ex:
                    raise CommandError(f"Invalid json file!: {repr(ex)}")
        except FileNotFoundError:
            raise CommandError(f"Unable to locate the data file: {data_file}")

        if not isinstance(data, List):
            raise CommandError(f"Invalid data format in data file: {data_file}")

        self.stdout.write("Start loading the company data to the database...\n")

        company_list = [Company(index=company.get("index"), name=company.get("company")) for company in data]

        # Bulk create company data
        Company.objects.bulk_create(company_list, batch_size=10000, ignore_conflicts=True)

        self.stdout.write("Loading is finished!\n")
