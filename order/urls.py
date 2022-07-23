from django.urls import path
from order.views import *

urlpatterns = [

    path('order/create/', UserCreteView.as_view()),
    path('all_orders/', UserListView.as_view()),
    path('order/detail/<int:pk>/', UserDetailView.as_view()),
    path('order/api/', api_post),
]