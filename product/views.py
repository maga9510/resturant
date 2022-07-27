
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


def get_api_view(request, id):
    org_data = organization_table.objects.get(id=id)
    org_id = org_data.room_id.oraganizatsion_id.id
    org_name = org_data.room_id.oraganizatsion_id.name
    data = {'organizatsion':org_name, 'category':[]}
    a = 0

    for i in category.objects.filter(oraganizatsion_id__id=org_id):
        data['category'].append({
                'name': i.name,
                'category_id': i.id,
                'organizatsion' : f'{i.oraganizatsion_id.name}',
                'photo_url' : f"{url}media/catigoris_logo/{str(i.photo).split('/')[1]}",
                'product': [],
                'next_page_url': f"{url}api/v1/org/next_page/{i.id}/1/",
                    }
        )
        num = 0

        for e in category_join_product.objects.filter(category_id=i.id):
            num += 1
            if num > 6:
                break
            data['category'][a]['product'].append({
                'product_name': e.product.name,
                'product_id': e.product.id,
                'amount':[],
                'unit': e.product.unit.name,
                'description': e.product.description,
                'url_photo': f"{url}media/catigoris_logo/{str(e.product.photo).split('/')[1]}"
            })

        for w in data['category'][a]['product']:
            amount_data = product_amount.objects.filter(product__id=w['product_id'])

            for q in amount_data:
                w['amount'].append({
                    'amount_id':q.id,
                    'amount': q.amount,
                    'price':q.price,
                    })
        a += 1
    return JsonResponse(data)

def get_api_pagination(request, id, num):
    product_data = category_join_product.objects.filter(category__id=id)
    if len(product_data) < 6 * num:
        data = {}
    else:
        number = (6 * num) + 1
        count = 0
        data = {
                'category': product_data[0].category.name, 
                'category_id': product_data[0].category.id,
                'product' : []
            }

        for i in range(number, len(product_data)):
            p_data = product_data[i]
            count += 1
            if count > 6:
                break
            data['product'].append({
                'product_id': p_data.product.id,
                'name': p_data.product.name,
                'amount': [],
                'unit': p_data.product.unit.name,
                'description': p_data.product.description,
                'url_photo': f"{url}media/product_photo/{str(p_data.product.photo).split('/')[1]}"
            })  
        
        for e in data['product']:
            amount_data = product_amount.objects.filter(product__id=e['product_id'])
            for w in amount_data:
                e['amount'].append({
                    'amount_id':w.id,
                    'amount': w.amount,
                    'price':w.price,
                })                
        data['next_page_url'] = f'{url}api/v1/org/next_page/{id}/{num+1}/'
    return JsonResponse(data)


