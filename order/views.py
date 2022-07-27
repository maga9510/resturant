import json
from django.http import HttpResponse, JsonResponse
from order.serializers import *
from order.models import order, cart
from rest_framework import generics

from django.views.decorators.csrf import csrf_exempt


class UserCreteView(generics.CreateAPIView):
    serializer_class = CartDetailSerializers

class UserListView(generics.ListAPIView):
    serializer_class = CartListView
    queryset = cart.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartDetailSerializers
    queryset = cart.objects.all()

@csrf_exempt 
def create_api(request, format=None):
    if request.method == "POST":
        data = json.loads(request.body)
        
        if data['order_id'] == None:
            order_data, create_order = order.objects.get_or_create(organization_table_id=data['table_num'], \
                status=data['status'], people_number=data['people_number'], paymants=data['paymant'])
            order_data.save()
            for i in data['product']:
                cart_data = cart(orders_id = order_data.id, product_amount_id=i['product_amount_id'], amount=i['quantity'])
                cart_data.save()
            return HttpResponse("200")
        else:
            for i in data['product']:
                cart_data = cart(orders_id = data['order_id'], product_amount_id=i['product_amount_id'], amount=i['quantity'])
                cart_data.save()
            return HttpResponse("200")





