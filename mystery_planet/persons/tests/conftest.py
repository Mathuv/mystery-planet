from pytest_factoryboy import register

from .factories import CompanyFactory, FoodFactory, PersonFactory

register(CompanyFactory)
register(FoodFactory)
register(PersonFactory)
