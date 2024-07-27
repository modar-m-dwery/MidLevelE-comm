from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from rest_framework.decorators import api_view
#from rest_framework import viewsets
from rest_framework.response import Response
#from django.views.decorators.csrf import csrf_exempt
from .models import Product
from core.models import Review
from category.models import Category
from .recent import RecentProduct
from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def ProductListAPI(request):
	product = Product.objects.all()
	serializer = ProductSerializer(product,many=True)
	return Response(serializer.data)

def collection(request,category_slug=None):
    category = None
    categories= Category.objects.all()
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    context = {
            'page_title' : 'Collection',
            'categories':categories,
            'products':products,
            }
    #messages.info(request,'Site Under construction')
    return render(request,"product.html",context)

def product_detail(request,pslug):
    recent_product = RecentProduct(request)
    categories = Category.objects.all()
    product = Product.objects.get(slug=pslug)
    reviews = Review.objects.filter(product=product)
    recent_product.add(product=product)
    context = {
    'categories':categories,
    'product':product,
    'reviews':reviews,
        }
    #messages.info(request,'Site Under construction')
    return render(request,'single_product.html',context)