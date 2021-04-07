from django.urls import reverse
from pprint import pprint

from rest_framework import status
from rest_framework.reverse import reverse as rest_reverse
from rest_framework.response import Response
from ..models import Company, Food, Person

import pytest


class TestCompanyEmployeesAPI:
    @pytest.mark.django_db
    def test_company_lsit_view(self, api_clinet, company_factory):
        company: Company = company_factory()
        url = reverse("company-list")
        response: Response = api_clinet.get(url)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_company_employees_view(self, api_clinet, company_factory, food_factory, person_factory):
        company: Company = company_factory()
        food: Food = food_factory()
        person: Person = person_factory()
        url = reverse("company-employees", kwargs={"company_id": company.index})
        response: Response = api_clinet.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data


class TestPersonAPIs:
    @pytest.mark.django_db
    def test_person_list_view(self, api_clinet, person_factory):
        person: Person = person_factory()
        url = reverse("person-list")
        response: Response = api_clinet.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data

    @pytest.mark.django_db
    def test_persons_common_friends_view(self, api_clinet, person_factory):
        person1: Person = person_factory()
        person2: Person = person_factory()
        url = reverse("common-friends", kwargs={"person1_id": person1.index, "person2_id": person2.index})
        response: Response = api_clinet.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data
        pprint(response.data)

    @pytest.mark.django_db
    def test_person_favourite_foods_view(self, api_clinet, food_factory, person_factory):
        person: Person = person_factory()
        url = reverse("favourite-food", )
        response: Response = api_clinet.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data
