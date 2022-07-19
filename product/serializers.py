from pyexpat import model
from rest_framework import serializers
from product.models import product

class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = product
        fields = "__all__"