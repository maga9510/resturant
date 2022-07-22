from django.urls import path, include
from organization.views import *

urlpatterns = [

    path('user/create/', UserCreteView.as_view()),
    path('all_user/', UserListView.as_view()),
    path('user/detail/<int:pk>/', UserDetailView.as_view()),

    path('partner/create/', PartnerCreteView.as_view()),
    path('all_partner/', PartnerListView.as_view()),
    path('partner/detail/<int:pk>/', PartnerDetailView.as_view()),
    
    path('organizatsion/create/', PartnerCreteView.as_view()),
    path('all_organizatsions/', PartnerListView.as_view()),
    path('organizatsion/detail/<int:pk>/', PartnerDetailView.as_view()),

    path('pf_user/create/', PlatformUserCreteView.as_view()),
    path('all_pf_user/', PlatformUserListView.as_view()),
    path('pf_user/detail/<int:pk>/', PlatformUserDetailView.as_view()), 

    path('room/create/', RoomCreteView.as_view()),
    path('all_room/', RoomListView.as_view()),
    path('room/detail/<int:pk>/', RoomDetailView.as_view()), 



]
