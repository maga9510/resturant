from django.urls import path
from order.views import *

urlpatterns = [
    path('all_orders/', UserListView.as_view()),
    path('order/detail/<int:pk>/', UserDetailView.as_view()),
    path('order/create/', create_order_api),
    path('order/update/', update_order_api),
    path('order/getOrder/<int:id>/', cart_list),

]