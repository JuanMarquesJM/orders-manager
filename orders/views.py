from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'orders/index.html')

def view_orders(request):
    print("View orders page accessed.")
    return render(request, 'orders/view_orders.html')
