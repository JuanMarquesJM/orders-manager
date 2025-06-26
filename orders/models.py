import uuid
from django.db import models
from django.utils import timezone

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    CATEGORY_CHOICES = [
        ('ELECTRONICS', 'Electronics'),
        ('OFFICE_SUPPLIES', 'Office Supplies'),
        ('CLOTHING', 'Clothing'),
        ('FOOD', 'Food'),
        ('OTHER', 'Other'),
    ]
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='OTHER')
    stock_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, editable=False)  

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_number = models.CharField(max_length=10, unique=True, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return f"Order {self.order_number} by {self.client.name}"

    @property
    def total(self):
        return sum(item.total_price for item in self.items.all())
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.order_by('-created_at').first()
            last_number = int(last_order.order_number.split('-')[-1]) if last_order else 0
            self.order_number = f"ORD-{str(last_number + 1).zfill(4)}"
        super().save(*args, **kwargs)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.order.order_number}"

    @property
    def total_price(self):
        return self.product.price * self.quantity
