import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from main.tests.factories import CategoryFactory, BrandFactory, ProductFactory


register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)

#category_factory = CategoryFactory()


@pytest.fixture
def api_client():
    return APIClient
