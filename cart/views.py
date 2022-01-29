from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
# from .serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CartAPI(APIView):
    permission_classes= [IsAuthenticated]
    def get(self, request):
        user= request.user
        print(user)

        return Response({'Success':"Authenticated successfully."})

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

        return Response({"success":"Product Added Successfully."})

    def update(self, request):
        return Response({})

    def delete(self, request):
        return Response({})