from rest_framework import serializers
from .models import Brand, Category, Product, ProductLine


# Create Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='name')

    class Meta:
        model = Category
        fields = ['category_name']


# Create Brand Serializer
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ['id']


# Create ProductLine Serializer
class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        exclude = ['id']


# Create Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name') 
    category_name = serializers.CharField(source='category.name')
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = ('name', 'slug', 'description', 'brand_name', 'category_name', 'product_line')
