from django import forms
from .models import Product, Order, Client, OrderItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'description', 'price', 'category', 'stock_quantity']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client  # Assuming you have a Client model similar to Product
        fields = ['client_id', 'name', 'email', 'company']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_id', 'client', 'status', 'payment_method']


OrderItemFormSet = forms.inlineformset_factory(
    Order, OrderItem,
    fields=['product', 'quantity'], extra=1, can_delete=True,
)