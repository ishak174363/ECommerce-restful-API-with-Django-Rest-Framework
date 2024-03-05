from django.contrib import admin
from .models import Category, Product,Brand, ProductLine


# Register your models here.

#ProductLineInline class created here
class ProductLineInline(admin.TabularInline):
    model = ProductLine


@admin.register(Product)  
class ProductAdmin(admin.ModelAdmin):
   inlines = [ProductLineInline]

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductLine)
