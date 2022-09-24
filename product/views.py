from calendar import month
from rest_framework import generics
from product.serializers import *
from product.models import product, category, category_join_product, product_amount
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse
from organization.models import *
from resturant.settings import url
from django.db.models import Count
from datetime import datetime, timedelta
from django.utils import timezone

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


def get_categorys_api(request, id):
    org_data = organization_table.objects.get(id=id)
    org_id = org_data.room_id.oraganizatsion_id.id
    org_name = org_data.room_id.oraganizatsion_id.name
    org_logo = org_data.room_id.oraganizatsion_id.logo
    date = (timezone.now() - timedelta(weeks = 18))
    data = {'organizatsion':org_name, "logo": f"{url}media/{str(org_logo)}", "categorys": []}
    query = list(category_join_product.objects.filter(category__oraganizatsion_id=org_id, product__product_amount__cart__craete_add__range = [date, timezone.now()]).annotate(dcount=Count('product__product_amount__cart__amount')).order_by('-dcount')\
        .values('category__id', 'category__name', 'category__photo', 'product__id','product__name', 'product__photo'))
    all_query = list(category_join_product.objects.filter(category__oraganizatsion_id=org_id).values('category__id', 'category__name', 'category__photo', 'product__id','product__name', 'product__photo'))
    x = []
    for i in all_query:
        if i not in query:
            query.append(i)
    for i in query:
        if i['category__id'] not in x:
            x.append(i['category__id'])
            data['categorys'].append({
                'name': i['category__name'],
                'category_id': i['category__id'],
                'category_photo_url': f"{url}media/{str(i['category__photo'])}",
                'products': [],
                'next_products_url': None,
                })
    some = {i : 0 for i in x}
    for i in query:
        some[i['category__id']] += 1
        q = x.index(i['category__id'])
        if some[i['category__id']] > 5:
            data['categorys'][q]['next_products_url'] = f"{url}api/v1/org/next_products/{i['category__id']}/1/"
            continue
        if len(data['categorys'][q]['products']) < 6:
            data['categorys'][q]['products'].append({
                'product_name': i['product__name'],
                'product_id': i['product__id'], 
                'product_photo_url': f"{url}media/{str(i['product__photo'])}",
                })
    return JsonResponse(data)
        

def get_products_api(requests, id):
    query = product_amount.objects.filter(product=id)
    data = {'product': query[0].product.name, "product_id":query[0].product.id, 'item': [], 'description': query[0].product.description, 'product_photo':f'{url}meida/{query[0].product.photo}'}
    for i in query:
        data['item'].append({
            "item_id" : i.id,
            'title':i.title,
            'price': i.price,
        })
    return JsonResponse(data)


def get_api_pagination(request, id, num):
    product_data = category_join_product.objects.filter(category__id=id).values('category__id','category__name',\
        'product__id','product__name', 'product__photo')[6:]
    q = len(product_data)
    data = {
            'category_name': product_data[0]['category__name'], 
            'category_id': product_data[0]['category__id'],
            'products' : []
        }
    count = 0
    for i in product_data:
        count += 1
        if count > 6:
            break
        data['products'].append({
            'product_name': i['product__name'],
            'product_id': i['product__id'],
            'product_photo_url': f"{url}media/{str(i['product__photo'])}"
        })  
    if q / 6 > num+1:           
        data['next_products_url'] = f'{url}api/v1/org/next_products/{id}/{num+1}/'
    else:
        data['next_products_url'] = None
    return JsonResponse(data)


