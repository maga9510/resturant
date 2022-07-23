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
    org_id = org_data.room_id.oraganizatsion_id
    org_name = org_data.room_id.oraganizatsion_id.name
    data = {'organizatsion':org_name, 'category':[]}
    a = 0
    for i in category.objects.filter(oraganizatsion_id=org_id):
        name = i.name.replace(' ', '_')
        data['category'].append({
                'name': name,
                'organizatsion' : f'{i.oraganizatsion_id.name}',
                'photo_url' : f"{url}media/catigoris_logo/{str(i.photo).split('/')[1]}",
                'product': [],
                'next_page_url': f"{url}api/v1/org/next_page/{name}/1/",
                    }
            
        )
        num = 0
        for e in category_join_product.objects.filter(category_id=i.id):
            amount_data = product_amount.objects.get(product__id=e.product.id)
            num += 1
            if num > 6:
                break
            data['category'][a]['product'].append({
                'name': e.product.name,
                'p_amount': amount_data.amount,
                'price': amount_data.price,
                'unit': e.product.unit.name,
                'description': e.product.description,
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
            p_data = product_data[i]
            amount_data = product_amount.objects.get(product__id=p_data.product.id)

            count += 1
            if count > 6:
                break
            data['product'].append({
                'name': p_data.product.name,
                'p_amount': amount_data.amount,
                'price': amount_data.price,
                'unit': p_data.product.unit.name,
                'description': p_data.product.description,
                'org_name': p_data.product.organization.name,
            }) 
        data['next_page_url'] = f'{url}api/v1/org/next_page/{cat_name}/{num+1}/'
    return JsonResponse(data)


