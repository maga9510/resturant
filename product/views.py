from django.shortcuts import render
from rest_framework import generics
from product.serializers import *


class ProductCreteView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializers