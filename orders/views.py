from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'orders/index.html')

def view_orders(request):
    return render(request, 'orders/view_orders.html')

def create_order(request):
    return render(request, 'orders/create_order.html')

def clients(request):
    return render(request, 'orders/clients.html')

def products(request):
    return render(request, 'orders/products.html')
