import datetime
import string

import factory
from factory.fuzzy import FuzzyChoice, FuzzyDateTime, FuzzyInteger, FuzzyText, FuzzyDecimal
from pytz import UTC

from ..models import Company, Food, Person


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    index = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f"Company{n}")


class FoodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Food

    name = factory.Sequence(lambda n: f"Food{n}")
    type = FuzzyChoice([Food.FOOD_TYPE_FRUIT, Food.FOOD_TYPE_VEGETABLE])


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    age = FuzzyInteger(21, 99)
    eye_color = FuzzyChoice([Person.EYE_BLUE, Person.EYE_BROWN])
    name = factory.Sequence(lambda n: f"Person{n}")
    gender = FuzzyChoice([Person.GENDER_MALE, Person.GENDER_FEMALE])
    phone = factory.Sequence(lambda n: "0486-992-%03d" % n)
    email = factory.LazyAttribute(lambda obj: f"{obj.name}@test.com".lower())
    address = factory.Faker("address")
    registered = FuzzyDateTime(datetime.datetime(2020, 1, 1, tzinfo=UTC))
    company = factory.SubFactory(CompanyFactory)
    about = FuzzyText()
    greeting = FuzzyText()
    balance = FuzzyDecimal(low=0)

    @factory.post_generation
    def favourite_foods(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for food in extracted:
                self.favourite_foods.add(food)

    @factory.post_generation
    def friends(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for friend in extracted:
                self.friends.add(friend)
