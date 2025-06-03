from django.urls import path
from orders.views import index, view_orders

urlpatterns = [
    path('', index, name='index'),
]