from django.contrib import admin
from django.urls import path
from orders.views import index, view_orders, create_order, clients, products, add_new_product, add_new_client


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('view_orders/', view_orders, name='view_orders'),
    path('create_order/', create_order, name='create_order'),
    path('clients/', clients, name='clients'),
    path('products/', products, name='products'),
    path('add_new_product/', add_new_product, name='add_new_product'),
    path('add_new_client/', add_new_client, name='add_new_client'),
]
