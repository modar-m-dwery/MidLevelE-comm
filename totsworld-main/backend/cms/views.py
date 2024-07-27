from django.shortcuts import render
#from django.shortcuts.urls import HttpResponse
from .forms import ProductForm,ProductImageForm
from django.views.generic import TemplateView
from core.models import Banner,FeaturedImage
from product.models import Product,ProductImage
from category.models import Category

# Create your views here.
class Home(TemplateView):
    template_name='inventory/dashboard.html'
    
class Inventory:
    def add(request):
        if request.method == "POST":
            productform = ProductForm.objects.create(request.POST)
            productimageform = ProductImage.objects.create(request.POST)
            if productform.is_valid() and productimageform.is_valid():
                product=productform.save(False)
                productimage=productimage.save(False)
                productimage.product = product
                product.save()
                productimage.save()
            for i in images:
                img = ProductImage.objects.create(product=newproduct,tags=title,description=description,image=i)
                img.save()
            return render(request,'inventory/product-list.html')
        return render(request,'inventory/add-product.html',{'Pform':ProductForm,'PIform':ProductImage,})
    def edit(request):
        pass
    def delete(request):
        pass
    def detail(request):
        pass
    def showall(request):
        products = Product.objects.all()
        return render(request,'inventory/product-list.html',{'products':products,})
class category:
    def add(request):
        if request.method == "POST":
            return render(request,'inventory/category-list.html')
        return render(request,'inventory/add-category.html')
    def edit(request):
        pass
    def delete(request):
        pass
    def detail(request):
        pass
    def showall(request):
        categories = Category.objects.all()
        return render(request,'inventory/category-list.html',{'categories':categories,})
class banner:
    def add(request):
        if request.method == "POST":
            return render(request,'inventory/banner-list.html')
        return render(request,'inventory/add-banner.html')
    def edit(request):
        pass
    def delete(request):
        pass
    def detail(request):
        pass
    def showall(request):
        banners = Banner.objects.all()
        return render(request,'inventory/category-list.html',{'banners':banners,})
class order:
    def add(request):
        pass
    def edit(request):
        pass
    def delete(request):
        pass
    def detail(request):
        pass
    def showall(request):
        pass
class IssueReport:
    def reply(request):
        pass
    def delete(request):
        pass
    def showall(request):
        pass
    def detail(request):
        pass
class Review:
    def delete(request):
        pass
    def showall(request):
        pass
    def detail(request):
        pass
class FeaturedImage:
    def add(request):
        if request.method == "POST":
            pass
        else:
            pass
    def edit(request):
        pass
    def delete(request):
        pass
    def showall(request):
        pass
    def detail(request):
        pass