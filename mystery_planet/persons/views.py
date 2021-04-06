from typing import Any, Dict, List

from django.shortcuts import render

from rest_framework import generics, views, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .models import Company, FavouriteFoods, Food, Person
from .serializers import (
    CompanySerializer,
    PersonFavouriteFoodSerializer,
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
        fruits = FavouriteFoods.objects.filter(person=person, food__type=Food.FOOD_TYPE_FRUIT).values_list(
            "food", flat=True
        )
        vegetables = FavouriteFoods.objects.filter(person=person, food__type=Food.FOOD_TYPE_VEGETABLE).values_list(
            "food",
            flat=True,
        )
        data: Dict[str, Any] = {"name": person.name, "age": person.age, "fruits": fruits, "vegetables": vegetables}
        return Response(data=data)

    def get_queryset(self):
        person_id = self.kwargs.get("person_id")
        return Person.objects.get(index=person_id)
