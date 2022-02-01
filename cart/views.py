from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CartAPI(APIView):
    permission_classes= [IsAuthenticated]
    def get(self, request):
        user= request.user
        print(user)
        quaryset= CartItem.objects.filter(user=user)

        
        serializer = CartItemSerializer(quaryset, many= True)


        return Response({'Success':"Authenticated successfully.", "data":serializer.data})

    def post(self, request):
        data= request.data
        user= request.user
        cart,_= Cart.objects.get_or_create(user=user, ordered=False)
        product= Product.objects.get(id= data.get('product_name'))
        price= product.product_price
        # price= Product.objects.get('product_price')
        quantity= data.get('quantity')
        cart_item= CartItem(product_name=product, user=user, cart=cart, price= price, quantity= quantity)
        cart_item.save()

        total_price= 0
        cart_item= CartItem.objects.filter(user=user , cart=cart.id)
        for item in cart_item:
            total_price += item.price
            print(f"Item Price :{item.price}")
        cart.total_price= total_price
        print(cart.total_price)

        cart.save()  


        return Response({"success":"Product Added Successfully."})

    def put(self, request):
        data= request.data
        item= CartItem.objects.get(id= data.get('id'))
        quantity= data.get('quantity')
        item.quantity += quantity
        item.save()

        return Response({"status":"data updated successfully."})

    def delete(self, request):
        user= request.user
        data= request.data
        item= CartItem.objects.get(id= data.get('id'))
        item.delete()
        queryset= CartItem.objects.filter(user=user)
        serializer= CartItemSerializer(queryset, many=True)



        return Response({"data":serializer.data})