from rest_framework import generics
from product.serializers import *
from product.models import product, category, category_join_product, product_amount
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse, HttpResponse
from organization.models import *
from resturant.settings import url

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
    query = category_join_product.objects.filter(category__oraganizatsion_id=org_id).values('category__id', 'category__name', 'category__photo', 'product__id','product__name', 'product__photo')
    cat_data = category.objects.filter(oraganizatsion_id=org_id)
    data = {'organizatsion':org_name, "logo": f"{url}media/{str(org_logo)}", "categorys": []}

    for i in cat_data:
        data['categorys'].append({
            'name': i.name,
            'category_id': i.id,
            'category_photo_url': f"{url}media/{str(i.photo)}",
            'products': [],
            'next_products_url': f"{url}api/v1/org/next_products/{i.id}/1/",
            })
    for i in query:
        for x in data['categorys']:
            if len(x['products'])<6 and x['category_id']== i['category__id']:
                x['products'].append({
                    'product_name': i['product__name'],
                    'product_id': i['product__id'], 
                    'product_photo_url': f"{url}media/{str(i['product__photo'])}",
                    })

    return JsonResponse(data)
        

def get_products_api(requests, id):
    query = product_amount.objects.filter(product=id)
    data = {'product': query[0].product.name, "product_id":query[0].product.id, 'unit': query[0].product.unit.name, 'item': [], 'description': query[0].product.description, 'product_photo':f'{url}meida/{query[0].product.photo}'}
    for i in query:
        data['item'].append({
            "item_id" : i.id,
            'title':i.amount,
            'price': i.price,
        })
    return JsonResponse(data)


def get_api_pagination(request, id, num):
    product_data = category_join_product.objects.filter(category__id=id).values('category__id','category__name',\
        'product__id','product__name', 'product__photo')
    q = len(product_data)
    if q <= 6 * num:
        data = {}
    else:
        number = (6 * num) + 1
        count = 0
        data = {
                'category_name': product_data[0]['category__name'], 
                'category_id': product_data[0]['category__id'],
                'products' : []
            }
        for i in range(number, q):
            count += 1
            if count > 6:
                break
            data['products'].append({
                'product_name': product_data[i]['product__name'],
                'product_id': product_data[i]['product__id'],
                'product_photo_url': f"{url}media/{str(product_data[i].photo)}"
            })              
        data['next_products_url'] = f'{url}api/v1/org/next_page/{id}/{num+1}/'
    return JsonResponse(data)



