from dataclasses import fields
from rest_framework import serializers
from .models import *
from products.serializers import *

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cart
        fields= '__all__'



class CartItemSerializer(serializers.ModelSerializer):
    product_name= ProductSerielizer()
    cart= CartSerializer()
    class Meta:
        model= CartItem
        fields= '__all__'

        