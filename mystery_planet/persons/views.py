from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from django_filters.rest_framework import DjangoFilterBackend

from .models import Company, Person
from .serializers import CompanySerializer, PersonSerializer


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
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["company"]
