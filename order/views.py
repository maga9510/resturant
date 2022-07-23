from django.http import HttpResponse
from order.serializers import *
from order.models import order, cart
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


class UserCreteView(generics.CreateAPIView):
    serializer_class = CartDetailSerializers

class UserListView(generics.ListAPIView):
    serializer_class = CartListView
    queryset = cart.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartDetailSerializers
    queryset = cart.objects.all()


def api_post(request):

    print(request.data)
    return HttpResponse('ok')