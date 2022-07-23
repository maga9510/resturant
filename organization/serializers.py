from pyexpat import model
from rest_framework import serializers
from organization.models import (
    organization_table,
    user,
    partner, 
    organizatsion, 
    platform_user, 
    room,
    organization_table,
)



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


class PlatformUserListView(serializers.ModelSerializer):
    class Meta():
        model = platform_user
        fields = ('id', 'organization', 'full_name', 'role')

class PlatformUserDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = platform_user
        fields = "__all__"


class RoomListView(serializers.ModelSerializer):
    class Meta():
        model = room
        fields = ('id', 'name', 'oraganizatsion_id')

class RoomDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = room
        fields = "__all__"


class Org_tableListView(serializers.ModelSerializer):
    class Meta():
        model = organization_table
        fields = ('id', 'number', 'room_id')

class Org_tableDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = organization_table
        fields = "__all__"




