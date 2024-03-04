from rest_framework import serializers
from .models import Brand, Category, Product,ProductLine


#Create Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        #fields = '__all__'
        fields=['name']


#Create Brand Serializer
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
    
    
#Create Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    brand=BrandSerializer()
    category=CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


#Create ProductLine Serializer
class ProductLineSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model = ProductLine
        fields = '__all__'
