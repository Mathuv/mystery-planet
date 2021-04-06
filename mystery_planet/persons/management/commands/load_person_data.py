import json
from decimal import Decimal
from pprint import pprint
from re import sub
from typing import Any, Dict, List

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import InternalError

import dateparser

from mystery_planet.persons.models import Person, Company, Friends, FavouriteFoods, Food

DEFAULT_DATA_FILE = "resources/people.json"


class Command(BaseCommand):
    help = "Loads data into the model person.model.Person"

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
        skipped_person_ids = []
        data_to_process = []
        for person in data:
            if Company.objects.filter(index=person.get("company_id")).exists():
                data_to_process.append(person)
            else:
                missing_company_ids.append(person.get("company_id"))
                skipped_person_ids.append(person.get("index"))

        for person in data_to_process:
            if not dryrun:
                # Create Person record
                person_obj, _ = Person.objects.get_or_create(
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
                # Create FavouriteFoods records
                f_food_list = [
                    FavouriteFoods(person=person_obj, food_id=f_food) for f_food in person.get("favouriteFood", [])
                ]

                FavouriteFoods.objects.bulk_create(f_food_list, batch_size=1000, ignore_conflicts=True)

                # Create Friends records
                friends_list = [
                    Friends(person=person_obj, friend_id=friend.get("index"))
                    for friend in person.get("friends", [])
                    if friend.get("index" not in skipped_person_ids)
                ]

                Friends.objects.bulk_create(friends_list, batch_size=1000, ignore_conflicts=True)

        self.stdout.write("Loading is finished!\n")
        self.stderr.write(
            f"{len(missing_company_ids)} records were not inserted "
            f"because following company_ids were not found in the database: {set(missing_company_ids)}. "
            f"Please load the updated company data and run the command again to insert skipped persons."
        )
