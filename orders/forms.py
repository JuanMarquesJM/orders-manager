from django import forms
from .models import Product, Order, Client, OrderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category' ,'stock_quantity']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'company']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client']


OrderItemFormSet = forms.inlineformset_factory(
    Order, 
    OrderItem,
    fields=['product', 'quantity'], 
    extra=1, 
    can_delete=False, 
)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Username",
            "password1": "Password",
            "password2": "Confirm Password",
        }