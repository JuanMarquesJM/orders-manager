from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('clients/', views.clients, name='clients'),
    path('clients/add/', views.add_new_client, name='add_new_client'),
    path('clients/<uuid:pk>/edit/', views.update_client, name='update_client'),
    path('clients/<uuid:pk>/delete/', views.delete_client, name='delete_client'),

    path('products/', views.products, name='products'),
    path('products/add/', views.add_new_product, name='add_new_product'),
    path('products/<uuid:pk>/edit/', views.update_product, name='update_product'),
    path('products/<uuid:pk>/delete/', views.delete_product, name='delete_product'),

    path('orders/', views.view_orders, name='view_orders'),
    path('orders/add/', views.create_order, name='create_order'),
    path('orders/<uuid:pk>/', views.order_detail, name='order_details'),
    path('orders/<uuid:pk>/edit/', views.update_order, name='update_order'),
    path('orders/<uuid:pk>/delete/', views.delete_order, name='delete_order'),
]
