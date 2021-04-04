import pytest
from pprint import pprint

from django.test import TestCase

from model_bakery import baker


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
def test_comnapy_model_create(company_factory):
    company = company_factory()
    assert company.name == "company0"
    assert company.index == 0
