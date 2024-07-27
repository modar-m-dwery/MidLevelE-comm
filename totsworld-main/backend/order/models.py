
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User
from core.models import UserAddress
from product.models import Product

# Create your models here.
class Order(models.Model):
    status = (('pending','Pending'),
        ('successful','Successful'),
        ('recived','Recived'),
        ('packed','Packed'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('canceled','Canceled'),
        ('return requested','Return requested'),
        ('returned','Returned'),
        ('refunded','Refunded'),
        ('failed','Failed'))
    
    pay_status = (('pending','Pending'),
        ('successful','Successful'),
        ('failed','Failed'))
    order_uniqid = models.CharField(max_length=30,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.ForeignKey(UserAddress,on_delete=models.CASCADE)
    coupon_code = models.CharField(max_length=50,null=True,blank=True)
    payment_status = models.CharField(choices=pay_status,max_length=50,default='pending')
    order_status = models.CharField(choices=status,max_length=50,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"
        
    def __str__(self):
        return 'Order {}'.format(self.pk)

    def get_products(self):
        items = ProductOrder.objects.filter(order=self.pk)

class ProductOrder(models.Model):
    ''' field : product_id, order_id and more to be decided '''
    status = (('pending','Pending'),
        ('successful','Successful'),
        ('recived','Recived'),
        ('packed','Packed'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('canceled','Canceled'),
        ('return requested','Return requested'),
        ('returned','Returned'),
        ('refunded','Refunded'),
        ('failed','Failed'))
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_status = models.CharField(choices=status,max_length=50,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title
