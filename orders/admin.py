from django.contrib import admin
from .models import Order, OrderItem, Client, Product

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

# Register your models here.
