from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product_list', views.products_list, name='list_products'),
    path('product_details', views.product_details, name='product_details')
]