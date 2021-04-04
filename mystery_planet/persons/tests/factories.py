import factory

from ..models import Company, Person


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    index = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f"company{n}")


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    index = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f"company{n}")
