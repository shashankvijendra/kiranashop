from django.urls import path
from kirana_app import views


urlpatterns = [
    path('shop_list/', views.ShopList.as_view()), # 1.rgister  shop 
    path('shop_details/<int:pk>/', views.ShopDetail.as_view()),
    path('product_list/', views.ProductList.as_view()),
    path('product_details/<int:pk>/', views.ProductDetail.as_view()),
    path('Product_availableDetail/<str:shop_size>/', views.Product_availableDetail.as_view()), #2. Display list of eligible products based on shop size
    path('Product_mapping', views.Product_Mapping_Shop.as_view()), #3. Add choosen product
    path('Product_mapping/<int:pk>/<int:sk>', views.ProductMapping_each.as_view()), # 4. Retailer can mark product status and price
    path('Product_retrieve/<int:pk>/', views.Retrieve_product.as_view()), # 5. Retrieve Products based on shop
    path('Product_retrieve_serviceable/<int:pk>/', views.Retrieve_serviceable_product.as_view()), # 5.Retrieve serviceable Product
]
