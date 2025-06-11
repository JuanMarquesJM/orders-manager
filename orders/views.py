from django.shortcuts import render, redirect
from orders.models import Order, Client, Product
from .forms import ProductForm

def index(request):
    return render(request, 'orders/index.html')

def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/view_orders.html', {'orders': orders})

def create_order(request):
    return render(request, 'orders/create_order.html')

def clients(request):
    clients = Client.objects.all()
    return render(request, 'orders/clients.html', {'clients': clients})

def products(request):
    products = Product.objects.all()
    return render(request, 'orders/products.html', {'products': products})

def add_new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'orders/add_new_product.html', {'form': form})

def add_new_client(request):
    return render(request, 'orders/add_new_client.html')
