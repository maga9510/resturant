from rest_framework import generics
from product.serializers import *
from product.models import product, category, category_join_product
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse
from organization.models import *
import os

url = os.environ.get('URL')

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

class Product_amountCreteView(generics.CreateAPIView):
    serializer_class = Product_amountDetailSerializers


class Product_amountListView(generics.ListAPIView):
    serializer_class = Product_amountListView
    queryset = product_amount.objects.all()


class Product_amountDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Product_amountDetailSerializers
    queryset = product_amount.objects.all()


class Category_JoinCreteView(generics.CreateAPIView):
    serializer_class = Category_JoinDetailSerializers


class Category_JoinListView(generics.ListAPIView):
    serializer_class = Category_JoinListView
    queryset = product_amount.objects.all()


class Category_JoinDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Category_JoinDetailSerializers
    queryset = product_amount.objects.all()







def get_api_view(request, id):
    org_data = organization_table.objects.get(id=id)
    org_id = org_data.room_id.oraganizatsion_id
    org_name = org_data.room_id.oraganizatsion_id.name
    data = {'organizatsion':org_name, 'category':[]}
    a = 0
    for i in category.objects.filter(oraganizatsion_id=org_id):
        name = i.name.replace(' ', '_')
        data['category'].append({
            f'{name}':{
                'organizatsion' : f'{i.oraganizatsion_id.name}',
                'photo_url' : f"{url}media/catigoris_logo/{str(i.photo).split('/')[1]}",
                'product': [],
                'next_page_url': f"{url}api/v1/org/next_page/{name}/1/",
                    }
            }
        )
        num = 0
        for e in category_join_product.objects.filter(category_id=i.id):
            num += 1
            if num > 6:
                break
            data['category'][a][name]['product'].append({
                'name': e.product.name,
                'unit': e.product.unit.name,
                'description': e.product.description,
                'org_name': e.product.organization.name,
            })
        a += 1
    return JsonResponse(data)

def get_api_pagination(request, cat_name, num):
    cat_name = cat_name.replace('_', ' ')
    product_data = category_join_product.objects.filter(category__name=cat_name)
    if len(product_data) < 6:
        data = {}
    else:
        w = 6
        w = (w * num) +1
        count = 0
        data = {
                'category': cat_name, 
                'product' : []
            }
        for i in range(w, len(product_data)):
            count += 1
            if count > 6:
                break
            data['product'].append({
                'name': product_data[i].product.name,
                'unit': product_data[i].product.unit.name,
                'description': product_data[i].product.description,
                'org_name': product_data[i].product.organization.name,
            }) 
        data['next_page_url'] = f'{url}api/v1/org/next_page/{cat_name}/{num+1}/'
    return JsonResponse(data)
