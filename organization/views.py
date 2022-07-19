from rest_framework import generics
from organization.serializers import *
from product.models import user, partner



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
