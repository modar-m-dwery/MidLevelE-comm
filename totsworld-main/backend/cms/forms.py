from django import forms
from product.models import Product,ProductImage
from category.models import Category

cats = Category.objects.all().values_list('name','slug')
product_choices = Product.objects.all().values_list('title','slug')

class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=('title','slug','category','price')

		widgets= {
		'title': forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Product Title',}),
		'slug': forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'product-slug',}),
		'category':forms.Select(choices=cats,attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Select Category',}),
		'price':forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Price',}),
		'colour': forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Product Title',}),
        'fabric': forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Product Title',}),
        'description': forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Product Title',}),
        'tags': forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Product Title',}),
        'sale': forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Product Title',}),
        'featured': forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Product Title',}),
        'stock': forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Product Title',}),
        'status': forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Product Title',}),
        'variant': forms.Select(choices=product_choices,attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Add Variant',}),
		}


class ProductImageForm(forms.ModelForm):
	class Meta:
		model= ProductImage
		fields=('product','image','caption','position')

		widgets= {
		'product': forms.Select(choices=product_choices,attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Product',}),
		'image': forms.ImageField(),
		'caption':forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Select Category',}),
		'position':forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Ordering',}),
		}
class CategoryForm(forms.ModelForm):
	"""docstring for ClassName"""
	class Meta:
		model = Category
		fields = ('name','parent','description','image')

		widgets = {
		'name': forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Name',}),
		'image': forms.ImageField(),
		'parent':forms.Select(choices=cats,attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Parent category',}),
		'slug':forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Slug',}),
		'tags':forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'keywords',}),
		'description':forms.TextInput(attrs={'class':'my-1 mx-1 py-1 px-1 border-1','placeholder':'Description',}),
		}
		