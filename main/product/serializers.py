from rest_framework import serializers
from .models import Brand, Category, Product,ProductLine



#Create Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        #fields = '__all__'
        fields=['name']
        #exclude=['id']


#Create Brand Serializer
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        #fields = '__all__'
        exclude=['id']


#Create ProductLine Serializer
class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        #fields = '__all__'
        exclude=['id']
    
    
#Create Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    brand=BrandSerializer()
    category=CategorySerializer()
    product_line=ProductLineSerializer(many=True)
    
    class Meta:
        model = Product
        #fields = '__all__'
        exclude=['id']

