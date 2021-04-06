import pytest
from pprint import pprint

from django.test import TestCase

from model_bakery import baker
from ..models import Food


class TestCompanyModel(TestCase):
    def setUp(self):
        self.company = baker.make("persons.Company")
        pprint(self.company.__dict__)

    def test_company_attrs(self):
        self.assertTrue(self.company.name)
        self.assertTrue(self.company.index)


class TestPersonModel(TestCase):
    def setUp(self):
        self.person = baker.make("persons.Person")
        pprint(self.person.__dict__)

    def test_person_attrs(self):
        self.assertTrue(self.person.name)
        self.assertTrue(self.person.age)


@pytest.mark.django_db
def test_compapy_model_create(company_factory):
    company = company_factory()
    assert company.name == "Company0"
    assert company.index == 0


@pytest.mark.django_db
def test_food_model_create(food_factory):
    food = food_factory()
    assert food.name == "Food0"
    # assert food.type in [Food.FOOD_TYPE_VEGETABLE, Food.FOOD_TYPE_FRUIT]
    assert food.type in Food.FOOD_TYPE_CHOICES

@pytest.mark.django_db
def test_person_model_create(person_factory):
    person = person_factory()
    assert person.name == "Person0"
