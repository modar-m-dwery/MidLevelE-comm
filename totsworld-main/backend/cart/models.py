from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Cart(models.Model):
    ''' field : user_id product_id and more to be decided '''
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

    @property
    def get_item_total_price(self):
        return self.product.price * float(self.quantity)

    def get_total_price(self,usr=None):
        """return sum(item.product.price*item.quantity for item in Cart.objects.filter(.
        items = Cart.objects.filter(user=usr)
        total = sum(item.get_item_total_price for item in items)
        return total"""
        pass