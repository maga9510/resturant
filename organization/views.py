from rest_framework import generics
from organization.serializers import *
from product.models import (
    user, 
    partner, 
    room, 
    platform_user, 
    organization_table
    )


class UserCreteView(generics.CreateAPIView):
    serializer_class = UserDetailSerializers

class UserListView(generics.ListAPIView):
    serializer_class = UserListView
    queryset = user.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializers
    queryset = user.objects.all()


class PartnerCreteView(generics.CreateAPIView):
    serializer_class = PartnerDetailSerializers

class PartnerListView(generics.ListAPIView):
    serializer_class = PartnerListView
    queryset = partner.objects.all()

class PartnerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PartnerDetailSerializers
    queryset = partner.objects.all()


class OrganizatsionCreteView(generics.CreateAPIView):
    serializer_class = OrganizatsionDetailSerializers

class OrganizatsionListView(generics.ListAPIView):
    serializer_class = OrganizatsionListView
    queryset = organizatsion.objects.all()

class OrganizatsionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrganizatsionDetailSerializers
    queryset = organizatsion.objects.all()


class PlatformUserCreteView(generics.CreateAPIView):
    serializer_class = PlatformUserDetailSerializers

class PlatformUserListView(generics.ListAPIView):
    serializer_class = PlatformUserListView
    queryset = platform_user.objects.all()

class PlatformUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlatformUserDetailSerializers
    queryset = platform_user.objects.all()


class RoomCreteView(generics.CreateAPIView):
    serializer_class = RoomDetailSerializers

class RoomListView(generics.ListAPIView):
    serializer_class = RoomListView
    queryset = room.objects.all()

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomDetailSerializers
    queryset = room.objects.all()

    
class Org_tableCreteView(generics.CreateAPIView):
    serializer_class = RoomDetailSerializers

class Org_tableListView(generics.ListAPIView):
    serializer_class = RoomListView
    queryset = organization_table.objects.all()

class Org_tableDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomDetailSerializers
    queryset = organization_table.objects.all()