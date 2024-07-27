from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
#from product.models import Product

# Create your models here.
class Category(models.Model):
    #field : category name, parent_id, image, description and more to be decided
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name="subcategory")
    image = models.ImageField(blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    tags = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:category",kwargs={
            'slug':self.slug
            })
    '''    
    def get_products(self):
        products = Product.objects.get(category=self)
        return products
    '''
    @property
    def children(self):
        return Category.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False