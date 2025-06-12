from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm, OrderItem

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