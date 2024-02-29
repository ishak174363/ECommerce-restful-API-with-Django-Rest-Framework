import pytest
pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self,category_factory):
        # Arrange
        # Act
        category = category_factory(name="test category")
        # Assert
        assert category.__str__() ==  "test category"
        

class TestProductModel:
        def test_str_method(self,product_factory):
            # Arrange
            # Act
            category = product_factory(name="test product")
            # Assert
            assert category.__str__() ==  "test product"

class TestBrandModel:
     def test_str_method(self,brand_factory):
        # Arrange
        # Act
        category = brand_factory(name="test brand")
        # Assert
        assert category.__str__() ==  "test brand"
        
