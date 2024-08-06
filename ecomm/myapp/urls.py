from django.urls import path
from .views import (index, product_list, product_detail , add_product, 
                    update_product, delete_product, my_listings, 
                    ProductListView, ProductDetailView, ProductCreateView,
                    ProductUpdateView, 
                    )


app_name= 'myapp' 

urlpatterns = [
    path('', index ), 
    path('products/', product_list, name='products'), 
    # path('products/', ProductListView.as_view(), name='products'),  
    
    # path('products/<int:pk>/',product_detail, name = 'product_detail'), 
    path('products/<int:pk>/',ProductDetailView.as_view(), name = 'product_detail'), 

    # path('products/add/', add_product, name = 'add_product'), 
    path('products/add/', ProductCreateView.as_view(), name = 'add_product'),  

    path('products/delete/<int:pk>', delete_product, name = 'delete_product'), 
    # path('products/update/<int:pk>', update_product, name = 'update_product'), 
    
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name = 'update_product'),  

    path('products/mylistings/', my_listings , name='mylistings'), 

] 
