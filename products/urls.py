
from unicodedata import name
from django.urls import path
from .views import *
urlpatterns = [

    path('', products , name= "products"),
    path('product/<id>', product ,name="product"),
    path('api', ProductAPI.as_view()),
    path('testing', jwtTesting.as_view())
    

    
]
