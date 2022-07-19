from pyexpat import model
from rest_framework import serializers
from organization.models import user, partner, organizatsion



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



class OrganizatsionListView(serializers.ModelSerializer):
    class Meta():
        model = organizatsion
        fields = ('id', 'name', 'partner', 'phone')

class OrganizatsionDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = organizatsion
        fields = "__all__"
