from django.contrib import admin
from django.urls import path, include
from orders.views import index, view_orders


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('view_orders/', view_orders, name='view_orders'),
]
