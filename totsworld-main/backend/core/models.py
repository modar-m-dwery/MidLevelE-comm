from django.db import models
from django.conf import settings
from django.utils import timezone
from django.shortcuts import reverse
#from authentication.models import CustomUser
from django.contrib.auth.models import User
#from order.models import Order
from product.models import Product
''' Create your models here.Category, Product, Product_images, Product_category,
Order, Product_order, referral, Cart,  Wishlist, Review, settings, Issue Report,
Payments, Billing Detail, Cancled order, Return, Refund, Newsletter subscrtiption,'''

class FeaturedImage(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField()
    description = models.TextField(max_length=250,blank=True,null=True)
    keyword = models.TextField(max_length=150,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class UserAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    phone_number_1 = models.IntegerField()
    phone_number_2 = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=50)
    pin = models.IntegerField()
    default_address = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "user address"
        verbose_name_plural = "user address"

    def __str__(self):
        return self.fullname


class Banner(models.Model):
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=100,blank=True,null=True)
    target = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:banner')

class Referral(models.Model):
    '''id, couponcode, productid or other detail, %discount, status, expiry date, terms&conditions'''
    coupon_code = models.CharField(max_length=50,null=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    discount = models.IntegerField()
    status = models.BooleanField()
    expiry = models.DateField()
    terms_condition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.coupon_code

'''class Wishlist(models.Model):
    # field : user_id product_id 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title
        '''

class Review(models.Model):
    ''' field : user_id product_id rating review '''
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField(max_length=250)
    parent =  models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='reply')
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    @property
    def children(self):
        return Review.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

class Setting(models.Model):
    ''' field : name, value '''
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.key

class ReportIssue(models.Model):
    ''' issue type detail user_id'''
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    issue_type = models.CharField(max_length=50)
    detail = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username