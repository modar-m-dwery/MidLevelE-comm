from django.db import models
from django.utils import timezone
from core.models import Product

# Create your models here.
class ProductViews(models.Model):
	product = models.OneToOneField(Product,on_delete=models.CASCADE,null=False)
	count = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "product view"
		verbose_name_plural = "product views"

	def __str__(self):
		return self.product.titles

