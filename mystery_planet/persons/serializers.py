from rest_framework import serializers

from .models import Company, Person


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class PersonFavouriteFoodSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    fruits = serializers.ListField(child=serializers.CharField(), default=[])
    vegetables = serializers.ListField(child=serializers.CharField(), default=[])
