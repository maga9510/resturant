from django.urls import path
from order.views import *

urlpatterns = [

    path('order/create/', UserCreteView.as_view()),
    path('all_orders/', UserListView.as_view()),
    path('order/detail/<int:pk>/', UserDetailView.as_view()),
    path('order/create_api/', create_api),
    # path('order/update_api/', api_post),
]