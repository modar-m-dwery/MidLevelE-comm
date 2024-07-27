from django.contrib import admin
from .models import Order,ProductOrder

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
	list_display = ('order_uniqid','payment_status','order_status','updated_at','created_at')

class ProductOrderAdmin(admin.ModelAdmin):
	list_display = ('pk','order','order_status','quantity','updated_at','created_at')

admin.site.register(Order,OrderAdmin)
admin.site.register(ProductOrder,ProductOrderAdmin)