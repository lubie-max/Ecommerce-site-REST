from dataclasses import field, fields
from rest_framework import serializers
from .models import *




class QuantityVarientSerializer(serializers.ModelSerializer):
 
 class Meta:

    model= QuantityVarient
    fields= "__all__"

class ColorVarientSerializer(serializers.ModelSerializer):
    
    class Meta:
         model=ColorVarient
         fields= "__all__"

class SizeVarientSerializer(serializers.ModelSerializer):
     
     class Meta:
         model=SizeVarient
         fields= '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= '__all__'


class ProductSerielizer(serializers.ModelSerializer):
    category= CategorySerializer()
    size= SizeVarientSerializer()
    quantity= QuantityVarientSerializer()
    color = ColorVarientSerializer()
    class Meta:
        model = Product
        fields = '__all__'
        



# class QuantityVarientSerializer(serializers.ModelSerializer):
