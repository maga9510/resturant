from rest_framework import generics
from organization.serializers import *
from product.models import user, partner
from django.http import request



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

def home(request):
    print(request.POST)