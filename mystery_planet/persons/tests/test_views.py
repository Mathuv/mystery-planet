from django.urls import reverse
from pprint import pprint, pformat

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
        assert response.data.get("results")

    @pytest.mark.django_db
    def test_company_detail_view(self, api_clinet, company_factory):
        company: Company = company_factory()
        url = reverse("company-detail", kwargs={"pk": company.index})
        response: Response = api_clinet.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data
        assert response.data.get("name") == company.name

    @pytest.mark.django_db
    def test_company_employees_view(self, api_clinet, company_factory, person_factory):
        company: Company = company_factory()
        person: Person = person_factory(company=company)
        url = reverse("company-employees", kwargs={"company_id": company.index})
        response: Response = api_clinet.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data
        assert response.data.get("results")


class TestPersonAPIs:
    @pytest.mark.django_db
    def test_person_list_view(self, api_clinet, person_factory):
        person: Person = person_factory()
        url = reverse("person-list")
        response: Response = api_clinet.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data
        assert response.data.get("results")

    @pytest.mark.django_db
    def test_person_details_view(self, api_clinet, food_factory, person_factory):
        food_1: Food = food_factory()
        food_2: Food = food_factory()
        food_3: Food = food_factory()
        friend_1: Person = person_factory()
        friend_2: Person = person_factory()
        person: Person = person_factory(favourite_foods=(food_1, food_2, food_3), friends=(friend_1, friend_2))
        url = reverse("person-detail", kwargs={"pk": person.index})
        response: Response = api_clinet.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data
        assert response.data.get("name") == person.name
        # pprint(response.data)

    @pytest.mark.django_db
    def test_persons_common_friends_view(self, api_clinet, person_factory):
        friend_1: Person = person_factory()
        friend_2: Person = person_factory(eye_color=Person.EYE_BROWN)
        friend_3: Person = person_factory()
        person1: Person = person_factory(friends=(friend_1, friend_2))
        person2: Person = person_factory(friends=(friend_2, friend_3))
        url = reverse("common-friends", kwargs={"person1_id": person1.index, "person2_id": person2.index})
        response: Response = api_clinet.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data
        assert response.data.get("common_friends")

    @pytest.mark.django_db
    def test_person_favourite_foods_view(self, api_clinet, food_factory, person_factory):
        food_1: Food = food_factory(type=Food.FOOD_TYPE_FRUIT)
        food_2: Food = food_factory()
        food_3: Food = food_factory(type=Food.FOOD_TYPE_VEGETABLE)
        person: Person = person_factory(favourite_foods=(food_1, food_2, food_3))
        url = reverse("favourite-food", kwargs={"person_id": person.index})
        response: Response = api_clinet.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data
        assert response.data.get("fruits")
        assert food_1.name in response.data.get("fruits")
        assert response.data.get("vegetables")
        assert food_3.name in response.data.get("vegetables")
        # pprint(response.data)
