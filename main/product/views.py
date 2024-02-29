from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer
from drf_spectacular.utils import extend_schema
# Create your views here.


#Create Category Viewset
class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


#Create Brand Viewset
class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


#Create Product Viewset
class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
