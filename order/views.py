from django.http import HttpResponse, JsonResponse
from order.serializers import *
from order.models import order, cart
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json


geo_pos = {
    'lon_1': 39.64805,
    'lon_2': 39.64815,
    'lat_1': 66.93725,
    'lat_2': 66.93755,
}

class UserListView(generics.ListAPIView):
    serializer_class = CartListView
    queryset = cart.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartDetailSerializers
    queryset = cart.objects.all()

def cart_list(request, id):
    if request.method == "GET":
        q = cart.objects.filter(orders_id=id)
        data = {"order_id" : id, "products":[]}
        for i in q:
            data['products'].append({
                "product_id": i.product_amount.product.id,
                "product_name": i.product_amount.product.name,
                "amount": i.product_amount.amount,
                "price": i.product_amount.price,
                "quantity" : i.amount,
            })
        return JsonResponse(data)

@csrf_exempt 
def create_order_api(request):
    if request.method == "POST":    
        data = json.loads(request.body)
        if geo_pos['lat_1'] <= data['geo_code'][0] <= geo_pos['lat_2'] and geo_pos['lon_1'] <= data['geo_code'][1] <= geo_pos['lon_2']:
            order_data = order(organization_table_id=data['table_num'], name=data['name'], last_name=data['last_name'], phone=data['phone'],\
                 people_number=data['people_number'], paymants=data['paymant'])
            order_data.save()
            for i in data['product']:
                cart_data = cart(orders_id = order_data.id, product_amount_id=i['product_amount_id'], amount=i['quantity'])
                cart_data.save()
            r = {
                "order_id": order_data.id,
                "order_status": "pending",
            }
            return JsonResponse(r)     

@csrf_exempt 
def update_order_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        cart_data = cart.objects.filter(orders_id=data['order_id']).values_list('product_amount')
        some = []
        for i in cart_data:
            some.append(i[0])
        if data['products']['product_amount_id'] not in some:
            q = cart(orders_id=data['order_id'], product_amount_id=data["products"]['product_amount_id'], amount = data["products"]['quantity'])
            q.save()
        else:
            print('sdsddsds')
            w = get_object_or_404(cart, orders_id=data['order_id'], product_amount_id=data['products']['product_amount_id'])
            w.amount += data['products']['quantity']
            w.save()

        return HttpResponse('200')


##### for create order
# {
#     "name": "Ali",
#     "last_name": "Ali-Axunov",
#     "phone":"+998971234567",
#     "table_num": 3,
#     "people_number": 3,
#     "paymant": "Cash",
#     "geo_code":[66.9373, 39.6479],
#     "product" : [
#         {"product_id": 1, "product_amount_id": 2, "quantity": 3 },
#         {"product_id": 2, "product_amount_id": 1, "quantity": 1 },
#         {"product_id": 3, "product_amount_id": 4, "quantity": 1 }
#     ]
# }


##### for update cart
# {
#     "order_id": 9,
#     "products" : {"product_id": 12, "product_amount_id": 8, "quantity": 1}
# }
