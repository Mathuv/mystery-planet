import json
from decimal import Decimal
from pprint import pprint
from re import sub
from typing import Any, Dict, List

from django.core.management.base import BaseCommand, CommandError

import dateparser

from mystery_planet.persons.models import Person, Company

DEFAULT_DATA_FILE = "resources/people.json"


class Command(BaseCommand):
    help = "Loads data into the model person.model.Company"

    def add_arguments(self, parser):

        parser.add_argument(
            "-d",
            "--dryrun",
            dest="dryrun",
            action="store_true",
        )

        parser.add_argument(
            "--data-file",
            default=DEFAULT_DATA_FILE,
            dest="data-file",
            help="Data file containing the persons data with path.",
        )

    def handle(self, *args, **options):
        dryrun: bool = options["dryrun"]
        data_file: str = options["data-file"]

        self.stdout.write("Start reading the person data from file...\n")
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

        self.stdout.write("Start loading the person data to the database...\n")

        person_list = []
        missing_company_ids = []
        for person in data:
            if Company.objects.filter(index=person.get("company_id")).exists():
                person_obj = Person(
                    index=person.get("index"),
                    guid=person.get("guid"),
                    name=person.get("name"),
                    age=person.get("age"),
                    gender=person.get("gender"),
                    has_died=person.get("has_died"),
                    picture=person.get("picture"),
                    balance=Decimal(sub(r"[^\d.]", "", person.get("balance"))),
                    eye_color=person.get("eyeColor"),
                    phone=person.get("phone"),
                    address=person.get("address"),
                    about=person.get("about"),
                    greeting=person.get("greeting"),
                    tags=person.get("tags"),
                    registered=dateparser.parse(person.get("registered")),
                    company_id=person.get("company_id"),
                )
                person_list.append(person_obj)
            else:
                missing_company_ids.append(person.get("company_id"))

        # Bulk create company data
        if not dryrun:
            Person.objects.bulk_create(person_list, batch_size=10000, ignore_conflicts=True)

        self.stdout.write("Loading is finished!\n")
        self.stderr.write(
            f"{len(missing_company_ids)} records were not inserted because following company_ids were not found in the database: {set(missing_company_ids)}. Please load the updated company data and run the command again to insert skipped persons."
        )
