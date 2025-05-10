from django.db import models
from users.models import User
from products.models import Product

# Order Model

class Orders(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'live'), (DELETE, 'delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_REJECTED = -1
    ORDER_PROCCESED = 2
    ORDER_DELIVERD = 3
    STATUS_CHOICE = (( ORDER_PROCCESED, "ORDER_PROCCESED"),
                     ( ORDER_DELIVERD, "ORDER_DELIVERD"),
                     ( ORDER_REJECTED, "ORDER_REJECTED"))
    ORDER_STATUS = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    owner=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='added_products')
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='added_items')
    
    