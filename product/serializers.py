from pyexpat import model
from rest_framework import serializers
from product.models import product, category



class CategoryListView(serializers.ModelSerializer):
    class Meta():
        model = category
        fields = ('id', 'name', 'organization_id.name')

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

