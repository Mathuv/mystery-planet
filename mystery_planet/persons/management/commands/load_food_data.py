import json
from typing import Any, Dict, List

from django.core.management.base import BaseCommand, CommandError

from mystery_planet.persons.models import Food

DEFAULT_DATA_FILE = "resources/food.json"


class Command(BaseCommand):
    help = "Loads data into the model person.model.Food"

    def add_arguments(self, parser):

        parser.add_argument(
            "--data-file",
            default=DEFAULT_DATA_FILE,
            dest="data-file",
            help="Data file containing the food data with path.",
        )

    def handle(self, *args, **options):
        data_file: str = options["data-file"]

        self.stdout.write("Start reading the food data from file...\n")
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

        self.stdout.write("Start loading the food data to the database...\n")

        food_list = [Food(name=food.get("name"), type=food.get("type")) for food in data]

        # Bulk create food data
        Food.objects.bulk_create(food_list, batch_size=10000, ignore_conflicts=True)

        self.stdout.write("Loading is finished!\n")
