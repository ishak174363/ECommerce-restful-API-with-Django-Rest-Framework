from pytest_factoryboy import register
from main.tests.factories import CategoryFactory, BrandFactory, ProductFactory


register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)

#category_factory = CategoryFactory()
