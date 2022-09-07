from pyexpat import model
from rest_framework import serializers
from order.models import ( 
    order, 
    cart
)

class OrderListView(serializers.ModelSerializer):
    class Meta():
        model = order
        fields = ('id', 'name', 'role')

class OrderDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = order
        fields = "__all__"



class CartListView(serializers.ModelSerializer):
    class Meta():
        model = cart
        fields = "__all__"


class CartDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = cart
        fields = "__all__"



