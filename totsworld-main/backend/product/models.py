from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
    """Product fields  title, slug, category, image, price, description, tags, sale%, featured, stock, status and more to be decided"""
    title = models.CharField(max_length=50,null=False)
    slug  = models.SlugField(null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    price = models.FloatField(max_length=7,blank=False,null=False)
    colour = models.CharField(max_length=50,blank=True,null=True)
    fabric = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(max_length=250,blank=True,null=False)
    tags = models.CharField(max_length=100,blank=True,null=False)
    sale = models.FloatField(max_length=4,blank=True,null=True,default=0.00)
    featured = models.BooleanField(default=False)
    stock =  models.IntegerField(default=1,null=False)
    status = models.BooleanField(default=True)
    variant= models.ManyToManyField("self",blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:collection",kwargs={
            'slug':(self.slug,)
            })

    def get_add_to_cart_url(self):
        return reverse("shop:add-to-cart",kwargs={
            'slug':(self.slug,)
            })

    def get_remove_from_cart_url(self):
        return reverse("shop:remove-from-cart",kwargs={
            'slug':(self.slug,)
            })

    @property
    def has_variant(self):
        if Product.variant == None:
            return False
        return True

    @property
    def product_variant(self):
        return Product.objects.filter(variant=self).reverse()
    @property
    def has_images(self):
        if ProductImage.objects.filter(product=self) != None:
            return True
        return False
    @property
    def get_images(self):
        return ProductImage.objects.filter(product=self)
    @property
    def get_thumbnail(self):
        thumbnail = ProductImage.objects.filter(product=self)[:1]
        return thumbnail
    @property
    def get_discount_price(self):
        discount_p = self.price-((self.price/100)*self.sale)
        return discount_p

class ProductImage(models.Model):
    # field : product_id, image url, alt, description and more to be decided
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    image = models.ImageField(null=False)
    caption = models.CharField(max_length=100,blank=True,null=True)
    position = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "product image"
        verbose_name_plural = "products images"
    
    def __str__(self):
        return self.product.title

class ProductCategory(models.Model):
    # field : product_id, category_id and more to be decided
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "product category"
        verbose_name_plural = "product categories"

    def __str__(self):
        return self.product.title