from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm, OrderItem, RegisterForm
from django.forms import inlineformset_factory
from .models import Order, Product
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

@login_required
def index(request):
    return render(request, 'orders/index.html')

@login_required
def clients(request):
    all_clients = Client.objects.all()
    return render(request, 'orders/clients.html', {'clients': all_clients})

@login_required
def add_new_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client added successfully.')
            return redirect('clients')
    else:
        form = ClientForm()
    return render(request, 'orders/add_client.html', {'form': form, 'title': 'Add New Client'})

@login_required
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client deleted successfully.')
        return redirect('clients')
    return render(request, 'orders/delete_client.html', {'client': client})

@login_required
def update_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated successfully.')
            return redirect('clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'orders/update_client.html', {'form': form, 'title': 'Edit Client'})

@login_required
def products(request):
    products = Product.objects.all()
    return render(request, 'orders/products.html', {'products': products})

@login_required
def add_new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully.')
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'orders/product_form.html', {'form': form, 'title': 'Add Product'})

@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            updated_product = form.save(commit=False)
            updated_product.save() 
            messages.success(request, f'Product "{updated_product.name}" updated successfully!')
            return redirect('products')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'orders/product_update.html', {
        'form': form,
        'product': product
    })

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('products')
    return render(request, 'orders/product_confirm_delete.html', {'object': product})

def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/view_orders.html', {'orders': orders})


OrderItemFormSet = inlineformset_factory(
    Order,
    OrderItem,
    fields=('product', 'quantity',),
    extra=1,
    can_delete=True
)

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            order = form.save()
            formset.instance = order
            formset.save()
            messages.success(request, 'Order created successfully.')
            return redirect('view_orders')
    else:
        form = OrderForm()
        formset = OrderItemFormSet()
    return render(request, 'orders/order_form.html', {
        'form': form,
        'formset': formset,
        'title': 'Create Order'
    })


@login_required
def update_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    OrderItemFormSet = inlineformset_factory(
        Order, 
        OrderItem,
        fields=('product', 'quantity'),
        extra=0  
    )

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        formset = OrderItemFormSet(request.POST, instance=order)
        
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()  # Isso já salva todas as instâncias
            messages.success(request, 'Order updated successfully.')
            return redirect('view_orders')
    else:
        form = OrderForm(instance=order)
        formset = OrderItemFormSet(instance=order)
    
    return render(request, 'orders/update_order.html', {
        'form': form,
        'formset': formset,
        'order': order
    })


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_details.html', {'order': order})


@login_required
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order deleted successfully.')
        return redirect('view_orders')
    return render(request, 'orders/order_confirm_delete.html', {'object': order})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')  
    else:
        form = RegisterForm()
    
    return render(request, 'orders/register.html', {
        'form': form,
        'hide_navbar': True
     })

class CustomLoginView(LoginView):
    template_name = 'orders/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_navbar'] = True
        return context