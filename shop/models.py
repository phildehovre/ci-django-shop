from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from base.models import Address
from django.db.models import JSONField

# Create your models here.

RATING = (
    (1, "Terrible"),
    (2, "Poor"),
    (3, "Average"),
    (4, "Good"),
    (5, "Excellent"),
)
ORDER_STATUS = (
    (0, "INERT"),
    (1, "PENDING"),
    (2, "PROCESSING"),
    (3, "SHIPPED"),
    (4, "COMPLETED"),
    (5, "CANCELLED"),
)

class ProductTag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(default='https://www.eag-led.com/wp-content/uploads/2017/04/Product-Image-Coming-Soon.png', upload_to='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(ProductTag)
    stock = models.IntegerField(default=999)

    def __str__(self):
        return self.name
    
class ProductSpecs(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    specs = JSONField()

    def __str__(self):
        return self.specs
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')
    alt=models.CharField(max_length=150)

    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=ORDER_STATUS, default=1)
    shipping = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.id} - User: {self.user.username}"

    def total(self):
        total = sum(item.total_item_price for item in self.order_items.all())
        return total
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order #{self.order.id} - {self.quantity} x {self.product.name}"
    
    def total(self):
        total = self.product.price * self.quantity
        return total

    @property
    def total_item_price(self):
        return self.quantity * self.product.price
    
class Feature(models.Model):
    image=models.ImageField(upload_to="feature_pictures")
    active=models.BooleanField(default=False)
    title=models.CharField(max_length=250)
    subtitle=models.CharField(max_length=250)
    tags = models.ManyToManyField(ProductTag)

    def __str__(self):
        return self.title
