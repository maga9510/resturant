from django.urls import path, include
from product.views import *

urlpatterns = [

    path('category/create/', CategoryCreteView.as_view()),
    path('all_category/', CategoryListView.as_view()),
    path('category/detail/<int:pk>', CategoryDetailView.as_view()),
    
    path('product/create/', ProductCreteView.as_view()),
    path('all_product/', ProductListView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view()),
    
    path('all_amount/', Product_amountListView.as_view()),
    path('product/amoun/create/', Product_amountCreteView.as_view()),
    path('product/amoun/detail/<int:pk>/', Product_amountDetailView.as_view()),

    path('all_cjp/', Product_amountListView.as_view()),
    path('product/cjp/create/', Product_amountCreteView.as_view()),
    path('product/cjp/detail/<int:pk>/', Product_amountDetailView.as_view()),

    path('org/<int:id>/getHomeDetail/', get_categorys_api),
    path('org/getProducts/<int:id>/', get_products_api),
    path('org/next_products/<int:id>/<int:num>/', get_api_pagination),


]
