from distutils.command.upload import upload
from operator import mod
# from pyexpat import model
from tkinter import CASCADE, Image
from unicodedata import category
from django.db import models
from django.utils.text import slugify

# Create your models here.

class QuantityVarient(models.Model):
    varient_name= models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.varient_name

class ColorVarient(models.Model):
    color_name= models.CharField(max_length=10)
    color_code= models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.color_name

class SizeVarient(models.Model):
    size= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.size




class Category(models.Model):
    category_name= models.CharField(max_length=100)
    slug= models.SlugField(max_length=200 , null=True, blank=True)
    def save(self, *args , **kwargs):
        self.slug= slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
 
    def __str__(self) -> str:
        return self.category_name


# class SubCategory(models.Model):
#     category= models.ForeignKey(Category, on_delete=models.PROTECT)
#     sub_category= models.CharField(max_length=200 , null=True ,blank= True)



class Product(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True , blank=True )
    # sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, null=True , blank= True)
    size= models.ForeignKey(SizeVarient, on_delete=models.PROTECT, null=True , blank=True)
    color= models.ForeignKey(ColorVarient, on_delete=models.PROTECT, null=True, blank=True)
    quantity= models.ForeignKey(QuantityVarient, on_delete=models.PROTECT ,null=True, blank=True)
    product_name= models.CharField(max_length=100)
    product_price= models.IntegerField(blank=False, null=False)
    product_img= models.ImageField(upload_to ='static/products')
    product_description = models.TextField()
    stock= models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.product_name
     
