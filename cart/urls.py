from django.urls import path
from .views import *

urlpatterns = [
    path('', CartAPI.as_view()),
    path('order/', OrderAPI.as_view())
]