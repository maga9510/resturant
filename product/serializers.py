from pyexpat import model
from rest_framework import serializers
from product.models import product, category, product_amount



class CategoryListView(serializers.ModelSerializer):
    class Meta():
        model = category
        fields = ('id', 'name', 'oraganizatsion_id', 'photo')

class CategoryDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = category
        fields = "__all__"




class ProductListView(serializers.ModelSerializer):
    class Meta():
        model = product
        fields = ('id', 'name', 'unit', 'organization')

class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = product
        fields = "__all__"


class UnitListView(serializers.ModelSerializer):
    class Meta():
        model = product
        fields = ('name')


class UnitDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = product
        fields = "__all__"


# class Product_amountListView(serializers.ModelSerializer):
#     class Meta():
#         model = product_amount
#         fields = ('product', 'amount', 'price')


# class Product_amountDetailSerializers(serializers.ModelSerializer):
#     class Meta():
#         model = product_amount
#         fields = "__all__"