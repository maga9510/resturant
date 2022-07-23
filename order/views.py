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

# @csrf_exempt 
# def api_post(request ,format=None):

#     if request.method == "POST":
#         data = json.loads(request.body)
#         if len(data['product'])
#         # for i in data['product']:
#         #     print(i)



#     return JsonResponse(data)