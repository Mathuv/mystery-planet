from typing import Any, Dict, List

from django.shortcuts import render

from rest_framework import generics, views, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .models import Company, FavouriteFoods, Food, Person, Friends
from .serializers import (
    CompanySerializer,
    PersonFavouriteFoodSerializer,
    PersonSerializer,
    PersonFriendsSerializer,
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
        fruits = FavouriteFoods.objects.filter(person=person, food__type=Food.FOOD_TYPE_FRUIT).values_list(
            "food", flat=True
        )
        vegetables = FavouriteFoods.objects.filter(person=person, food__type=Food.FOOD_TYPE_VEGETABLE).values_list(
            "food",
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

    serializer_class = PersonFriendsSerializer
    permission_classes = (AllowAny,)

    def get(self, request, person1_id, person2_id):
        breakpoint()
        person_1: Person = Person.objects.get(index=person1_id)
        person_2: Person = Person.objects.get(index=person2_id)
        # person_1_friends: List[Person] = Friends.objects.select_related("friend").filter(person=person_1)
        person_1_friends: List[Person] = Person.objects.raw(
            " select p.* from persons_person p inner join persons_friends f on f.friend_id = p.index where f.person_id = %s",
            [person1_id],
        )

        # person_2_friends: List[Person] = Friends.objects.select_related("friend").filter(person=person_2)
        person_2_friends: List[Person] = Person.objects.raw(
            " select p.* from persons_person p inner join persons_friends f on f.friend_id = p.index where f.person_id = %s",
            [person2_id],
        )
        # common_friends: List[Person] = list(Friends.objects.filter(person=person_1) & Friends.objects.filter(person=person_2))
        # common_friends = person_1_friends & person_2_friends
        common_friends = person_1_friends.intersection(person_2_friends)

        data = {
            "person1_id": person1_id,
            "person2_id": person2_id,
        }
        return Response(data=data)
