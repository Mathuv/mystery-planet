from typing import Any, Dict, List

from django.shortcuts import render

from rest_framework import generics, views, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .models import Company, Food, Person
from .serializers import (
    CompanySerializer,
    PersonDetailMinSerializer,
    PersonFavouriteFoodSerializer,
    PersonsCommonFriendsSerializer,
    PersonSerializer,
)


class CompanyVieSet(viewsets.ModelViewSet):
    """
    CRUD on Company model.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend]
    # lookup_field = "index"


class PersonViewSet(viewsets.ModelViewSet):
    """
    CRUD on Person model
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = (AllowAny,)
    filter_fields = ["company"]


class PersonFavouriteFoodView(views.APIView):
    """Given 1 people, provide a list of fruits and vegetables they like."""

    permission_classes = (AllowAny,)
    serializer_class = PersonFavouriteFoodSerializer

    def get(self, request, person_id):
        person: Person = self.get_queryset()
        data = self.serializer_class(person).data
        fruits = person.favourite_foods.filter(type=Food.FOOD_TYPE_FRUIT).values_list("name", flat=True)
        vegetables = person.favourite_foods.filter(type=Food.FOOD_TYPE_VEGETABLE).values_list(
            "name",
            flat=True,
        )
        data["fruits"] = fruits
        data["vegetables"] = vegetables
        return Response(data=data)

    def get_queryset(self):
        person_id = self.kwargs.get("person_id")
        return Person.objects.get(index=person_id)


class CompanyEmployeeView(generics.ListAPIView):
    """Given a company, return all their employees."""

    permission_classes = (AllowAny,)
    serializer_class = PersonSerializer

    def get_queryset(self):
        company_id = self.kwargs.get("company_id")
        return Person.objects.filter(company_id=company_id)


class CommonFriends(views.APIView):
    """
    Given 2 people, provide their information (Name, Age, Address, phone)
    and the list of their friends in common which have brown eyes and are still alive.
    """

    serializer_class = PersonDetailMinSerializer
    permission_classes = (AllowAny,)

    def get(self, request, person1_id, person2_id):
        person_1: Person = Person.objects.get(index=person1_id)
        person_2: Person = Person.objects.get(index=person2_id)
        common_friends = person_1.friends.all() & person_2.friends.all()
        common_friends_alive_brown = common_friends.filter(has_died=False, eye_color=Person.EYE_BROWN)

        d = {"person_1": person_1, "person_2": person_2, "common_friends": common_friends_alive_brown}
        data = PersonsCommonFriendsSerializer(d).data

        return Response(data=data)
