from pyexpat import model
from rest_framework import serializers
from organization.models import user, partner



class UserListView(serializers.ModelSerializer):
    class Meta():
        model = user
        fields = ('id', 'name', 'role')

class UserDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = user
        fields = "__all__"




class PartnerListView(serializers.ModelSerializer):
    class Meta():
        model = partner
        fields = ('id', 'first_name', 'last_name', 'phone')

class PartnerDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = partner
        fields = "__all__"

