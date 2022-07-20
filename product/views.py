from django.shortcuts import render
from rest_framework import generics
from product.serializers import *
from product.models import product, category
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CategoryCreteView(generics.CreateAPIView):
    serializer_class = CategoryDetailSerializers

class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListView
    queryset = category.objects.all()
    pagination_class = StandardResultsSetPagination

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializers
    queryset = category.objects.all()





class ProductCreteView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializers

class ProductListView(generics.ListAPIView):
    serializer_class = ProductListView
    queryset = product.objects.all()
    pagination_class = StandardResultsSetPagination

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializers
    queryset = product.objects.all()
