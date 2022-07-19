from django.urls import path, include
from organization.views import *

urlpatterns = [

    path('user/create/', UserCreteView.as_view()),
    path('all_user/', UserListView.as_view()),
    path('user/detail/<int:pk>/', UserDetailView.as_view()),
    path('partner/create/', PartnerCreteView.as_view()),
    path('all_partner/', PartnerListView.as_view()),
    path('partner/detail/<int:pk>/', PartnerDetailView.as_view()),
]
