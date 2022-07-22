from django.urls import path, include
from product.views import *

urlpatterns = [

    path('category/create/', CategoryCreteView.as_view()),
    path('all_category/', CategoryListView.as_view()),
    path('category/detail/<int:pk>', CategoryListView.as_view()),
    path('product/create/', ProductCreteView.as_view()),
    path('all_product/', ProductListView.as_view()),
    path('product/detail/<int:pk>/', ProductListView.as_view()),
    path('org/<int:id>/getHomeDetail/', get_api_view),
    path('org/next_page/<str:cat_name>/<int:num>/', get_api_pagination),

    


]
