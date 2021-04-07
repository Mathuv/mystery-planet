import pytest

from ..models import Company, Food, Person


@pytest.mark.django_db
def test_compapy_model_create(company_factory):
    company = company_factory()
    company_db = Company.objects.get(index=company.index)
    assert company_db.name == company.name
    assert company_db.index == company.index


@pytest.mark.django_db
def test_food_model_create(food_factory):
    food = food_factory()
    food_db = Food.objects.get(name=food.name)
    assert food_db.name == food.name
    assert food_db.type == food.type
    assert food_db.type in [Food.FOOD_TYPE_FRUIT, Food.FOOD_TYPE_VEGETABLE]


@pytest.mark.django_db
def test_person_model_create(person_factory, food_factory, company_factory):
    food_1: Food = food_factory()
    food_2: Food = food_factory()
    food_3: Food = food_factory()
    friend_1: Person = person_factory()
    friend_2: Person = person_factory()
    company: Company = company_factory()
    person: Person = person_factory(
        favourite_foods=(food_1, food_2, food_3), friends=(friend_1, friend_2), company=(company)
    )
    person_db = Person.objects.get(index=person.index)
    assert person_db.name == person.name
    assert person_db.friends
    assert person_db.favourite_foods
    assert person_db.company
