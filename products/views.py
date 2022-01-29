

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class jwtTesting(APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        print(request.user)
        return Response({"Status":'authenticated successfully.'})

class ProductAPI(APIView):
    def get(self, request):
        category= self.request.query_params.get('category')
        if category:
            
            queryset= Product.objects.filter(category__category_name= category)
            if len(queryset)==0 :
                queryset= Product.objects.filter(category__category_name__contains= category)

                print('size', len(queryset))
        else:
           queryset = Product.objects.all()
           
        serializer= ProductSerielizer(queryset, many= True)

        return Response({"status":"working","total": len(serializer.data), "data": serializer.data})


def products(request):
    return render(request, 'products.html')


def product(request, id):
    return render(request, 'product.html')