from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from autoslug import AutoSlugField

# Create your models here.
#Category model created here
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    #slug = models.SlugField(max_length=250, unique=True)
    slug = AutoSlugField(max_length=250, unique=True, populate_from='name')
    is_active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


#Brand model created here
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    
#Product model created here
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    is_digital= models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) #on_delete=models.SET
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
   