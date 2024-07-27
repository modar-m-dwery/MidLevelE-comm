from django.contrib import admin
from .models import Product,ProductImage,ProductCategory

# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','price','sale','stock','status','featured','colour','fabric']
    list_filter = ['status','featured','category']
    list_editable = ['price','sale','stock','status','featured']
    prepopulated_fields = {'slug':('title',)}
    inlines = [ProductImageInline,]

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)